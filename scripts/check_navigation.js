/* Exercise production header events with a small DOM fixture; visual QA is separate. */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const source = fs.readFileSync(path.join(__dirname, '../prototype/script.js'), 'utf8');

function fixture({width = 1600, reduced = false, href = 'https://preview.test/DeCocoa/', capability = false} = {}) {
  const events = new Map(), timers = new Map(), elements = new Map();
  let timer = 0, document;
  const media = query => ({matches: query.includes('max-width: 600') ? width <= 600 :
    query.includes('min-width: 1536') ? width >= 1536 : query.includes('min-width: 1200') ? width >= 1200 :
    query.includes('prefers-reduced-motion') ? reduced : query.includes('hover: hover'), addEventListener() {}});
  class Element {
    constructor(name, classes = []) {
      this.name = name; this.classes = new Set(classes); this.children = []; this.listeners = new Map();
      this.attributes = {}; this.dataset = {}; this.style = {setProperty() {}}; this.hidden = false; this.offsetHeight = 112;
      this.classList = {
        add: (...names) => names.forEach(value => this.classes.add(value)),
        remove: (...names) => names.forEach(value => this.classes.delete(value)),
        contains: value => this.classes.has(value),
        toggle: (name, force) => {const value = force ?? !this.classes.has(name); if(value)this.classes.add(name);else this.classes.delete(name);return value;}
      };
    }
    append(child) { this.children.push(child); child.parent = this; return child; }
    descendants() { return this.children.flatMap(child => [child, ...child.descendants()]); }
    querySelector(selector) { return this.querySelectorAll(selector)[0] || null; }
    querySelectorAll(selector) {
      return this.descendants().filter(element => selector.split(',').some(part => {
        if(part.startsWith('.'))return element.classes.has(part.slice(1));
        if(part === 'a' || part === 'a[href]')return !!element.href;
        return part === 'button' && element.name.includes('toggle');
      }));
    }
    addEventListener(name, fn) { if(!this.listeners.has(name))this.listeners.set(name, []); this.listeners.get(name).push(fn); }
    emit(name, extra = {}) { const event = {target:this, detail:0, pointerType:'mouse', preventDefault(){this.prevented=true;}, ...extra}; (this.listeners.get(name) || []).forEach(fn => fn(event)); return event; }
    setAttribute(name, value) { this.attributes[name] = value; }
    removeAttribute(name) { delete this.attributes[name]; }
    contains(element) { return element === this || this.descendants().includes(element); }
    focus() { document.activeElement = this; }
    getBoundingClientRect() { return {height:112,bottom:112}; }
    getClientRects() { let parent = this; while(parent){if(parent.hidden)return [];parent=parent.parent;}return [this.getBoundingClientRect()]; }
    closest(selector) { let parent = this; while(parent){if(selector === '[inert]' && parent.inert)return parent;parent=parent.parent;}return null; }
  }
  const body = new Element('body'), html = new Element('html');
  const headers = ['original','scroll'].map((name, index) => {
    const header = body.append(new Element(name, [name+'-header']));
    const brand = header.append(new Element('brand',['brand'])); brand.href = '/';
    const toggle = header.append(new Element('menu-toggle',['menu-toggle']));
    toggle.display = width >= (index ? 1536 : 1200) ? 'none' : 'block';
    const nav = header.append(new Element('nav',['main-navigation']));
    const dropdown = nav.append(new Element('dropdown',['nav-dropdown']));
    const parent = dropdown.append(new Element('parent',['nav-parent'])); parent.href = '/products/';
    const subToggle = dropdown.append(new Element('submenu-toggle',['submenu-toggle']));
    const panel = dropdown.append(new Element('panel',['submenu'])); panel.hidden = true;
    const destination = panel.append(new Element('destination')); destination.href = '/products/#tablet';
    return {header,toggle,nav,dropdown,parent,subToggle,panel,destination};
  });
  const contactReason = new Element('contact-reason');
  contactReason.options = [{value:'Partner Brands'},{value:'Our craft'}];
  elements.set('contact-reason', contactReason);
  if(capability){const target = new Element('mixing');target.dataset.capabilityDestination='../our-craft/#mixing';elements.set('mixing',target);}
  document = {
    body,documentElement:html,activeElement:body,currentScript:{src:'https://preview.test/DeCocoa/script.js'},hidden:false,
    getElementById:id => elements.get(id),
    querySelector:selector => selector === '.original-header' ? headers[0].header : selector === '.scroll-header' ? headers[1].header : null,
    querySelectorAll:selector => selector === '[data-header]' ? headers.map(item=>item.header) : selector === 'a[href]' ? body.querySelectorAll(selector) : [],
    addEventListener(name, fn) { if(!events.has(name))events.set(name,[]);events.get(name).push(fn); }
  };
  const location = new URL(href), redirects = [];
  location.replace = value => redirects.push(value); location.assign = value => redirects.push(value);
  const context = {document,location,URL,URLSearchParams,innerHeight:900,scrollY:0,window:{},
    history:{replaceState(){},pushState(){}},matchMedia:media,getComputedStyle:element=>({display:element.display || 'block'}),
    addEventListener:document.addEventListener,requestAnimationFrame:fn=>fn(),
    setTimeout:fn=>{timers.set(++timer,fn);return timer;},clearTimeout:id=>timers.delete(id),console};
  vm.runInNewContext(source, context);
  return {headers,body,document,redirects,contactReason,
    flush(){while(timers.size){const pending=[...timers.values()];timers.clear();pending.forEach(fn=>fn());}},
    emit(name, extra = {}) { const event={target:body,preventDefault(){this.prevented=true;},...extra};(events.get(name)||[]).forEach(fn=>fn(event));return event; }
  };
}

