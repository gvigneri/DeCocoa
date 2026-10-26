"""Export the untouched three-piece core, excluding only the isolated faint duplicate."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageChops
import json
ROOT=Path(__file__).resolve().parents[1]
source=ROOT/'brand/source/Decocoa Get Started/images/Pretzels.png'
image=Image.open(source).convert('RGBA')
# Only the detached faint tiny image occupies this upper-right area.
# Every pixel of the three overlapping core pieces is retained with original alpha.
scale=image.width/565
points=[(0,0),(345,0),(345,185),(565,185),(565,800),(0,800)]
points=[(round(x*scale),round(y*scale)) for x,y in points]
selection=Image.new('L',image.size,0);ImageDraw.Draw(selection).polygon(points,fill=255)
image.putalpha(ImageChops.multiply(image.getchannel('A'),selection))
bounds=image.getchannel('A').getbbox();image=image.crop(bounds)
image.thumbnail((1700,1700),Image.Resampling.LANCZOS)
image.save(ROOT/'assets/images/dipped-pretzel-trio.webp',quality=94,method=6)
proof=Image.new('RGBA',image.size,'#512316');proof.alpha_composite(image)
proof.thumbnail((700,900));proof.convert('RGB').save(ROOT/'assets/images/pretzel-trio-export-proof.jpg',quality=95)
(ROOT/'assets/pretzel-trio-export-details.json').write_text(json.dumps({'source':str(source.relative_to(ROOT)),'source_dimensions':[3232,4576],'selection_polygon_source_pixels':points,'alpha_bounds':bounds,'export_dimensions':image.size,'operation':'Excludes isolated faint tiny duplicate only. Three-piece core retains original pixels, alpha, overlap and edges; proportional resize and WebP.'},indent=2),encoding='utf-8')
print('Prepared intact original pretzel trio:',image.size)
