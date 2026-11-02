"""Build the existing portable site from authoritative content and shared partials.

Python standard library only. Original artwork and *-master.svg files are inputs.
"""
from pathlib import Path
from html import escape, unescape
from urllib.parse import quote, urlsplit, urljoin
import hashlib, json, posixpath, re
ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'prototype'
DATA=json.loads((SITE/'site-content.json').read_text(encoding='utf-8'))
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
    parts=[]
    for item in DATA['navigation']:
        if item.get('children'):
            active=' is-current' if current.startswith(item['route']) or any(child['route'].split('#')[0]==current for child in item['children']) else ''
            menu_id=prefix+'-'+item['route'].strip('/').replace('/','-')+'-menu'
            parts.append('<div class="nav-dropdown"><button type="button" class="nav-link submenu-toggle'+active+'" aria-expanded="false" aria-controls="'+menu_id+'">'+escape(item['label'])+'</button><div class="submenu" id="'+menu_id+'" hidden>'+''.join(link(child,current) for child in item['children'])+'</div></div>')
        else: parts.append(link(item,current,'nav-link'))
    parts.append('<a class="nav-link nav-mobile-contact" href="'+url('lets-talk/#inquiry',current)+'">Let\'s Talk</a>')
    return ''.join(parts)
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
        out.append(f'<article class="product-item"><a class="product-card-link" href="{href}"><div class="card product-image {p["class"]}"><img src="{{{{asset:images/{p["image"]}}}}}" width="{p["width"]}" height="{p["height"]}" alt="{escape(p["alt"])}" loading="lazy"></div><p>{escape(p["caption"])}</p><h3>{escape(p["title"])}</h3><span class="text-link">Explore {escape(p["title"])}</span></a></article>')
    return ''.join(out)

def icon(name):
    svg=ICONS[name]
    return svg.replace('<svg ','<svg class="fa-icon" aria-hidden="true" focusable="false" fill="currentColor" ',1)

def category_cards(current,static=False):
    out=[]
    for index,c in enumerate(DATA['categories']):
        heading='h2' if static else 'h3'
        route='lets-talk/?topic=Chocolate%20%26%20products#inquiry' if static else 'products/#'+c['slug']
        label='Ask About '+c['title'] if static else 'Explore '+c['title']
        prefix=c['slug'] if static else 'category-'+c['slug']
        attrs=f' id="{c["slug"]}"' if static else ''
        out.append(f'<a class="category-card"{attrs} draggable="false" href="{escape(url(route,current),quote=True)}" aria-labelledby="{prefix}-action" style="--reveal-delay:{index*.14:.2f}s"><div class="category-image surface-{c["surface"]}"><span class="reveal-drop"><img src="{{{{asset:images/{c["image"]}}}}}" width="{c["width"]}" height="{c["height"]}" alt="{escape(c["alt"])}" loading="lazy" draggable="false"></span></div><div class="category-copy"><{heading} id="{prefix}-title">{escape(c["title"])}</{heading}><p>{escape(c["description"])}</p><span class="category-action" id="{prefix}-action">{escape(label)}'+icon('arrow-right')+'</span></div></a>')
    return ''.join(out)

