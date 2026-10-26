"""Faithful exports from preserved DeCocoa originals; no source files are changed."""
from pathlib import Path
import json
from PIL import Image, ImageChops
from pypdf import PdfReader
from pypdf.generic import ContentStream

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'brand/source/Decocoa Get Started'

# The strict exporter owns logo/pattern geometry, including filled rectangles and clips.
import runpy
runpy.run_path(str(ROOT/'scripts/export_vectors.py'), run_name='__main__')
info = {'vector_exports':'assets/vector-export-details.json'}
products = {'Bark filled.png':'filled-chocolate','Bark.png':'chocolate-bar','Chocolate Powder.png':'cocoa-powder','Nuts Upscale.png':'nuts-and-chocolate','Wellness.png':'chocolate-drizzle','Pretzels.png':'dipped-pretzels','Pretzel + RedGreen sprinkles.png':'dipped-pretzel'}
for original, slug in products.items():
    im=Image.open(SOURCE/'images'/original).convert('RGBA')
    im=im.crop(im.getchannel('A').getbbox())
    im.thumbnail((1500,1500),Image.Resampling.LANCZOS)
    im.save(ROOT/'assets/images'/f'{slug}.webp',quality=94,method=6)
    info[slug]={'original':original,'dimensions':im.size,'operation':'alpha-bounds crop, proportional resize, WebP RGBA'}
for original, slug in {'P179-X4.jpg':'people-at-work','P184-X17.jpg':'chocolate-craft'}.items():
    im=Image.open(ROOT/'references/wireframe-images'/original).convert('RGB')
    im.save(ROOT/'assets/images'/f'{slug}.webp',quality=92,method=6)
    info[slug]={'original':'wireframe page 2 Pattern resource '+original,'dimensions':im.size,'operation':'WebP RGB; original framing; provisional photography'}
(ROOT/'assets/export-details.json').write_text(json.dumps(info,indent=2),encoding='utf-8')
print(json.dumps(info,indent=2))

runpy.run_path(str(ROOT/'scripts/prepare_pretzel_trio.py'),run_name='__main__')
runpy.run_path(str(ROOT/'scripts/prepare_r6_cutouts.py'),run_name='__main__')
