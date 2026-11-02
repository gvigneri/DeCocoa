"""Prepare manifest-selected transparent artwork while preserving prior source records.

Only alpha-padding crops, proportionate resizing and lossless PNG encoding are
performed. Source files are read only. Pillow is required; no network is used.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
from PIL import Image, ImageDraw

ROOT=Path(__file__).resolve().parents[1]
ASSET_ROOT=ROOT/'assets/images/chocolate-history'
MANIFEST=ROOT/'assets/chocolate-history-assets.json'
PROCESSING='Crop surplus alpha padding with up to 8px retained margin; proportionate Lanczos downsampling; lossless PNG encoding. Sources unchanged.'

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def details(path):
    with Image.open(path) as image:
        alpha=image.getchannel('A')
        return {'file':path.relative_to(ROOT).as_posix(),'width':image.width,'height':image.height,
                'mode':image.mode,'alpha_bounds':list(alpha.getbbox()),'alpha_extrema':list(alpha.getextrema()),
                'bytes':path.stat().st_size,'sha256':digest(path)}

def contact_sheet(records,destination):
    sheet=Image.new('RGB',(1050,370*len(records)),'#e3d9ce')
    draw=ImageDraw.Draw(sheet)
    for row,record in enumerate(records):
        for column,(label,color) in enumerate([('Cream','#F7EFE6'),('Dark Brown','#170905'),('Checkerboard',None)]):
            x,y=column*350,row*370
            tile=Image.new('RGBA',(350,330),color or '#eeeeee')
            if color is None:
                checker=ImageDraw.Draw(tile)
                for cy in range(0,330,20):
                    for cx in range(0,350,20):
                        if (cx//20+cy//20)%2:checker.rectangle((cx,cy,cx+19,cy+19),fill='#cccccc')
            with Image.open(ROOT/record['production']['file']) as artwork:
                artwork.thumbnail((320,300),Image.Resampling.LANCZOS)
                tile.alpha_composite(artwork,((350-artwork.width)//2,(330-artwork.height)//2))
            sheet.paste(tile.convert('RGB'),(x,y+30))
            draw.text((x+10,y+8),record['chapter']+' / '+record['role']+' / '+label,fill='#170905')
    destination.parent.mkdir(parents=True,exist_ok=True)
    sheet.save(destination)

def prepare(inputs,visual_review='pending',source_dir=None,chapters=None,qa_sheet=None):
    input_data=json.loads(inputs.read_text(encoding='utf-8'))
    specs=input_data['assets']
    composition=json.loads((ROOT/'prototype/chocolate-history.json').read_text(encoding='utf-8'))
    placements={}
    for chapter in composition['chapters']:
        for layer in chapter['layers']:
            placements.setdefault('assets/'+layer['asset'],[]).append({'chapter':chapter['id'],'role':layer['role'],'decorative':layer['decorative'],'alt':layer['alt'],'placement':layer['placement']})
    manifest=json.loads(MANIFEST.read_text(encoding='utf-8')) if MANIFEST.exists() else {'processing':PROCESSING,'assets':[]}
    records={record['production']['file']:record for record in manifest['assets']}
    prepared=[]
    for spec in specs:
        if chapters and spec['chapter'] not in chapters:continue
        chapter,name=spec['chapter'],spec['name']
        if not all(re.fullmatch(r'[a-z0-9-]+',value) for value in (chapter,name)):
            raise ValueError('Use plain chapter and asset filenames')
        output=ASSET_ROOT/chapter
        output.mkdir(parents=True,exist_ok=True)
        source=Path(spec['source'])
        if source_dir:source=source_dir/source.name
        if not source.is_absolute():source=ROOT/source
        destination=output/(name+'.png')
        key=destination.relative_to(ROOT).as_posix()
        existing=records.get(key)
        if existing:
            # Never silently replace an established source/provenance record.
            if source.exists() and digest(source)!=existing['source']['sha256']:
                raise ValueError('Changed source requires a new production filename: '+key)
            for variant in (existing['production'],existing['small']):
                if not (ROOT/variant['file']).exists() or digest(ROOT/variant['file'])!=variant['sha256']:
                    raise ValueError('Existing production asset changed: '+variant['file'])
            record=existing
        else:
            with Image.open(source) as image:
                if image.mode!='RGBA' or image.getchannel('A').getextrema()!=(0,255):
                    raise ValueError('Expected true-alpha RGBA artwork: '+str(source))
                bounds=image.getchannel('A').getbbox()
                crop=(max(0,bounds[0]-8),max(0,bounds[1]-8),min(image.width,bounds[2]+8),min(image.height,bounds[3]+8))
                cropped=image.crop(crop)
                source_record={'file':str(source.resolve()),'width':image.width,'height':image.height,'mode':image.mode,
                               'alpha_bounds':list(bounds),'bytes':source.stat().st_size,'sha256':digest(source)}
                variants=[]
                for maximum,suffix in [(spec['large'],''),(spec['small'],'-'+str(spec['small']))]:
                    variant=cropped.copy()
                    variant.thumbnail((maximum,maximum),Image.Resampling.LANCZOS)
                    path=output/(name+suffix+'.png')
                    variant.save(path,optimize=True,compress_level=9)
                    variants.append(details(path))
            record={'chapter':chapter,'role':spec['role'],'decorative':spec['decorative'],'alt':spec['alt'],
                    'generation_status':'generated original; implementation visually checked; pending Guy artwork approval' if visual_review=='implementation-checked' else 'generated original; visual review pending',
                    'placement_source':'prototype/chocolate-history.json','interpretation':spec.get('interpretation','Interpretive historical illustration.'),
                    'source':source_record,'crop_box':list(crop),'production':variants[0],'small':variants[1]}
        if key in placements:
            record['placements']=placements[key]
            record['placement']=next((p['placement'] for p in placements[key] if p['chapter']==record['chapter']),placements[key][0]['placement'])
        if source.exists():
            archive=ROOT/'brand/source/chocolate-history-2026-10-31'/chapter/(name+'-original.png')
            archive.parent.mkdir(parents=True,exist_ok=True)
            if archive.exists() and digest(archive)!=record['source']['sha256']:
                raise ValueError('Existing source archive differs: '+str(archive))
            if not archive.exists():shutil.copyfile(source,archive)
            record['archive']=details(archive)
        if visual_review=='implementation-checked':
            record['generation_status']='generated original; implementation visually checked; pending Guy artwork approval'
        records[key]=record
        prepared.append(record)
    manifest['assets']=list(records.values())
    rejected={record['archive']['file']:record for record in manifest.get('rejected_sources',[])}
    for spec in input_data.get('rejected_sources',[]):
        source=Path(spec['source'])
        archive=ROOT/'brand/source/chocolate-history-2026-10-31'/spec['chapter']/(spec['name']+'-original.png')
        archive.parent.mkdir(parents=True,exist_ok=True)
        if archive.exists() and digest(archive)!=digest(source):
            raise ValueError('Existing rejected-source archive differs: '+str(archive))
        if not archive.exists():shutil.copyfile(source,archive)
        rejected[archive.relative_to(ROOT).as_posix()]={'source':str(source.resolve()),'archive':details(archive),'status':spec['status']}
    if rejected:manifest['rejected_sources']=list(rejected.values())
    manifest['input_manifest']=inputs.relative_to(ROOT).as_posix()
    MANIFEST.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    if qa_sheet and prepared:contact_sheet(prepared,qa_sheet)
    print(json.dumps({'manifest':str(MANIFEST),'assets_verified_or_prepared':len(prepared),
                      'production':[{k:v for k,v in r['production'].items() if k!='sha256'} for r in prepared]},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-manifest',type=Path,default=ROOT/'prototype/chocolate-history-artwork.json')
    parser.add_argument('--source-dir',type=Path,help='Optional override for the source PNG directory.')
    parser.add_argument('--chapters',nargs='+',help='Prepare only these chapter IDs; retain all prior metadata.')
    parser.add_argument('--qa-sheet',type=Path,help='Optional QA-only light/dark/checker contact sheet output.')
    parser.add_argument('--visual-review',choices=('pending','implementation-checked'),default='pending')
    args=parser.parse_args()
    prepare(args.input_manifest,args.visual_review,args.source_dir,args.chapters,args.qa_sheet)
