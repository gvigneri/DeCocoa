# November 15 local presentation revision

Implemented Guy's current chat request in the existing local site. The supplied `C:/Users/guyta/Desktop/DeCocoa-2.png` is the layout reference for the four business segment columns, not a replacement source of segment copy.

## Result and source ownership

- Public HTML has no em dashes; archived supplied copy remains intact. The renderer converts spaced heading separators to colons and sentence interruptions to commas.
- Default body text is 24px at 1200px and wider; mobile/tablet retains 16px.
- Both headers have five groups. Our Segments follows Our Chocolate and links to `/our-segments/`. Its four landings are `/branded-chocolate/`, `/b2b/`, `/decor/` and `/fulfillment/`. Each links to three relevant Our Chocolate categories. Former Craft segment fragments forward to their new destinations, with a hub link as the no-script fallback.
- Full-row Orange navigation underlines persist while menus are open. Submenu links have rounded 10% Primary Orange hover/focus backgrounds without animated lines. The scrolling header uses Cream to keep Orange states visible.
- People, Craft and Experience menus have square generated photographs in a one-third-width column aligned with the submenu height, without captions. The 640px WebP assets total 254,726 bytes. Original PNGs and hashes are preserved in `brand/source/menu-images-2026-11-15/` and `assets/menu-image-provenance-2026-11-15.json`. These are illustrative placeholders, not photographs of the actual company.
- Homepage hero reads “Crafted. To delight.” Category cards center larger headings, Orange taglines, new one-sentence introductions and Orange actions. People and Craft have White backgrounds and distinct, shorter introductions.
- A separate Cream business section has four desktop columns, icons, headings, Orange subheadings, short rules and copy, and whole-card links; two columns on tablet and one on phones.
- Shadows use soft 12% black. Buttons change both concentric borders and label color on hover/focus. Partner/certification links use 10% Orange backgrounds without animated lines. Footer links are Primary Orange and headings are White.

`prototype/homepage-content.json` owns the new editorial summaries. `scripts/presentation_updates.py` adds the segment pages to retained content. `prototype/navigation.json` owns both menus. Existing shared renderers and CSS implement the presentation.

## Verification

- Build: 22 public pages.
- Static checks: 3,335 local references, 57 protected artwork records, deterministic rebuild and shared partial propagation, no errors.
- Retained content: 721 checks allowing the requested em dash removal and segment relocation, no errors.
- Navigation and category-motion state tests pass, including keyboard/Escape, phone inert closure and reduced motion.
- HTTP checks pass for all public pages/assets, recovery and legacy routes; source material remains unserved.
- Local `/DeCocoa/` export: 132 artifact files, 3,817 references and 162 loopback HTTP cases, no errors. This revision has not been published.
- Hidden in-app browser: homepage at 320, 390, 768, 1200, 1280 and 1600px, no document overflow. Desktop body 24px, phone/tablet 16px; four/two/one segment columns.
- Browser checks: phone segment menu and Fulfillment page; Branded Chocolate and segment hub product connections; old Craft Fulfillment redirect; square 272×272px People/Craft menu images; Orange parent state and full-row underline; rounded submenu focus background; certification focus background; footer colors.

Preview remains at http://127.0.0.1:4174/. Forms and bookings retain their existing non-transmitting behavior.

## Follow-up: menu width, shadows and button motion

Guy requested slightly darker shadows, stationary primary/secondary buttons, full-container and equal-height desktop submenus, an Our Segments supporting image, and a scrolling-header shadow. Shared `--soft-shadow` is now 18% black. Button transitions include shadow/color/border only. Desktop menu dimensions use the header content container and the original header's viewport clearance so both header variants agree; feature images remain square and full-height. Phone/tablet accordion panels keep natural content height. Our Segments now has a fourth generated placeholder, preserved with the other originals and provenance records.

