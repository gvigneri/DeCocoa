"""Build the existing portable site from authoritative content and shared partials.

Python standard library only. Original artwork and *-master.svg files are inputs.
"""
from pathlib import Path
from html import escape, unescape
from urllib.parse import quote, urlsplit, urljoin
import hashlib, json, posixpath, re
from content_updates import apply_content
from presentation_updates import without_em_dashes
from navigation_components import load_navigation, navigation as render_navigation
from shared_components import hero, paragraphs, image, family_timeline, info_grid
ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'prototype'
DATA=json.loads((SITE/'site-content.json').read_text(encoding='utf-8'))
DATA=apply_content(DATA)
DATA['navigation']=load_navigation(SITE)
ICONS={name:(ROOT/f'assets/icons/fontawesome-free-6.7.2/{name}.svg').read_text(encoding='utf-8') for name in ('arrow-right','arrow-right-long','gift','wand-magic-sparkles','handshake','shield-heart','leaf','gears')}
def read(name): return (SITE/name).read_text(encoding='utf-8')
def url(route,current):
    parts=urlsplit(route)
    if not parts.path and parts.fragment:return ('?'+parts.query if parts.query else '')+'#'+parts.fragment
    base=current if current.endswith('/') else posixpath.dirname(current)
    result=posixpath.relpath(parts.path or '.',base or '.')
    if not parts.path or parts.path.endswith('/'): result=result.rstrip('/')+'/'
    return result+('?' + parts.query if parts.query else '')+('#'+parts.fragment if parts.fragment else '')
def link(item,current,cls=''):
    attrs=(' class="'+cls+'"' if cls else '')+' href="'+escape(url(item['route'],current),quote=True)+'"'
    if item['route']==current: attrs+=' aria-current="page"'
    return '<a'+attrs+'>'+escape(item['label'])+'</a>'
def navigation(current,prefix):
    return render_navigation(DATA,current,prefix,url,link)
def pattern(key,name):
    svg=(ROOT/f'assets/patterns/{name}-master.svg').read_text(encoding='utf-8')
    svg=re.sub(r'(class="pattern-background" fill=")#[0-9a-fA-F]+',r'\g<1>#3A170D',svg)
    for old in re.findall(r'\bid="([^"]+)"',svg):
        svg=svg.replace(f'id="{old}"',f'id="{key}-{old}"').replace(f'url(#{old})',f'url(#{key}-{old})')
    svg=svg.replace('<svg ','<svg aria-hidden="true" focusable="false" preserveAspectRatio="xMidYMid slice" ')
    return svg
PATTERN_SOURCES={'hero':'stripes','people':'floweroflife','experience':'growth','craft':'rings'}
PATTERNS={key:pattern(key,name) for key,name in PATTERN_SOURCES.items()}
def cards(current,exclude=None):
    out=[]
    for p in DATA['products']:
        if p['slug']==exclude: continue
        href=url('products/'+p['slug']+'/',current)
        out.append(f'<article class="product-item"><a class="product-card-link" href="{href}"><div class="card product-image {p["class"]}"><img src="{{{{asset:images/{p["image"]}}}}}" width="{p["width"]}" height="{p["height"]}" alt="{escape(p["alt"])}" loading="lazy"></div><h3><span class="product-caption">{escape(p["caption"])}</span> <span>{escape(p["title"])}</span></h3><span class="text-link">Explore {escape(p["title"])}</span></a></article>')
    return ''.join(out)

def icon(name):
    svg=ICONS[name]
    return svg.replace('<svg ','<svg class="fa-icon" aria-hidden="true" focusable="false" fill="currentColor" ',1)

