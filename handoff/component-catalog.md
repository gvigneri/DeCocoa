# DeCocoa shared component catalog

This catalog describes the existing Python/static HTML build after the November 11 content and component revision. It uses the existing Montserrat typography, Primary Orange `#E87933`, Primary Brown `#3A170D`, Cream `#F7EFE6`, Ripe interactions, image treatments and responsive layout conventions. There is no additional framework, UI library or component-preview platform.

## Content and rendering ownership

`scripts/build_homepage.py` assembles the site. `prototype/site.template.html` owns the document shell; generated `index.html` files are outputs, not editing sources. Every render resolves site-relative routes and runtime asset references for both root-mounted local previews and the `/DeCocoa/` Pages export.

| Source | Responsibility |
|---|---|
| `prototype/site-content.json` | Retained content, page identities, product examples, source images, Food Safety, Sweet Careers, legal draft notices and shared defaults. |
| `prototype/approved-content.json` | Authoritative verbatim C01–C14 replacement blocks; the C07 taglines are stored separately within that collection. |
| `scripts/content_updates.py` | `apply_content(data)` maps the approved blocks into the existing content schema without modifying the retained source records. Shared focus, hero/tagline, category, business-segment and partner-introduction values are derived once. |
| `scripts/shared_components.py` | Small presentation primitives: `hero()`, `image()`, `paragraphs()`, `section_navigation()`, `family_timeline()` and `info_grid()`. |
| `prototype/navigation.json` | One navigation hierarchy, including main-page destinations, child destinations, active-route grouping and menu image configuration. |
| `prototype/logo-links.json` | Verified logo destinations and unresolved identity information, paired by existing mark identifiers. |
| `prototype/hero-bark.json` | Existing homepage bark assets, responsive variants, sizing and staggered entrance classes. |
| `prototype/chocolate-history.json` | The ten chocolate-history chapters and their layered artwork; independent of the Vigneri family timeline. |
| `handoff/content-component-brief-2026-11-11.md` | Archived source brief for provenance and source-to-rendered verification; not a runtime asset. |

Change approved copy in the authoritative source and keep its placement in `content_updates.py`. Do not place second versions in page templates or navigation. The `C01`–`C14` identifiers, source notes and deferred media notes are not visitor copy.

## Component catalog

All paths below are repository-relative; unqualified template/partial names are inside `prototype/`. Existing theme rules remain in `prototype/styles.css`. The new shared composition rules are in `assets/css/components.css`, and the image-menu rules are in `assets/css/navigation.css`.