def discovery_cards(current):
    return ''.join(f'<a class="discovery-card" data-reveal href="{escape(url(c["route"],current),quote=True)}" style="--reveal-delay:{index*.16:.2f}s"><span class="discovery-icon reveal-drop">'+icon(c['icon'])+f'</span><h4>{escape(c["title"])}</h4><p>{escape(c["text"])}</p><span class="discovery-action">{escape(c.get("link_label","Explore "+c["title"]))}'+icon('arrow-right')+'</span></a>' for index,c in enumerate(DATA['discovery_cards']))
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
    return '<section class="content-section chocolate-history" id="'+section['id']+'" aria-labelledby="'+section['id']+'-title">'+aliases+'<div class="history-intro"><h2 class="section-title" id="'+section['id']+'-title"><span class="eyebrow">'+escape(section['title'])+'</span> <span class="heading-title">'+escape(history['heading'])+'</span></h2><p>'+escape(history['intro'])+'</p></div><ol class="history-list" aria-label="Chocolate history">'+''.join(chapters)+'</ol><div class="history-invitation"><h3>'+escape(history['invitation'])+'</h3><a class="button button-primary" href="{{url:'+history['cta_route']+'}}">'+escape(history['cta_label'])+'</a></div></section>'
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
        aliases=''.join('<span class="anchor-alias" id="'+alias+'" aria-hidden="true"></span>' for alias in s.get('aliases',[]))
        actions=(inquiry(s['topic'],page['route'],s.get('cta',"Let's Talk")) if s.get('topic') else '')
        if s.get('related_route'):actions+='<a class="text-link" href="{{url:'+s['related_route']+'}}">'+escape(s['related_label'])+'</a>'
        actions+=''.join(related_link(item) for item in s.get('related_links',[]))
        if page['route']=='experience-center/' and s['id']=='tours-and-classes':
            actions+='<a class="button button-primary" href="{{url:'+page['cta_route']+'}}">'+escape(page['cta'])+'</a>'
        items=''.join('<article class="info-item"><h3>'+escape(i['title'])+'</h3><p>'+escape(i['text'])+'</p></article>' for i in s.get('items',[]))
        bullets=''.join('<li>'+escape(item)+'</li>' for item in s.get('bullets',[]))
        steps=''.join('<li><h3>'+escape(step['title'])+'</h3><p>'+escape(step['text'])+'</p></li>' for step in s.get('ordered_steps',[]))
        out.append('<section class="content-section" id="'+s['id']+'" aria-labelledby="'+s['id']+'-title">'+aliases+'<h2 id="'+s['id']+'-title">'+escape(s['title'])+'</h2>'+''.join('<p>'+escape(p)+'</p>' for p in s.get('paragraphs',[]))+('<ul class="content-bullets">'+bullets+'</ul>' if bullets else '')+('<ol class="content-steps">'+steps+'</ol>' if steps else '')+('<div class="info-grid">'+items+'</div>' if items else '')+('<div class="closing-actions">'+actions+'</div>' if actions else '')+'</section>')
    return ''.join(out)
def general(page):
    fc='experience-photo' if page.get('mask') else 'card page-photo'
    figure=f'<figure class="{fc}"><img src="{{{{asset:images/{page["image"]}}}}}" width="{page["width"]}" height="{page["height"]}" alt="{escape(page["alt"])}" fetchpriority="high"></figure>'
    jumps=''.join('<a href="#'+s['id']+'">'+escape(s['title'])+'</a>' for s in page['sections'])
    topic=page.get('topic') or {'our-people/':'Our story','our-craft/':'Our craft','experience-center/':'Experience Center'}[page['route']]
    related='<a class="button button-primary" href="{{url:'+page['related_route']+'}}">'+escape(page['related_label'])+'</a>' if page.get('related_route') else inquiry(topic,page['route'],"Let's Talk")
    closing='' if page['route']=='experience-center/' else '<div class="closing-actions"><a class="button button-primary" href="{{url:'+page['cta_route']+'}}">'+escape(page['cta'])+'</a>'+related+'</div>'
    heading='<h1 id="page-title">'+escape(page['heading'])+'</h1>' if page.get('simple_heading') else '<h1 id="page-title" class="section-title"><span class="eyebrow">'+escape(page['eyebrow'])+'</span> <span class="heading-title">'+escape(page['heading'])+'</span></h1>'
    intro=''.join('<p class="lead">'+escape(paragraph)+'</p>' for paragraph in page.get('intro_paragraphs',[page['intro']]))
    return '<section class="page-intro container"><div>'+heading+intro+'</div>'+figure+'</section><div class="container editorial-layout"><nav class="section-nav" aria-label="On this page">'+jumps+'</nav><div class="editorial-content">'+sections(page)+closing+'</div></div>'
def inquiry_section(section_id='inquiry',stacked=False):
    return read('partials/inquiry.html').replace('{{inquiry-id}}',section_id).replace('{{inquiry-layout}}',' home-inquiry' if stacked else '').replace('{{inquiry-intro}}','A question, an idea, a chocolate possibility.' if stacked else 'Choose a topic and add your questions below.')