def category_cards():
    out=[]
    for c in DATA['chocolate_formats']:
        prefix='category-'+c['slug']
        out.append(f'<article class="category-card" aria-labelledby="{prefix}-title"><div class="category-image surface-{c["surface"]}"><span class="reveal-drop"><img src="{{{{asset:images/{c["image"]}}}}}" width="{c["width"]}" height="{c["height"]}" alt="{escape(c["alt"])}" loading="lazy" draggable="false"></span></div><div class="category-copy"><h3 id="{prefix}-title">{escape(c["title"])} <span class="category-tagline">{escape(c["tagline"])}</span></h3><p class="category-intro">{escape(c["home_intro"])}</p></div></article>')
    return ''.join(out)

def category_block(c,current,capability=False,topic=None,action_route=None,show_action=True):
    rank='h3' if capability else 'h2'
    tagline=' <span class="category-tagline">'+escape(c['tagline'])+'</span>' if c.get('tagline') else ''
    action=('<a class="button button-primary" href="'+escape(url(action_route,current),quote=True)+'">Explore '+escape(c['title'])+'</a>' if action_route else inquiry(topic or ('Our craft' if capability else 'Chocolate & products'),current,'Ask About '+c['title']))
    if not show_action:action=''
    return '<section class="category-block" id="'+c['slug']+'" aria-labelledby="'+c['slug']+'-title">'+image(c,'category-image')+'<div><'+rank+' id="'+c['slug']+'-title">'+escape(c['title'])+tagline+'</'+rank+'>'+paragraphs([c['description']])+action+'</div></section>'

def discovery_cards(current):
    return ''.join(f'<a class="segment-card" href="{escape(url(c["route"],current),quote=True)}"><span class="segment-icon">'+icon(c['icon'])+f'</span><h3>{escape(c["label"])} <span class="segment-kicker">{escape(c["kicker"])}</span></h3><span class="segment-rule" aria-hidden="true"></span><p class="segment-summary">{escape(c["summary"])}</p><span class="segment-action">Explore '+escape(c['label'])+icon('arrow-right')+'</span></a>' for c in DATA['business_segments'])

def hero_bark_art():
    images=json.loads(read('hero-bark.json'))['images']
    return ''.join('<span class="pretzel-drop '+image['motion_class']+' bark-piece bark-piece-'+image['id']+'"><img class="hero-pretzel bark-image" src="{{asset:'+image['image']+'}}" srcset="'+', '.join('{{asset:'+variant['image']+'}} '+str(variant['width'])+'w' for variant in image['variants'])+'" sizes="'+escape(image['sizes'],quote=True)+'" width="'+str(image['width'])+'" height="'+str(image['height'])+'" alt="'+escape(image['alt'],quote=True)+'" decoding="async"'+(' fetchpriority="high"' if index==0 else '')+'></span>' for index,image in enumerate(images))
def inquiry(topic,current,label='Start an Inquiry'):
    variant='button-primary'+(' button-talk' if label.replace('\u2019',"'")=="Let's Talk" else '')
    return '<a class="button '+variant+'" href="'+escape(url('lets-talk/?topic='+quote(topic)+'#inquiry',current),quote=True)+'">'+escape(label)+'</a>'