Rebuilt all 22 pages. Static checks pass for 3,423 local references and protected artwork; navigation state tests pass. At 1600px, all five original-header menus measure 1,372 × 485px, matching the content-container width. The four supporting images measure 429 × 429px. Browser checks confirm 18% black menu/header shadows and no button transform or transform transition. Screenshot: `reviews/presentation-2026-11-15/full-width-segment-menu.jpg`.

Follow-up browser verification also confirms all five scrolling-header menus at the same 1,372 × 485px. At 1200 × 700px, the full-width category menu is 1,084 × 389px and stays within the viewport. The 390px phone drawer retains its natural-height four-link segment submenu without horizontal overflow.

## Follow-up: button variants, Ripe accents and segment grid

Secondary buttons now have Cream borders/text, changing both borders to Primary Brown on hover/focus while retaining Cream text. Primary buttons retain Orange borders/Brown text at rest and change to Brown borders/Orange text on hover/focus. Meet Our People and Explore Our Craft share the primary class and presentation. The light scrolling-header contact also uses primary so its text remains visible on Cream. No button movement was reintroduced.

Removed the 300 font-weight declaration from hero paragraphs, which inherit the normal 400 body weight. Homepage People/Craft eyebrows, segment kickers, category taglines and category actions use Ripe. Certifications have a White background. Homepage Experience uses Cream and a separate one-paragraph summary from homepage-content.json; the dedicated page retains the supplied wording.

Business Segments has the “From craft to customer” eyebrow, a two-column/two-row desktop and tablet layout, equal-height rows, and one continuous vertical and horizontal divider forming a plus. There is no perimeter border. Phones retain a single column with horizontal separators.

Rebuilt all 22 pages. Static checks pass for 3,423 references and 57 protected artwork records. Retained-copy checks pass (718 checks, with the homepage Experience summary now intentionally separate). Hidden-browser checks confirm all requested surface/text colors, normal hero paragraph weight, matching primary CTAs, both concentric button borders and text colors on keyboard focus, no button transforms, and centered grid-divider geometry.

Responsive checks confirm two columns at 768px and one column with separators at 390px, with no horizontal overflow. The desktop grid screenshot is saved at `reviews/presentation-2026-11-15/segments-two-by-two.jpg`. Temporary browser viewport overrides were reset after verification.

## Follow-up: heading and redundant-link alerts

Category taglines, segment labels and product example captions now belong to their existing semantic headings, preserving layout and copy. Supporting menu photos are decorative, removing their duplicate destination links. Redundant drawer contact links are removed; header contact actions remain. All 22 pages were rebuilt and checked. The supplied heading heuristic decreased from 45 to 10 matches; the ten retained matches are genuine body paragraphs, documented with the verification evidence in `reviews/presentation-2026-11-15/heading-link-verification.md`. Static, retained-copy and navigation checks pass. Preview remains local.

## Follow-up: secondary text and inquiry surface

Secondary buttons use Primary Brown text at rest and pure White on hover/keyboard focus, retaining Cream resting borders, Brown interaction borders and the stationary soft-shadow treatment. Let's Talk is interpreted as the inquiry section: the shared inquiry partial now has a full-width White surface on both the homepage and dedicated page. Header buttons retain their prior background treatment.

All 22 pages were rebuilt and static checks pass. Browser checks confirm Brown resting text, White focus text, Brown focus borders, no button movement, and White inquiry surfaces matching the available page width on desktop and phone with one form instance and no horizontal overflow. Screenshots: `secondary-white-focus.jpg` and `lets-talk-white.jpg` in `reviews/presentation-2026-11-15/`.

## Follow-up: Our Chocolate card tiles

Our Chocolate now displays its eleven existing categories as three equal card tiles per desktop row, two per tablet row and one per phone row. Each tile retains its image, combined h2 and tagline, full supplied description, category fragment and inquiry action. Removed the jump navigation, A closer look at chocolate section, and Find your chocolate starting point section from this page. Legacy manufacturing-fragment redirects remain, with fallback links shown only when directly targeted. Other product/service pages and the homepage carousel are unchanged.