| Component | Implementation and purpose | Inputs and variants | Actual use |
|---|---|---|---|
| Site shell | `site.template.html` and `render()` in `scripts/build_homepage.py`; document metadata, one main landmark and common resources. | Route, title, description, content, body classes, optional `noindex`. | Every generated public page. |
| Header/navigation | `partials/header.html`, `scripts/navigation_components.py`, `navigation.json`, shared `script.js`; both original and scroll header use the same hierarchy. | Main label/route, children, active routes, unique header prefix. Main labels are links; adjacent buttons control disclosures. | Every generated public page. |
| Image menu | `navigation_components.navigation()` and `.image-submenu` in `assets/css/navigation.css`. | Category thumbnails resolve existing category records; editorial menus use configured image, dimensions and existing labels. Category and editorial variants. | All four navigation groups in both headers. |
| Footer | `partials/footer.html` and `render()`; shared navigation, business/supporting destinations, legal links and existing badge treatment. | Primary navigation, service records, policy records. | Every generated public page, retaining Gifting, Craft Your Own, Fundraising and Wholesale. |
| Orange hero | `shared_components.hero()` and `partials/hero.html`; existing `.hero`, `.hero-layout`, `.hero-copy`, `.hero-art` foundation extended by `assets/css/components.css`. | `read`, label, heading, body paragraphs, optional rendered media/actions, and `home`. The `hero--bark` homepage and `hero--page` interior variants use the same template and orange token. | Homepage, editorial pages, six service pages, three product details, contact, three policy pages and recovery page. |
| Section container | `sections()` and `.container`/`.content-section`. | Stable `id`, title, aliases, paragraphs, optional blocks/items/bullets/steps/image/actions. | Editorial and service pages, including Roots, Values, Craft, Partner Brands and Décor. |
| Image-and-text layout | `shared_components.image()` within the shared hero/section layout, plus existing homepage split layouts; `.page-photo` and existing image variants. | Asset or image filename, dimensions, alt text, class and eager/lazy loading. Factory GIF handling includes a reduced-motion still. | All page heroes; homepage People, Craft and Experience sections; factory capabilities imagery. |
| Category block/card | `category_cards()`, `category_block()` and the category content collection; `.category-block` in `assets/css/components.css` extends the existing card treatment. | Heading, exact tagline, full description, source image, dimensions, alt, slug and destination. Homepage preview and full category variants; the capability variant uses H3 below its section H2. | Eleven homepage previews and eleven category blocks on `/products/`; four manufacturing blocks under Craft capabilities. |
| Card grid | `shared_components.info_grid()`, `cards()`, `service_cards()` and existing `.info-grid`, `.product-grid`, `.service-grid` and `.discovery-grid` variants. | Item title, text or paragraphs, optional image, route, icon and anchor. | Values and Principals, four business segments, related products and supporting pages. |
| Logo collection | `trust_section()`, `trust-section.template.html`, retained mark data and `logo-links.json`. | Section eyebrow/title/paragraphs; image, dimensions, alt, mark class and verified URL. Linked and unresolved-mark variants. | Homepage Our Partners and Our Certifications. Verified external links use `_blank` and `noopener noreferrer`. |
| Family timeline | `shared_components.family_timeline()` and `.family-timeline` in `assets/css/components.css`, composed by `sections()`. | Ordered records with `date`, literal `separator` and `text`; no automatic punctuation changes. | Five family milestones within `/our-people/#our-roots`. |
| Chocolate-history timeline | `chocolate_history()`, `chocolate-history-chapter.template.html`, `assets/css/chocolate-history.css`, `assets/js/chocolate-history.js`. | Existing date/region/title, caption, source link, artwork layers and placement values. | Ten chapters in `/experience-center/#museum-virtual-exhibition`; existing animations and responsive compositions retained. |
| Section navigation | `shared_components.section_navigation()` composed by `general()` and `.section-nav`; anchor offsets use existing shared header measurements. | Section `id`, visible title or optional `nav_title`. | Editorial and service pages; links target native section IDs and preserve aliases. |
| Buttons and links | `inquiry()`, `related_link()`, `link()`; existing `.button-primary`, `.button-secondary`, `.text-link`. | Label, route, inquiry topic, existing variant. | Every page; transparent Brown double borders remain on Orange, with existing hover/focus effects. |
| Inquiry | `partials/inquiry.html`, `inquiry_section()` and shared `script.js`. | Unique local anchor, stacked/home or contact layout, shared topics/product choices. | Exactly one instance on the homepage and one on `/lets-talk/`; local validation and unavailable-delivery behavior retained. |

## Section data contract

`general(page)` composes a hero, in-page navigation, sections and closing actions. A page supplies `route`, `title`, `eyebrow`, `heading`, `intro` (or `intro_paragraphs`), image metadata, `sections`, `topic`, `cta` and `cta_route`. A related action can use `related_route`/`related_label`.

Each section has `id` and `title`. Optional fields are:

- `nav_title`: concise in-page navigation label when the supplied display heading is longer.
- `aliases`: retained fragment IDs pointing to the same section.
- `paragraphs`: complete strings with their original punctuation.
- `blocks`: ordered subheadings and paragraph groups, each with `title` and `paragraphs`.
- `items`: card records with `title` and `text` or `paragraphs`, plus optional `id`, `route` and `icon`.
- `bullets`: semantic list strings; `ordered_steps`: records with `title` and `text`.
- `timeline`: ordered `date`, `separator`, `text` records for the family history.
- `image`, `width`, `height`, `alt`: existing section artwork.
- `capabilities`: retained manufacturing-method records using the existing category image/text schema.
- `topic`/`cta`, `related_route`/`related_label`, or `related_links`: shared inquiry and destination actions.

The four business segments are derived once as `DATA['business_segments']` with their full C13 paragraphs. The homepage Craft area and the dedicated Craft page consume that collection. `DATA['business_intro']` supplies the common C13 heading and introduction. The four manufacturing methods remain a distinct `DATA['capabilities']` collection; they are not consumer categories.

