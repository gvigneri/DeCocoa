"""Prepare source category imagery and seven pinned Font Awesome Free SVGs."""
from pathlib import Path
from PIL import Image
from urllib.request import urlopen
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'brand/source/Decocoa Get Started/images'
IMAGES=ROOT/'assets/images'
ICON_DIR=ROOT/'assets/icons/fontawesome-free-6.7.2'
BASE='https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.7.2/'

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
    source=SOURCE/'Bunny 2.png'
    image=Image.open(source).convert('RGBA')
    bounds=image.getchannel('A').getbbox()
    image=image.crop(bounds)
    image.thumbnail((1200,1200),Image.Resampling.LANCZOS)
    destination=IMAGES/'hollow-chocolate-figure.webp'
    image.save(destination,quality=94,method=6)
    entries=[]
    for original,web in [('Wellness.png','chocolate-drizzle.webp'),('Bark filled.png','filled-chocolate.webp'),('Bunny 2.png','hollow-chocolate-figure.webp'),('Nuts Upscale.png','nuts-and-chocolate.webp'),('Chocolate Powder.png','cocoa-powder.webp')]:
        path=IMAGES/web
        entries.append({'source':(SOURCE/original).relative_to(ROOT).as_posix(),'source_sha256':sha(SOURCE/original),'web':path.relative_to(ROOT).as_posix(),'web_sha256':sha(path),'dimensions':Image.open(path).size,'operation':'Original alpha-bounds crop and proportional resize; RGBA WebP. No generated art, recoloring or retouching.','new_export':original=='Bunny 2.png'})
    ICON_DIR.mkdir(parents=True,exist_ok=True)
    icons=[]
    for name in ('arrow-right','gift','wand-magic-sparkles','handshake','shield-heart','leaf','gears'):
        url=BASE+'svgs/solid/'+name+'.svg'
        path=ICON_DIR/(name+'.svg')
        if not path.exists():path.write_bytes(urlopen(url,timeout=30).read())
        icons.append({'file':path.relative_to(ROOT).as_posix(),'source_url':url,'sha256':sha(path),'license':'CC BY 4.0','changes':'None; original SVG file and attribution retained. Embedded instances add presentation attributes only.'})
    license_path=ICON_DIR/'LICENSE.txt'
    if not license_path.exists():license_path.write_bytes(urlopen(BASE+'LICENSE.txt',timeout=30).read())
    (ICON_DIR/'provenance.json').write_text(json.dumps({'project':'Font Awesome Free','release':'6.7.2','publisher':'Fonticons, Inc.','source_repository':'https://github.com/FortAwesome/Font-Awesome/tree/6.7.2','license_file':'LICENSE.txt','icons':icons},indent=2)+'\n',encoding='utf-8')
    (ROOT/'assets/category-export-details.json').write_text(json.dumps(entries,indent=2)+'\n',encoding='utf-8')
    print('Prepared five source-derived category mappings and seven pinned Font Awesome Free icons.')
if __name__=='__main__':main()