All 22 pages were rebuilt. Static checks pass for 3,178 references and 57 protected artwork records; all 718 retained-copy checks pass. Hidden-browser checks confirm 3 columns at 1600px, 2 at 768px and 1 at 390px, all eleven tiles, no removed-section markup and no horizontal overflow. The first desktop row has matching 436px widths and 714px heights. Evidence: `chocolate-tiles-checks.json` and `chocolate-three-column-tiles.jpg` in `reviews/presentation-2026-11-15/`.

## Follow-up: three chocolate collections

Our Chocolate now contains three cards: Snacking, Gifting and Entertaining. Each links to its dedicated root-level page, preserving the existing `/gifting/` route and adding `/snacking/` and `/entertaining/`. Each collection page has the same eight requested formats in order: Tablet, Filled, Covered, Dipped, Novelty, Drink, Wellness and Assortment. Supplied heading, tagline and descriptive copy remains authoritative. The shared grid remains transparent on Cream, with three desktop columns, two tablet columns and one phone column. Collection inquiry actions preselect the relevant collection in the existing non-transmitting form.

Both Our Chocolate submenus now contain exactly the three collection links and one decorative square photo, matching other menu dimensions and interactions. The built-in image_gen tool created the supporting editorial chocolate still life. Original: `brand/source/menu-images-2026-11-15/menu-chocolate-2026-11-15.png`; runtime: `assets/images/menu-chocolate-2026-11-15.webp` (640px square, 112,140 bytes). The complete prompt, generator and hashes are recorded in `assets/menu-image-provenance-2026-11-15.json`. It is an illustrative placeholder, not an actual product photograph.

Homepage carousel wording and behavior remain, with direct links updated to the new collection destinations. Business format links use the Snacking catalogue, which contains all eight formats. Older `/products/#tablet` and equivalent format links forward there; old manufacturing links still forward to Our Craft. Historic Gifting fragment IDs remain useful. The footer includes the three collections without a duplicate Gifting entry.

Verification: 24 generated pages; 2,662 static references and 57 protected artwork checks pass; all 649 retained-copy checks pass. Navigation and carousel state tests pass. Loopback HTTP checks confirm all 24 pages and 84 runtime resources, including the new image, with source isolation and legacy-route handling intact. The initial sandboxed HTTP test could not open its loopback connection; the approved unsandboxed rerun passed. The preview was restarted to serve the new inventory and remains on port 4174.

Browser verification at 1600px: three root collection cards and eight formats on each collection page, transparent surfaces, active Our Chocolate navigation, working Snacking inquiry preselection, and `/products/#tablet` forwarding to `/snacking/#tablet`. Original and scrolling menus both measure 1,372 × 485px with a 429px square supporting image and exactly three links. Phone checks at 390px verify the three-link accordion, working Entertaining navigation, single-column cards and no horizontal overflow on all four pages. Screenshots and measurements: `chocolate-collections-menu.jpg`, `chocolate-three-collections.jpg` and `chocolate-collections-checks.json` in `reviews/presentation-2026-11-15/`.

## Follow-up: eight unlinked homepage cards

The homepage Our Chocolate carousel now contains only Tablet, Filled, Covered, Dipped, Novelty, Drink, Wellness and Assortment. Snacking, Gifting and Entertaining were removed from this homepage block. Each format is a semantic article with its existing image, combined heading/tagline and short introduction. Card links, Explore action labels, hover lift and hover shadows are removed. The section-level Explore Our Products button remains. Navigation and collection pages retain their three-collection structure.

The carousel has one keyboard focus stop with an accessible left/right arrow instruction. Existing automatic motion, dragging, focus pause and reduced-motion behavior remain. Browser verification confirms that Tab moves from Explore Our Products to the carousel, ArrowRight moves the cards, and the next Tab reaches Meet Our People without stopping on card content.

Verification: rebuilt 24 pages; static checks pass for 2,648 references and 57 protected artwork records; all 643 retained-copy checks pass; eight-card carousel state tests pass. Hidden-browser checks at 1600px and 390px confirm eight articles, zero card links/actions and no document horizontal overflow. Temporary viewport overrides were reset. Screenshot: `reviews/presentation-2026-11-15/home-eight-format-cards.jpg`. Local preview remains available on port 4174.

