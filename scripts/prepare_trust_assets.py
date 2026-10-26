"""Cache official identity assets and prepare faithful local PNG web copies.

Original supplied marks are never edited. SVG conversion uses the bundled
Sharp renderer; pass --sharp-module when it is outside normal Node resolution.
"""
from pathlib import Path
from urllib.request import Request,urlopen
from PIL import Image,ImageOps
import argparse,hashlib,json,re,shutil,subprocess

ROOT=Path(__file__).resolve().parents[1]
CACHE=ROOT/'assets/source-external/trust'
WEB=ROOT/'assets/images'
SOURCES=[
    ('wegmans','https://www.wegmans.com/news-media/photo-logo-gallery','https://images.wegmans.com/is/image/wegmanscsprod/media-Wegmans-Logo-color-p?fmt=png-alpha&hei=379&wid=1000','partner-wegmans-official.png','official'),
    ('haccp-plants','https://www.plants2market.com/en/qualitatsmanagement','https://www.plants2market.com/web/image/112969-49256f38/HACCP%20Blau%20auf%20transparent.png','certification-haccp.png','third-party generic draft reference; issuer unknown; replace after verification'),
]
VECTORS=[
    ('sqf-site','https://www.sqfi.com/integrity-program/logo-rules-of-use','https://www.sqfi.com/images/sqfilibraries/theme/sqfilogo.svg','certification-sqf.png','official complete SQF Institute identity'),
    ('ou-commons','https://commons.wikimedia.org/wiki/File:Ou_kosher.svg','https://upload.wikimedia.org/wikipedia/commons/4/40/Ou_kosher.svg','certification-ou-kosher.png','third-party vector recreation by Messedrocker per Commons description; PD-textlogo, trademark retained; local draft fallback, not issuer master'),
    ('rainforest-seal','https://www.rainforest-alliance.org/business/marketing-sustainability/using-our-logo-and-seal/','https://www.rainforest-alliance.org/wp-content/themes/rainforest-replant/dist/img/icon-navigation-seal-forest.svg','certification-rainforest-alliance.png','official People & Nature seal; not Regenerative program'),
    ('cacao-trace','https://www.cacaotrace.com/',None,'certification-cacao-trace.png','official inline header SVG'),
]
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def download(url):return urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0 DeCocoa-local-asset-preparation'}),timeout=45).read()
def entry(name,page,url,source,destination,operation):
    im=Image.open(destination)
    return {'name':name,'source_page':page,'asset_url':url,'source':source.relative_to(ROOT).as_posix(),'source_sha256':sha(source),'web':destination.relative_to(ROOT).as_posix(),'web_sha256':sha(destination),'dimensions':im.size,'mode':im.mode,'alpha_extrema':im.convert('RGBA').getchannel('A').getextrema(),'operation':operation,'retrieved':'2026-10-25','scope':'Local draft mark reference; does not verify DeCocoa relationship or certification.'}
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--sharp-module',default='sharp');args=parser.parse_args()
    CACHE.mkdir(parents=True,exist_ok=True);entries=[]
    for name,page,url,filename,status in SOURCES:
        source=CACHE/(name+'.png')
        if not source.exists():source.write_bytes(download(url))
        destination=WEB/filename;shutil.copyfile(source,destination)
        record=entry(name,page,url,source,destination,'Unmodified PNG copied byte-for-byte. No recoloring, tracing, cropping or background removal.')
        record['source_status']=status;entries.append(record)
    # Retain the user's exact replacement rather than restoring the prior download.
    source=ROOT/'assets/source-external/user-attachments/626950-h-media-logo-fyfga.webp'
    destination=WEB/'partner-wegmans-supplied-626950.webp';shutil.copyfile(source,destination)
    record=entry('wegmans-supplied','User-supplied attachment, October 25, 2026','C:/Users/guyta/Desktop/626950-h-media-logo-fyfga.webp',source,destination,'Supplied WebP copied byte-for-byte; original transparency, artwork, colors and geometry unchanged.')
    record['source_status']='user-supplied replacement, explicitly authorized October 25, 2026';entries.append(record)
    for name,page,url,filename,status in VECTORS:
        source=CACHE/(name+'.svg')
        if not source.exists():
            if url:source.write_bytes(download(url))
            else:
                svgs=re.findall(r'<svg\b.*?</svg>',download(page).decode('utf-8'),re.S)
                selected=[svg for svg in svgs if 'viewBox="-0.007 0 160.437 130.28"' in svg]
                if not selected:raise ValueError('Expected official Cacao-Trace SVG not found')
                source.write_text(selected[0],encoding='utf-8',newline='\n')
        destination=WEB/filename
        # One official SVG incorrectly declares UTF-16 despite UTF-8 bytes.
        # Removing only that declaration in renderer memory fixes parsing;
        # the exact downloaded source file, paths, fills and transforms remain.
        code="const fs=require('fs'),sharp=require(process.argv[1]);const svg=fs.readFileSync(process.argv[2],'utf8').replace(/^<\\?xml.*?\\?>/,'');sharp(Buffer.from(svg),{density:192}).resize({width:Number(process.argv[4])}).png().toFile(process.argv[3]).catch(e=>{console.error(e);process.exit(1)})"
        width=1280 if name=='ou-commons' else 640
        subprocess.run(['node','-e',code,args.sharp_module,str(source),str(destination),str(width)],check=True)
        operation=f'Exact SVG rendered to transparent {width}px-wide PNG with Sharp; XML declaration normalized in renderer memory only. Original fills, paths, transforms and proportions retained.'
        if name=='ou-commons':
            image=Image.open(destination).convert('RGBA')
            bounds=image.getchannel('A').getbbox()
            ImageOps.expand(image.crop(bounds),border=40,fill=(0,0,0,0)).save(destination)
            operation+=' Empty transparent canvas trimmed to alpha bounds, then40px transparent clear space added; mark pixels unaltered.'
        record=entry(name,page,url or page+' (inline header SVG)',source,destination,operation)
        record['source_status']=status;entries.append(record)
    for name in ('puratos','guittard'):
        destination=WEB/('partner-'+name+'.png')
        record=entry(name,'Existing supplied wireframe imagery','Preserved existing partner PNG',destination,destination,'Existing supplied PNG used unchanged. Its exact Cream raster backdrop matches website Cream(247,239,230); no background removal or recoloring.')
        record['source_status']='existing local draft reference from supplied wireframe';entries.append(record)
    (ROOT/'assets/trust-export-details.json').write_text(json.dumps(entries,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(entries,indent=2))
if __name__=='__main__':main()