The HACCP artwork does not identify an issuing organization. Its logo record intentionally has no URL; the other eight verified organization/program marks are linked. Supply the actual issuer and verified official URL before adding a HACCP destination.

## Reusable page composition

Add a page record to the appropriate source collection so the existing build loop renders it; avoid editing generated HTML. For example, this development-only Python composition reuses the source of an existing service while demonstrating the required contract without adding another copy source:

```python
from copy import deepcopy

# Inside the existing build module, DATA is already resolved by apply_content().
source_page = next(page for page in DATA['services'] if page['route'] == 'decor/')
example = deepcopy(source_page)
example['route'] = 'example/'

# general() owns hero, section navigation, sections and closing actions.
# render() owns the document, headers, footer, route and asset resolution.
inventory.append(render(
    example['route'], example['title'], example['description'],
    general(example), 'interior service-landing section-nav-top',
))
```

This example is documentation only; `/example/` is not generated. For a real new page, define approved content and an existing image in the content source, add its record to `pages` or `services`, and add an entry in `navigation.json` only when the destination belongs in the primary menu. The footer already derives supporting destinations from the service records.

## Public page coverage and routing

The generated inventory is `prototype/generated-pages.json`. The content-page set contains 19 routes:

| Group | Routes |
|---|---|
| Main pages | `/`, `/products/`, `/our-people/`, `/our-craft/`, `/experience-center/` |
| Retained product details | `/products/filled-chocolate/`, `/products/chocolate-bar/`, `/products/chocolate-drizzle/` |
| Service/supporting pages | `/gifting/`, `/craft-your-own/`, `/fundraising/`, `/wholesale/`, `/b2b/`, `/decor/` |
| Contact | `/lets-talk/` |
| Utility | `/privacy-policy/`, `/terms-and-conditions/`, `/accessibility/`, `/404.html` |

Route strings in data omit the leading deployment base. `url()` emits relative destinations. Template tokens `{{url:our-craft/#our-segments}}` and `{{asset:images/chocolate-craft.webp}}` resolve for the current output route. Do not hard-code `/DeCocoa/` into content, and do not reintroduce `/prototype/` into public destinations.

`scripts/preview_server.py` serves only generated pages and referenced runtime assets at root-mounted URLs. `scripts/export_pages.py --base-path /DeCocoa/` packages those pages/resources, fixes recovery URLs for the project base and preserves legacy compatibility routes. Source briefs, original artwork, templates and handoff records remain outside the website artifact.

## Validation and preview

Run the existing build and checks from the repository root:

```powershell
python scripts/build_homepage.py
python scripts/check_content_components.py
python scripts/check_site.py
python scripts/check_preview.py
python scripts/export_pages.py --base-path /DeCocoa/
python scripts/check_pages_export.py --base-path /DeCocoa/
```

The current review server is [http://127.0.0.1:4174/](http://127.0.0.1:4174/). Use `Start-Preview.ps1 -Port 4174` to rebuild and start it when it is not already running. Hidden in-app browser checks cover desktop/mobile hero layouts, independent link/toggle behavior, keyboard/Escape handling, topic preselection and fragment visibility. `check_content_components.py` compares the independent archived brief against rendered text with presentation whitespace normalization only; its report is `reviews/content-components-2026-11-11/exact-copy-checks.json`. A successful static check is not a claim of whole-site accessibility conformance or independent certification of supplied business claims. Logo destination evidence is recorded separately in `handoff/logo-links-2026-11-11.md`.

The existing build remains the only component preview facility: review real public pages at their local routes. This revision does not add a separate storybook, publish a site or enable transmitting forms.

Latest image treatment (November 11): shared image surfaces use borderless frames with 16px container corners and 12px inner-image corners. The former card pseudo-element border is removed; standalone homepage photos and factory media use 16px corners. This supersedes the initial brief's image-border deferral.


## November 15 presentation additions

`prototype/homepage-content.json` owns homepage summaries, category introductions and short segment-card labels. `scripts/presentation_updates.py` adds the segment hub and individual Branded Chocolate/Fulfillment pages, and links all four segment landings to Our Chocolate categories. The same navigation model now has five groups. See [revision and verification](presentation-revision-2026-11-15.md).