const desktop = fixture(), d = desktop.headers[0];
d.dropdown.emit('pointerenter');
assert.equal(d.panel.hidden,false,'desktop hover opens the image panel');
assert.equal(d.subToggle.attributes['aria-expanded'],'true');
d.dropdown.emit('pointerleave');desktop.flush();
assert.equal(d.panel.hidden,true,'leaving the complete trigger/panel closes the hover disclosure');
d.parent.emit('keydown',{key:'ArrowDown'});
assert.equal(desktop.document.activeElement,d.destination,'parent ArrowDown opens and enters the submenu');
desktop.emit('keydown',{key:'Escape'});
assert.equal(d.panel.hidden,true);assert.equal(desktop.document.activeElement,d.subToggle,'Escape returns focus to the independent toggle');
d.subToggle.emit('click');
desktop.emit('click',{target:d.destination});assert.equal(d.panel.hidden,false,'clicking inside the panel does not close before navigation');
desktop.emit('click');assert.equal(d.panel.hidden,true,'outside click closes the disclosure');

const mobile = fixture({width:390}), m = mobile.headers[0];
m.dropdown.emit('pointerenter');assert.equal(m.panel.hidden,true,'compact menus do not open from hover');
m.toggle.emit('click');assert.equal(m.nav.classList.contains('is-open'),true);assert.equal(mobile.body.style.overflow,'hidden');
m.subToggle.emit('click');assert.equal(m.panel.hidden,false);
m.subToggle.emit('click',{detail:1});
assert.equal(m.panel.inert,true,'closing submenu immediately becomes noninteractive');
assert.equal(m.subToggle.attributes['aria-expanded'],'false');
mobile.flush();assert.equal(m.panel.hidden,true);
m.toggle.focus();mobile.emit('keydown',{key:'Escape'});
assert.equal(m.nav.inert,true,'closing drawer immediately becomes noninteractive');
mobile.flush();assert.equal(m.nav.classList.contains('is-open'),false);assert.equal(mobile.body.style.overflow,'');

const staticMenu=fixture({width:390,reduced:true}), s=staticMenu.headers[0];
s.toggle.emit('click');s.subToggle.emit('click');s.subToggle.emit('click');
assert.equal(s.panel.hidden,true,'reduced motion closes without waiting for an animation');
const topic = fixture({href:'https://preview.test/DeCocoa/lets-talk/?topic=B2B#inquiry'});
assert.equal(topic.contactReason.value,'Partner Brands','legacy B2B inquiries retain their renamed selection');
const moved = fixture({href:'https://preview.test/DeCocoa/products/#mixing',capability:true});
assert.deepEqual(moved.redirects,['https://preview.test/DeCocoa/our-craft/#mixing'],'old capability hashes resolve beneath the deployment base');
console.log('Navigation checks passed: desktop hover, keyboard focus/Escape, outside click, mobile inert exit, reduced motion, legacy topic and capability routes.');
