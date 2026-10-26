# Homepage-r6 implementation self-check

October 11, 2026. This records focused coding/self-check coverage for the user's revision. It is not independent design acceptance. All five independent review slots were consumed before r6; the user has taken over design review.

## Changed behavior and assets

The hero now contains three distinct image nodes, each inside its own falling wrapper. Durations are **1.55, 1.65 and 1.7 seconds**, with **0, 0.2 and 0.4 second delays**. Easing is `cubic-bezier(.16,.78,.24,1)`. Each begins 1100px above its settled position, enters from above the hero and finishes with a subtle individual image tilt; the final entrance finishes after 2.1 seconds. There is no repeating product fall.

The red-drizzle and chunky-sprinkle cutouts are Imagegen-assisted reconstructions supplied by the coordinator, including restored small occluded edges. They are not pixel-identical original exports. Their retained PNG inputs measure **1230 × 1278**, as verified by Pillow and browser natural dimensions. Mechanical quality94 WebP copies preserve framing and exact alpha bytes, with alpha range0..255. Export records and PNG hashes are in `assets/r6-cutout-export-details.json`; generation prompts/provenance are in `handoff/pretzel-cutout-provenance.json`. The beaded pretzel is the unchanged source-derived `dipped-pretzel.webp`. Original artwork remains unchanged.

Eight shared cards cover the hero copy, three product visuals, People copy/photo, Craft photo and Experience copy. Computed styles show a transparent4px outer perimeter, radius16px, padding-box background clipping, and a visible4px contextual Cream/Orange inset ring. Image corners round inside those surfaces. The exact Experience icon mask is separate and unchanged. Eyebrows compute to8px radius; primary/secondary button inner borders compute to2px, retaining8/4px radii and outer2px borders.

## Actual browser checks

CUA Chrome was used against the retained local server. Saved screenshots were viewed. Browser viewport overrides and actual captured pixel dimensions differ because the screenshot surface excludes scrollbar/browser space; dimensions were read from the saved images rather than inferred from filenames.

| Requested viewport | Client / scroll width | Saved screenshot dimensions | Inspected view |
| --- | --- | --- | --- |
| 1920 × 1080 | 1905 / 1905px | 1905 × 1072px | Settled hero, product cards and People cards (`hero-1920.jpg`, `products-1920.jpg`, `people-1920.jpg`) |
| 1440 × 1000 | 1425 / 1425px | 1425 × 990px | Settled three-piece hero and card (`hero-1440.jpg`) |
| 768 × 1024 | 753 / 753px | 753 × 1004px | Tablet header/card, complete settled pretzels (`hero-768.jpg`) |
| 390 × 844 | 375 / 375px | 375 × 812px | Hero top and scrolled complete settled artwork (`hero-390.jpg`, `pretzels-390.jpg`) |
| 320 × 900 | 305 / 305px | 305 × 858px | Hero card, full artwork and first product card (`hero-320.jpg`, `pretzels-320.jpg`, `products-320.jpg`) |

All files are in `prototype/qa-r6/`, with machine-readable sizes in `dimensions.json`. No horizontal overflow was observed at any required width. Body and all nine button instances retain16px computed type at320px; main navigation remains20px. Full outer pretzel edges are visible in the settled mobile views. No screenshot needs replacement after these checks; later changes were documentation/static check updates only.

Runtime motion checks captured distinct in-flight positions: the first had moved to approximately -953px while the next two remained at -1100px during their delays. This confirms separate staggered entry rather than a group transform. A later mid-entry pause held three different translate values **0.881px, 4.762px and -10.229px** unchanged across400ms, all with computed `animation-play-state:paused`. Resume continued to settled translate0/opacity1 rather than restarting. Reloading with the saved pause flag produced `entrance-static`, animation:none and opacity1 on all three pieces. Motion was left resumed at the end.

An earlier ordinary reload retained an old script during testing. Versioned local references `styles.css?v=6` and `script.js?v=6` ensure the updated behavior loads; they still refer to the same portable files. Actual pause checks above used the current versioned script.

Reduced-motion CSS/JS paths, hidden/offscreen handling, menu focus logic, footer identity and local-only contact behavior retain preceding coverage and were source-checked here. OS reduced-motion and background-tab behavior were not newly emulated. No broad unchanged form regression or new independent design review was performed. There are zero native forms/submits and no transport code; only the non-sensitive motion preference flag is stored.

Build/source checks pass (`build_homepage.py`, `check_homepage.py`, Node `--check prototype/script.js`). Current implementation hashes are in `source-checks.json`. Temporary QA tab158815762 was closed, viewport reset, and retained user preview tab158815740 was refreshed to r6 and kept open. Browser ownership is released.
