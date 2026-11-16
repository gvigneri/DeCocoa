"""Map the approved content brief onto the existing site's content model.

The verbatim C01–C14 blocks in prototype/approved-content.json are the sole
replacement-copy source. This adapter preserves unrelated baseline content,
assets and routes, and shares the same source values across repeated uses.
"""
from copy import deepcopy
import json
from pathlib import Path
import re
from presentation_updates import apply_presentation

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'prototype' / 'approved-content.json'


def apply_content(data):
    source = json.loads(SOURCE.read_text(encoding='utf-8'))['blocks']

    def block(key, index=0):
        return source[key]['blocks'][index]

    def paragraphs(text):
        return [' '.join(part.splitlines()) for part in text.split('\n\n')]

    def titled(text):
        title, body = text.split('\n', 1)
        return {'title': title, 'paragraphs': paragraphs(body)}

    pages = {page['route']: page for page in data['pages']}
    services = {page['route']: page for page in data['services']}
    old_categories = {item['slug']: deepcopy(item) for item in data['categories']}
    products = {item['slug']: item for item in data['products']}
    data['capabilities'] = [old_categories[slug] for slug in
                            ('one-shot-depositing', 'hollow-moulding', 'mixing', 'dry-filling')]

    def image_from(item):
        return {key: item[key] for key in ('image', 'width', 'height', 'alt')}

    assets = {
        'tablet': image_from(products['chocolate-bar']),
        'filled': image_from(products['filled-chocolate']),
        'covered': image_from(old_categories['mixing']),
        'dipped': {'image': 'dipped-pretzels.webp', 'width': 1085, 'height': 1500,
                   'alt': 'Chocolate-dipped pretzels with decorative finishes'},
        'novelty': image_from(old_categories['hollow-moulding']),
        'drink': image_from(old_categories['dry-filling']),
        'wellness': image_from(old_categories['wellness']),
        'assortment': image_from(old_categories['mixing']),
        'snacking': image_from(old_categories['mixing']),
        'gifting': image_from(products['filled-chocolate']),
        'entertaining': image_from(products['chocolate-drizzle']),
    }
    data['categories'] = []
    for text in source['C02']['blocks']:
        title, tagline, description = text.split('\n', 2)
        slug = title.lower()
        data['categories'].append({
            'slug': slug, 'title': title, 'tagline': tagline,
            'description': description, 'surface': 'cream', **assets[slug],
            'source': 'C02; existing illustrative site asset reused without a product claim.',
        })
    assert [c['title'] for c in data['categories']] == block('C01').splitlines()
    taglines = source['C07']['taglines']
    data['home_section_headings'] = taglines
    data['chocolate_intro'] = {'eyebrow': 'Our Chocolate', 'heading': taglines['products'], 'text': ''}

    people = pages['our-people/']
    people['heading'] = taglines['our-people']
    people['simple_heading'] = False
    roots, journey, birth, today, statements = block('C04').split('\n\n')
    mission = today.split('\n', 1)[1]
    vision, focus = statements.splitlines()
    people_sections = {section['id']: section for section in people['sections']}
    people_sections['our-roots'].update({
        **titled(roots),
        'blocks': [titled(journey), titled(birth),
                   {'title': today.split('\n', 1)[0],
                    'paragraphs': [mission, ' '.join(statements.splitlines())]}],
        'timeline': [],
    })
    for entry in block('C05').split('\n\n'):
        match = re.fullmatch(r'(\d{4})([- –]+)(.*)', entry)
        assert match, entry
        date, separator, text = match.groups()
        people_sections['our-roots']['timeline'].append({'date': date, 'separator': separator, 'text': text})
    people_sections['our-principals']['items'] = [
        {'title': 'VISION', 'text': vision},
        {'title': 'FOCUS', 'text': focus},
        {'title': 'MISSION', 'text': mission},
    ]
    value_lines = block('C06').splitlines()
    people_sections['our-values']['items'] = [
        {'title': value_lines[index], 'text': value_lines[index + 1]}
        for index in range(0, len(value_lines), 2)
    ]
    people['source'] = 'C04–C07, approved content/component brief; existing introduction and Sweet Careers retained.'

    craft = pages['our-craft/']
    craft['heading'] = taglines['our-craft']
    craft['simple_heading'] = False
    craft_sections = {section['id']: section for section in craft['sections']}
    _, promise_text, sustainability_text = block('C10').split('\n\n')
    craft_sections['promise']['paragraphs'] = promise_text.splitlines()
    craft_sections['focus']['paragraphs'] = [focus]
    craft_sections['focus']['aliases'] = []
    craft_sections['sustainability']['paragraphs'] = []
    sustainability_heading, sustainability_body = sustainability_text.split('\n', 1)
    craft_sections['sustainability']['blocks'] = [
        {'title': sustainability_heading, 'paragraphs': sustainability_body.splitlines()}
    ]

    business_groups = block('C13').split('\n\n')
    data['business_intro'] = titled(business_groups[0])
    segment_routes = ('products/', 'b2b/', 'decor/', 'our-craft/#fulfillment')
    segment_ids = ('branded-chocolate', 'partner-brands', 'decor', 'fulfillment')
    segment_icons = ('gift', 'handshake', 'wand-magic-sparkles', 'gears')
    data['business_segments'] = [
        {**titled(text), 'id': segment_id, 'route': route, 'icon': icon}
        for text, segment_id, route, icon in zip(business_groups[1:], segment_ids, segment_routes, segment_icons)
    ]
    craft_sections['our-segments'].update({
        **data['business_intro'], 'nav_title': 'Our Segments',
        'items': data['business_segments'], 'related_route': 'our-segments/',
        'related_label': 'Explore Our Segments',
    })
    craft['sections'].append({
        'id': 'process-capabilities', 'aliases': ['capabilities'],
        'title': 'Process & Capabilities', 'paragraphs': paragraphs(block('C14')),
        'image': 'decocoa-factory-still.png', 'width': 1200, 'height': 422,
        'alt': 'The DeCocoa chocolate factory', 'capabilities': data['capabilities'],
    })
    craft['cta'] = 'Explore Partner Brands'
    craft['source'] = 'C04, C07, C10, C13, C14; existing introduction, Food Safety and manufacturing copy retained.'

    experience = pages['experience-center/']
    exp_intro, museum, tours = block('C03').split('\n\n')
    experience['intro_paragraphs'] = exp_intro.splitlines()[1:]
    experience['intro'] = experience['intro_paragraphs'][0]
    experience['sections'] = [s for s in experience['sections'] if s['id'] != 'experience-overview']
    exp_sections = {section['id']: section for section in experience['sections']}
    exp_sections['museum-virtual-exhibition']['paragraphs'] = museum.splitlines()[1:]
    exp_sections['museum-virtual-exhibition']['aliases'].append('experience-overview')
    exp_sections['tours-and-classes']['paragraphs'] = tours.splitlines()[1:]
    exp_sections['tours-and-classes']['related_links'] = [
        {'route': 'craft-your-own/', 'label': 'Explore Craft Your Own', 'style': 'primary'}
    ]
    experience['source'] = 'C03 verbatim; existing seven process steps and chocolate-history experience retained.'

    gifting_category = next(c for c in data['categories'] if c['slug'] == 'gifting')
    services['gifting/'].update({
        'heading': gifting_category['tagline'], 'intro': gifting_category['description'],
        'intro_paragraphs': [gifting_category['description']],
    })

    partner = services['b2b/']
    partner_groups = block('C09').split('\n\n')
    partner_label = partner_groups[0]
    partner_hero = titled(partner_groups[1])
    partner.update({
        'title': partner_label, 'eyebrow': partner_label, 'heading': partner_hero['title'],
        'intro': partner_hero['paragraphs'][0], 'intro_paragraphs': partner_hero['paragraphs'],
        'description': partner_hero['paragraphs'][0], 'topic': 'Partner Brands',
        'section_nav_top': True, 'cta': 'Ask About Partner Brands',
        'cta_route': 'lets-talk/?topic=Partner%20Brands#inquiry',
        'sections': [], 'source': 'C09 verbatim; reuses the existing /b2b/ route.',
    })
    driving = titled(partner_groups[2])
    why = titled(partner_groups[3])
    what = partner_groups[4].splitlines()
    how = partner_groups[5].splitlines()
    how_steps = []
    for line in how[1:]:
        if line in ('Align', 'Prepare', 'Produce', 'Deliver'):
            how_steps.append({'title': line, 'text': ''})
        else:
            how_steps[-1]['text'] += (' ' if how_steps[-1]['text'] else '') + line
    growth = titled(partner_groups[6])
    partner['sections'] = [
        {'id': 'driving-your-brand', 'aliases': ['product-ideas'], **driving},
        {'id': 'why-partner', **why},
        {'id': 'what-we-do', 'title': what[0], 'bullets': [line.removeprefix('•') for line in what[1:]]},
        {'id': 'how-we-do-it', 'aliases': ['craft-and-process'], 'title': how[0], 'ordered_steps': how_steps},
        {'id': 'built-for-growth', 'aliases': ['your-project-brief'], **growth},
    ]

    decor_groups = block('C08').split('\n\n')
    decor_intro = titled(decor_groups[0])
    decor_hero = titled(decor_groups[1])
    decor_body = titled(decor_groups[2])
    data['services'].append({
        'route': 'decor/', 'title': decor_intro['title'], 'eyebrow': decor_intro['title'],
        'heading': decor_hero['title'], 'intro': decor_hero['paragraphs'][0],
        'intro_paragraphs': decor_hero['paragraphs'], 'description': decor_intro['paragraphs'][0],
        'image': 'chocolate-drizzle.webp', 'width': 1500, 'height': 1486,
        'alt': 'A chocolate creation with a decorative drizzle finish',
        'topic': 'Décor', 'section_nav_top': True,
        'sections': [{'id': 'professional-decor', **decor_intro}, {'id': 'created-for-professionals', **decor_body}],
        'cta': 'Ask About Décor', 'cta_route': 'lets-talk/?topic=D%C3%A9cor#inquiry',
        'related_route': 'our-craft/#our-segments', 'related_label': 'Explore Our Segments',
        'source': 'C08 verbatim; existing illustrative asset and shared inquiry behavior.',
    })

    data['topics'] = ['Partner Brands' if topic == 'B2B' else topic for topic in data['topics']]
    data['topics'].insert(data['topics'].index('Partner Brands') + 1, 'Décor')
    data['topic_aliases'] = {'B2B': 'Partner Brands'}
    partner_copy = block('C11').splitlines()
    data['trust_sections']['partners'].update({
        'eyebrow': partner_copy[0], 'title': partner_copy[1],
        'intro_paragraphs': partner_copy[2:], 'intro': ' '.join(partner_copy[2:]),
    })
    return apply_presentation(data)