## Follow-up: segment-page cards and deferred PDFs

Removed Explore chocolate formats and the existing closing CTA groups from all four segment pages. Branded Chocolate now ends with Snacking, Gifting and Entertaining tiles, using the collection images, supplied copy and links to the dedicated pages. Partner Brands ends with the eight format tiles in the requested order, without links or inquiry actions. Both use the shared transparent category grid: three columns on desktop, two on tablet and one on phones.

Décor and Fulfillment each end with one native disabled primary button, labeled View Décor PDF and View Fulfillment PDF, with the associated text “PDF coming soon.” No empty or fabricated link is rendered. When Guy supplies a document, set that page's `pdf_action.asset` in `scripts/presentation_updates.py` to its real runtime asset path; the renderer then emits an ordinary primary link and removes the pending status. Existing page introductions and editorial copy remain intact.

Verification: rebuilt 24 pages; 2,634 static references, 57 protected artwork checks, shared partial propagation and deterministic rebuild pass. All 643 retained-copy checks pass. Hidden-browser checks confirm three collection cards, eight informational format cards, no old section or closing actions, and exactly one disabled PDF button on each relevant page. All four pages have no horizontal overflow at 390px; desktop cards have three 436px columns and tablet cards have two columns. Viewport overrides were reset. Evidence in `reviews/presentation-2026-11-15/`: `branded-chocolate-collections.jpg`, `partner-brands-formats.jpg`, `decor-pdf-placeholder.jpg` and `segment-revision-phone-checks.json`. Preview remains local on port 4174.

## Follow-up: navigation order

Moved Our Segments immediately after Our Craft in `prototype/navigation.json`. The shared order is now Our Chocolate, Our People, Our Craft, Our Segments, Experience Center. Both headers, responsive menus and the shared footer Explore list use this source. Rebuilt all 24 pages; static checks pass for 2,634 references, shared partial propagation and deterministic rebuild. Hidden-browser verification confirms the new order in both original and scrolling navigation. Screenshot: `reviews/presentation-2026-11-15/navigation-segments-after-craft.jpg`.

## Follow-up: remove current-page navigation styles

Removed the persistent bold weight and underline selectors for `.is-current` and `aria-current` navigation items. Semantic current-page metadata remains. Hover, expanded-menu and keyboard-focus rules remain independent and unchanged. Both navigation stylesheets have updated cache versions.

Rebuilt 24 pages; static checks, 2,634 local references and deterministic rebuild pass. Hidden-browser verification on Our Craft confirms normal 400 text weight, Primary Brown text and a collapsed underline in both headers while `aria-current="page"` remains. Keyboard focus still activates the Orange text and row underline transition. Screenshot: `reviews/presentation-2026-11-15/navigation-without-current-style.jpg`.

## Follow-up: remove section jumps and breadcrumbs sitewide

Removed the shared section navigation renderer and its calls, collection breadcrumbs, and the product-detail breadcrumb template. Removed obsolete navigation CSS and changed the editorial layout to a single full-container content column, including pages that previously reserved a sidebar. Section IDs, legacy fragment forwarding, main/submenu navigation, skip-to-content and Back to top remain intact.

All 24 generated pages were scanned: no section-jump navigation or breadcrumb markup remains. Static checks pass for 2,594 references, protected artwork, shared partial propagation and deterministic rebuild; all 643 retained-copy checks pass. Hidden-browser checks confirm Our Craft proceeds from hero to Promise, collections and product details start with their hero, and Wholesale no longer reserves a sidebar. Representative desktop and 390px phone layouts have no horizontal overflow. Screenshot: `reviews/presentation-2026-11-15/our-craft-without-jump-navigation.jpg`. Viewport overrides were reset and preview remains local on port 4174.

## Follow-up: Our People hero, story headings and closing actions

