"""Small presentation primitives for the existing standard-library site builder."""
from html import escape


def paragraphs(values, cls=''):
    attr = ' class="'+cls+'"' if cls else ''
    return ''.join('<p'+attr+'>'+escape(value)+'</p>' for value in values)


def image(data, cls='card page-photo', eager=False):
    source = data.get('asset', 'images/'+data.get('image', ''))
    img = '<img src="{{asset:'+source+'}}" width="'+str(data['width'])+'" height="'+str(data['height'])+'" alt="'+escape(data['alt'], quote=True)+'" '+('fetchpriority="high"' if eager else 'loading="lazy"')+'>'
    if source.endswith('decocoa-factory.gif'):
        img = '<picture><source media="(prefers-reduced-motion: reduce)" srcset="{{asset:images/decocoa-factory-still.png}}">'+img+'</picture>'
    return '<figure class="'+cls+'">'+img+'</figure>'


def hero(read, label, heading, body=(), media=None, actions='', home=False, notice=''):
    heading_id = 'hero-title' if home else 'page-title'
    title = ('Crafted.<br><strong>To delight.</strong>' if home else escape(heading))
    # All Orange hero banners use a single heading without an eyebrow.
    title_html = '<h1 id="'+heading_id+'" class="heading-title">'+title+'</h1>'
    if media is None:
        media = image({'asset':'logos/decocoa-brandmark.svg','width':1309,'height':1512,'alt':'DeCocoa brandmark'}, 'page-hero-media brandmark-media', True)
    copy=('<h2 class="hero-notice">'+escape(notice)+'</h2>' if notice else '')+paragraphs(body)
    values = {'variant':'hero--orange hero--bark' if home else 'hero--orange hero--page', 'id':'home' if home else 'page-hero', 'heading-id':heading_id, 'heading':title_html, 'copy':copy, 'actions':'<div class="hero-actions">'+actions+'</div>' if actions else '', 'media':media}
    html = read('partials/hero.html')
    for key, value in values.items():
        html = html.replace('{{hero-'+key+'}}', value)
    return html


def family_timeline(items):
    return '<ol class="family-timeline" aria-label="Vigneri family history">'+''.join('<li><p><time datetime="'+item['date']+'">'+item['date']+'</time>'+escape(item['separator']+item['text'])+'</p></li>' for item in items)+'</ol>'


def info_grid(items):
    cards = []
    for item in items:
        attrs = ' id="'+item['id']+'" aria-labelledby="'+item['id']+'-title"' if item.get('id') else ''
        heading_attrs = ' id="'+item['id']+'-title"' if item.get('id') else ''
        title = escape(item['title'])
        if item.get('route'):
            title = '<a href="{{url:'+item['route']+'}}">'+title+'</a>'
        cards.append('<article class="info-item"'+attrs+'><h3'+heading_attrs+'>'+title+'</h3>'+paragraphs(item.get('paragraphs',[item.get('text','')]))+'</article>')
    return '<div class="info-grid">'+''.join(cards)+'</div>' if cards else ''
