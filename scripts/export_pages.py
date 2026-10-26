"""Package generated DeCocoa pages and runtime resources for GitHub Pages."""
from html import escape, unescape
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit
import argparse
import hashlib
import json
import posixpath
import re
import shutil
from preview_server import PublicSite, ROOT

OUTPUT = ROOT / '_site'
REPORT = ROOT / 'prototype/qa-site-build/pages-export.json'
LICENSES = ('assets/fonts/Montserrat-OFL.txt', 'assets/icons/fontawesome-free-6.7.2/LICENSE.txt')

def normalize_base(value):
    value = '/' + value.strip('/') + '/' if value.strip('/') else '/'
    if not re.fullmatch(r'/(?:[A-Za-z0-9_-][A-Za-z0-9_.-]*/)*', value):
        raise ValueError('Use a URL directory such as /DeCocoa/')
    return value

def output_name(route):
    return route.lstrip('/') + ('index.html' if route.endswith('/') else '')

def recovery_html(html, base):
    def reference(ref):
        if ref.startswith(('#', 'data:')) or urlsplit(ref).scheme or urlsplit(ref).netloc:
            return ref
        parts = urlsplit(urljoin('/404.html', ref))
        return urlunsplit(('', '', base.rstrip('/') + parts.path, parts.query, parts.fragment))
    def attribute(match):
        key, value = match[1], unescape(match[2])
        if key == 'srcset':
            value = ', '.join(' '.join([reference(parts[0]), *parts[1:]]) for candidate in value.split(',') if (parts := candidate.split()))
        else:
            value = reference(value)
        return key + '="' + escape(value, quote=True) + '"'
    return re.sub(r'(href|src|srcset)="([^"]+)"', attribute, html)

def compatibility_routes(site):
    routes = {'/prototype/' + route.lstrip('/'): route for route in site.pages}
    routes.update({'/work-with-us/': '/lets-talk/', '/prototype/work-with-us/': '/lets-talk/'})
    return routes

def redirect_html(route, target):
    folder = posixpath.dirname(output_name(route))
    destination = posixpath.relpath(target.lstrip('/') or '.', folder)
    if target.endswith('/'):
        destination = destination.rstrip('/') + '/'
    script = posixpath.relpath('redirect.js', folder)
    safe = escape(destination, quote=True)
    return ('<!doctype html>\n<html lang="en" data-redirect="' + safe + '"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex">'
            '<title>DeCocoa</title><script src="' + script + '" defer></script>'
            '<noscript><meta http-equiv="refresh" content="0;url=' + safe + '"></noscript></head>'
            '<body><a href="' + safe + '">Continue to DeCocoa</a></body></html>\n')

def export(base):
    base = normalize_base(base)
    site = PublicSite()
    # Only this dedicated generated directory may be replaced, never sources.
    if OUTPUT.is_symlink() or OUTPUT.resolve() != ROOT.resolve() / '_site':
        raise ValueError('Unsafe export output')
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir()
    for route, source in sorted(site.files.items()):
        destination = OUTPUT / output_name(route)
        destination.parent.mkdir(parents=True, exist_ok=True)
        if route == '/404.html':
            destination.write_text(recovery_html(source.read_text(encoding='utf-8'), base), encoding='utf-8', newline='\n')
        else:
            shutil.copyfile(source, destination)
    for name in LICENSES:
        destination = OUTPUT / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, destination)
    redirects = compatibility_routes(site)
    for route, target in sorted(redirects.items()):
        destination = OUTPUT / output_name(route)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(redirect_html(route, target), encoding='utf-8', newline='\n')
    (OUTPUT / 'redirect.js').write_text("(() => {\n  const target = document.documentElement.dataset.redirect;\n  if (!target) return;\n  const destination = new URL(target, location.href);\n  destination.search = location.search;\n  destination.hash = location.hash;\n  location.replace(destination.href);\n})();\n", encoding='utf-8', newline='\n')
    (OUTPUT / '.nojekyll').write_text('', encoding='utf-8')
    files = [{'file': path.relative_to(OUTPUT).as_posix(), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
             for path in sorted(OUTPUT.rglob('*')) if path.is_file()]
    report = {'base_path': base, 'content_pages': len(site.pages), 'runtime_resources': len(site.files) - len(site.pages),
              'compatibility_redirects': redirects, 'files': files}
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(f'Exported {len(site.pages)} pages, {len(site.files)-len(site.pages)} runtime resources, {len(redirects)} redirects and bundled licenses to {OUTPUT}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-path', default='/DeCocoa/')
    export(parser.parse_args().base_path)