The dedicated Our People hero now reads “Our Chocolate Crafters” with no eyebrow. The Journey to America, The Birth of DeCocoa and Today retain their semantic h3 elements and use 700 weight. Today has no trailing comma. The two final Explore Our Craft and Let's Talk actions are removed; the specific Sweet Careers action remains. The homepage People display heading retains “Your Chocolate Crafters” from its own heading source.

Rebuilt all 24 pages; static checks pass for 2,592 references, shared partial propagation and deterministic rebuild. All 643 retained-copy checks pass with the two requested text changes explicitly accounted for. Hidden-browser checks confirm the exact hero, no eyebrow, all three 700-weight story headings, no closing CTA group, and no horizontal overflow at 1600px or 390px. Screenshot: `reviews/presentation-2026-11-15/our-people-revised-hero.jpg`. Viewport overrides were reset; local preview remains available on port 4174.

## Follow-up: Our Craft sustainability marks and shorter page

Removed the dedicated hero eyebrow, retaining Crafting the Future. Sustainability now ends with the existing Cacao-Trace and Rainforest Alliance artwork in a responsive two-logo row. The shared logo renderer supplies the same official destinations, alternative text, new-tab announcements and Orange hover/focus treatment used on the homepage. No logo artwork or source files changed.

Removed Ask About Food Safety, the complete Process & Capabilities section, its factory media and four manufacturing cards, and the final Explore Partner Brands / Let's Talk actions. The page now contains Promise, Focus, Sustainability and Food Safety, in that order. Historical process fragments forward to the Craft overview; historical segment fragments retain their segment destinations through nonvisual aliases. Archived source copy is preserved, while the retained-copy checks no longer require the removed process content.

Rebuilt 24 pages; static checks pass for 2,581 references, protected artwork, shared partial propagation and deterministic rebuild. All 632 retained-copy checks pass. Hidden-browser checks confirm no hero eyebrow, four remaining sections, two loaded Sustainability logos, no content buttons or closing actions, and no horizontal overflow at 1600px or 390px. The old `/products/#one-shot-depositing` URL successfully forwards to `/our-craft/`. Screenshot: `reviews/presentation-2026-11-15/our-craft-sustainability-logos.jpg`. Viewport overrides were reset; preview remains local on port 4174.

## Follow-up: Partner Brands process introduction

Added the Process & Capabilities h2 and Guy's exact supplied Rochester factory paragraph immediately after Built for Growth on `/b2b/`, before the eight format cards. Reuses the matching archived C14 paragraph without restoring the removed Craft media or actions. Rebuilt 24 pages; static checks pass for 2,581 references and all 635 retained-copy checks pass. Hidden-browser verification confirms the preceding section, exact text, no images/actions in the new section and no overflow. Screenshot: `reviews/presentation-2026-11-15/partner-brands-process-intro.jpg`.

## Follow-up: remove Wholesale

Removed the Wholesale offering from the runtime service model, both Craft submenus, shared footer, inquiry topics and contact-page metadata. Deleted its generated HTML and removed it from the public inventory and local export. The site now has 23 pages; `/wholesale/`, `/wholesale` and `/wholesale/index.html` resolve to the not-found response. The source baseline and historical records remain archived. The approved 1971 family timeline sentence retains its historical use of the word wholesale.

Static checks pass for 2,413 references, protected artwork, shared partial propagation and deterministic rebuild. All 622 retained-copy checks and navigation state checks pass. Local export checks pass for 23 pages, 136 artifact files, 2,768 references and 167 loopback HTTP cases, with no Wholesale page or redirect included. The preview was restarted with the new inventory on port 4174. Hidden-browser checks confirm four Craft menu entries, no Wholesale footer link or inquiry option, and the not-found page at the retired URL. Evidence: `reviews/presentation-2026-11-15/wholesale-removal-checks.json` and `navigation-without-wholesale.jpg`.

## Follow-up: remove all Orange hero eyebrows

