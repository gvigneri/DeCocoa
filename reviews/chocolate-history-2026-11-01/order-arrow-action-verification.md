# Timeline order, subnavigation and actions

Subsequent marker revision: base `.history-item::before` top changes from 46px to 42px; the existing responsive override at 700px and below remains 34px. Timeline CSS advances to version 6 and the generated page/export are refreshed.

Subsequent direct spacing revision: `.history-metadata` now uses `.25rem` rather than 1rem, with date/region/title order retained. The 16px measurements below document the preceding version. Timeline CSS advances to version 5 and the generated page/export are refreshed.

November 1, 2026. Guy requested Primary Brown subnavigation, region between date and title, slim Font Awesome timeline arrows, and one Explore Our Craft primary action in How It's Made.

## Result

- Every chapter remains one native h3 with the original ID. Its spans now read date, region, title, with equal 1rem gaps.
- Header submenu and in-page section navigation anchors use Primary Brown #3A170D at rest. Their existing Ripe hover/focus color and animated 2px bottom line remain.
- Ten source links have the original [Font Awesome Free 6.7.2 arrow-right-long SVG](https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.7.2/svgs/solid/arrow-right-long.svg), rendered at .75em height with its natural proportions and current text color. This is a compact Free icon, not the separate Font Awesome Pro Thin family. The existing bundle's CC BY attribution/license and provenance record cover the new asset; the SVG geometry is unmodified. It is decorative (`aria-hidden="true"`, `focusable="false"`) and does not alter accessible link names or destinations.
- How It's Made keeps all four paragraphs and has exactly one link: Explore Our Craft, styled as a primary button and linking to `/our-craft/`. Explore Craft Your Own is removed only from this section. The timeline Craft Your Own Chocolate Bar invitation remains.

The related-link primary style is an explicit content property; other related links retain their default styling. Shared CSS is version 10; timeline CSS is version 4. JavaScript and chapter caption/art data are unchanged.

## Checks

- Hidden in-app browser at 1920, 1440, 768, 390 and 320px: all ten headings have the requested order and 16px/16px gaps; all ten decorative arrows fit their links and columns; no horizontal document overflow. The previous possible-heading paragraph heuristic still finds zero matches. [Measurements](order-arrow-action-browser.json).
- In-page navigation computes to Primary Brown at rest. The phone submenu opens with Brown links and collapsed lines; keyboard focus changes a link to Ripe #B83B28 and expands its single 2px line. Escape closes the disclosure and drawer. [Subnavigation states](brown-subnavigation-states.json).
- How It's Made contains one `button button-primary` anchor to `../our-craft/` at every tested width.
- Viewed [desktop order and arrows](timeline-region-middle-arrows-desktop.jpg), [How It's Made action](how-its-made-primary-action.jpg) and [wrapped phone source link with focus](timeline-arrow-wrapping-phone.jpg).

Build/static/deterministic checks and both export checks pass: 114 files and 1,682 references; 139 root-path and 140 `/DeCocoa/` HTTP cases, with no errors. The final local `_site` uses `/DeCocoa/`. [Source checks](../../prototype/qa-site-build/source-arrows-2026-11-01-checks.json) also confirm unchanged actions on the other 17 pages and unchanged chapter data. This is a local revision, with no deployment, push or independent design-review invocation. The hidden test tab is closed and temporary viewport sizing is reset for handoff; the normal port 4174 preview remains available.
