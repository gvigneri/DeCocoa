# Timeline and shared-link refinement

November 1, 2026. Implementation checks for Guy's direct revision; no independent design review or publication.

## Requested result

- All ten chapter headings read date, title, then region, with one equal metadata gap.
- The complete Museum & Virtual Exhibition introduction is centered at desktop, tablet and phone widths.
- Ordinary text anchors use Ripe without a permanent underline. Their 2px bottom line grows from the left on hover and keyboard focus; reduced motion remains supported. On Brown, the existing lighter Ripe token preserves ordinary-text contrast. Buttons, brand artwork and whole-card links retain their component treatment.
- Main editorial section separators are removed. Deliberate button, field and footer borders remain.
- One Tours and Classes section follows the timeline and its Craft Your Own invitation. It combines the former museum context with the tours/classes introduction and retains one specific Experience Center inquiry action. The redundant body Let's Talk button is removed; shared header/footer contact links remain.

## Editing sources

`prototype/chocolate-history-chapter.template.html`, `assets/css/chocolate-history.css`, `prototype/styles.css`, `prototype/site-content.json` and `scripts/build_homepage.py`. The chapter data, artwork manifest and scripts are compared against `preservation-before.json`.

## Validation

- Hidden in-app browser checks at 1920, 1440, 768, 390 and 320px: all ten metadata groups have 16px/16px gaps in date/title/region order, the museum eyebrow and introduction have identical horizontal centers, and there is no document horizontal overflow. See [responsive measurements](responsive-checks.json).
- At 200% root text size, 1440px and 320px retain equal 32px/32px gaps, centered introduction and contained document width. This used the existing QA-only response fixture, not a production change. See [large-text measurements](large-text-checks.json).
- Ordinary links show no underline or border at rest. Source, section-navigation and submenu links compute to #B83B28; footer and homepage Craft links use #E05F49 on #3A170D. The existing contextual colors provide 4.99:1 on Cream and 4.51:1 on Primary Brown. Keyboard focus visibly grows the 2px line from the left: measured scale 0.519 during transition, then 1. Hover uses the same CSS target state; reduced-motion media/class branches disable the transition. Direct hover and OS reduced-motion emulation were not driven in this browser check. See [rest states](link-rest-checks.json), [focus states](source-focus-check.json), [phone submenu links](phone-menu-links.json) and [homepage components](home-link-checks.json).
- Skip to content remains fixed with Cream backing, offscreen at rest and visible on keyboard focus. The phone drawer opens; Experience Center disclosure opens and Escape collapses it with focus returned. Buttons, logos and whole-card links do not acquire the ordinary-anchor line.
- All Experience main-section top and bottom borders compute to zero. The former history-context block is gone. Tours and Classes contains the combined two paragraphs and exactly one Ask About the Experience Center action; there is no body Let's Talk action. Header/footer contact links remain. The other 17 pages' main CTAs are unchanged, as recorded in [source checks](../../prototype/qa-site-build/link-refinement-2026-11-01-checks.json).
- Chapter data (captions, source URLs and placement), artwork manifest, timeline JavaScript and shared JavaScript hashes are unchanged. See [preservation comparison](preservation-checks.json).
- Build/static/deterministic checks pass. The coding owner also ran the existing 4/10 chapter motion checks, root preview HTTP checks and root/subpath export checks: 18 pages, 72 runtime resources, 114 export files, 1,683 references, 139 root and 140 `/DeCocoa/` HTTP cases, no errors. Final local `_site` export uses `/DeCocoa/`; no push or deployment was performed.

## Screenshots viewed

- [Desktop museum introduction and first chapter](museum-desktop-1440.jpg)
- [320px museum introduction](museum-phone-320.jpg)
- [Phone source link with keyboard focus line](source-focus-phone.jpg)
- [Combined Tours and Classes ending](tours-ending-desktop.jpg)
- [Homepage Craft links on Brown](home-craft-links.jpg)

The ordinary preview remains at port 4174 as previously requested. The QA-only fixture on port 4175 is stopped after checking; browser viewport overrides are reset and the hidden QA tab is closed. Earlier October 31 evidence remains historical.
