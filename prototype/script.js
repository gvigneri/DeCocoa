(() => {
  const body = document.body;
  if (!body || body.dataset.decocoaInitialized) return;
  body.dataset.decocoaInitialized = "true";
  const siteRoot = new URL('./', document.currentScript?.src || location.href);
  const canonicalPath = pathname => pathname.replace(/\/index\.html$/, '/');
  // Old Work With Us links are redirected here by the preview. Only these
  // public offering fragments are forwarded; message fields never enter URLs.
  if(canonicalPath(location.pathname)===new URL('lets-talk/',siteRoot).pathname){
    const legacy={gifting:'../gifting/','craft-your-own':'../craft-your-own/','chocolate-bar':'../craft-your-own/#chocolate-bars',basket:'../craft-your-own/#baskets',fundraising:'../fundraising/',business:'../b2b/'};
    const route=legacy[location.hash.slice(1)];
    if(route){const destination=new URL(route,location.href);destination.search=location.search;location.replace(destination.href);return;}
  }
  const original = document.querySelector('.original-header');
  const sticky = document.querySelector('.scroll-header');
  const desktop = matchMedia('(min-width: 1536px)');
  const phone = matchMedia('(max-width: 600px)');
  const contexts = [...document.querySelectorAll('[data-header]')].map(header => ({
    header, toggle:header.querySelector('.menu-toggle'), nav:header.querySelector('.main-navigation'),
    dropdowns:[...header.querySelectorAll('.nav-dropdown')].map(dropdown=>({
      dropdown,toggle:dropdown.querySelector('.submenu-toggle'),panel:dropdown.querySelector('.submenu'),
      latched:false,pointerInside:false,hoverSuppressed:false,hoverTimer:null
    })).filter(d=>d.toggle && d.panel)
  })).filter(c=>c.toggle && c.nav);
  const syncHeaderMetrics = () => {
    const originalHeight=original?.getBoundingClientRect().height || 0;
    const menuHeight=original?.querySelector('.menu-toggle')?.getBoundingClientRect().height || 0;
    original?.style.setProperty('--phone-header-top-height',`${Math.max(0,originalHeight-menuHeight)}px`);
    contexts.forEach(c=>{
      c.header.style.setProperty('--header-height',`${c.header.offsetHeight}px`);
      const bottom=Math.max(0,c.header.getBoundingClientRect().bottom);
      c.header.style.setProperty('--drawer-height',`${Math.max(0,innerHeight-bottom)}px`);
    });
    document.documentElement.style.setProperty('--sticky-height',`${phone.matches?menuHeight:(sticky?.offsetHeight || 0)}px`);
    document.documentElement.style.setProperty('--original-header-height',`${originalHeight}px`);
  };
  syncHeaderMetrics();
  if ('ResizeObserver' in window) {
    const observer=new ResizeObserver(syncHeaderMetrics);
    contexts.forEach(c=>observer.observe(c.header));
  }
  addEventListener('resize',syncHeaderMetrics);
  sticky?.addEventListener('transitionend',event=>{if(event.target===sticky)syncHeaderMetrics();});
  const openMenu=c=>c.nav.classList.contains('is-open') && !c.menuClosing;
  const phoneAnimationAllowed=()=>phone.matches && !matchMedia('(prefers-reduced-motion: reduce)').matches;
  const syncMenuToggle=(c,open)=>{c.toggle.setAttribute('aria-expanded',String(open));c.toggle.textContent=phone.matches && open?'Close':'Menu';};
  const updateScrollLock=()=>{const open=contexts.some(c=>openMenu(c) || c.menuClosing);body.style.overflow=open?'hidden':'';body.classList.toggle('menu-open',open);};
  const finishSub=d=>{
    clearTimeout(d.closeTimer);d.closing=false;d.panel.hidden=true;
    d.panel.classList.remove('is-closing');d.panel.inert=false;d.panel.removeAttribute('aria-hidden');
  };
  const closeSub=(d,focus=false,suppressHover=false,animate=phoneAnimationAllowed())=>{
    const returnFocus=focus || d.panel.contains(document.activeElement);
    clearTimeout(d.hoverTimer);d.latched=false;
    if(suppressHover)d.hoverSuppressed=true;
    d.toggle.setAttribute('aria-expanded','false');
    if(returnFocus)d.toggle.focus();
    if(d.closing && animate)return;
    if(!animate || d.panel.hidden){finishSub(d);return;}
    d.closing=true;d.panel.inert=true;d.panel.setAttribute('aria-hidden','true');
    d.panel.classList.add('is-closing');d.closeTimer=setTimeout(()=>finishSub(d),180);
  };
  const showSub=(c,d,latch=false)=>{
    // Pointer hover never hides a sibling that currently holds keyboard focus.
    if(!latch && c.dropdowns.some(other=>other!==d && other.panel.contains(document.activeElement)))return;
    c.dropdowns.filter(other=>other!==d).forEach(other=>closeSub(other,false,other.pointerInside));
    clearTimeout(d.hoverTimer);clearTimeout(d.closeTimer);d.closing=false;
    d.panel.classList.remove('is-closing');d.panel.inert=false;d.panel.removeAttribute('aria-hidden');
    if(latch){d.latched=true;d.hoverSuppressed=false;}
    d.toggle.classList.remove('pointer-collapsed');
    d.panel.hidden=false;d.toggle.setAttribute('aria-expanded','true');
  };
  const finishMenu=c=>{
    clearTimeout(c.closeTimer);c.menuClosing=false;
    c.nav.classList.remove('is-open','is-closing');c.nav.inert=false;c.nav.removeAttribute('aria-hidden');
    c.dropdowns.forEach(finishSub);updateScrollLock();
  };
  const closeMenu=(c,focus=false,animate=phoneAnimationAllowed())=>{
    if(!c)return;
    const returnFocus=focus || c.nav.contains(document.activeElement);
    syncMenuToggle(c,false);
    if(returnFocus && c.toggle.getClientRects().length)c.toggle.focus();
    if(c.menuClosing && animate)return;
    const wasOpen=openMenu(c);
    c.dropdowns.forEach(d=>closeSub(d,false,false,animate));
    if(!animate || !wasOpen){finishMenu(c);return;}
    c.menuClosing=true;c.nav.inert=true;c.nav.setAttribute('aria-hidden','true');
    c.nav.classList.add('is-closing');updateScrollLock();
    c.closeTimer=setTimeout(()=>finishMenu(c),240);
  };
  const showMenu=c=>{
    clearTimeout(c.closeTimer);c.menuClosing=false;c.nav.classList.remove('is-closing');
    c.dropdowns.filter(d=>d.closing).forEach(finishSub);
    c.nav.inert=false;c.nav.removeAttribute('aria-hidden');c.nav.classList.add('is-open');
    syncMenuToggle(c,true);updateScrollLock();syncHeaderMetrics();
  };
  contexts.forEach(c=>{
    c.toggle.addEventListener('click',()=>{
      const open=!openMenu(c);
      contexts.filter(other=>other!==c).forEach(other=>closeMenu(other));
      if(open)showMenu(c);else closeMenu(c);
      syncHeaderMetrics();
    });
    c.dropdowns.forEach(d=>{
      d.toggle.addEventListener('click',event=>{
        if(d.panel.hidden || d.closing || !d.latched)showSub(c,d,true);
        else {closeSub(d,false,true);if(phone.matches && event.detail>0)d.toggle.classList.add('pointer-collapsed');}
      });
      d.toggle.addEventListener('keydown',event=>{
        if(event.key==='ArrowDown'){event.preventDefault();showSub(c,d,true);d.panel.querySelector('a')?.focus();}
      });
      const hoverPointer=event=>!phone.matches && event.pointerType!=='touch' && matchMedia('(hover: hover)').matches;
      d.dropdown.addEventListener('pointerenter',event=>{
        if(!hoverPointer(event))return;
        d.pointerInside=true;clearTimeout(d.hoverTimer);
        if(!d.hoverSuppressed)showSub(c,d);
      });
      d.dropdown.addEventListener('pointerleave',event=>{
        if(!hoverPointer(event))return;
        d.pointerInside=false;d.hoverSuppressed=false;clearTimeout(d.hoverTimer);
        d.hoverTimer=setTimeout(()=>{
          if(!d.pointerInside && !d.latched && !d.dropdown.contains(document.activeElement))closeSub(d);
        },160);
      });
      d.dropdown.addEventListener('focusout',()=>requestAnimationFrame(()=>{
        if(!d.dropdown.contains(document.activeElement) && !d.pointerInside)closeSub(d);
      }));
    });
    c.header.addEventListener('focusout',()=>requestAnimationFrame(()=>{
      if(!c.header.contains(document.activeElement)){
        if(!openMenu(c))c.dropdowns.forEach(d=>closeSub(d));updateHeaderState();
      }
    }));
  });
  document.addEventListener('keydown',event=>{
    contexts.forEach(c=>c.dropdowns.forEach(d=>d.toggle.classList.remove('pointer-collapsed')));
    const c=contexts.find(c=>c.header.contains(document.activeElement)) || contexts.find(openMenu) || contexts.find(c=>c.dropdowns.some(d=>!d.panel.hidden && !d.closing));
    if(!c)return;
    if(event.key==='Escape'){
      const d=c.dropdowns.find(d=>!d.panel.hidden && !d.closing);
      if(d){event.preventDefault();closeSub(d,true,true);}
      else if(openMenu(c)){event.preventDefault();closeMenu(c,true);}
    }
    if(event.key==='Tab' && openMenu(c) && getComputedStyle(c.toggle).display!=='none'){
      const controls=[c.toggle,...c.nav.querySelectorAll('button,a[href]')].filter(el=>!el.hidden && !el.closest('[inert]') && el.getClientRects().length);
      const current=controls.indexOf(document.activeElement);
      const next=current<0?(event.shiftKey?controls.length-1:0):(current+(event.shiftKey?-1:1)+controls.length)%controls.length;
      event.preventDefault();controls[next]?.focus();
    }
  });
  document.addEventListener('click',event=>contexts.forEach(c=>c.dropdowns.forEach(d=>{if(!d.dropdown.contains(event.target))closeSub(d);} )));
  const resetNavigation=()=>{
    const focusedHeader=contexts.some(c=>c.header.contains(document.activeElement));
    contexts.forEach(c=>{c.dropdowns.forEach(d=>{d.pointerInside=false;d.hoverSuppressed=false;d.toggle.classList.remove('pointer-collapsed');});closeMenu(c,false,false);});
    if(focusedHeader && !document.activeElement.getClientRects().length)(phone.matches?original?.querySelector('.menu-toggle'):original?.querySelector('.brand'))?.focus();
    updateHeaderState();
  };
  desktop.addEventListener('change',resetNavigation);
  phone.addEventListener('change',resetNavigation);
  matchMedia('(min-width: 1200px)').addEventListener('change',resetNavigation);
  const contextFields=[['topic','contact-reason'],['product','contact-product']];
  const setContext = (search,resetMissing=false) => {
    const params=new URLSearchParams(search);
    for (const [key,id] of contextFields) {
      const select=document.getElementById(id),raw=params.get(key),value=key==='topic' && raw==='Wholesale / B2B'?'B2B':raw;
      if(!select)continue;
      if(value!==null && [...select.options].some(option=>option.value===value)) select.value=value;
      else if(resetMissing)select.value='';
    }
  };
  const publicContextURL = (hash) => {
    const next=new URL(location.href);
    next.pathname=canonicalPath(next.pathname);
    next.search='';
    for(const [key,id] of contextFields){
      const select=document.getElementById(id);
      if(select?.value)next.searchParams.set(key,select.value);
    }
    next.hash=hash;
    return next;
  };
  setContext(location.search);
  // Only public topic/product selections enter history. Personal fields stay in
  // the current DOM and are never serialized, persisted or transmitted.
  contextFields.forEach(([,id])=>document.getElementById(id)?.addEventListener('change',()=>{
    history.replaceState(null,'',publicContextURL(location.hash));
  }));
  addEventListener('popstate',()=>setContext(location.search,true));
  const focusFragment=(hash,keyboardArrival=false)=>{
    let section;
    try{section=document.getElementById(decodeURIComponent(hash.slice(1)));}catch{return false;}
    if(!section)return false;
    if(section.classList.contains('anchor-alias'))section=section.closest('section') || section;
    const target=section.matches('h1,h2,h3')?section:section.querySelector('h1,h2,h3') || section;
    // Keep semantic focus/Tab continuation without painting a large arrival
    // rectangle after page load or pointer activation. Keyboard jumps retain
    // the usual focus indicator; controls and validation focus are untouched.
    const quiet=!keyboardArrival && target.matches('h1,h2,h3,h4,h5,h6,section,main');
    target.classList.toggle('fragment-arrival-quiet',quiet);
    if(quiet)target.addEventListener('blur',()=>target.classList.remove('fragment-arrival-quiet'),{once:true});
    target.tabIndex=-1;target.focus({preventScroll:true});section.scrollIntoView({block:'start'});
    return true;
  };
  document.querySelectorAll('a[href]').forEach(link=>link.addEventListener('click',event=>{
    const destination=new URL(link.href,location.href);
    if(destination.origin!==location.origin || canonicalPath(destination.pathname)!==canonicalPath(location.pathname) || !destination.hash || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey)return;
    let section;
    try{section=document.getElementById(decodeURIComponent(destination.hash.slice(1)));}catch{return;}
    if(!section)return;
    event.preventDefault();
    setContext(destination.search);
    const next=publicContextURL(destination.hash);
    if(next.href!==location.href)history.pushState(null,'',next);
    contexts.forEach(c=>closeMenu(c));
    focusFragment(destination.hash,event.detail===0);
    requestAnimationFrame(updateHeaderState);
  }));
  let lastY=scrollY,showOnDown=false,queued=false;
  function updateHeaderState() {
    if (!original || !sticky) return;
    if(phone.matches){
      sticky.classList.remove('is-visible');sticky.inert=true;sticky.setAttribute('aria-hidden','true');
      original.inert=false;original.removeAttribute('aria-hidden');
      if(openMenu(contexts[1]) || contexts[1]?.menuClosing)closeMenu(contexts[1],false,false);
      syncHeaderMetrics();return;
    }
    const past=scrollY>original.offsetHeight+20;
    const focusOriginal=original.contains(document.activeElement);
    const focusSticky=sticky.contains(document.activeElement);
    const show=focusSticky||(past&&showOnDown);
    // Never remove a focused control from the accessible tree. It settles after focus leaves.
    sticky.classList.toggle('is-visible',show);
    sticky.inert=!show; sticky.setAttribute('aria-hidden',String(!show));
    original.inert=past&&!focusOriginal;
    if(original.inert)original.setAttribute('aria-hidden','true');else original.removeAttribute('aria-hidden');
    if(!show&&!focusSticky)closeMenu(contexts[1]);
    syncHeaderMetrics();
  }
  addEventListener('scroll',()=>{
    const y=scrollY,delta=y-lastY;
    if(Math.abs(delta)>2)showOnDown=delta>0;
    lastY=y;
    if(!queued){queued=true;requestAnimationFrame(()=>{queued=false;updateHeaderState();});}
  },{passive:true});
  updateHeaderState();
  if(location.hash)requestAnimationFrame(()=>{focusFragment(location.hash);updateHeaderState();});
  // Motion follows the current system preference. No stored pause state or
  // removed control is needed to initialize shared motion behavior.
  const reduced=matchMedia('(prefers-reduced-motion: reduce)');
  const syncMotion=()=>{
    body.classList.toggle('reduce-motion',reduced.matches);
    if(reduced.matches)contexts.forEach(c=>{if(c.menuClosing)finishMenu(c);else c.dropdowns.filter(d=>d.closing).forEach(finishSub);});
    document.querySelectorAll('[data-category-carousel]').forEach(root=>root.dispatchEvent(new Event('decocoa-motion-change')));
  };
  reduced.addEventListener('change',syncMotion);syncMotion();
  body.classList.toggle('entrance-static',reduced.matches);
  body.classList.add('motion-ready');
  document.addEventListener('visibilitychange',()=>body.classList.toggle('is-document-hidden',document.hidden));
  body.classList.toggle('is-document-hidden',document.hidden);
  if('IntersectionObserver' in window) {
    const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{entry.target.classList.toggle('is-in-view',entry.isIntersecting);if(entry.isIntersecting)entry.target.classList.add('has-entered');}),{threshold:0.01});
    document.querySelectorAll('.hero,.pattern-surface,[data-reveal]').forEach(el=>observer.observe(el));
  } // Missing observers leave decorative motion paused.
  document.querySelectorAll('[data-category-carousel]').forEach(root=>window.DeCocoaCategories?.mount(root,()=>({reduced:reduced.matches})));
  const group=document.querySelector('.contact-form');
  if (!group) return;
  const status=group.querySelector('.form-status');
  if (!status || !group.querySelector('.local-fields') || !group.querySelector('.preview-message')) return;
  const checks=[
    {field:group.querySelector('#contact-name'),error:group.querySelector('#name-error'),message:'Please enter your name.'},
    {field:group.querySelector('#contact-email'),error:group.querySelector('#email-error'),message:'Please enter a valid email address.'},
    {field:group.querySelector('#contact-message'),error:group.querySelector('#message-error'),message:'Please enter a message.'}
  ];
  checks.forEach(({field,error})=>{
    field.setAttribute('aria-describedby',error.id);
    field.addEventListener('input',()=>{field.removeAttribute('aria-invalid');error.textContent='';status.hidden=true;});
  });
  group.querySelector('.preview-message').addEventListener('click',()=>{
    let firstInvalid;
    checks.forEach(({field,error,message})=>{
      const invalid=!field.value.trim()||!field.validity.valid;
      error.textContent=invalid?message:'';
      if(invalid){field.setAttribute('aria-invalid','true');firstInvalid ||= field;}else field.removeAttribute('aria-invalid');
    });
    if(firstInvalid){status.hidden=true;firstInvalid.focus();}
    else {status.hidden=false;status.textContent='Message delivery is not connected yet.';status.focus();}
  });
  group.querySelector('.local-fields').disabled=false;
})();
