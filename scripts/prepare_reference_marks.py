"""Extract supplied reference marks, preserving their forms and colors.

These are provisional assets, not evidence of current business/certification status.
"""
from pathlib import Path
from pypdf import PdfReader
import pypdfium2 as pdfium

root=Path(__file__).resolve().parents[1]
source=root/'brand/source/Decocoa Get Started/Decocoa 2026 Wireframe + Branded.pdf'
out=root/'assets/images'
reader=PdfReader(source)
base=reader.pages[1]['/Resources']['/XObject']['/X233']['/Resources']['/XObject']
for node,inner,pattern,image,slug in [('X224','X223','P80','X77','certification-reference-a'),('X226','X225','P85','X83','certification-reference-b')]:
    stream=base['/'+node]['/Resources']['/XObject']['/'+inner]['/Resources']['/Pattern']['/'+pattern]['/Resources']['/XObject']['/'+image]
    (out/f'{slug}.jpg').write_bytes(stream.get_data())
pdf=pdfium.PdfDocument(source)
page=pdf[1].render(scale=2).to_pil()
for slug,box in {'partner-puratos':(44,2710,272,2870),'partner-wegmans':(304,2710,550,2870),'partner-guittard':(568,2710,838,2870)}.items():
    page.crop(tuple(v*2 for v in box)).save(out/f'{slug}.png')
print('Three original partner crops and two exact embedded certification JPEGs exported.')
