"""Shared image-menu renderer; all destinations live in navigation.json."""
from html import escape
import json


def load_navigation(site):
    return json.loads((site / 'navigation.json').read_text(encoding='utf-8'))


def navigation(data, current, prefix, url, link):
    """Render the same navigation into either existing header shell.

    `data` is resolved site content. Category thumbnails reuse category records;
    other menus use the existing image named by their navigation record.
    `url` and `link` are the portable build's route helpers.
    """
    parts = []
    categories = {item['slug']: item for item in data['categories']}
    for item in data['navigation']:
        if not item.get('children'):
            parts.append(link(item, current, 'nav-link'))
            continue
        active = current == item['route'] or any(
            current.startswith(route) for route in item.get('active_routes', [item['route']])
        )
        active_class = ' is-current' if active else ''
        menu_id = prefix + '-' + item['route'].strip('/').replace('/', '-') + '-menu'
        main = link(item, current, 'nav-link nav-parent' + active_class)
        toggle = ('<button type="button" class="nav-link submenu-toggle' + active_class +
                  '" aria-label="Toggle ' + escape(item['label'], quote=True) +
                  ' submenu" aria-expanded="false" aria-controls="' + menu_id +
                  '"><span class="submenu-chevron" aria-hidden="true"></span></button>')
        entries = []
        category_menu = item.get('variant') == 'categories'
        for child in item['children']:
            thumbnail = ''
            if child.get('category'):
                category = categories[child['category']]
                thumbnail = ('<span class="submenu-thumbnail"><img src="{{asset:images/' +
                             category['image'] + '}}" width="' + str(category['width']) +
                             '" height="' + str(category['height']) +
                             '" alt="" loading="lazy"></span>')
            entries.append('<li><a class="submenu-link" href="' + escape(url(child['route'], current), quote=True) +
                           '">' + thumbnail + '<span>' + escape(child['label']) + '</span></a></li>')
        feature = ''
        if not category_menu and item.get('image'):
            # Supporting photography is decorative; the parent already links here.
            feature = ('<div class="submenu-feature" aria-hidden="true">'
                       '<span class="card submenu-feature-image"><img src="{{asset:images/' + item['image'] +
                       '}}" width="' + str(item['width']) + '" height="' + str(item['height']) +
                       '" alt="" loading="lazy"></span></div>')
        panel_class = 'submenu image-submenu' + (' category-submenu' if category_menu else ' feature-submenu' if feature else ' segment-submenu')
        panel = ('<div class="' + panel_class + '" id="' + menu_id + '" hidden>' + feature +
                 '<ul class="submenu-grid">' + ''.join(entries) + '</ul></div>')
        parts.append('<div class="nav-dropdown"><div class="nav-row">' + main + toggle + '</div>' + panel + '</div>')
    return ''.join(parts)
