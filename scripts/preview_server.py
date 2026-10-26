"""Root-mounted, loopback-only preview for generated DeCocoa pages.

Only the generated page inventory and referenced runtime assets are served.
Editable templates, reports, artwork masters and other workspace files are not
public files. There is no form handler or directory-listing endpoint.
"""
from html.parser import HTMLParser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import quote, unquote, urljoin, urlsplit
import argparse
import json
import mimetypes
import re
import socket

ROOT = Path(__file__).resolve().parents[1]

class LoopbackPreviewServer(ThreadingHTTPServer):
    """Do not share a listening port, including with Windows reuse listeners."""
    allow_reuse_address = False
    allow_reuse_port = False

    def server_bind(self):
        # Windows SO_REUSEADDR can silently attach a second listener to the
        # same endpoint. Exclusive use rejects both earlier and later binders.
        # Other platforms fall back to a normal socket without address reuse.
        if hasattr(socket, 'SO_EXCLUSIVEADDRUSE'):
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 1)
        super().server_bind()

class Resources(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        key = 'src' if tag in ('img', 'script', 'source') else 'href' if tag == 'link' else None
        if key and attrs.get(key):
            self.refs.append(attrs[key])
        if tag in ('source','img') and attrs.get('srcset'):
            self.refs.extend(candidate.strip().split()[0] for candidate in attrs['srcset'].split(',') if candidate.strip())

class PublicSite:
    def __init__(self, root=ROOT):
        self.root = Path(root).resolve()
        self.site = self.root / 'prototype'
        inventory = json.loads((self.site / 'generated-pages.json').read_text(encoding='utf-8'))
        self.pages = {}
        for item in inventory['pages']:
            path = (self.root / item['file']).resolve()
            if not path.is_relative_to(self.site) or not path.is_file():
                raise ValueError('Invalid generated page inventory')
            self.pages[item['route']] = path
        if '/' not in self.pages or '/404.html' not in self.pages:
            raise ValueError('Build root-mounted pages before starting the preview')
        self.files = dict(self.pages)
        pending = []
        for route, path in self.pages.items():
            parser = Resources()
            parser.feed(path.read_text(encoding='utf-8'))
            pending.extend(urlsplit(urljoin(route, ref)).path for ref in parser.refs)
        while pending:
            route = pending.pop()
            if route in self.files:
                continue
            path = self.runtime_path(route)
            if path is None or not path.is_file():
                raise ValueError('Missing or unsupported runtime resource: ' + route)
            self.files[route] = path
            if path.suffix.lower() == '.css':
                refs = re.findall(r'url\([\'\"]?([^\)\'\"]+)', path.read_text(encoding='utf-8'))
                pending.extend(urlsplit(urljoin(route, ref)).path for ref in refs if not ref.startswith(('data:', '#')))

    def runtime_path(self, route):
        if route in ('/styles.css', '/script.js'):
            return self.site / route.lstrip('/')
        if not route.startswith('/assets/'):
            return None
        path = (self.root / unquote(route).lstrip('/')).resolve()
        asset_root = (self.root / 'assets').resolve()
        return path if path.is_relative_to(asset_root) else None

    def resolve_reference(self, ref, current):
        parts = urlsplit(urljoin(current, ref))
        if parts.scheme or parts.netloc:
            return None, ''
        return self.files.get(parts.path), unquote(parts.fragment)

    def response(self, request_path):
        parts = urlsplit(request_path)
        path = unquote(parts.path)
        if not path.startswith('/') or '\\' in path or any(ord(char) < 32 or ord(char) == 127 for char in path) or any(segment in ('.', '..') for segment in path.split('/')):
            return 404, self.pages['/404.html'], None
        if path == '/prototype' or path.startswith('/prototype/'):
            clean = '/' + path[len('/prototype'):].lstrip('/')
            if clean.endswith('/index.html'):
                clean = clean[:-len('index.html')]
            if clean + '/' in self.pages:
                clean += '/'
            if clean in ('/work-with-us', '/work-with-us/', '/work-with-us/index.html'):
                clean = '/lets-talk/'
            return 308, None, quote(clean, safe='/') + ('?' + parts.query if parts.query else '')
        if path in ('/work-with-us', '/work-with-us/', '/work-with-us/index.html'):
            return 308, None, '/lets-talk/' + ('?' + parts.query if parts.query else '')
        if path.endswith('/index.html') and path[:-len('index.html')] in self.pages:
            return 308, None, path[:-len('index.html')] + ('?' + parts.query if parts.query else '')
        if path + '/' in self.pages:
            return 308, None, path + '/' + ('?' + parts.query if parts.query else '')
        if path in self.files:
            return (404 if path == '/404.html' else 200), self.files[path], None
        return 404, self.pages['/404.html'], None

def handler_for(site, quiet=False):
    class PreviewHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.serve()
        def do_HEAD(self):
            self.serve(head=True)
        def do_POST(self):
            self.send_response(405)
            self.send_header('Allow', 'GET, HEAD')
            self.send_header('Content-Length', '0')
            self.end_headers()
        def serve(self, head=False):
            status, path, location = site.response(self.path)
            self.send_response(status)
            self.send_header('Cache-Control', 'no-store')
            self.send_header('X-Content-Type-Options', 'nosniff')
            if location:
                self.send_header('Location', location)
                self.send_header('Content-Length', '0')
                self.end_headers()
                return
            data = path.read_bytes()
            mime = mimetypes.guess_type(path.name)[0] or 'application/octet-stream'
            if path.suffix in ('.html', '.css', '.js'):
                mime += '; charset=utf-8'
            self.send_header('Content-Type', mime)
            self.send_header('Content-Length', str(len(data)))
            self.end_headers()
            if not head:
                self.wfile.write(data)
        def log_message(self, message, *args):
            if not quiet:
                super().log_message(message, *args)
    return PreviewHandler

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=4173)
    args = parser.parse_args()
    site = PublicSite()
    try:
        server = LoopbackPreviewServer(('127.0.0.1', args.port), handler_for(site))
    except OSError as error:
        parser.exit(2, f'Cannot start DeCocoa preview on 127.0.0.1:{args.port}. The port is already in use or cannot be bound: {error}\n')
    with server:
        print(f'DeCocoa preview: http://127.0.0.1:{server.server_port}/', flush=True)
        print('Local only. Press Ctrl+C to stop.', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    main()