def chocolate_history(section):
    history=json.loads(read('chocolate-history.json'))
    chapters=[]
    for chapter in history['chapters']:
        layers=[]
        for index,layer in enumerate(chapter['layers']):
            placement=';'.join('--layer-'+key+':'+str(value) for key,value in layer['placement'].items())
            placement+=';--layer-delay:'+str(round(index*.1,2))+'s'
            src='{{asset:'+layer['asset']+'}}'
            responsive=''
            if layer.get('variants'):
                responsive=' srcset="'+', '.join('{{asset:'+v['asset']+'}} '+str(v['width'])+'w' for v in layer['variants'])+'" sizes="'+escape(layer['sizes'],quote=True)+'"'
            decorative=' aria-hidden="true"' if layer['decorative'] else ''
            layers.append('<span class="history-layer history-layer--'+escape(layer['role'],quote=True)+'" style="'+escape(placement,quote=True)+'"'+decorative+'><span class="history-visual"><img src="'+src+'"'+responsive+' width="'+str(layer['width'])+'" height="'+str(layer['height'])+'" alt="'+escape(layer['alt'],quote=True)+'" loading="lazy" decoding="async"></span></span>')
        template=read('chocolate-history-chapter.template.html')
        values={**chapter,'scene-style':';'.join('--scene-'+key+':'+str(value) for key,value in chapter['scene'].items()),'layers':''.join(layers),'source-label':chapter['source_label'],'source-icon':icon('arrow-right-long')}
        for key,value in values.items():
            template=template.replace('{{history-'+key+'}}',value if key in ('layers','source-icon') else escape(str(value),quote=True))
        chapters.append(template)
    aliases=''.join('<span class="anchor-alias" id="'+alias+'" aria-hidden="true"></span>' for alias in section.get('aliases',[]))
    return '<section class="content-section chocolate-history" id="'+section['id']+'" aria-labelledby="'+section['id']+'-title">'+aliases+'<div class="history-intro"><h2 class="section-title" id="'+section['id']+'-title"><span class="eyebrow">'+escape(section['title'])+'</span> <span class="heading-title">'+escape(history['heading'])+'</span></h2>'+paragraphs(section.get('paragraphs',[]))+'<p>'+escape(history['intro'])+'</p></div><ol class="history-list" aria-label="Chocolate history">'+''.join(chapters)+'</ol></section>'
def related_link(item):
    styles={'text':'text-link','primary':'button button-primary'}
    style=item.get('style','text')
    if style not in styles:raise ValueError('Unsupported related-link style: '+style)
    return '<a class="'+styles[style]+'" href="{{url:'+item['route']+'}}">'+escape(item['label'])+'</a>'
def sections(page):
    out=[]
    for s in page['sections']:
        if page['route']=='experience-center/' and s['id']=='museum-virtual-exhibition':
            out.append(chocolate_history(s))
            continue
        aliases=''.join('<span class="anchor-alias" id="'+alias+'"'+(' data-capability-destination="{{url:'+s['alias_destinations'][alias]+'}}"' if alias in s.get('alias_destinations',{}) else '')+' aria-hidden="true"></span>' for alias in s.get('aliases',[]))
        actions=(inquiry(s['topic'],page['route'],s.get('cta',"Let's Talk")) if s.get('topic') else '')
        if s.get('related_route'):actions+='<a class="text-link" href="{{url:'+s['related_route']+'}}">'+escape(s['related_label'])+'</a>'
        actions+=''.join(related_link(item) for item in s.get('related_links',[]))
        if page['route']=='experience-center/' and s['id']=='tours-and-classes':
            actions+='<a class="button button-primary" href="{{url:'+page['cta_route']+'}}">'+escape(page['cta'])+'</a>'
        items=info_grid(s.get('items',[]))
        bullets=''.join('<li>'+escape(item)+'</li>' for item in s.get('bullets',[]))
        steps=''.join('<li><h3>'+escape(step['title'])+'</h3><p>'+escape(step['text'])+'</p></li>' for step in s.get('ordered_steps',[]))
        blocks=''.join('<div class="content-block">'+('<h3>'+escape(block['title'])+'</h3>' if block.get('title') else '')+paragraphs(block.get('paragraphs',[]))+'</div>' for block in s.get('blocks',[]))
        timeline=family_timeline(s['timeline']) if s.get('timeline') else ''
        media=image(s,'card content-media') if s.get('image') else ''
        leading_media=''
        if media and s.get('media_position')=='before-heading':
            leading_media=image(s,'card content-media content-media--leading')
            media=''
        logos='<ul class="logo-marks sustainability-marks" aria-label="Sustainability programs">'+logo_marks(s['logo_group'],s['logo_keys'])+'</ul>' if s.get('logo_group') else ''
        capabilities=''.join(category_block(c,page['route'],True) for c in s.get('capabilities',[]))
        out.append('<section class="content-section" id="'+s['id']+'" aria-labelledby="'+s['id']+'-title">'+aliases+leading_media+'<h2 id="'+s['id']+'-title">'+escape(s['title'])+'</h2>'+paragraphs(s.get('paragraphs',[]))+blocks+timeline+('<ul class="content-bullets">'+bullets+'</ul>' if bullets else '')+('<ol class="content-steps">'+steps+'</ol>' if steps else '')+items+media+capabilities+logos+('<div class="closing-actions">'+actions+'</div>' if actions else '')+'</section>')
    return ''.join(out)
