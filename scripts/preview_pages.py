"""Loopback preview of the exact Pages artifact under its project URL prefix."""
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit
import argparse
from export_pages import OUTPUT, normalize_base
from preview_server import LoopbackPreviewServer, handler_for

class ExportSite:
    def __init__(self, base='/DeCocoa/'):
        self.base = normalize_base(base)
        self.files = {p.relative_to(OUTPUT).as_posix(): p for p in OUTPUT.rglob('*') if p.is_file()}
        if 'index.html' not in self.files or '404.html' not in self.files:
            raise ValueError('Run export_pages.py first')

    def response(self, request):
        parts = urlsplit(request)
        path = unquote(parts.path)
        query = '?' + parts.query if parts.query else ''
        if path in ('/', self.base.rstrip('/')):
            return 308, None, self.base + query
        invalid = '\\' in path or any(ord(c) < 32 for c in path) or any(p in ('.', '..') for p in path.split('/'))
        if invalid or not path.startswith(self.base):
            return 404, self.files['404.html'], None
        name = path[len(self.base):]
        if name and not name.endswith('/') and name + '/index.html' in self.files:
            return 308, None, quote(path + '/', safe='/') + query
        name += 'index.html' if not name or name.endswith('/') else ''
        target = self.files.get(name)
        return (200, target, None) if target else (404, self.files['404.html'], None)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=4180)
    parser.add_argument('--base-path', default='/DeCocoa/')
    args = parser.parse_args()
    with LoopbackPreviewServer(('127.0.0.1', args.port), handler_for(ExportSite(args.base_path))) as server:
        print(f'Pages artifact preview: http://127.0.0.1:{args.port}{normalize_base(args.base_path)}', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