def trust_section(section_id):
    section=DATA['trust_sections'][section_id]
    marks=''.join('<li class="mark-'+mark['class']+'"><img src="{{asset:images/'+mark['image']+'}}" width="'+str(mark['width'])+'" height="'+str(mark['height'])+'" alt="'+escape(mark['alt'])+'" loading="lazy"></li>' for mark in section['marks'])
    html=read('trust-section.template.html')
    for key,value in {'id':section_id,'eyebrow':escape(section['eyebrow']),'title':escape(section['title']),'intro':escape(section['intro']),'marks':marks}.items():html=html.replace('{{trust-'+key+'}}',value)
    return html
def contact():
    return '<section class="container page-intro text-intro"><div><h1 id="page-title" class="section-title"><span class="eyebrow">Let\'s Talk</span> <span class="heading-title">Tell us what you have in mind.</span></h1><p class="lead">A chocolate question, a gift idea or a project for your business. Choose a topic and share the details you would like to discuss.</p></div></section>'+inquiry_section()
def service_cards(current):
    return ''.join('<a class="service-card" href="'+url(page['route'],current)+'"><h3>'+escape(page['eyebrow'])+'</h3><p>'+escape(page['intro'])+'</p><span>Explore '+escape(page['eyebrow'])+'</span></a>' for page in DATA['services'])
def render(route,title,description,content,body_class,noindex=False):
    header=read('partials/header.html').replace('{{navigation-original}}',navigation(route,'main')).replace('{{navigation-scroll}}',navigation(route,'scroll'))
    footer=read('partials/footer.html').replace('{{footer-explore}}',''.join(link(i,route) for i in DATA['navigation'])).replace('{{footer-possibilities}}',''.join(link({'label':i['eyebrow'],'route':i['route']},route) for i in DATA['services']))
    footer=footer.replace('{{footer-policies}}',''.join(link({'label':item['title'],'route':item['route']},route) for item in DATA['policies']))
    html=read('site.template.html')
    for key,value in {'title':escape(title),'description':escape(description,quote=True),'content':content,'header':header,'footer':footer,'body-class':body_class,'robots':'<meta name="robots" content="noindex">' if noindex else ''}.items(): html=html.replace('{{'+key+'}}',value)
    for key,value in PATTERNS.items(): html=html.replace('{{pattern-'+key+'}}',value)
    for name in DATA['trust_sections']:html=html.replace('{{'+name+'-section}}',trust_section(name))
    if route=='':
        html=html.replace('{{hero-bark-art}}',hero_bark_art())
        experience=next(page for page in DATA['pages'] if page['route']=='experience-center/')
        html=html.replace('{{experience-intro-paragraphs}}',''.join('<p>'+escape(paragraph)+'</p>' for paragraph in experience['intro_paragraphs']))
    for key,value in {'chocolate-eyebrow':escape(DATA['chocolate_intro']['eyebrow']),'chocolate-heading':escape(DATA['chocolate_intro']['heading']),'chocolate-intro':escape(DATA['chocolate_intro']['text']),'category-cards':category_cards(route),'discovery-cards':discovery_cards(route)}.items():html=html.replace('{{'+key+'}}',value)
    html=re.sub(r'\{\{icon:([^}]+)\}\}',lambda m:icon(m[1]),html)
    html=html.replace('{{category-script}}','<script src="{{asset:js/category-motion.js}}?v=1" defer></script>' if route=='' else '')
    html=html.replace('{{history-assets}}','<link rel="stylesheet" href="{{asset:css/chocolate-history.css}}?v=6"><script src="{{asset:js/chocolate-history.js}}?v=1" defer></script>' if route=='experience-center/' else '')
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
    if '{{' in html: raise ValueError('Unresolved token on '+route)
    path=SITE/(route+'index.html' if route.endswith('/') or not route else route)
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(html,encoding='utf-8',newline='\n')
    return {'route':'/'+route,'file':path.relative_to(ROOT).as_posix(),'title':title,'sha256':hashlib.sha256(html.encode()).hexdigest()}
