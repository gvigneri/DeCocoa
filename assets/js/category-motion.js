/* DeCocoa single-copy category row. No cloned links or reordered DOM content. */
((host) => {
  const modulo=(value,span)=>((value%span)+span)%span;
  function responsiveLayout(view,columns,gap=24) {
    const width=(view-gap*(columns-1))/columns;
    return {width,pitch:width+gap};
  }
  function createInteractionPause(duration=3000) {
    let until=0;
    return {pause:time=>{until=Math.max(until,time+duration);},active:time=>time<until};
  }
  function createState({count,pitch,width,view,speed=15}) {
    const state={count,pitch,width,view,speed,phase:0};
    state.position=index=>modulo(index*pitch+state.phase+pitch,count*pitch)-pitch;
    state.tick=(seconds,gates={})=>{
      if(!Object.values(gates).some(Boolean))state.phase=modulo(state.phase+Math.max(0,seconds)*speed,count*pitch);
    };
    state.reveal=index=>{
      const x=state.position(index);
      if(x<0 || x+width>view)state.phase=modulo(state.phase+(view-width)/2-x,count*pitch);
    };
    state.move=direction=>{state.phase=modulo(state.phase-direction*pitch,count*pitch);};
    return state;
  }
  function mount(root,preference) {
    if(root.dataset.categoryInitialized)return;
    root.dataset.categoryInitialized='true';
    const track=root.querySelector('.category-track'),cards=[...track.children];
    const interaction=createInteractionPause();
    let state,looping=false,inView=false,hovered=false,focused=false,lastTime=0,drag=null,moved=false;
    const render=()=>{
      if(!looping)return;
      // Enhanced positions own horizontal placement. A legacy overflow:hidden
      // fallback must not retain a browser-created scroll offset after focus.
      if(track.scrollLeft)track.scrollLeft=0;
      cards.forEach((card,index)=>card.style.transform=`translate3d(${state.position(index)}px,0,0)`);
    };
    const measure=()=>{
      root.classList.remove('is-looping');track.style.height='';
      cards.forEach(card=>card.style.transform='');
      const view=track.clientWidth-24,gap=parseFloat(getComputedStyle(track).gap)||24;
      const columns=parseInt(getComputedStyle(root).getPropertyValue('--category-columns'))||4;
      const {width,pitch}=responsiveLayout(view,columns,gap);
      root.style.setProperty('--category-width',`${width}px`);
      const height=Math.max(...cards.map(card=>card.offsetHeight));
      looping=!preference().reduced && 'IntersectionObserver' in host && (cards.length-1)*(width+gap)>view;
      state=createState({count:cards.length,pitch,width,view});
      if(looping){
        track.scrollLeft=0;track.style.height=`${height+24}px`;root.classList.add('is-looping');
        const active=cards.findIndex(card=>card.contains(document.activeElement));
        if(active>=0)state.reveal(active);render();
      }
    };
    measure();
    const move=direction=>{
      interaction.pause(performance.now());
      if(looping){state.move(direction);render();}
      else track.scrollBy({left:direction*(cards[0].offsetWidth+24),behavior:'auto'});
    };
    root.addEventListener('pointerenter',event=>{if(event.pointerType!=='touch')hovered=true;});
    root.addEventListener('pointerleave',()=>{hovered=false;});
    root.addEventListener('focusin',event=>{
      focused=true;
      const index=cards.findIndex(card=>card.contains(event.target));
      if(looping && index>=0){state.reveal(index);render();requestAnimationFrame(()=>{if(looping && track.scrollLeft)track.scrollLeft=0;});}
    });
    track.addEventListener('scroll',()=>{if(looping && track.scrollLeft)track.scrollLeft=0;},{passive:true});
    root.addEventListener('focusout',()=>requestAnimationFrame(()=>{focused=root.contains(document.activeElement);}));
    track.addEventListener('wheel',()=>interaction.pause(performance.now()),{passive:true});
    track.addEventListener('pointerdown',event=>{
      interaction.pause(performance.now());moved=false;
      if(looping && event.isPrimary && event.button===0)drag={id:event.pointerId,x:event.clientX,phase:state.phase};
    });
    track.addEventListener('pointermove',event=>{
      if(!drag || event.pointerId!==drag.id)return;
      const delta=event.clientX-drag.x;
      if(Math.abs(delta)>8){moved=true;track.setPointerCapture(event.pointerId);state.phase=modulo(drag.phase+delta,state.count*state.pitch);render();}
    });
    const endDrag=event=>{interaction.pause(performance.now());if(drag?.id===event.pointerId){drag=null;if(track.hasPointerCapture(event.pointerId))track.releasePointerCapture(event.pointerId);}};
    track.addEventListener('pointerup',endDrag);track.addEventListener('pointercancel',endDrag);
    track.addEventListener('click',event=>{if(moved){event.preventDefault();moved=false;}},true);
    track.addEventListener('keydown',event=>{
      if(event.key==='ArrowRight' || event.key==='ArrowLeft'){
        event.preventDefault();const direction=event.key==='ArrowRight'?1:-1;
        const index=cards.findIndex(card=>card.contains(event.target));move(direction);
        if(index>=0){const card=cards[modulo(index+direction,cards.length)];(card.matches('a[href]')?card:card.querySelector('a[href]'))?.focus({preventScroll:true});}
      }
    });
    if('IntersectionObserver' in host){
      const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{
        entry.target.classList.toggle('is-in-view',entry.isIntersecting);
        if(entry.target===root)inView=entry.isIntersecting;
        else if(entry.isIntersecting)entry.target.classList.add('has-entered');
      }),{threshold:.05});observer.observe(root);cards.forEach(card=>observer.observe(card));
    }
    let resizeFrame;
    host.addEventListener('resize',()=>{cancelAnimationFrame(resizeFrame);resizeFrame=requestAnimationFrame(measure);});
    document.fonts?.ready.then(measure);
    root.addEventListener('decocoa-motion-change',()=>{if(looping===preference().reduced)measure();});
    const frame=time=>{
      const seconds=lastTime?Math.min((time-lastTime)/1000,.05):0;lastTime=time;
      if(looping){const {reduced}=preference(),before=state.phase;state.tick(seconds,{reduced,offscreen:!inView,hidden:document.hidden,hovered,focused,manual:drag!==null || interaction.active(time)});if(state.phase!==before)render();}
      requestAnimationFrame(frame);
    };
    requestAnimationFrame(frame);
  }
  const api={responsiveLayout,createInteractionPause,createState,mount};
  if(typeof module==='object' && module.exports)module.exports=api;
  else host.DeCocoaCategories=api;
})(typeof window==='undefined'?globalThis:window);
