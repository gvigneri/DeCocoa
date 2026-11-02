/* Optional, once-only artwork entrances. HTML and artwork are visible by default. */
(() => {
  'use strict';
  if (window.DeCocoaChocolateHistory) {
    window.DeCocoaChocolateHistory.init();
    return;
  }
  const initialized = new WeakSet();
  const pending = new Set();
  const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let observer;
  const reveal = (scene, animate = false) => {
    pending.delete(scene);
    scene.classList.remove('is-history-pending');
    if (animate && !motion.matches) scene.classList.add('is-history-entering');
    else scene.classList.remove('is-history-entering');
    if (observer) observer.unobserve(scene);
  };
  const failOpen = () => {
    pending.forEach(scene => reveal(scene));
    if (observer) observer.disconnect();
    observer = undefined;
  };
  const init = () => {
    const scenes = [...document.querySelectorAll('[data-history-scene]')].filter(scene => !initialized.has(scene));
    if (!scenes.length) return;
    if (motion.matches || !('IntersectionObserver' in window)) {
      scenes.forEach(scene => initialized.add(scene));
      return;
    }
    try {
      if (!observer) observer = new IntersectionObserver(entries => {
        try {
          entries.forEach(entry => {
            if (entry.isIntersecting) reveal(entry.target, true);
          });
        } catch (_) { failOpen(); }
      }, {rootMargin: '0px 0px -6% 0px', threshold: 0});
      scenes.forEach(scene => {
        initialized.add(scene);
        pending.add(scene);
        observer.observe(scene);
        scene.classList.add('is-history-pending');
      });
    } catch (_) { failOpen(); }
  };
  if (motion.addEventListener) motion.addEventListener('change', () => {
    if (motion.matches) {
      failOpen();
      document.querySelectorAll('.is-history-entering').forEach(scene => scene.classList.remove('is-history-entering'));
    }
  });
  window.DeCocoaChocolateHistory = {init};
  init();
})();