def general(page):
    fc='page-hero-media experience-photo' if page.get('mask') else 'page-hero-media card page-photo'
    figure=image(page,fc,True)
    topic=page.get('topic') or {'our-people/':'Our story','our-craft/':'Our craft','experience-center/':'Experience Center'}[page['route']]
    related='<a class="button button-primary" href="{{url:'+page['related_route']+'}}">'+escape(page['related_label'])+'</a>' if page.get('related_route') else inquiry(topic,page['route'],"Let's Talk")
    primary='<a class="button button-primary" href="{{url:'+page['cta_route']+'}}">'+escape(page['cta'])+'</a>' if page.get('cta') else ''
    closing='' if page['route']=='experience-center/' or page.get('hide_closing_actions') else '<div class="closing-actions">'+primary+related+'</div>'
    if page.get('chocolate_tiles'):
        collections=page['chocolate_tiles']=='collections'
        items=DATA['chocolate_collections' if collections else 'chocolate_formats']
        closing='<div class="category-tiles">'+''.join(category_block(item,page['route'],action_route=item['route'] if collections else None,show_action=collections) for item in items)+'</div>'
    if page.get('pdf_action'):
        pdf=page['pdf_action']
        if pdf.get('asset'):
            control='<a class="button button-primary" href="{{asset:'+pdf['asset']+'}}">'+escape(pdf['label'])+'</a>'
            status=''
        else:
            control='<button class="button button-primary" type="button" disabled aria-describedby="pdf-status">'+escape(pdf['label'])+'</button>'
            status='<p id="pdf-status">PDF coming soon.</p>'
        closing='<div class="pdf-action">'+control+status+'</div>'
    intro=hero(read,page['eyebrow'],page['heading'],page.get('intro_paragraphs',[page['intro']]),figure,notice=page.get('hero_notice',''))
    return intro+'<div class="container editorial-layout"><div class="editorial-content">'+sections(page)+closing+'</div></div>'
def inquiry_section(section_id='inquiry',stacked=False):
    return read('partials/inquiry.html').replace('{{inquiry-id}}',section_id).replace('{{inquiry-layout}}',' home-inquiry' if stacked else '').replace('{{inquiry-intro}}','A question, an idea, a chocolate possibility.' if stacked else 'Choose a topic and add your questions below.')
def logo_marks(section_id, selected=None):
    section=DATA['trust_sections'][section_id]
    links=json.loads(read('logo-links.json'))[section_id]
    marks=[]
    for mark in section['marks']:
        if selected is not None and mark['class'] not in selected:continue
        img='<img src="{{asset:images/'+mark['image']+'}}" width="'+str(mark['width'])+'" height="'+str(mark['height'])+'" alt="'+escape(mark['alt'])+'" loading="lazy">'
        href=links[mark['class']]['href']
        if href:img='<a class="logo-link" href="'+escape(href,quote=True)+'" target="_blank" rel="noopener noreferrer" aria-label="'+escape(mark['alt'],quote=True)+' (opens in a new tab)">'+img+'</a>'
        marks.append('<li class="mark-'+mark['class']+'">'+img+'</li>')
    return ''.join(marks)

def trust_section(section_id):
    section=DATA['trust_sections'][section_id]
    html=read('trust-section.template.html')
    for key,value in {'id':section_id,'eyebrow':escape(section['eyebrow']),'title':escape(section['title']),'intro':paragraphs(section.get('intro_paragraphs',[section['intro']])),'marks':logo_marks(section_id)}.items():html=html.replace('{{trust-'+key+'}}',value)
    return html
