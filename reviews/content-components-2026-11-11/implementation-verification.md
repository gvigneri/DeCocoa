# Content and component implementation — November 11, 2026

Implemented the supplied brief in the existing Python/static repository. The revision remains local and uncommitted; no GitHub push, Pages deployment, WordPress connection, form transmission or booking backend was performed.

Preview: <http://127.0.0.1:4174/>. The separate export preview is <http://127.0.0.1:4180/DeCocoa/>.

## Baseline and theme

The working tree was clean at baseline commit `62c394a21d317d504328b31144dc2f7cd5cc7cb6`. Before source changes, the hidden in-app browser was used to inspect the homepage at desktop 1440px and phone 390px, plus the existing People page at 390px. Baseline screenshots were captured in the review chat. Existing repository screenshot records remain unchanged.

The current homepage Orange token (`#E87933`), Brown/Cream colors, fonts, heading scale, double-border buttons, hover shadows, photographs, logo artwork, bark composition and motion are retained. A common `.hero--orange` rule now supplies the existing transparent hero copy/button treatment to both the homepage and interior hero variants. No global border, cursor, font or button redesign was introduced.

## Delivered scope

- All 19 content routes, including the recovery page and three pending policy pages, render through the same Orange hero partial. The 21 legacy redirect documents remain redirects.
- All 11 supplied consumer categories appear on `/products/` in source order, with their full headings, taglines and descriptions. Home previews use the exact headings and taglines. Manufacturing methods and their imagery now appear under `/our-craft/#process-capabilities`; old product-page hashes forward to the corresponding Craft blocks, with real links available without JavaScript.
- Main navigation labels are links. Independent toggles control themed image menus with shared desktop, keyboard and mobile behavior. Partner Brands, Décor and Wholesale belong to Our Craft; Craft Your Own is available under Experience Center. Supporting routes remain accessible.
- Our People includes the complete roots story, separate five-entry family timeline and revised values. Experience retains the ten illustrated chocolate-history chapters and seven process steps, with the supplied museum copy relocated to the museum section.
- The four full business segments appear within homepage Craft and the Craft page. `/b2b/` now contains Partner Brands, and `/decor/` is the only new content route.
- Eight verified partner/certification logos are external links with accessible names, `target="_blank"`, and `rel="noopener noreferrer"`. HACCP remains visible without a fabricated destination.

## Changed source files and component reuse

| Files | Responsibility |
|---|---|
| `prototype/approved-content.json`, `scripts/content_updates.py` | Authoritative verbatim C01–C14 blocks and mappings onto retained content; shared source values for repeated introductions, statements and segments |
| `prototype/navigation.json`, `scripts/navigation_components.py` | One menu model and renderer for both headers and main footer links; category imagery reused from category data |
| `prototype/logo-links.json` | Verified logo/destination pairs and the explicit missing HACCP destination |
| `prototype/partials/hero.html`, `scripts/shared_components.py` | Reusable hero, image, paragraph, section navigation, information grid and family-timeline primitives |
| `scripts/build_homepage.py` | Shared page composition, category blocks/cards, sections, logo collections and portable relative URLs |
| `prototype/homepage.template.html`, `product-detail.template.html`, `trust-section.template.html`, `site.template.html` | Shared template integration and homepage content placement |
| `prototype/styles.css`, `assets/css/components.css`, `assets/css/navigation.css` | Existing theme reused with scoped page/menu layouts and responsive behavior |
| `prototype/script.js` | Existing interaction module extended for separate links/toggles, capability redirects and legacy inquiry-topic aliases |
| `scripts/check_content_components.py`, `check_site.py`, `check_navigation.js`, `check_category_motion.js`, `check_pages_export.py` | Current acceptance and regression checks, including updated fixtures for approved scope |
| `.github/workflows/pages.yml` | Existing Pages workflow now also runs content, navigation and category checks; no publication triggered |
| `README.md`, `handoff/component-catalog.md` | Current source ownership, 19-route inventory, component inputs/variants/usage and a reusable page-composition example |
| Generated HTML and `prototype/generated-pages.json` | Rebuilt 19-page output and updated source inventory |

## Validation

| Check | Result |
|---|---|
| Build | 19 pages generated; deterministic rebuild passed |
| Exact source comparison | 643 checks passed; only presentation whitespace normalized, punctuation/capitalization retained |
| Static site integrity | 2,838 local references; one H1/main/footer per page; 57 protected source files unchanged; shared header/footer/inquiry propagation passed |
| Root HTTP preview | 19 pages and 79 runtime assets served correctly; source directories excluded; legacy redirects and nested recovery passed; POST remains rejected |
| Pages export | 123 artifact files, 3,305 references and 150 loopback HTTP cases passed under `/DeCocoa/`; 21 compatibility and 24 legacy-context cases passed |
| Runtime harnesses | Navigation, 11-category motion and ten-chapter history checks passed, including reduced-motion and initialization behavior |
| Browser layout | 76 route/viewport combinations: all 19 pages at 320, 390, 768 and 1440px. No horizontal overflow, one H1, and the exact Orange hero token in every case. Desktop copy is left of media. Additional 1920px homepage check passed. |
| Browser interaction | Desktop menu toggle, Escape and focus return; parent-link navigation; mobile Menu and Craft accordion; Partner Brands navigation; local field validation/unavailable-delivery result; old B2B topic mapping; root and Pages capability redirects; nested Pages 404 verified |
| Anchor positioning | Settled relocated capability target was 122px below the viewport top with a 104px sticky header, and focus on its semantic heading |
| Homepage phone composition | Art ends at 497px, copy begins at 513px in the reviewed 390px viewport; no overlap |
| Whitespace | `git -c core.whitespace=cr-at-eol diff --check` passed, respecting the repository's preserved Windows line endings |

Browser checks used only hidden in-app tabs. The temporary viewport override was reset. Desktop hover and reduced-motion state logic were exercised in the runtime harness; browser pointer toggles, keyboard behavior and phone layout were also checked. These scoped checks are not a claim of comprehensive accessibility conformance.

Evidence: [layout matrix](browser-layout-matrix.json), [exact-copy results](exact-copy-checks.json), [static checks](static-verification.md), and the PNG views in this directory. The supplied brief is archived at `handoff/content-component-brief-2026-11-11.md`; [component catalog](../../handoff/component-catalog.md) contains the page-composition example.

## Specific remaining item

The HACCP artwork is a generic badge and neither the image nor existing project provenance identifies its issuing organization. The other eight official destinations are verified. An issuer name or official destination is needed to make this ninth logo a correct link. Details and source evidence: [logo destinations](../../handoff/logo-links-2026-11-11.md).

## Image-border follow-up

Guy's subsequent request removes all image-frame borders and retains rounded corners. Updated the shared card style and rounded standalone homepage media; rebuilt all 19 pages and refreshed the local export. Hidden-browser inspection found zero image/frame borders and retained rounded card corners across all 19 routes. The 390px check has no horizontal overflow. Existing static site checks pass. Evidence: image-border-checks.json, borderless-images-desktop.png and borderless-images-phone.png. No publication performed.
