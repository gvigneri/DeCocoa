"""Preserve the user-supplied GIF and export its first frame for reduced motion."""
from pathlib import Path
from PIL import Image,ImageDraw
import argparse,hashlib,json,shutil

ROOT=Path(__file__).resolve().parents[1]
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--source',type=Path,default=Path.home()/'Downloads/DeCocoa-Factory.gif');args=parser.parse_args()
    preserved=ROOT/'assets/source-external/user-attachments/DeCocoa-Factory.gif';preserved.parent.mkdir(parents=True,exist_ok=True)
    if not preserved.exists():shutil.copyfile(args.source,preserved)
    web=ROOT/'assets/images/decocoa-factory.gif';shutil.copyfile(preserved,web)
    gif=Image.open(preserved);durations=[]
    for index in range(gif.n_frames):gif.seek(index);durations.append(gif.info.get('duration',0))
    gif.seek(0);still=ROOT/'assets/images/decocoa-factory-still.png';gif.convert('RGBA').save(still)
    proof=Image.new('RGB',(1200,480),(247,239,230));draw=ImageDraw.Draw(proof)
    for index,frame in enumerate((0,gif.n_frames//4,gif.n_frames//2,3*gif.n_frames//4)):
        gif.seek(frame);image=gif.convert('RGBA');image.thumbnail((580,204));x=(index%2)*600+10;y=(index//2)*240
        proof.paste(image,(x,y),image);draw.text((x,y+210),f'Frame {frame}',fill=(58,23,13))
    proof.save(ROOT/'prototype/qa-site-build/factory-gif-inspection.jpg',quality=95)
    result={'source_original':str(args.source),'preserved':preserved.relative_to(ROOT).as_posix(),'source_sha256':sha(preserved),'web':web.relative_to(ROOT).as_posix(),'web_sha256':sha(web),'dimensions':gif.size,'frames':gif.n_frames,'frame_durations_ms':sorted(set(durations)),'duration_ms':sum(durations),'loop':gif.info.get('loop'),'operation':'GIF preserved and copied byte-for-byte; no frame, palette, geometry or timing edits.','reduced_motion':{'file':still.relative_to(ROOT).as_posix(),'sha256':sha(still),'operation':'Lossless RGBA PNG of composited first frame; original dimensions and colors.'}}
    (ROOT/'assets/factory-media-details.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
