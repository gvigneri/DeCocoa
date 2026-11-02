/* Motion gate checks without browser automation. Visual checks are separate. */
const fs = require('fs');
const vm = require('vm');
const assert = require('assert/strict');
const path = require('path');
const source = fs.readFileSync(path.join(__dirname, '../assets/js/chocolate-history.js'), 'utf8');
function fixture({reduced = false, supported = true, throws = false, count = 1} = {}) {
  const classSets = Array.from({length: count}, () => new Set());
  const scenes = classSets.map(classes => ({classList: {add: value => classes.add(value), remove: value => classes.delete(value)}}));
  const classes = classSets[0];
  const state = {created: 0, observed: 0, unobserved: 0};
  const media = {matches: reduced, addEventListener: (_, callback) => state.change = callback};
  class Observer {
    constructor(callback, options) {
      if (throws) throw new Error('Observer unavailable');
      state.created++;
      state.enter = (index = 0) => callback([{target: scenes[index], isIntersecting: true}]);
      assert.equal(options.threshold, 0);
    }
    observe() { state.observed++; }
    unobserve() { state.unobserved++; }
    disconnect() { state.disconnected = true; }
  }
  const window = {matchMedia: () => media};
  if (supported) window.IntersectionObserver = Observer;
  const context = {window, IntersectionObserver: Observer, document: {querySelectorAll: selector => selector === '[data-history-scene]' ? scenes : scenes.filter((_, index) => classSets[index].has('is-history-entering'))}};
  vm.createContext(context);
  vm.runInContext(source, context);
  return {classes, classSets, state, media, window, context};
}
const normal = fixture();
assert(normal.classes.has('is-history-pending'));
normal.window.DeCocoaChocolateHistory.init();
vm.runInContext(source, normal.context);
assert.equal(normal.state.created, 1, 'Repeated initialization must share one observer');
assert.equal(normal.state.observed, 1, 'Each scene is observed only once');
normal.state.enter();
assert(!normal.classes.has('is-history-pending'));
assert(normal.classes.has('is-history-entering'));
assert.equal(normal.state.unobserved, 1, 'Entered scenes stop being observed');
normal.media.matches = true;
normal.state.change();
assert.equal(normal.classes.size, 0, 'Reduced motion finishes an active entrance immediately');
for (const options of [{reduced: true}, {supported: false}, {throws: true}]) {
  const gate = fixture(options);
  assert.equal(gate.classes.size, 0, 'Unsupported or disabled motion leaves all artwork visible');
}
const pending = fixture();
pending.media.matches = true;
pending.state.change();
assert.equal(pending.classes.size, 0, 'Changing motion preference reveals waiting artwork');
assert(pending.state.disconnected);
for (const count of [4, 10]) {
  const batch = fixture({count});
  assert.equal(batch.state.created, 1, 'All chapters share one observer');
  assert.equal(batch.state.observed, count);
  batch.state.enter(1);
  assert(batch.classSets[1].has('is-history-entering'));
  for (let index = 0; index < count; index++) {
    if (index !== 1) assert(batch.classSets[index].has('is-history-pending'), 'One entrance does not reveal or reset another chapter');
  }
  batch.window.DeCocoaChocolateHistory.init();
  assert.equal(batch.state.observed, count, 'Reinitialization does not duplicate chapter observers');
  for (let index = count - 1; index >= 0; index--) if (index !== 1) batch.state.enter(index);
  assert.equal(batch.state.unobserved, count);
  assert(batch.classSets.every(classes => classes.has('is-history-entering') && !classes.has('is-history-pending')));
  batch.media.matches = true;
  batch.state.change();
  assert(batch.classSets.every(classes => classes.size === 0));
}
const mixed = fixture({count: 10});
mixed.state.enter(2);
mixed.media.matches = true;
mixed.state.change();
assert(mixed.classSets.every(classes => classes.size === 0), 'A preference change reveals every waiting chapter and finishes the active chapter');
assert.equal(mixed.state.unobserved, 10);
console.log('Chocolate history: 4/10 independent once-only entrances, duplicate initialization, reduced motion and fail-open gates passed.');
