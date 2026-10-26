"""Package the local prototype and its referenced assets without original source archives."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ('img', 'script') and attrs.get('src'):
            self.links.append(attrs['src'])
        if tag == 'link' and attrs.get('rel') == 'stylesheet':
            self.links.append(attrs['href'])

pending = [ROOT / 'prototype/index.html']
selected = set()
while pending:
    path = pending.pop().resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError(f'Outside project: {path}')
    if path in selected:
        continue
    if not path.is_file():
        raise FileNotFoundError(path)
    selected.add(path)
    references = []
    if path.suffix == '.html':
        parser = Links()
        parser.feed(path.read_text(encoding='utf-8-sig'))
        references = parser.links
    elif path.suffix == '.css':
        references = re.findall(r'url\([\s\"\x27]*([^\)\"\x27\s]+)', path.read_text(encoding='utf-8-sig'))
    for ref in references:
        url = urlsplit(ref)
        if url.scheme or url.netloc or not url.path:
            continue
        pending.append(path.parent / unquote(url.path))

for name in ['README.md', 'Start-Preview.ps1', 'DeCocoa-Codex-Master-Brief.md',
             'brand/brand-rules.md', 'brand/brand-exceptions.md', 'brand/asset-manifest.md',
             'assets/fonts/Montserrat-OFL.txt', 'assets/fonts/provenance.json',
             'reviews/ledger.md']:
    selected.add(ROOT / name)
selected.update((ROOT / 'handoff').glob('*.md'))
selected.update((ROOT / 'reviews').glob('session-*.md'))
selected.update((ROOT / 'handoff/screenshots').glob('*.jpg'))
# The requested editable vector library is part of the deliverable even when a
# given master is not used by the current homepage composition.
selected.update((ROOT / 'assets/patterns').glob('*.svg'))
selected.update((ROOT / 'assets/logos').glob('*.svg'))
selected.add(ROOT / 'assets/vector-export-details.json')
selected.add(ROOT / 'handoff/source-integrity.json')
selected.add(ROOT / 'handoff/pretzel-cutout-provenance.json')
selected.add(ROOT / 'prototype/source-checks.json')
selected.update((ROOT / 'prototype').glob('*.md'))
selected.add(ROOT / 'prototype/homepage.template.html')
selected.add(ROOT / 'scripts/build_homepage.py')
selected.add(ROOT / 'scripts/export_vectors.py')
selected.add(ROOT / 'scripts/check_homepage.py')

destination = ROOT / 'handoff/DeCocoa-preview.zip'
with zipfile.ZipFile(destination, 'w', zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(selected):
        archive.write(path, path.relative_to(ROOT).as_posix())
    archive.writestr('PACKAGE.txt', 'DeCocoa local homepage. Run Start-Preview.ps1 and open the printed URL. This portable package contains the website, editable SVG patterns, referenced web assets, fonts/license, final desktop/mobile screenshots and handoff documents. Original AI/PDF/PNG sources and intermediate review screenshots remain in the full project workspace. Nothing has been published. Contact fields validate locally; message delivery is not connected. See handoff/open-items.md before any production implementation.\n')
with zipfile.ZipFile(destination) as archive:
    if archive.testzip() is not None:
        raise RuntimeError('Archive validation failed')
print(f'{destination}\n{len(selected)} files; {destination.stat().st_size:,} bytes; CRC checks passed')

pattern_files = sorted((ROOT / 'assets/patterns').glob('*-master.svg'))
if len(pattern_files) != 6:
    raise RuntimeError('Expected all six requested pattern masters')
for path in pattern_files:
    svg = path.read_text(encoding='utf-8')
    if '<path ' not in svg or re.search(r'<(?:\w+:)?image\b|data:image/', svg):
        raise RuntimeError(f'Pattern must remain genuine vector artwork: {path.name}')
pattern_package = ROOT / 'handoff/DeCocoa-patterns-svg.zip'
with zipfile.ZipFile(pattern_package, 'w', zipfile.ZIP_DEFLATED) as archive:
    for path in pattern_files:
        archive.write(path, path.name)
    archive.write(ROOT / 'assets/vector-export-details.json', 'vector-export-details.json')
    archive.write(ROOT / 'handoff/patterns-and-motion.md', 'patterns-and-motion.md')
with zipfile.ZipFile(pattern_package) as archive:
    if archive.testzip() is not None:
        raise RuntimeError('Pattern archive validation failed')
print(f'{pattern_package}\n6 vector masters; {pattern_package.stat().st_size:,} bytes; CRC checks passed')
