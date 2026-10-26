"""Compress approved image_gen cutouts without cropping, resizing or alpha edits."""
from pathlib import Path
from PIL import Image
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
records=[]
for name in ['pretzel-red-drizzle-r6','pretzel-chunky-sprinkles-r6']:
    source=ROOT/f'assets/images/{name}.png'; target=source.with_suffix('.webp')
    image=Image.open(source).convert('RGBA')
    image.save(target,quality=94,method=6)
    exported=Image.open(target).convert('RGBA')
    assert image.getchannel('A').tobytes()==exported.getchannel('A').tobytes()
    records.append({'input':str(source.relative_to(ROOT)),'export':str(target.relative_to(ROOT)),
        'dimensions':image.size,'alpha_extrema':image.getchannel('A').getextrema(),
        'alpha_preserved_exactly':True,'export_bytes':target.stat().st_size,
        'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'operation':'WebP quality94 compression only; no resize, crop, retouch or alpha edit. Imagegen reconstruction provenance is in handoff/pretzel-cutout-provenance.json.'})
(ROOT/'assets/r6-cutout-export-details.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
print(json.dumps(records,indent=2))