def contact():
    return hero(read,"Let's Talk",'Tell us what you have in mind.',['A chocolate question, a gift idea or a project for your business. Choose a topic and share the details you would like to discuss.'])+inquiry_section()
def service_cards(current):
    return ''.join('<a class="service-card" href="'+url(page['route'],current)+'"><h3>'+escape(page['eyebrow'])+'</h3><p>'+escape(page['intro'])+'</p><span>Explore '+escape(page['eyebrow'])+'</span></a>' for page in DATA['services'])
def render(route,title,description,content,body_class,noindex=False):
    header=read('partials/header.html').replace('{{navigation-original}}',navigation(route,'main')).replace('{{navigation-scroll}}',navigation(route,'scroll'))
    collection_routes={item['route'] for item in DATA['chocolate_collections']}
    possibilities=[{'label':item['title'],'route':item['route']} for item in DATA['chocolate_collections']]+[{'label':item['eyebrow'],'route':item['route']} for item in DATA['services'] if item['route'] not in collection_routes]
    footer=read('partials/footer.html').replace('{{footer-explore}}',''.join(link(i,route) for i in DATA['navigation'])).replace('{{footer-possibilities}}',''.join(link(item,route) for item in possibilities))
    footer=footer.replace('{{footer-policies}}',''.join(link({'label':item['title'],'route':item['route']},route) for item in DATA['policies']))
    html=read('site.template.html')
    for key,value in {'title':escape(title),'description':escape(description,quote=True),'content':content,'header':header,'footer':footer,'body-class':body_class,'robots':'<meta name="robots" content="noindex">' if noindex else ''}.items(): html=html.replace('{{'+key+'}}',value)
    for key,value in PATTERNS.items(): html=html.replace('{{pattern-'+key+'}}',value)
    for name in DATA['trust_sections']:html=html.replace('{{'+name+'-section}}',trust_section(name))
    if route=='':
        home_hero=hero(read,'Chocolate crafters','Experience. Chocolate.',['At DeCocoa, every chocolate is handcrafted with care using the world’s finest sustainably sourced cocoa.'],'<figure class="hero-art" aria-label="Three separate pieces of chocolate bark">'+hero_bark_art()+'</figure>','<a class="button button-secondary" href="{{url:lets-talk/#inquiry}}">Let’s Craft Something Together</a>',home=True)
        html=html.replace('{{home-hero}}',home_hero)
        html=html.replace('{{experience-intro-paragraphs}}',paragraphs([DATA['home']['experience_intro']]))
        for key in ('people','craft'):
            html=html.replace('{{'+key+'-heading}}',escape(DATA['home_section_headings']['our-'+key])).replace('{{'+key+'-intro-paragraphs}}',paragraphs([DATA['home'][key+'_intro']]))
        craft=next(page for page in DATA['pages'] if page['route']=='our-craft/')
        highlights=[]
        for section in craft['sections']:
            if section['id'] not in DATA['home']['craft_highlights']:continue
            copy=[DATA['home']['craft_highlights'][section['id']]]
            highlights.append('<li><a class="craft-summary-link" href="{{url:our-craft/#'+section['id']+'}}">'+escape(section.get('nav_title',section['title']))+'</a>'+paragraphs(copy)+'</li>')
        html=html.replace('{{craft-highlights}}','<ul class="craft-highlight-list">'+''.join(highlights)+'</ul>')
        business='<section class="business-overview" id="segments" aria-labelledby="discover-title"><div class="container"><div class="business-intro"><h2 class="section-title" id="discover-title"><span class="eyebrow">'+escape(DATA['home']['business_eyebrow'])+'</span> <span class="heading-title">'+escape(DATA['business_intro']['title'])+'</span></h2>'+paragraphs([DATA['home']['business_intro']])+'</div><div class="segment-grid">'+discovery_cards(route)+'</div></div></section>'
        html=html.replace('{{business-overview}}',business)
    for key,value in {'chocolate-eyebrow':escape(DATA['chocolate_intro']['eyebrow']),'chocolate-heading':escape(DATA['chocolate_intro']['heading']),'chocolate-intro':escape(DATA['chocolate_intro']['text']),'category-cards':category_cards(),'discovery-cards':discovery_cards(route)}.items():html=html.replace('{{'+key+'}}',value)
    html=re.sub(r'\{\{icon:([^}]+)\}\}',lambda m:icon(m[1]),html)
    html=html.replace('{{category-script}}','<script src="{{asset:js/category-motion.js}}?v=1" defer></script>' if route=='' else '')
    html=html.replace('{{history-assets}}','<link rel="stylesheet" href="{{asset:css/chocolate-history.css}}?v=7"><script src="{{asset:js/chocolate-history.js}}?v=1" defer></script>' if route=='experience-center/' else '')
    html=html.replace('{{product-cards}}',cards(route)).replace('{{topic-options}}',''.join('<option>'+escape(t)+'</option>' for t in DATA['topics'])).replace('{{product-options}}',''.join('<option value="'+p['slug']+'">'+escape(p['title'])+'</option>' for p in DATA['products']))
    html=re.sub(r'\{\{url:([^}]*)\}\}',lambda m:escape(url(m[1],route),quote=True),html)
    base=route if route.endswith('/') else posixpath.dirname(route)
    asset_base=posixpath.relpath('assets',base or '.')
    html=re.sub(r'\{\{asset:([^}]+)\}\}',lambda m:asset_base+'/'+m[1],html)
    # A recovery response may be served at any missing URL depth. Its resource
    # and destination URLs therefore use the public root; fragments stay local.
    if route=='404.html':
        def recovery_url(match):
            value=unescape(match[2])
            if value.startswith('#') or urlsplit(value).scheme or urlsplit(value).netloc:
                return match[0]
            return match[1]+'="'+escape(urljoin('/404.html',value),quote=True)+'"'
        html=re.sub(r'(href|src)="([^"]+)"',recovery_url,html)
    html=without_em_dashes(html)
    if '{{' in html: raise ValueError('Unresolved token on '+route)
    path=SITE/(route+'index.html' if route.endswith('/') or not route else route)
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(html,encoding='utf-8',newline='\n')
    return {'route':'/'+route,'file':path.relative_to(ROOT).as_posix(),'title':title,'sha256':hashlib.sha256(html.encode()).hexdigest()}
