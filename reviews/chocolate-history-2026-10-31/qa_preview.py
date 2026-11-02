"""Local QA fixtures only; production files and exports remain unchanged.

Experience query modes: ?qa=large-text injects a 200% root text size;
?qa=no-script blocks all script execution through a response CSP.
All other requests use the existing public-resource allowlist and handler.
"""
from pathlib import Path
from urllib.parse import parse_qs, urlsplit
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))
from preview_server import LoopbackPreviewServer, PublicSite, handler_for

site = PublicSite()
PublicHandler = handler_for(site)

class QAHandler(PublicHandler):
    def serve(self, head=False):
        request = urlsplit(self.path)
        mode = parse_qs(request.query).get('qa', [''])[0]
        if request.path != '/experience-center/' or mode not in ('large-text', 'no-script'):
            return super().serve(head=head)
        status, source, redirect = site.response(self.path)
        if status != 200 or redirect:
            return super().serve(head=head)
        data = source.read_bytes()
        if mode == 'large-text':
            data = data.replace(b'</head>', b'<style>html{font-size:200%!important}</style></head>', 1)
        self.send_response(200)
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(data)))
        if mode == 'no-script':
            self.send_header('Content-Security-Policy', "script-src 'none'; object-src 'none'; base-uri 'none'")
        self.end_headers()
        if not head:
            self.wfile.write(data)

if __name__ == '__main__':
    with LoopbackPreviewServer(('127.0.0.1', 4175), QAHandler) as server:
        print('Local QA fixtures: http://127.0.0.1:4175/experience-center/?qa=large-text', flush=True)
        print('No scripts: http://127.0.0.1:4175/experience-center/?qa=no-script', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
