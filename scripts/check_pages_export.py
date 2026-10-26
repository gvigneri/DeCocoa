"""Validate the actual Pages artifact, including project-prefix recovery URLs."""
from html.parser import HTMLParser
from contextlib import closing
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import argparse
import hashlib
import http.client
import json
import re
import subprocess
import threading
from export_pages import OUTPUT, REPORT, LICENSES, compatibility_routes, normalize_base, output_name
from preview_server import PublicSite, ROOT
from preview_server import LoopbackPreviewServer, handler_for
from preview_pages import ExportSite

class Document(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids = set()
        self.refs = []
        self.redirect = None
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if 'data-redirect' in attrs:
            self.redirect = attrs['data-redirect']
        self.refs.extend(attrs[key] for key in ('href', 'src', 'xlink:href') if attrs.get(key))
        if attrs.get('srcset'):
            self.refs.extend(candidate.split()[0] for candidate in attrs['srcset'].split(',') if candidate.strip())

def check(base):
    base = normalize_base(base)
    site = PublicSite()
    actual = {p.relative_to(OUTPUT).as_posix(): p for p in OUTPUT.rglob('*') if p.is_file()}
    redirects = compatibility_routes(site)
    expected = {output_name(route) for route in site.files} | set(LICENSES) | {output_name(route) for route in redirects} | {'redirect.js', '.nojekyll'}
    errors = []
    if set(actual) != expected:
        errors.append(['artifact file inventory', sorted(expected-set(actual)), sorted(set(actual)-expected)])
    manifest = json.loads(REPORT.read_text(encoding='utf-8'))
    if manifest['base_path'] != base:
        errors.append(['wrong export base path'])
    if {item['file']: item['sha256'] for item in manifest['files']} != {name: hashlib.sha256(path.read_bytes()).hexdigest() for name,path in actual.items()}:
        errors.append(['artifact manifest/hash mismatch'])
    for name in actual:
        if any(part in ('brand', 'source-external', 'reviews', 'handoff') for part in Path(name).parts) or name.endswith(('-master.svg', '.template.html')) or Path(name).name in ('site-content.json', 'generated-pages.json'):
            errors.append(['private/source file exported', name])
    for route, source in site.files.items():
        path = actual.get(output_name(route))
        if route != '/404.html' and (path is None or path.read_bytes() != source.read_bytes()):
            errors.append(['runtime source changed or missing', route])
    for name in LICENSES:
        if name not in actual or actual[name].read_bytes() != (ROOT/name).read_bytes():
            errors.append(['bundled license missing/modified', name])
    documents = {name: Document(path.read_text(encoding='utf-8')) for name,path in actual.items() if path.suffix=='.html'}
    checked = 0
    def resolve(ref, current, document=None):
        nonlocal checked
        if ref.startswith(('data:', 'mailto:', 'tel:')):
            return
        if ref.startswith('#') and document:
            if unquote(ref[1:]) not in document.ids:
                errors.append(['missing local fragment', current, ref])
            checked += 1
            return
        parts = urlsplit(urljoin(current, ref))
        if parts.scheme not in ('', 'https') or parts.netloc != 'pages.test':
            return
        checked += 1
        if not parts.path.startswith(base):
            errors.append(['reference escapes project base', current, ref, parts.path])
            return
        name = unquote(parts.path[len(base):])
        if not name or name.endswith('/'):
            name += 'index.html'
        if name not in actual:
            errors.append(['missing exported target', current, ref, name])
        elif parts.fragment:
            ids = documents[name].ids if name in documents else set(re.findall(r'\bid=[\'"]([^\'"]+)', actual[name].read_text(encoding='utf-8'))) if actual[name].suffix=='.svg' else set()
            if unquote(parts.fragment) not in ids:
                errors.append(['missing destination fragment', current, ref])
    for name, document in documents.items():
        current = 'https://pages.test' + base + name
        for ref in document.refs:
            resolve(ref, current, document)
    for name,path in actual.items():
        if path.suffix=='.css':
            for ref in re.findall(r'url\([\'\"]?([^\)\'\"]+)',path.read_text(encoding='utf-8')):
                if not ref.startswith('#'):
                    resolve(ref, 'https://pages.test'+base+name)
        elif path.suffix=='.svg':
            for ref in re.findall(r'(?:href|xlink:href)=[\'"]([^\'"]+)',path.read_text(encoding='utf-8')):
                if not ref.startswith('#'):
                    resolve(ref, 'https://pages.test'+base+name)
    # Pages serves the same 404 document at the original missing URL depth.
    for missing in ('unknown/deep/path', 'unknown/deep/', 'prototype/unknown/'):
        for ref in documents['404.html'].refs:
            resolve(ref, 'https://pages.test'+base+missing, documents['404.html'])
    redirect_cases = []
    for route,target in redirects.items():
        document = documents.get(output_name(route))
        if not document or not document.redirect:
            errors.append(['missing compatibility redirect', route])
            continue
        current = 'https://pages.test'+base+output_name(route)
        destination = 'https://pages.test'+base+target.lstrip('/')
        if urljoin(current, document.redirect) != destination:
            errors.append(['compatibility destination mismatch', route])
        redirect_cases.append({'current':current+'?topic=Gifting&product=chocolate-bar#inquiry', 'target':document.redirect,
                               'expected':destination+'?topic=Gifting&product=chocolate-bar#inquiry'})
    # Execute the shipped redirect/shared code against real prefixed URLs.
    code = r"""
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const shared=fs.readFileSync(process.argv[1],'utf8'),redirect=fs.readFileSync(process.argv[2],'utf8');
const cases=JSON.parse(process.argv[3]);
for(const c of cases){let result;const current=new URL(c.current);vm.runInNewContext(redirect,{URL,document:{documentElement:{dataset:{redirect:c.target}}},location:{href:current.href,search:current.search,hash:current.hash,replace:v=>result=v}});assert.equal(result,c.expected);}
let legacy=0;
for(const base of ['/', '/DeCocoa/'])for(const suffix of ['lets-talk/', 'lets-talk/index.html'])for(const [hash,target] of Object.entries({gifting:'gifting/','craft-your-own':'craft-your-own/','chocolate-bar':'craft-your-own/#chocolate-bars',basket:'craft-your-own/#baskets',fundraising:'fundraising/',business:'b2b/'})){
 let result;const current=new URL('https://pages.test'+base+suffix+'?topic=Gifting#'+hash);
 vm.runInNewContext(shared,{URL,document:{body:{dataset:{}},currentScript:{src:'https://pages.test'+base+'script.js'}},location:{pathname:current.pathname,href:current.href,hash:current.hash,search:current.search,replace:v=>result=v}});
 const expected=new URL(target,'https://pages.test'+base);expected.search=current.search;assert.equal(result,expected.href);legacy++;
}
const helper=shared.match(/const canonicalPath = [^\n]+/)[0];
const context=shared.match(/const publicContextURL = \(hash\) => \{[\s\S]*?\n  \};/)[0];
const sandbox={URL,location:{href:'https://pages.test/DeCocoa/lets-talk/index.html?old=context'},contextFields:[['topic','contact-reason'],['product','contact-product']],document:{getElementById:id=>({value:id==='contact-reason'?'Gifting':'chocolate-bar'})}};
vm.runInNewContext(helper+'\n'+context+'\nresult=publicContextURL("#inquiry").href;',sandbox);
assert.equal(sandbox.result,'https://pages.test/DeCocoa/lets-talk/?topic=Gifting&product=chocolate-bar#inquiry');
console.log(JSON.stringify({compatibility_context_cases:cases.length,legacy_context_cases:legacy,project_context_url:'pass'}));
"""
    try:
        result = subprocess.run(['node','-e',code,str(OUTPUT/'script.js'),str(OUTPUT/'redirect.js'),json.dumps(redirect_cases)],check=True,capture_output=True,text=True,encoding='utf-8')
        behavior = json.loads(result.stdout)
    except subprocess.CalledProcessError as error:
        behavior = 'fail'
        errors.append(['exported JavaScript URL/context behavior', error.stderr])
    # Serve only the finished artifact, with the same project prefix as Pages.
    http_checked = 0
    with LoopbackPreviewServer(('127.0.0.1',0),handler_for(ExportSite(base),quiet=True)) as server:
        worker=threading.Thread(target=lambda:server.serve_forever(poll_interval=.02),daemon=True)
        worker.start()
        try:
            cases=[(base+name,200,path) for name,path in actual.items()]
            cases.extend((base+route.lstrip('/'),200,actual[output_name(route)]) for route in site.pages)
            cases.extend((base+name,404,actual['404.html']) for name in ('unknown/deep/path','unknown/deep/','assets/','prototype/site-content.json','brand/source/','reviews/'))
            for route,status,path in cases:
                with closing(http.client.HTTPConnection('127.0.0.1',server.server_port,timeout=10)) as connection:
                    connection.request('GET',route)
                    response=connection.getresponse()
                    if response.status!=status or response.read()!=path.read_bytes():
                        errors.append(['project-prefix HTTP response mismatch',route,response.status])
                    http_checked+=1
            for route,destination in (('/',base),(base+'products?topic=Gifting',base+'products/?topic=Gifting')):
                with closing(http.client.HTTPConnection('127.0.0.1',server.server_port,timeout=10)) as connection:
                    connection.request('GET',route)
                    response=connection.getresponse();response.read()
                    if response.status!=308 or response.getheader('Location')!=destination:
                        errors.append(['project-prefix directory redirect mismatch',route])
                    http_checked+=1
        finally:
            server.shutdown();worker.join(timeout=5)
    report = {'base_path':base,'content_pages':len(site.pages),'artifact_files':len(actual),'local_references_checked':checked,
              'runtime_resources':len(site.files)-len(site.pages),'nested_404_recovery':'pass' if not errors else 'see errors',
              'javascript_context':behavior,'loopback_http_cases':http_checked,'errors':errors}
    (REPORT.parent/'pages-export-checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
    if errors:
        raise SystemExit(1)

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-path',default='/DeCocoa/')
    check(parser.parse_args().base_path)