def build():
    inventory=[]
    inventory.append(render('','Experience. Chocolate.','Explore DeCocoa chocolate products, gifting ideas, the craft and the people behind them.',read('homepage.template.html').replace('{{inquiry-home}}',inquiry_section('talk',stacked=True)),'homepage'))
    listing='<section class="container products product-overview"><div class="chocolate-intro"><h1 id="page-title" class="section-title"><span class="eyebrow">Our Chocolate</span> <span class="heading-title">Chocolate possibilities.</span></h1><p>{{chocolate-intro}}</p></div><div class="category-static">'+category_cards('products/',static=True)+'</div><section class="product-examples" aria-labelledby="examples-title"><h2 id="examples-title">A closer look at chocolate.</h2><div class="product-grid">{{product-cards}}</div></section><section class="service-overview" aria-labelledby="services-title"><h2 id="services-title">Find your chocolate starting point.</h2><div class="service-grid">'+service_cards('products/')+'</div></section></section>'
    inventory.append(render('products/','Our Chocolate','Explore filled chocolate, chocolate bars and chocolate drizzle, and ask about the chocolate that interests you.',listing,'interior'))
    for p in DATA['products']:
        route='products/'+p['slug']+'/'
        template=read('product-detail.template.html')
        values={**p,'inquiry':escape(url('lets-talk/?topic=Chocolate%20%26%20products&product='+p['slug']+'#inquiry',route),quote=True)}
        for key,value in values.items(): template=template.replace('{{product-'+key+'}}',str(value) if key in ('width','height','inquiry') else escape(str(value),quote=True))
        template=template.replace('{{related-products}}',cards(route,p['slug']))
        inventory.append(render(route,p['title'],p['description'],template,'interior'))
    for page in DATA['pages']:
        body_class='interior'+(' experience-history' if page['route']=='experience-center/' else '')+(' section-nav-top' if page.get('section_nav_top') else '')
        inventory.append(render(page['route'],page['title'],page['intro'],general(page),body_class))
    for page in DATA['services']:inventory.append(render(page['route'],page['title'],page['description'],general(page),'interior service-landing'))
    inventory.append(render('lets-talk/',"Let's Talk",'Ask DeCocoa about chocolate products, gifting, Craft Your Own, fundraising, wholesale, business projects and the Experience Center.',contact(),'interior'))
    for page in DATA['policies']:
        content='<section class="container page-intro text-intro policy-draft" aria-labelledby="page-title"><div><h1 id="page-title">'+escape(page['title'])+'</h1><p class="lead">'+escape(page['notice'])+'</p></div></section>'
        inventory.append(render(page['route'],page['title'],page['notice'],content,'interior',noindex=True))
    recovery='<section class="container page-intro text-intro not-found"><div><h1 id="page-title" class="section-title"><span class="eyebrow">Page not found</span> <span class="heading-title">Something is missing.</span></h1><p class="lead">The page you are looking for may have moved. Keep exploring our chocolate or find your way home.</p><div class="hero-actions"><a class="button button-primary" href="{{url:products/}}">Explore Our Products</a><a class="button button-primary" href="{{url:}}">Go Home</a></div></div></section>'
    inventory.append(render('404.html','Page Not Found','Find your way back to DeCocoa products and information.',recovery,'interior'))
    for key,name in PATTERN_SOURCES.items(): (ROOT/f'assets/patterns/{name}-website.svg').write_text(PATTERNS[key],encoding='utf-8',newline='\n')
    (SITE/'generated-pages.json').write_text(json.dumps({'build':'local-site-2026-10-24','pages':inventory,'sources':['prototype/site-content.json','prototype/site.template.html','prototype/homepage.template.html','prototype/hero-bark.json','prototype/product-detail.template.html','prototype/trust-section.template.html','prototype/chocolate-history.json','prototype/chocolate-history-chapter.template.html','prototype/partials/header.html','prototype/partials/footer.html','prototype/partials/inquiry.html']},indent=2)+'\n',encoding='utf-8')
    print(f'Built {len(inventory)} local pages from shared templates and content. Original artwork unchanged.')
if __name__=='__main__': build()
