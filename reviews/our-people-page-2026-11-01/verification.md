# Our People page copy and jump navigation

November 1, 2026. Implementation checks for Guy's exact-copy revision. This is a local update; no publishing or independent review was performed.

## Delivered

The page uses one Our People h1 and the two supplied introduction paragraphs. OUR ROOTS contains the three supplied sentences as separate paragraphs. Our Principals contains VISION, FOCUS and MISSION in that order. Our Values contains the supplied introduction and all five titles/descriptions in the order Integrity, Inspire, Ingredients, Innovation, Invest. Wording, capitalization, punctuation and “cobble stoned” are preserved exactly against [the approved transcription](../../handoff/our-people-copy-2026-11-01.json).

The section jump links sit in a horizontal wrapping row below the intro and above the full-width sections, matching the Experience Center arrangement. Existing fragment IDs/aliases, photograph, Sweet Careers copy and all actions remain. The homepage's separately approved copy is untouched.

## Verification

- Rendered heading, introduction paragraphs, section titles, paragraphs and item titles/descriptions match the supplied JSON field for field at 1920, 1440, 768, 390 and 320px. [Browser evidence](browser-checks.json).
- All five widths have no horizontal document overflow, exactly one h1, native h2/h3 hierarchy, unique preserved aliases and a horizontal wrapping navigation row positioned above the section content.
- At 320px, selecting Our Values navigates to `#our-values` and focuses `our-values-title`. [Jump-link evidence](jump-link-check.json).
- Viewed screenshots: [introduction and navigation](introduction-desktop.jpg), [top navigation and Roots](roots-top-navigation-desktop.jpg), and [phone Values](values-phone-320.jpg).
- Build/static/deterministic checks pass. Other 17 generated pages match the previous export after accounting for the shared stylesheet query advancing from version 10 to 11. Experience Center markup and history assets are unchanged; Our People does not load history assets. [Source checks](../../prototype/qa-site-build/our-people-2026-11-01-checks.json).
- The `/DeCocoa/` export is refreshed with 18 pages and 72 runtime resources. The exported Our People page matches generated HTML; the comparison JSON stays out of the published artifact. No HTTP/motion suite was repeated for this copy/layout change.

Authoritative implementation: `prototype/site-content.json`, `scripts/build_homepage.py`, `prototype/styles.css` and the shared stylesheet version in `prototype/site.template.html`. Optional simple-heading, intro-paragraph and top-navigation settings preserve existing defaults for other pages.

The hidden QA tab is closed and viewport overrides reset at handoff. The normal local preview remains running on port 4174.
