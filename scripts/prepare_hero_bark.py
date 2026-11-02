"""Archive supplied/generated hero artwork and prepare proportionate alpha WebP.

No crop, retouching, background removal, color adjustment, or content edits.
"""
from pathlib import Path
import argparse, hashlib, json, shutil
from PIL import Image, ImageDraw

ROOT=Path(__file__).resolve().parents[1]
ARCHIVE=ROOT/'brand/source/hero-bark-2026-11-01'
OUTPUT=ROOT/'assets/images/hero-bark'
SPECS=[('nut-bark','Chocolate bark with almonds and hazelnuts.','pretzel-drizzle'),
       ('pistachio-bark','Chocolate bark with pistachios and almonds.','pretzel-chunky'),
       ('crisp-bark','Chocolate bark with a crisp golden filling.','pretzel-sprinkles')]

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def image_details(path):
    with Image.open(path) as image:
        alpha=image.getchannel('A') if 'A' in image.getbands() else None
        return {'file':path.relative_to(ROOT).as_posix(),'width':image.width,'height':image.height,'mode':image.mode,
                'alpha_bounds':list(alpha.getbbox()) if alpha else None,'alpha_extrema':list(alpha.getextrema()) if alpha else None,
                'bytes':path.stat().st_size,'sha256':sha(path)}
def archive(source,destination):
    if destination.exists() and sha(destination)!=sha(source):raise ValueError('Archive already contains different bytes: '+str(destination))
    if not destination.exists():shutil.copyfile(source,destination)
    return image_details(destination)
def prepare(sources,reference):
    ARCHIVE.mkdir(parents=True,exist_ok=True);OUTPUT.mkdir(parents=True,exist_ok=True)
    reference_record=archive(reference,ARCHIVE/'chocolate-bark-no-shadow-reference.webp')
    assets=[];images=[]
    for source,(slug,alt,motion_class) in zip(sources,SPECS):
        preserved=archive(source,ARCHIVE/(slug+'-generated-original.png'))
        with Image.open(source) as image:
            if image.mode!='RGBA' or image.getchannel('A').getextrema()!=(0,255):raise ValueError('Expected true-alpha RGBA PNG: '+str(source))
            variants=[]
            for maximum,suffix in [(1280,''),(640,'-640')]:
                variant=image.copy();variant.thumbnail((maximum,maximum),Image.Resampling.LANCZOS)
                path=OUTPUT/(slug+suffix+'.webp')
                variant.save(path,format='WEBP',lossless=True,exact=True,method=6)
                variants.append(image_details(path))
        assets.append({'id':slug,'source':str(source.resolve()),'original':preserved,'production':variants[0],'small':variants[1],
                       'alt':alt,'motion_class':motion_class,'status':'generated original; implementation visual review pending'})
        images.append({'id':slug,'motion_class':motion_class,'image':variants[0]['file'].removeprefix('assets/'),
                       'width':variants[0]['width'],'height':variants[0]['height'],'alt':alt,
                       'variants':[{'image':v['file'].removeprefix('assets/'),'width':v['width']} for v in reversed(variants)],
                       'sizes':'(min-width:1500px) 660px, (min-width:601px) 48vw, 78vw'})
    manifest={'reference_original':str(reference.resolve()),'reference':reference_record,
              'operation':'Byte-identical source archives; proportional Lanczos runtime resizing and lossless alpha WebP encoding only. Full source canvas retained; no crop or retouching.',
              'assets':assets}
    (ROOT/'assets/hero-bark-details.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    (ROOT/'prototype/hero-bark.json').write_text(json.dumps({'images':images},indent=2)+'\n',encoding='utf-8')
    sheet=Image.new('RGB',(1050,1110),'#e3d9ce');draw=ImageDraw.Draw(sheet)
    for row,asset in enumerate(assets):
        for col,(label,color) in enumerate([('Orange','#E87933'),('Cream','#F7EFE6'),('Checkerboard',None)]):
            tile=Image.new('RGBA',(350,330),color or '#eeeeee')
            if not color:
                checker=ImageDraw.Draw(tile)
                for y in range(0,330,20):
                    for x in range(0,350,20):
                        if (x//20+y//20)%2:checker.rectangle((x,y,x+19,y+19),fill='#cccccc')
            with Image.open(ROOT/asset['production']['file']) as image:
                image.thumbnail((330,310),Image.Resampling.LANCZOS)
                tile.alpha_composite(image,((350-image.width)//2,(330-image.height)//2))
            sheet.paste(tile.convert('RGB'),(col*350,row*370+30));draw.text((col*350+10,row*370+8),asset['id']+' / '+label,fill='#170905')
    qa=ROOT/'reviews/hero-bark-2026-11-01/alpha-qa.png';qa.parent.mkdir(parents=True,exist_ok=True);sheet.save(qa)
    print(json.dumps({'manifest':'assets/hero-bark-details.json','images':images},indent=2))
if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--sources',nargs=3,type=Path,required=True);parser.add_argument('--reference',type=Path,required=True)
    args=parser.parse_args();prepare(args.sources,args.reference)
