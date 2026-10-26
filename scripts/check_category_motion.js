/* Exercise the actual row state used by the DOM controller, without a browser. */
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const {responsiveLayout,createInteractionPause,createState}=require('../assets/js/category-motion.js');
const results=[];
for(const [view,columns] of [[1881,4],[1401,4],[729,2],[351,1],[281,1]]){
  const {width,pitch}=responsiveLayout(view,columns);
  assert.equal(width*columns+24*(columns-1),view,'equal responsive cards and gutters fill the track inner width');
  const state=createState({count:5,pitch,width,view,speed:15});
  assert.equal(state.position(0),0,'Wellness begins at the left edge');
  const x=state.position(0);state.tick(1);
  assert.equal(state.position(0)-x,15,'actual visual motion is rightward at 15 px/s');
  for(const gate of ['reduced','offscreen','hidden','hovered','focused','manual']){
    const before=state.phase;state.tick(2,{[gate]:true});assert.equal(state.phase,before,gate+' prevents movement');
  }
  for(let step=0;step<1000;step++){
    const previous=Array.from({length:5},(_,index)=>state.position(index));
    state.tick(.1);
    const positions=Array.from({length:5},(_,index)=>state.position(index));
    assert.equal(new Set(positions).size,5,'one distinct position per real card');
    const sorted=positions.slice().sort((a,b)=>a-b);
    for(let i=1;i<sorted.length;i++)assert.ok(Math.abs((sorted[i]-sorted[i-1])-pitch)<.00001,'cards retain pitch and do not overlap');
    positions.forEach((position,index)=>{
      if(position<previous[index])assert.ok(previous[index]>view && position+width<0,'wrapping happens only beyond both visible edges');
    });
  }
  for(let index=0;index<5;index++){
    state.reveal(index);const position=state.position(index);
    assert.ok(position>=-.00001 && position+width<=view+.00001,'each focused card can be fully revealed while paused');
  }
  const before=state.phase;state.move(1);state.move(-1);
  assert.ok(Math.abs(state.phase-before)<.00001,'manual previous/next preserve a stable cycle');
  const interaction=createInteractionPause();
  interaction.pause(100);
  const stopped=state.phase;state.tick(1,{manual:interaction.active(200)});
  assert.equal(state.phase,stopped,'manual interaction temporarily stops motion');
  state.tick(1,{manual:interaction.active(3100)});
  assert.notEqual(state.phase,stopped,'manual pause expires without a Resume control');
  interaction.pause(4000);interaction.pause(6000);
  assert.equal(interaction.active(8999),true,'later interactions extend the pause');
  assert.equal(interaction.active(9000),false,'extended pause still expires');
  results.push({inner_view_width:view,columns,card_width:width,rightward_pixels_per_second:15,pause_gates:6,manual_pause_expires:true,focusable_cards_revealed:5,wrapping_steps:1000});
}
const output={scope:'Production motion-state logic only; DOM, swipe, CSS entrances and visual geometry require coordinator browser checks.',results,errors:[]};
fs.writeFileSync(path.join(__dirname,'../prototype/qa-site-build/category-motion-checks.json'),JSON.stringify(output,null,2)+'\n');
console.log(JSON.stringify(output,null,2));
