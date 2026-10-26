"""Cross-route integrity and build regression checks for the local site.

These are static checks, not browser or accessibility conformance results.
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote,urljoin
from preview_server import PublicSite
import collections, hashlib, importlib.util, json, re, tempfile
ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'prototype'
PUBLIC=PublicSite(ROOT)
PAGE_ROUTES={path:route for route,path in PUBLIC.pages.items()}
class Scan(HTMLParser):
    def __init__(self):
        super().__init__();self.ids=[];self.tags=[];self.text=[];self.stack=[];self.header=None;self.nav_links=collections.defaultdict(list);self.anchor_depth=0;self.nested_anchors=0;self.discovery_links=[];self.category_links=[]
    def handle_starttag(self,tag,items):
        a=dict(items);self.tags.append((tag,a));self.stack.append(tag)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='header':self.header=a.get('data-header')
        if tag=='a' and self.header:self.nav_links[self.header].append(a.get('href'))
        if tag=='a':
            self.nested_anchors+=self.anchor_depth>0
            self.anchor_depth+=1
            if 'discovery-card' in a.get('class','').split():self.discovery_links.append(a.get('href'))
            if 'category-card' in a.get('class','').split():self.category_links.append(a.get('href'))
    def handle_endtag(self,tag):
        if tag=='header':self.header=None
        if tag=='a':self.anchor_depth=max(0,self.anchor_depth-1)
    def handle_data(self,text):self.text.append(text)
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
class HeadingScan(HTMLParser):
    """Inspect heading names and paired-label structure, independent of CSS."""
    def __init__(self):
        super().__init__();self.current=None;self.headings=[];self.errors=[]
    def handle_starttag(self,tag,items):
        attrs=dict(items);classes=attrs.get('class','').split()
        if re.fullmatch('h[1-6]',tag):
            if self.current:self.errors.append('nested heading')
            self.current={'rank':tag,'id':attrs.get('id'),'paired':'section-title' in classes,'parts':[],'text':[]}
            self.headings.append(self.current)
        for role in ('eyebrow','heading-title'):
            if role in classes:
                if tag!='span' or not self.current or self.current['rank'] not in ('h1','h2') or not self.current['paired']:
                    self.errors.append('unpaired '+role)
                else:self.current['parts'].append(role)
        if tag=='br' and self.current:self.current['text'].append(' ')
    def handle_data(self,value):
        if self.current:self.current['text'].append(value)
    def handle_endtag(self,tag):
        if self.current and tag==self.current['rank']:
            if self.current['paired'] and self.current['parts']!=['eyebrow','heading-title']:self.errors.append('invalid heading label/title structure')
            if not ''.join(self.current['text']).strip():self.errors.append('empty heading name')
            self.current=None
def target(ref,path):
    u=urlsplit(ref)
    if u.scheme or u.netloc or not u.path and not u.fragment:return None,None
    resolved=urlsplit(urljoin(PAGE_ROUTES[path],ref))
    dest=PUBLIC.files.get(resolved.path,ROOT/'__missing_public_resource__')
    return dest,unquote(resolved.fragment)
def run():
    inventory=json.loads((SITE/'generated-pages.json').read_text())['pages']
    pages={ROOT/i['file']:Scan() for i in inventory}
    for path,scan in pages.items():scan.feed(path.read_text(encoding='utf-8'))
    errors=[];details=[];titles=[];all_forms=[];links=0
    for path,scan in pages.items():
        name=path.relative_to(ROOT).as_posix();html=path.read_text(encoding='utf-8')
        headings=HeadingScan();headings.feed(html)
        if headings.errors:errors.append([name,'heading semantics',headings.errors])
        paired=re.findall(r'<h[12]\b[^>]*class="section-title"[^>]*>(.*?)</h[12]>',html,re.S)
        if any(not re.search(r'</span>\s+<span class="heading-title">',heading) for heading in paired):errors.append([name,'missing accessible heading-name separator'])
        duplicates=[i for i,n in collections.Counter(scan.ids).items() if n>1]
        if duplicates:errors.append([name,'duplicate IDs',duplicates])
        def count(t):return sum(tag==t for tag,a in scan.tags)
        if (count('main'),count('h1'),count('footer'),count('header'))!=(1,1,1,2):errors.append([name,'landmark/heading counts'])
        title=re.search('<title>(.*?)</title>',html).group(1);titles.append(title)
        if collections.Counter(scan.nav_links['original'])!=collections.Counter(scan.nav_links['scroll']):errors.append([name,'header destination mismatch'])
        scripts=[a for tag,a in scan.tags if tag=='script']
        expected_scripts=2 if PAGE_ROUTES[path]=='/' else 1
        if len(scripts)!=expected_scripts or any(not script.get('src') for script in scripts) or len({script.get('src') for script in scripts})!=expected_scripts:errors.append([name,'script ownership'])
        forms=count('form');all_forms.append(forms)
        if forms:errors.append([name,'unexpected native form'])
        if scan.nested_anchors:errors.append([name,'nested navigation links'])
        if any('motion-toggle' in a.get('class','') or any(key in a for key in ('data-category-pause','data-category-previous','data-category-next')) for tag,a in scan.tags):errors.append([name,'removed motion control remains'])
        if '{{' in html:errors.append([name,'unresolved build token'])
        public=' '.join(scan.text)
        policy_draft=PAGE_ROUTES[path] in ('/privacy-policy/','/terms-and-conditions/','/accessibility/')
        if re.search(r'\b(prototype|provisional|placeholder|streamline|seamless|enhance)\b|—|Work With Us',public,re.I) or (not policy_draft and re.search(r'\bdraft\b',public,re.I)):errors.append([name,'forbidden customer copy'])
        controls=[a for tag,a in scan.tags if tag=='button' and 'submenu-toggle' in a.get('class','').split()]
        panels={a.get('id'):a for tag,a in scan.tags if 'submenu' in a.get('class','').split()}
        if len(controls)!=8 or len(panels)!=8:errors.append([name,'four independent dropdowns per header required'])
        for control in controls:
            panel=panels.get(control.get('aria-controls'))
            if panel is None or 'hidden' not in panel or control.get('aria-expanded')!='false':errors.append([name,'invalid disclosure relationship',control.get('aria-controls')])
        inquiry_groups=[a for tag,a in scan.tags if 'contact-form' in a.get('class','').split()]
        if len(inquiry_groups)!=(1 if PAGE_ROUTES[path] in ('/','/lets-talk/') else 0):errors.append([name,'inquiry ownership'])
        for tag,a in scan.tags:
            if any(k.startswith('on') for k in a):errors.append([name,'inline event handler'])
            if tag=='img' and ('alt' not in a or not a.get('width') or not a.get('height')):errors.append([name,'missing image text/dimensions',a.get('src')])
            if tag=='button' and a.get('type')!='button':errors.append([name,'implicit submit'])
            refs=[a[key] for key in ('href','src') if key in a]
            refs.extend(candidate.strip().split()[0] for candidate in a.get('srcset','').split(',') if candidate.strip())
            for ref in refs:
                if 'work-with-us' in ref:errors.append([name,'obsolete public route',ref])
                dest,fragment=target(ref,path)
                if dest is None:continue
                links+=1
                if not dest.exists():errors.append([name,'missing resource',ref])
                elif fragment and dest in pages and fragment not in pages[dest].ids:errors.append([name,'missing fragment',ref])
        details.append({'route':PAGE_ROUTES[path],'file':name,'title':title,'ids':len(scan.ids),'headers_match':collections.Counter(scan.nav_links['original'])==collections.Counter(scan.nav_links['scroll']),'main':count('main'),'h1':count('h1'),'footer':count('footer'),'scripts':len(scripts),'paired_headings':len(paired),'heading_ranks':dict(collections.Counter(h['rank'] for h in headings.headings))})
    if len(titles)!=len(set(titles)):errors.append(['duplicate page titles'])
    content=json.loads((SITE/'site-content.json').read_text(encoding='utf-8'))
    for item in content['navigation']:
        for child in item.get('children',[]):
            dest,fragment=target(child['route'],SITE/'index.html')
            if fragment and not any(tag=='section' and a.get('id')==fragment and a.get('aria-labelledby') in pages[dest].ids for tag,a in pages[dest].tags):errors.append(['dropdown destination must be a labelled section',child['route']])
    for service in content['services']:
        if len(service['sections'])<2 or any(not section.get('paragraphs') for section in service['sections']):errors.append(['service landing content structure',service['route']])
    categories=content['categories']
    expected_categories=['Wellness','One Shot Depositing','Hollow Moulding','Mixing','Dry Filling']
    home=(SITE/'index.html').read_text(encoding='utf-8')
    home_categories=re.findall(r'<div class="category-copy"><h3[^>]*>(.*?)</h3>',home)
    if [category['title'] for category in categories]!=expected_categories or home_categories!=expected_categories:errors.append(['category logical order'])
    for category in categories:
        if home.count('href="products/#'+category['slug']+'"')!=1:errors.append(['missing or duplicate category CTA',category['slug']])
        if category['slug'] not in pages[SITE/'products/index.html'].ids:errors.append(['missing category destination',category['slug']])
    if home.count('class="category-card"')!=5:errors.append(['duplicate category cards'])
    if pages[SITE/'index.html'].category_links!=['products/#'+item['slug'] for item in categories]:errors.append(['category whole-card link destinations'])
    if len(pages[SITE/'products/index.html'].category_links)!=5:errors.append(['static category whole-card links'])
    if home.count('class="discovery-card" data-reveal')!=3:errors.append(['individual discovery entrance hooks'])
    if pages[SITE/'index.html'].discovery_links!=[item['route'] for item in content['discovery_cards']]:errors.append(['discovery whole-card link destinations'])
    for item in json.loads((ROOT/'assets/category-export-details.json').read_text()):
        if digest(ROOT/item['source'])!=item['source_sha256'] or digest(ROOT/item['web'])!=item['web_sha256']:errors.append(['category image provenance mismatch',item['web']])
    for item in json.loads((ROOT/'assets/trust-export-details.json').read_text()):
        if digest(ROOT/item['source'])!=item['source_sha256'] or digest(ROOT/item['web'])!=item['web_sha256']:errors.append(['trust mark provenance mismatch',item['web']])
    media=json.loads((ROOT/'assets/factory-media-details.json').read_text())
    if digest(ROOT/media['preserved'])!=media['source_sha256'] or digest(ROOT/media['web'])!=media['web_sha256'] or digest(ROOT/media['reduced_motion']['file'])!=media['reduced_motion']['sha256']:errors.append(['factory media provenance mismatch'])
    for item in json.loads((ROOT/'assets/icons/fontawesome-free-6.7.2/provenance.json').read_text())['icons']:
        if digest(ROOT/item['file'])!=item['sha256']:errors.append(['Font Awesome provenance mismatch',item['file']])
    css=(SITE/'styles.css').read_text(encoding='utf-8');js=(SITE/'script.js').read_text(encoding='utf-8')
    for ref in re.findall(r'url\([\'\"]?([^\)\'\"]+)',css):
        if not ref.startswith('#') and urlsplit(urljoin('/styles.css',ref)).path not in PUBLIC.files:errors.append(['CSS missing asset',ref])
    if re.search(r'\b(fetch|XMLHttpRequest|sendBeacon|WebSocket)\s*\(',js):errors.append(['unexpected network transport'])
    if re.search(r'\b(?:localStorage|sessionStorage)\b',js):errors.append(['unexpected storage'])
    # Verify retained artwork against the frozen intake baseline, rather than
    # recording current files and assuming they were always this way.
    baseline=json.loads((ROOT/'reviews/site-build-2026-10-24/local-source-manifest.json').read_text())['files']
    protected=[]
    for item in baseline:
        name=item['path'].replace('\\','/')
        if name.startswith('brand/source/') or name.endswith('-master.svg') or name.startswith('assets/logos/'):
            p=ROOT/name
            expected=item.get('sha256','').lower()
            if expected and (not p.exists() or digest(p)!=expected):errors.append(['protected input changed',name])
            protected.append(name)
    # Build in an isolated temporary root with sentinel edits to authoritative
    # partials. Assert propagation to every output, then rebuild unmodified and
    # compare all generated HTML byte-for-byte with the real build.
    spec=importlib.util.spec_from_file_location('site_builder',ROOT/'scripts/build_homepage.py');builder=importlib.util.module_from_spec(spec);spec.loader.exec_module(builder)
    original_read=lambda name:(SITE/name).read_text(encoding='utf-8')
    with tempfile.TemporaryDirectory(prefix='decocoa-check-',dir=SITE) as tmp:
        temp=Path(tmp);assert temp.resolve().is_relative_to(SITE.resolve());(temp/'assets/patterns').mkdir(parents=True);(temp/'prototype').mkdir()
        builder.ROOT=temp;builder.SITE=temp/'prototype'
        markers={'partials/header.html':'shared-header-propagation','partials/footer.html':'shared-footer-propagation','partials/inquiry.html':'shared-inquiry-propagation'}
        builder.read=lambda name:original_read(name)+ ('<!-- '+markers[name]+' -->' if name in markers else '')
        builder.build()
        for item in inventory:
            h=(temp/item['file']).read_text(encoding='utf-8')
            for marker in ('shared-header-propagation','shared-footer-propagation'):
                if h.count(marker)!=1:errors.append([item['file'],'shared partial propagation',marker])
            expected_inquiry=1 if item['route'] in ('/','/lets-talk/') else 0
            if h.count('shared-inquiry-propagation')!=expected_inquiry:errors.append([item['file'],'shared partial propagation','inquiry'])
        builder.read=original_read;builder.build()
        for item in inventory:
            if (temp/item['file']).read_bytes()!=(ROOT/item['file']).read_bytes():errors.append([item['file'],'nondeterministic build'])
    expected={'/','/products/','/products/filled-chocolate/','/products/chocolate-bar/','/products/chocolate-drizzle/','/our-people/','/our-craft/','/experience-center/','/lets-talk/','/gifting/','/craft-your-own/','/fundraising/','/wholesale/','/b2b/','/privacy-policy/','/terms-and-conditions/','/accessibility/','/404.html'}
    if {i['route'] for i in inventory}!=expected:errors.append(['route inventory mismatch'])
    result={'scope':'Static implementation checks only; browser interaction and visual checks separate.','pages':details,'category_order':home_categories,'category_cards':home.count('class="category-card"'),'discovery_cards':home.count('class="discovery-card" data-reveal'),'local_references_checked':links,'protected_baseline_files_checked':len(protected),'shared_header_footer_propagation':'pass' if not any('shared partial propagation' in e for e in errors) else 'fail','shared_inquiry_propagation':'pass' if not any('inquiry' in e and 'shared partial propagation' in e for e in errors) else 'fail','deterministic_rebuild':'pass' if not any('nondeterministic build' in e for e in errors) else 'fail','errors':errors}
    out=SITE/'qa-site-build';out.mkdir(exist_ok=True);(out/'static-checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    if errors:raise SystemExit(1)
if __name__=='__main__':run()
