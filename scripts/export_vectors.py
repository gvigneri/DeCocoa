"""Convert the supplied PDF-compatible AI paths, rectangles and clips to editable SVG.

The selected originals contain only outlined filled vector artwork. Unsupported paint,
image, text, or compositing operators fail rather than silently discard geometry.
"""
from pathlib import Path
from pypdf import PdfReader
from pypdf.generic import ContentStream
import copy,json,re
from PIL import Image,ImageChops

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'brand/source/Decocoa Get Started'

def export(source,target,trim=False,animated=False):
    page=PdfReader(source).pages[0]
    width,height=map(float,(page.mediabox.width,page.mediabox.height))
    state={'matrix':(1,0,0,1,0,0),'fill':'#000000','clips':[]}
    stack=[];parts=[];points=[];clips=[];shapes=[];pending=None
    def point(x,y):
        a,b,c,d,e,f=state['matrix'];xy=(a*x+c*y+e,height-(b*x+d*y+f));points.append(xy)
        return ' '.join(f'{v:.5f}' for v in xy)
    def path():return ' '.join(parts)
    for args,op in ContentStream(page.get_contents(),page.pdf).operations:
        if op==b'q':stack.append(copy.deepcopy(state))
        elif op==b'Q':state=stack.pop()
        elif op==b'cm':
            a,b,c,d,e,f=state['matrix'];A,B,C,D,E,F=map(float,args)
            state['matrix']=(a*A+c*B,b*A+d*B,a*C+c*D,b*C+d*D,a*E+c*F+e,b*E+d*F+f)
        elif op in (b'scn',b'rg'):
            if len(args)!=3:raise ValueError('Expected source RGB color')
            state['fill']='#'+''.join(f'{round(float(v)*255):02x}' for v in args)
        elif op==b'm':parts.append('M'+point(*map(float,args)))
        elif op==b'l':parts.append('L'+point(*map(float,args)))
        elif op==b'c':
            a=list(map(float,args));parts.append('C'+' '.join(point(*a[i:i+2]) for i in (0,2,4)))
        elif op==b'h':parts.append('Z')
        elif op==b're':
            x,y,w,h=map(float,args)
            parts.append('M'+point(x,y)+'L'+point(x+w,y)+'L'+point(x+w,y+h)+'L'+point(x,y+h)+'Z')
        elif op in (b'W',b'W*'):pending=(path(),'evenodd' if op==b'W*' else 'nonzero')
        elif op in (b'n',b'f',b'f*'):
            if op!=b'n':
                if not parts:raise ValueError('Empty paint')
                shapes.append({'d':path(),'fill':state['fill'],'clips':state['clips'][:],'points':points[:],'rule':'evenodd' if op==b'f*' else 'nonzero'})
            if pending:
                clip_id=f'clip-{len(clips)}';clips.append((clip_id,*pending));state['clips'].append(clip_id);pending=None
            parts=[];points=[]
        elif op==b'gs':
            gs=page['/Resources']['/ExtGState'][args[0]].get_object()
            if gs.get('/ca',1)!=1 or gs.get('/BM','/Normal')!='/Normal':raise ValueError('Unsupported compositing')
        elif op not in (b'BDC',b'EMC',b'cs'):raise ValueError(f'Unsupported operator {op!r}')
    view=(0,0,width,height)
    if trim:
        allpoints=[p for s in shapes for p in s['points']]
        # Cubic control bounds keep all original geometry; small quiet bleed is deliberate.
        x0=min(p[0] for p in allpoints);y0=min(p[1] for p in allpoints)
        x1=max(p[0] for p in allpoints);y1=max(p[1] for p in allpoints)
        view=(x0-2,y0-2,x1-x0+4,y1-y0+4)
    defs=''.join(f'<clipPath id="{id}" clipPathUnits="userSpaceOnUse"><path d="{d}" clip-rule="{rule}"/></clipPath>' for id,d,rule in clips)
    output=[]
    for i,s in enumerate(shapes):
        isbg=(i==0 and not trim)
        y=sum(p[1] for p in s['points'])/len(s['points'])
        row=max(0,min(8,int(y/height*9)))
        klass='pattern-background' if isbg else f'pattern-motif row-{row}'
        shape=f'<path id="source-path-{i}" class="{klass}" fill="{s["fill"]}" fill-rule="{s["rule"]}" d="{s["d"]}"/>'
        for cid in reversed(s['clips']):shape=f'<g clip-path="url(#{cid})">{shape}</g>'
        output.append(shape)
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="'+' '.join(f'{v:.5f}' for v in view)+'">\n<defs>'+defs+'</defs>\n<g id="source-artwork">\n'+'\n'.join(output)+'\n</g></svg>',encoding='utf-8')
    return {'source':source.name,'export':str(target.relative_to(ROOT)),'viewBox':view,'painted_paths':len(shapes),'clips':len(clips),'source_colors':sorted(set(s['fill'] for s in shapes))},shapes,view

manifest=[]
for name in ['Circles','FlowerOfLife','Growth','Luxury','Rings','Stripes']:
    meta,_,_=export(SRC/f'DeCocoa_BrandPatterns_{name}_Pattern.ai',ROOT/f'assets/patterns/{name.lower()}-master.svg')
    manifest.append(meta)
meta,_,_=export(SRC/'DeCocoa_Logo_RGB_LightBG_Horiztonal.ai',ROOT/'assets/logos/decocoa-horizontal.svg',True);manifest.append(meta)
meta,shapes,view=export(SRC/'DeCocoa_Logo_RGB_LightBG_Brandmark.ai',ROOT/'assets/logos/decocoa-brandmark.svg',True);manifest.append(meta)
# The exterior silhouette is an exact subpath from the original, not a redraw.
# Source artwork uses its last closed contour for the six-pod exterior boundary.
outer='M'+shapes[0]['d'].split('M')[-1]
(ROOT/'assets/logos/decocoa-brandmark-silhouette.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="'+' '.join(f'{v:.5f}' for v in view)+'"><path fill="white" d="'+outer+'"/></svg>',encoding='utf-8')
meta,_,_=export(SRC/'DeCocoa_Logo_RGB_DarkBG_Badge.ai',ROOT/'assets/logos/decocoa-dark-badge.svg',True);manifest.append(meta)
(ROOT/'assets/vector-export-details.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps(manifest,indent=2))
