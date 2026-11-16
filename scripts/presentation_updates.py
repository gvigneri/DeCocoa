"""November 15 presentation copy and segment routes, layered over retained sources."""
import json
import re
from pathlib import Path
from copy import deepcopy

ROOT = Path(__file__).resolve().parents[1]


def without_em_dashes(text):
    # Spaced heading separators become colons; sentence interruptions become commas.
    return re.sub(r'\s+—\s+', ': ', text).replace('—', ', ')


def apply_presentation(data):
    data['services'] = [page for page in data['services'] if page['route'] != 'wholesale/']
    data['topics'] = [topic for topic in data['topics'] if topic != 'Wholesale']
    home = json.loads((ROOT / 'prototype/homepage-content.json').read_text(encoding='utf-8'))
    data['home'] = home
    categories = {item['slug']: item for item in data['categories']}
    for item in data['categories']:
        item['home_intro'] = home['category_intros'][item['slug']]
    collection_slugs = ('snacking', 'gifting', 'entertaining')
    format_slugs = ('tablet', 'filled', 'covered', 'dipped', 'novelty', 'drink', 'wellness', 'assortment')
    for item in data['categories']:
        item['route'] = item['slug']+'/' if item['slug'] in collection_slugs else 'snacking/#'+item['slug']
    data['chocolate_collections'] = [categories[slug] for slug in collection_slugs]
    data['chocolate_formats'] = [categories[slug] for slug in format_slugs]
    for collection in data['chocolate_collections']:
        if collection['title'] not in data['topics']:
            data['topics'].insert(-1, collection['title'])
    for segment, update in zip(data['business_segments'], home['segments']):
        segment.update(update)

    people = next(page for page in data['pages'] if page['route'] == 'our-people/')
    people.update({'heading':'Our Chocolate Crafters', 'eyebrow':'', 'hide_closing_actions':True})
    roots = next(section for section in people['sections'] if section['id'] == 'our-roots')
    for block in roots['blocks']:
        if block['title'] == 'Today,':
            block['title'] = 'Today'

    craft = next(page for page in data['pages'] if page['route'] == 'our-craft/')
    craft.update({'eyebrow':'', 'hide_closing_actions':True})
    process = next(section for section in craft['sections'] if section['id'] == 'process-capabilities')
    # Keep historic URLs useful without rendering retired process content.
    retired = [process['id'], *process.get('aliases', []), *[item['slug'] for item in data['capabilities']]]
    redirects = {**{alias:'our-craft/' for alias in retired},
                 'our-segments':'our-segments/', 'segments':'our-segments/',
                 **{segment['id']:segment['route'] for segment in data['business_segments']}}
    promise = next(section for section in craft['sections'] if section['id'] == 'promise')
    promise['aliases'] = list(dict.fromkeys(promise.get('aliases', []) + list(redirects)))
    promise['alias_destinations'] = redirects
    craft['sections'] = [section for section in craft['sections'][:craft['sections'].index(process)] if section['id'] != 'our-segments']
    sustainability = next(section for section in craft['sections'] if section['id'] == 'sustainability')
    sustainability.update({'logo_group':'certifications', 'logo_keys':['cacao-trace', 'rainforest']})
    food_safety = next(section for section in craft['sections'] if section['id'] == 'food-safety')
    food_safety.pop('topic', None)
    food_safety.pop('cta', None)

    experience = next(page for page in data['pages'] if page['route'] == 'experience-center/')
    experience['hero_notice'] = 'Coming Soon'
    made = next(section for section in experience['sections'] if section['id'] == 'how-its-made')
    made.pop('related_links', None)
    made.update({'image':'decocoa-factory.gif', 'width':1200, 'height':422,
                 'alt':'The DeCocoa chocolate factory', 'media_position':'before-heading'})
    tours = next(section for section in experience['sections'] if section['id'] == 'tours-and-classes')
    tours.pop('related_links', None)
    experience['cta'] = 'Book Your Appointment'

    craft_your_own = next(page for page in data['services'] if page['route'] == 'craft-your-own/')
    craft_your_own['intro'] = 'Build your own chocolate bar, basket or gift box. Choose the shapes, finishes and details to suit your occasion, and create something uniquely yours.'
    craft_your_own['intro_paragraphs'] = [craft_your_own['intro']]
    craft_your_own['sections'] = [section for section in craft_your_own['sections'] if section['id'] != 'share-your-idea']
    craft_your_own['hide_closing_actions'] = True

    segments = data['business_segments']
    data['pages'].append({
        'route':'our-segments/', 'title':'Our Segments', 'eyebrow':'Our Segments',
        'heading':'Chocolate for every possibility.', 'intro':home['business_intro'],
        'intro_paragraphs':[home['business_intro']],
        **{key:categories['tablet'][key] for key in ('image','width','height','alt')},
        'topic':'Chocolate & products', 'section_nav_top':True,
        'sections':[{'id':'business-segments', 'title':data['business_intro']['title'],
                     'paragraphs':data['business_intro']['paragraphs'], 'items':deepcopy(segments)}],
        'related_route':'lets-talk/#inquiry', 'related_label':"Let's Talk",
    })

    existing = {page['route']:page for page in data['services']}
    for segment in segments:
        if segment['route'] not in existing:
            branded = segment['id'] == 'branded-chocolate'
            product = categories['tablet' if branded else 'assortment']
            page = {
                'route':segment['route'], 'title':segment['label'], 'eyebrow':segment['label'],
                'heading':'Our chocolate. Your everyday delight.' if branded else 'From our craft to your customer.',
                'intro':segment['summary'], 'intro_paragraphs':[segment['summary']],
                'description':segment['summary'],
                **{key:product[key] for key in ('image','width','height','alt')},
                'topic':segment['label'], 'section_nav_top':True,
                'sections':[{'id':segment['id'], 'title':segment['title'], 'paragraphs':segment['paragraphs']}],
                'cta':'Ask About '+segment['label'],
                'cta_route':'lets-talk/?topic='+('Branded%20Chocolate' if branded else 'Fulfillment')+'#inquiry',
                'related_route':'our-segments/', 'related_label':'Explore Our Segments',
            }
            data['services'].append(page)
            existing[segment['route']] = page
            data['topics'].insert(-1, segment['label'])
        page = existing[segment['route']]
        page['hide_closing_actions'] = True
        if segment['id'] == 'branded-chocolate':
            page['chocolate_tiles'] = 'collections'
        elif segment['id'] == 'partner-brands':
            page['chocolate_tiles'] = 'formats'
            growth_index = next(index for index, section in enumerate(page['sections']) if section['id'] == 'built-for-growth')
            page['sections'].insert(growth_index + 1, {key:deepcopy(process[key]) for key in ('id', 'title', 'paragraphs')})
        else:
            # Supply a real runtime asset here when Guy provides each PDF.
            page['pdf_action'] = {'label':'View '+segment['label']+' PDF', 'asset':None}
    return data
