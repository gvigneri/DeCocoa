"""Compare the approved brief to rendered destinations, preserving punctuation.

This test reads the archived client brief independently of the runtime content
data. Presentation whitespace, source bullet markers and the authorized
November 15 em dash removal are normalized; segment copy follows its new hub.
Run after build_homepage.py. Browser layout/interaction checks are separate.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, urljoin
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'prototype'
BRIEF = ROOT / 'handoff/content-component-brief-2026-11-11.md'


def normalized(value):
    value = re.sub(r'\s+—\s+', ': ', value).replace('—', ', ')
    return re.sub(r'\s+', ' ', value.replace('\u200b', '')).strip()


class Document(HTMLParser):
    """Track main content and ID scopes without depending on markup layout."""
    VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
    BLOCK = {'address', 'article', 'aside', 'blockquote', 'br', 'dd', 'div', 'dl', 'dt', 'fieldset', 'figcaption', 'figure', 'footer', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'hr', 'li', 'main', 'nav', 'ol', 'p', 'section', 'table', 'td', 'th', 'tr', 'ul'}

    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.anchors = []
        self.image_links = []
        self.scopes = {'__all__': []}
        self.elements = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.elements.append((tag, attrs))
        if tag == 'a':
            self.anchors.append(attrs)
        if tag == 'img':
            self.image_links.append((attrs, self.anchors[-1] if self.anchors else None))
        key = attrs.get('id')
        if key:
            self.scopes.setdefault(key, [])
        if tag == 'main':
            self.scopes.setdefault('__main__', [])
        if tag not in self.VOID:
            self.stack.append((tag, key))
        if tag in self.BLOCK:
            self.handle_data(' ')

    def handle_endtag(self, tag):
        if tag in self.BLOCK:
            self.handle_data(' ')
        if tag == 'a' and self.anchors:
            self.anchors.pop()
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                del self.stack[index:]
                break

    def handle_data(self, value):
        if any(tag in ('script', 'style') for tag, _ in self.stack):
            return
        self.scopes['__all__'].append(value)
        if any(tag == 'main' for tag, _ in self.stack):
            self.scopes['__main__'].append(value)
        for _, key in self.stack:
            if key:
                self.scopes[key].append(value)

    def text(self, key='__main__'):
        return normalized(''.join(self.scopes.get(key, [])))


def copy_blocks(source):
    sections = dict(re.findall(r'^### (C\d\d) [^\n]+\n(.*?)(?=^### C\d\d |\Z)', source, re.M | re.S))
    return {key: re.findall(r'```text\s*\n(.*?)\n```', text, re.S) for key, text in sections.items()}


def run():
    blocks = copy_blocks(BRIEF.read_text(encoding='utf-8-sig'))
    inventory = json.loads((SITE / 'generated-pages.json').read_text(encoding='utf-8'))['pages']
    docs = {item['route']: Document((ROOT / item['file']).read_text(encoding='utf-8')) for item in inventory}
    errors, checks = [], []

    def require(condition, label, detail=None):
        checks.append(label)
        if not condition:
            errors.append([label, detail] if detail is not None else [label])

    def lines(block, route, scope='__main__', skip=(), ordered=True):
        actual = docs[route].text(scope)
        cursor = 0
        for line in block.splitlines():
            expected = normalized(line.lstrip('•'))
            if not expected or expected in skip:
                continue
            position = actual.find(expected, cursor if ordered else 0)
            require(position >= 0, 'verbatim source at ' + route + '#' + scope, expected)
            if position >= 0 and ordered:
                cursor = position + len(expected)

    categories = blocks['C01'][0].splitlines()
    require(len(categories) == 11, '11 source categories')
    collection_routes = ('/snacking/', '/gifting/', '/entertaining/')
    category_positions = {route: [] for route in collection_routes}
    for category in blocks['C02']:
        heading, tagline, description = category.splitlines()
        scope = heading.lower()
        if '/'+scope+'/' in collection_routes:
            lines(category, '/products/', scope)
            # Collection names were hero eyebrows; the tagline and copy remain.
            lines(category, '/'+scope+'/', skip=(heading,))
        else:
            for route in collection_routes:
                lines(category, route, scope)
                category_positions[route].append(docs[route].text().find(normalized(category)))
            lines(heading + '\n' + tagline, '/', 'products')
    for route, doc in docs.items():
        for destination in collection_routes:
            controls = [a for tag, a in doc.elements if tag == 'a' and 'submenu-link' in a.get('class', '').split() and urljoin(route, a.get('href', '')) == destination]
            require(len(controls) == 2, 'collection in both shared menus ' + route, destination)
        old_format_links = [a for tag, a in doc.elements if tag == 'a' and 'submenu-link' in a.get('class', '').split() and urlsplit(urljoin(route, a.get('href', ''))).path == '/products/']
        require(not old_format_links, 'formats removed from main chocolate submenu ' + route)
    for route, positions in category_positions.items():
        require(len(positions) == 8 and all(position >= 0 for position in positions) and positions == sorted(positions), 'eight formats in supplied order ' + route)
    require(not any('/products/' + name.lower() + '/' in docs for name in categories), 'no new individual category pages')

    c03 = blocks['C03'][0].split('\n\n')
    lines(c03[0], '/experience-center/')
    # Homepage Experience now uses its own November 15 summary.
    lines(c03[1], '/experience-center/', 'museum-virtual-exhibition')
    lines(c03[2], '/experience-center/', 'tours-and-classes')
    # November 15: Guy removed the comma from the Today story heading.
    lines(blocks['C04'][0].replace('\nToday,\n', '\nToday\n'), '/our-people/', 'our-roots')
    lines(blocks['C05'][0], '/our-people/', 'our-roots')
    lines(blocks['C06'][0], '/our-people/', 'our-values')
    for route, heading in [('/products/', 'Experience. Chocolate.'), ('/our-people/', 'Our Chocolate Crafters'), ('/our-craft/', 'Crafting the Future'), ('/b2b/', 'Crafting the Future'), ('/decor/', 'Chocolate as Art')]:
        h1_ids = [a.get('id') for tag, a in docs[route].elements if tag == 'h1']
        require(len(h1_ids) == 1 and heading in docs[route].text(h1_ids[0]), 'mapped hero heading ' + route, heading)
    for scope, heading in [('products', 'Experience. Chocolate.'), ('people', 'Your Chocolate Crafters'), ('craft', 'Crafting the Future')]:
        require(heading in docs['/'].text(scope), 'homepage mapped tagline ' + scope, heading)

    # Décor deliberately places the second source block in its hero. Check all
    # source lines without imposing the old source ordering across that move.
    lines(blocks['C08'][0], '/decor/', ordered=False)
    lines(blocks['C09'][0], '/b2b/', skip=('Partner Brands',))
    c10 = blocks['C10'][0].split('\n\n')
    lines(c10[1], '/our-craft/', 'promise')
    lines(c10[2], '/our-craft/', 'sustainability')
    focus = blocks['C04'][0].splitlines()[-1]
    lines(focus, '/our-craft/', 'focus')
    lines(blocks['C11'][0], '/', 'partners')
    lines(blocks['C13'][0], '/our-segments/', 'business-segments')
    # November 15: the process introduction now follows Built for Growth on Partner Brands.
    lines(blocks['C14'][0], '/b2b/', 'process-capabilities')
    gifting = next(block for block in blocks['C02'] if block.startswith('Gifting\n'))
    lines(gifting, '/gifting/', skip=('Gifting',))

    retained = json.loads((SITE / 'site-content.json').read_text(encoding='utf-8'))
    for page in retained['pages']:
        for section in page['sections']:
            if section['id'] not in ('sweet-careers', 'food-safety', 'how-its-made'):
                continue
            chunks = [section['title'], *section.get('paragraphs', []), *section.get('bullets', [])]
            for step in section.get('ordered_steps', []):
                chunks.extend([step['title'], step['text']])
            lines('\n'.join(chunks), '/' + page['route'], section['id'])
    for product in retained['products']:
        lines(product['description'] + '\n' + product['detail'], '/products/' + product['slug'] + '/')
    for category in retained['categories']:
        if category['slug'] == 'wellness':
            continue
        require(category['slug'] in docs['/products/'].scopes, 'retained manufacturing anchor ' + category['slug'])
        replacement = '/our-craft/'
        require(any(tag == 'a' and urljoin('/products/', attrs.get('href', '')) == replacement for tag, attrs in docs['/products/'].elements), 'manufacturing compatibility destination ' + category['slug'])

    # Every inventoried public page must expose the same hero base and one H1.
    for route, doc in docs.items():
        heroes = [a for tag, a in doc.elements if tag == 'section' and 'hero' in a.get('class', '').split()]
        require(len(heroes) == 1, 'one shared hero ' + route)
        require(sum(tag == 'h1' for tag, _ in doc.elements) == 1, 'one semantic H1 ' + route)
        for main_route in ('/products/', '/our-segments/', '/our-people/', '/our-craft/', '/experience-center/'):
            labels = [a for tag, a in doc.elements if tag == 'a' and 'nav-link' in a.get('class', '').split() and urlsplit(urljoin(route, a.get('href', ''))).path == main_route]
            require(len(labels) == 2, 'linked primary label in both headers ' + route, main_route)
        require('—' not in ''.join(doc.scopes['__all__']), 'no em dashes in public content ' + route)
        editable = ' '.join([doc.text('__all__'), *(attrs.get(key, '') for _, attrs in doc.elements for key in ('alt', 'aria-label', 'content', 'title'))])
        require(all(brand == 'DeCocoa' for brand in re.findall(r'\bdecocoa\b', editable, re.I)), 'consistent editable brand spelling ' + route)

    # Original history is distinct from the five-date family timeline.
    history = json.loads((SITE / 'chocolate-history.json').read_text(encoding='utf-8'))
    for chapter in history['chapters']:
        for key in ('title', 'caption'):
            if chapter.get(key):
                lines(chapter[key], '/experience-center/', 'museum-virtual-exhibition')
    for year in ('1951', '1967', '1971', '2014', '2024'):
        require(year in docs['/our-people/'].text('our-roots'), 'family timeline year ' + year)

    links = json.loads((SITE / 'logo-links.json').read_text(encoding='utf-8'))
    logo_groups = retained['trust_sections']
    for group in ('partners', 'certifications'):
        for key, mark in links[group].items():
            source = next(item for item in logo_groups[group]['marks'] if item['class'] == key)
            image_matches = [(img, anchor) for img, anchor in docs['/'].image_links if img.get('src', '').endswith('/' + source['image'])]
            require(len(image_matches) == 1, 'one retained logo image ' + key)
            candidates = [anchor for _, anchor in image_matches if anchor]
            if mark['href']:
                require(len(candidates) == 1 and candidates[0].get('href') == mark['href'] and candidates[0].get('target') == '_blank' and set(candidates[0].get('rel', '').split()) >= {'noopener', 'noreferrer'}, 'verified external logo link ' + key)
            else:
                require(not candidates, 'unresolved logo remains unlinked ' + key)
    require(links['certifications']['haccp']['href'] is None, 'unresolved HACCP destination not invented')
    report = {'source': BRIEF.relative_to(ROOT).as_posix(), 'normalization': 'Presentation whitespace and source bullet markers normalized; November 15 authorized em dash removal. Remaining wording and capitalization preserved.', 'public_pages': len(docs), 'checks': len(checks), 'errors': errors, 'specific_open_issue': 'HACCP certifying organization and official website remain unidentified.'}
    output = ROOT / 'reviews/presentation-2026-11-15'
    output.mkdir(parents=True, exist_ok=True)
    (output / 'exact-copy-checks.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == '__main__':
    run()