Removed eyebrow rendering from the shared Orange hero component across all 23 generated pages, including the homepage. Main h1 headings, copy, media and actions remain unchanged. Section eyebrows outside the hero banners remain. Retained-copy checks exclude the five intentionally removed hero-label assertions while preserving all other content checks.

Static checks pass for 2,413 references, protected artwork, shared partial propagation and deterministic rebuild. All 617 retained-copy checks pass. A generated-page scan confirms zero eyebrows inside all 23 Orange heroes. Hidden-browser checks confirm the homepage desktop hero and Snacking phone hero render without eyebrows or horizontal overflow at 1600px and 390px respectively. Screenshot: `reviews/presentation-2026-11-15/hero-banners-without-eyebrows.jpg`. Viewport overrides were reset; the local preview remains available on port 4174.

## Follow-up: remove Our Segments chocolate CTA

Removed the bottom Explore Our Chocolate action from `/our-segments/`, preserving Let's Talk and the four segment links. The shared page renderer now permits a closing action group without a primary destination. Rebuilt 23 pages; static checks pass for 2,412 references, shared partial propagation and deterministic rebuild, and all 617 retained-copy checks pass. Hidden-browser verification confirms Let's Talk is the only closing action and no Explore Chocolate link remains in the page content. Screenshot: `reviews/presentation-2026-11-15/segments-without-chocolate-cta.jpg`. Viewport overrides were reset; local preview remains available on port 4174.

## Follow-up: Experience Center factory media and actions

Added the existing factory GIF immediately above How its Made, using a responsive full-container figure with rounded corners and no frame border. The shared image component retains the existing still image for reduced motion. Removed the section's Explore Our Craft button. Removed the Museum & Virtual Exhibition closing question and Craft Your Own Chocolate Bar button, preserving all ten timeline chapters and their source links. Tours and Classes now has one primary Book Your Appointment action linking to the existing Experience Center inquiry route. This remains an inquiry destination, with no booking backend introduced.

Rebuilt 23 pages; static checks pass for 2,411 local references, 57 protected artwork files, shared partial propagation and deterministic rebuild. All 617 retained-copy checks pass. Hidden-browser checks confirm the loaded GIF and fallback, figure-before-heading order, seven process steps, no How its Made button, no museum closing invitation, ten timeline chapters and one Tours action. Desktop and phone layouts have no horizontal overflow. Keyboard access and following Book Your Appointment were verified; the destination selects Experience Center in the inquiry form. Screenshots: `reviews/presentation-2026-11-15/experience-factory-above-process.jpg` and `experience-book-appointment-phone.jpg`. Viewport overrides were reset; preview remains local on port 4174.

## Follow-up: Craft Your Own introduction and shorter page

Replaced the dedicated introduction with Guy's exact Build your own chocolate bar, basket or gift box paragraph. Removed the Share Your Idea section and both paragraphs, plus the closing Ask About Craft Your Own and Explore the Experience Center actions. Chocolate Bars and Baskets & gift boxes remain unchanged.

Rebuilt 23 pages; static checks pass for 2,409 references, protected artwork, shared partial propagation and deterministic rebuild. All 617 retained-copy checks pass. Hidden-browser verification confirms the exact new introduction, only the two retained content sections, no removed text or closing actions, and no horizontal overflow. Screenshot: `reviews/presentation-2026-11-15/craft-your-own-revised-copy.jpg`. Viewport overrides were reset; local preview remains available on port 4174.

## Follow-up: Experience Center Coming Soon notice

Added Coming Soon as a compact semantic h2 directly below the Experience Center hero h1 and before its three existing introduction paragraphs. The shared hero accepts an optional notice; only this dedicated page supplies it. Existing introduction wording, media and section content remain unchanged.

Rebuilt 23 pages; static checks pass for 2,409 local references, protected artwork, shared partial propagation and deterministic rebuild, and all 617 retained-copy checks pass. Hidden-browser verification confirms the notice order and no horizontal overflow at 1600px and 390px. Screenshot: `reviews/presentation-2026-11-15/experience-coming-soon-hero.jpg`. Viewport overrides were reset; local preview remains available on port 4174.