def build():
    inventory=[]
    inventory.append(render('',DATA['home']['hero_heading'],'Explore DeCocoa chocolate products, gifting ideas, the craft and the people behind them.',read('homepage.template.html').replace('{{inquiry-home}}',inquiry_section('talk',stacked=True)),'homepage'))
    chocolate_media=image(DATA['products'][0],'page-hero-media card product-image product-filled',True)
    legacy=[{'slug':c['slug'],'route':c['route'],'label':'Explore '+c['title']} for c in DATA['chocolate_formats']]+[{'slug':c['slug'],'route':'our-craft/','label':'Explore Our Craft'} for c in DATA['capabilities']]
    compatibility='<div class="compatibility-links">'+''.join('<section id="'+c['slug']+'" data-capability-destination="'+escape(url(c['route'],'products/'),quote=True)+'"><a href="{{url:'+c['route']+'}}">'+escape(c['label'])+'</a></section>' for c in legacy)+'</div>'
    collection_tiles=''.join(category_block(c,'products/',action_route=c['route']) for c in DATA['chocolate_collections'])
    listing=hero(read,'Our Chocolate','Experience. Chocolate.',media=chocolate_media)+'<div class="container product-overview"><div class="category-tiles">'+collection_tiles+'</div>'+compatibility+'</div>'
    inventory.append(render('products/','Our Chocolate','Explore DeCocoa chocolate for snacking, gifting and entertaining, with eight chocolate categories for every occasion.',listing,'interior'))
    collection_routes={item['route'] for item in DATA['chocolate_collections']}
    for collection in DATA['chocolate_collections']:
        route=collection['route']
        intro=hero(read,collection['title'],collection['tagline'],[collection['description']],image(collection,'page-hero-media card category-collection-photo',True))
        aliases=''.join('<span class="anchor-alias" id="'+name+'" aria-hidden="true"></span>' for name in ('occasions','corporate-gifts','planning-details')) if route=='gifting/' else ''
        tiles=''.join(category_block(category,route,topic=collection['title']) for category in DATA['chocolate_formats'])
        content=intro+'<div class="container product-overview">'+aliases+'<div class="category-tiles">'+tiles+'</div></div>'
        inventory.append(render(route,'Chocolate '+collection['title'],collection['description'],content,'interior chocolate-collection'))
    for p in DATA['products']:
        route='products/'+p['slug']+'/'
        template=read('product-detail.template.html')
        product_hero=hero(read,'Our Chocolate',p['title'],[p['description'],p['detail']],image(p,'page-hero-media card product-image '+p['class'],True),inquiry('Chocolate & products',route,'Ask About This Chocolate').replace('#inquiry','&amp;product='+p['slug']+'#inquiry')+'<a class="text-link" href="{{url:products/}}">Explore all chocolate</a>')
        template=template.replace('{{product-hero}}',product_hero)
        values={**p,'inquiry':escape(url('lets-talk/?topic=Chocolate%20%26%20products&product='+p['slug']+'#inquiry',route),quote=True)}
        for key,value in values.items(): template=template.replace('{{product-'+key+'}}',str(value) if key in ('width','height','inquiry') else escape(str(value),quote=True))
        template=template.replace('{{related-products}}',cards(route,p['slug']))
        inventory.append(render(route,p['title'],p['description'],template,'interior'))
    for page in DATA['pages']:
        body_class='interior'+(' experience-history' if page['route']=='experience-center/' else '')
        inventory.append(render(page['route'],page['title'],page['intro'],general(page),body_class))
    for page in DATA['services']:
        if page['route'] not in collection_routes:
            inventory.append(render(page['route'],page['title'],page['description'],general(page),'interior service-landing'))
    inventory.append(render('lets-talk/',"Let's Talk",'Ask DeCocoa about chocolate products, gifting, Craft Your Own, fundraising, business projects and the Experience Center.',contact(),'interior'))
    for page in DATA['policies']:
        content=hero(read,page['title'],page['title'],[page['notice']])
        inventory.append(render(page['route'],page['title'],page['notice'],content,'interior',noindex=True))
    recovery=hero(read,'Page not found','Something is missing.',['The page you are looking for may have moved. Keep exploring our chocolate or find your way home.'],actions='<a class="button button-primary" href="{{url:products/}}">Explore Our Products</a><a class="button button-primary" href="{{url:}}">Go Home</a>')
    inventory.append(render('404.html','Page Not Found','Find your way back to DeCocoa products and information.',recovery,'interior'))
    for key,name in PATTERN_SOURCES.items(): (ROOT/f'assets/patterns/{name}-website.svg').write_text(PATTERNS[key],encoding='utf-8',newline='\n')
    (SITE/'generated-pages.json').write_text(json.dumps({'build':'presentation-2026-11-15','pages':inventory,'sources':['prototype/homepage-content.json','scripts/presentation_updates.py','prototype/approved-content.json','prototype/navigation.json','prototype/logo-links.json','prototype/partials/hero.html','scripts/shared_components.py','scripts/content_updates.py','scripts/navigation_components.py','prototype/site-content.json','prototype/site.template.html','prototype/homepage.template.html','prototype/hero-bark.json','prototype/product-detail.template.html','prototype/trust-section.template.html','prototype/chocolate-history.json','prototype/chocolate-history-chapter.template.html','prototype/partials/header.html','prototype/partials/footer.html','prototype/partials/inquiry.html']},indent=2)+'\n',encoding='utf-8')
    print(f'Built {len(inventory)} local pages from shared templates and content. Original artwork unchanged.')
if __name__=='__main__': build()
