"""Exercise the real root-mounted HTTP preview on an ephemeral loopback port.

No browser, external service, or live message recipient is used.
"""
from html.parser import HTMLParser
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urljoin, urlsplit
import hashlib
import json
import threading
from preview_server import LoopbackPreviewServer, PublicSite, handler_for

ROOT = Path(__file__).resolve().parents[1]

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.refs.extend(attrs[key] for key in ('href', 'src') if key in attrs)

def run():
    site = PublicSite(ROOT)
    errors, checks = [], []
    server = LoopbackPreviewServer(('127.0.0.1', 0), handler_for(site, quiet=True))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    def request(path, method='GET'):
        connection = HTTPConnection('127.0.0.1', server.server_port, timeout=5)
        try:
            connection.request(method, path)
            response = connection.getresponse()
            return response.status, dict(response.getheaders()), response.read()
        finally:
            connection.close()
    try:
        # A running preview must reject another preview AND a generic Windows
        # reuse-address server. Conversely, preview startup must reject an
        # endpoint already owned by a generic server. All ports are ephemeral.
        duplicate_checks = []
        def duplicate_rejected(server_type, address, label):
            try:
                duplicate = server_type(address, handler_for(site, quiet=True))
            except OSError:
                duplicate_checks.append({'scenario': label, 'rejected': True})
            else:
                duplicate.server_close()
                duplicate_checks.append({'scenario': label, 'rejected': False})
                errors.append(['duplicate listener accepted', label])
        duplicate_rejected(LoopbackPreviewServer, server.server_address, 'second preview on preview port')
        duplicate_rejected(ThreadingHTTPServer, server.server_address, 'generic reuse listener on preview port')
        with ThreadingHTTPServer(('127.0.0.1', 0), handler_for(site, quiet=True)) as existing:
            duplicate_rejected(LoopbackPreviewServer, existing.server_address, 'preview on existing generic-server port')
        # Exercise every public page and runtime asset through the actual server.
        for route, path in site.files.items():
            status, headers, body = request(route)
            expected_status = 404 if route == '/404.html' else 200
            good = status == expected_status and hashlib.sha256(body).digest() == hashlib.sha256(path.read_bytes()).digest()
            if not good:
                errors.append(['public file response', route, status])
            checks.append({'request': route, 'status': status, 'matches_generated_file': good})
        query = '?topic=Chocolate%20%26%20products&product=filled-chocolate'
        for route in site.pages:
            legacy = '/prototype' + route
            status, headers, body = request(legacy + query)
            if status != 308 or headers.get('Location') != route + query or body:
                errors.append(['legacy redirect', legacy, status, headers.get('Location')])
        for old, new in [('/prototype', '/'), ('/index.html', '/'), ('/products', '/products/'), ('/products/index.html', '/products/'), ('/prototype/missing%20page', '/missing%20page')]+[(old,'/lets-talk/') for old in ('/work-with-us','/work-with-us/','/work-with-us/index.html','/prototype/work-with-us','/prototype/work-with-us/','/prototype/work-with-us/index.html')]:
            status, headers, body = request(old + query)
            if status != 308 or headers.get('Location') != new + query:
                errors.append(['canonical redirect', old, status, headers.get('Location')])
        # Unknown paths at different depths must return the branded recovery page.
        # Resolve its resource AND navigation URLs at each missing-path depth.
        for missing in ('/missing', '/missing/deep/path/', '/assets/', '/brand/source/', '/scripts/', '/references/', '/handoff/', '/AGENTS.md', '/site-content.json', '/partials/header.html', '/assets/patterns/stripes-master.svg', '/assets/fonts/OFL.txt', '/%2e%2e/AGENTS.md', '/prototype/%2e%2e/AGENTS.md'):
            status, headers, body = request(missing)
            if status != 404 or body != site.pages['/404.html'].read_bytes():
                errors.append(['unknown/source path not isolated', missing, status])
            parser = Links()
            parser.feed(body.decode('utf-8'))
            for ref in parser.refs:
                if ref.startswith('#'):
                    continue
                destination = urlsplit(urljoin(missing, ref))
                if destination.scheme or destination.netloc:
                    continue
                if destination.path not in site.files:
                    errors.append(['404 recovery reference', missing, ref, destination.path])
        status, headers, body = request('/products/filled-chocolate/', 'HEAD')
        if status != 200 or body or int(headers.get('Content-Length', 0)) == 0:
            errors.append(['HEAD response'])
        status, headers, body = request('/lets-talk/', 'POST')
        if status != 405 or body:
            errors.append(['unexpected POST handler', status])
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)
    result = {'scope': 'Real HTTP requests to an ephemeral 127.0.0.1 preview; no browser or external traffic.', 'duplicate_port_checks': duplicate_checks, 'public_pages': len(site.pages), 'public_runtime_assets': len(site.files) - len(site.pages), 'public_file_responses': checks, 'legacy_context_redirects': len(site.pages), 'root_and_nested_recovery': 'pass' if not errors else 'fail', 'source_directories_and_unreferenced_assets': 'not served', 'errors': errors}
    output = ROOT / 'prototype/qa-site-build/preview-http-checks.json'
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
    if errors:
        raise SystemExit(1)

if __name__ == '__main__':
    run()
