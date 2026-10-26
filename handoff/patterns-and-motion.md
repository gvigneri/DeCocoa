# Editable patterns and approved motion

## Current homepage revision, October 25, 2026

Our Craft uses a full-width Primary Brown surface and a static Orange Rings instance derived from `rings-master.svg`, with uniquely prefixed IDs. Cream text sits over solid Brown areas. Preserve the master unchanged. The hero remains Orange with a static Brown Stripes pattern; People and Experience retain their existing motion. Guy has removed visible motion controls; reduced-motion and offscreen/hidden-page gates remain. The older pause-control description below is historical and does not describe the current UI.

All six supplied AI pattern files have dedicated SVG master exports in `assets/patterns/`:

| Master | Original family |
| --- | --- |
| `circles-master.svg` | Circles |
| `floweroflife-master.svg` | Flower of Life |
| `growth-master.svg` | Growth |
| `luxury-master.svg` | Luxury |
| `rings-master.svg` | Rings |
| `stripes-master.svg` | Stripes |

These are outlined vector paths with original fills and explicit clipping paths, not bitmap images embedded in SVG wrappers. The AI sources are unchanged. `assets/vector-export-details.json` identifies each source, viewBox, paint count, clipping count and source colors. `scripts/export_vectors.py` reproduces the exports and rejects unsupported drawing/compositing commands rather than silently omitting them.

Keep these masters intact. For a static background, use the SVG as a CSS background image with cover sizing. For individually animated motifs, use an inline SVG instance so CSS and JavaScript can address its paths/groups. Prefix IDs and all references when inserting multiple copies to prevent clip-path collisions. Do not assume the full artboards are seamless repeat tiles.

Guy explicitly authorized slow row movement and changing pod colors in this revision. Animated website instances may use the established DeCocoa palette while the masters retain source colors. The full identity wordmark remains static on a quiet solid background. The exact source icon exterior may be used as a photographic mask, as recorded in `brand/brand-exceptions.md`.

The delivered website offers Pause motion, preserves only that preference, and respects reduced motion. Contact fields are never persisted. Each of the three hero pretzels has a separate finite eased falling entrance with a short stagger; all start above the hero and settle into place. Background movement stops when paused, outside the viewport, in a hidden document or when reduced motion is requested. Content and navigation remain usable with all motion stopped. Individual highlights use scattered independent phases and durations for a restrained, irregular appearance.

See `prototype/script.js` and `prototype/styles.css` for the final runtime implementation and `handoff/review-summary.md` for the motion states actually verified. Full source-art geometry and masks should be visually rechecked after any future optimization or SVG editor export, especially the underline below the e in the wordmark.
