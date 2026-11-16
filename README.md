# DeCocoa site

The current [November 15 presentation revision](handoff/presentation-revision-2026-11-15.md) contains 23 pages. Wholesale has been removed as a service and page. Our Chocolate presents Snacking, Gifting and Entertaining, each with a dedicated page containing eight chocolate formats. All five navigation groups have square supporting menu photos. The revision also places Our Segments after Our Craft, adds a segment hub and dedicated Branded Chocolate/Fulfillment pages alongside Partner Brands/Décor, updates homepage copy and card layouts, uses 24px desktop body text, removes public em dashes, and refines heading semantics, hover states and shadows. The preview remains at [127.0.0.1:4174](http://127.0.0.1:4174/).

This continues the established DeCocoa design as a portable, responsive informational site. Guy approved the local draft build in [the consolidated plan](handoff/site-build-plan.md) and authorized temporary GitHub Pages hosting on October 25, 2026. WordPress transfer remains a later phase. Inquiry fields do not send or save messages.

The November 11 baseline implements the [content and component brief](handoff/content-component-brief-2026-11-11.md) while preserving the theme. It covers 19 public pages with shared Orange heroes, 11 consumer categories on Our Chocolate, linked primary navigation with image menus, the full family story, four business segments, Partner Brands at `/b2b/`, and the new `/decor/` page. The [component catalog](handoff/component-catalog.md) documents source ownership, shared components, their inputs and a reusable page composition. Guy authorized pushing all November 11–15 changes to the existing GitHub repository and Pages workflow on November 15. See the [release scope and verification](handoff/github-release-2026-11-15.md).

The complete ten-chapter chocolate-history timeline is in `/experience-center/#museum-virtual-exhibition`, following Guy's reference image through A Sweeter Tomorrow. The approved first four chapters are preserved. [Artwork, sources and editing notes](handoff/chocolate-history-complete.md).

Historical November 1 GitHub revision: Guy requested pushing the latest homepage, People, Craft and Experience Center changes to this repository and its existing Pages workflow. That update included the chocolate bark hero, Orange homepage sections, shared page introductions, Cream product cards, Key Segments cards and updated partner/certification logos. [Release scope and verification](handoff/github-release-2026-11-01.md).

Retained November 1 timeline refinements include semantic date/region/title headings with equal spacing, centered museum introduction, compact source arrows and borderless main sections. The November 15 Experience Center revision adds Coming Soon to its hero and the factory GIF above How its Made, removes the process Explore button and museum closing invitation, and replaces the Tours actions with Book Your Appointment linking to the existing inquiry form. [Historical timeline revision checks](reviews/chocolate-history-2026-11-01/order-arrow-action-verification.md).

## GitHub Pages

The public homepage is [gvigneri.github.io/DeCocoa/](https://gvigneri.github.io/DeCocoa/). The workflow in `.github/workflows/pages.yml` builds and checks the site, exports the generated pages and runtime assets into `_site/`, validates their URLs under `/DeCocoa/`, then deploys that artifact. The repository's Pages publishing source must be **GitHub Actions**. Pushes to `main` deploy automatically; the workflow can also be run manually.

The November 15 release includes the reviewed November 11 baseline and all subsequent presentation revisions. Building, exporting and checking locally does not publish; pushing to `main` starts the existing deployment workflow.

The published artifact has `index.html`, `styles.css`, `script.js`, `assets/` and the page directories at its root. `prototype/` remains the editable/generated source folder in this repository. Compatibility pages redirect the old `/DeCocoa/prototype/index.html` and related legacy URLs to the new public routes. Original artwork, templates and review/handoff records are not included in the website artifact.

To check the same artifact locally after rebuilding:

```powershell
python scripts/build_homepage.py
python scripts/check_content_components.py
python scripts/check_site.py
python scripts/export_pages.py --base-path /DeCocoa/
python scripts/check_pages_export.py --base-path /DeCocoa/
python scripts/preview_pages.py --port 4180 --base-path /DeCocoa/
```

Open [the project-path preview](http://127.0.0.1:4180/DeCocoa/). This separate preview reproduces the GitHub Pages project path and nested 404 handling; it does not replace the normal local preview below.

## Preview

From this folder in PowerShell:

```powershell
.\Start-Preview.ps1 -Port 4174
```

The current review server is [http://127.0.0.1:4174/](http://127.0.0.1:4174/). Open that address if the server is already running. Press Ctrl+C in its serving terminal to stop. The helper uses Codex's bundled Python when present, or an installed Python otherwise; omitting `-Port` uses its existing default of 4173.

The public site starts at `/`, with standard paths such as `/products/`, `/gifting/`, `/our-people/` and `/lets-talk/`. `prototype/` remains an internal source/output folder; it is not part of the site's public slugs. Older `/prototype/…` preview URLs redirect to their clean equivalents. The retired `/work-with-us/` route redirects to Let's Talk; its former service fragments forward to their new destinations.

The delivered pages are already generated. All fonts and website assets are local, and preview needs no package installation.

## Edit and rebuild

Use Python 3 to regenerate the complete site:

```powershell
python scripts/build_homepage.py
```

The existing generator name is retained for continuity; it now generates the entire approved local site using Python's standard library.

| Editable source | Responsibility |
| --- | --- |
| `prototype/site-content.json` | Retained page content, product examples, images, inquiry defaults, Food Safety, Sweet Careers and policy notices |
| `prototype/approved-content.json`, `scripts/content_updates.py` | Authoritative C01–C14 replacement copy and its mapping into existing page data; shared text is resolved once for reuse |
| `prototype/navigation.json`, `scripts/navigation_components.py` | One authoritative main-page/menu hierarchy, active-route grouping and image-menu presentation |
| `prototype/logo-links.json` | Verified destinations paired with existing partner/certification marks; HACCP issuer remains unresolved |
| `prototype/partials/header.html` | One master header, including original and scroll variants |
| `prototype/partials/footer.html` | One master footer |
| `prototype/partials/hero.html`, `scripts/shared_components.py` | Shared Orange hero and optional notice, images, paragraphs, family timeline and information grids |
| `prototype/partials/inquiry.html` | Shared inquiry interface used once on Home and once on Let's Talk |
| `prototype/site.template.html` | Shared document structure and asset includes |
| `prototype/homepage.template.html` | Homepage sections and established visual composition |
| `prototype/trust-section.template.html` | Shared Partners/Certifications section; retained mark artwork, resolved approved copy and verified external links |
| `prototype/product-detail.template.html` | Reusable product detail layout |
| `prototype/styles.css`, `prototype/script.js` | Shared responsive styling and behavior |
| `assets/css/components.css`, `assets/css/navigation.css` | Shared page/category/timeline compositions and image menus, extending existing theme tokens and responsive rules |
| `assets/js/category-motion.js` | Full-width single-copy category row, keyboard access and interaction/motion gates |
| `prototype/chocolate-history.json`, `prototype/chocolate-history-chapter.template.html` | Experience timeline copy, source links, scene/layer controls and reusable chapter markup |
| `assets/css/chocolate-history.css`, `assets/js/chocolate-history.js` | Experience-only responsive timeline styling and optional once-only artwork entrances |
| `assets/chocolate-history-assets.json` | Generated PNG provenance, dimensions, transparency bounds, responsive variants and review status |
| `prototype/chocolate-history-artwork.json`, `scripts/prepare_chocolate_history_assets.py` | Incremental artwork preparation, preserved source archives and alpha QA sheets |
| `scripts/build_homepage.py` | Resolve content/navigation, assemble shared components, generate the page inventory and portable relative URLs |
| `scripts/prepare_trust_assets.py` | Reproducible PNG preparation from preserved external logo sources; provenance in `assets/trust-export-details.json` |
| `scripts/prepare_factory_media.py` | Preserve the supplied factory GIF and export a lossless first-frame reduced-motion fallback; provenance in `assets/factory-media-details.json` |

Edit sources, then rebuild. Generated `index.html` files and `prototype/404.html` are outputs; edits made directly to those files are overwritten by the generator. Faithful `assets/patterns/*-master.svg` files and original artwork remain separate from generated website SVG instances.

Use [the component catalog](handoff/component-catalog.md) for component inputs, variants, route coverage and a page composition example. `python scripts/check_content_components.py` compares the independent archived brief with generated text, normalizing presentation whitespace only. Run the existing `check_site.py`, `check_preview.py` and Pages export checks for structure, links, resources and project-path compatibility.

## Pages and behavior

The November 11 baseline contained 19 pages: Home; Our Chocolate with all 11 consumer categories; three retained descriptive product examples; Gifting; Craft Your Own; Fundraising; Wholesale; Partner Brands at the retained `/b2b/` route; Décor; Our People; Our Craft; Experience Center; Let's Talk; three pending draft destinations for Privacy Policy, Terms and Conditions and Accessibility; and a not-found recovery page. Every page uses the shared Orange hero. Home's centered, stacked `#talk` section and the dedicated Let's Talk `#inquiry` section reuse the same inquiry component and validation, once per document. Chocolate Bars and Baskets remain sections of Craft Your Own. Local links carry only public product/topic context. No catalog specifications, prices, checkout, accounts, booking or delivery backend are added.

The five main navigation groups share one model in both headers: Our Chocolate, Our People, Our Craft, Our Segments and Experience Center. Each primary label links to its main page; an independent toggle opens its submenu for keyboard/touch use, with image menus on desktop hover. Our Chocolate links to Snacking, Gifting and Entertaining. Our People retains its section destinations. Our Craft links to Promise, Focus, Sustainability and Food Safety. Craft Your Own, Fundraising and the other supporting pages retain footer access. Wholesale has no page, navigation link or inquiry option.

The four complete business-segment descriptions now appear on `/our-segments/`, with shortened summaries in their own homepage section. Partner Brands has the supplied Process & Capabilities introduction at `/b2b/#process-capabilities`; the old manufacturing-method cards are removed. Legacy manufacturing fragments forward to the Craft overview. The five Vigneri family milestones stay within Our Roots, separate from the existing ten-chapter chocolate-history experience.

The brief's supplied replacement wording is approved for this local implementation and preserved verbatim, including its authorized corrections. Business claims and logo inclusion do not independently establish certification or partnership status. Eight marks have verified official destinations and open in new tabs; the generic HACCP badge remains unlinked because its issuing organization is not identified. [Logo evidence and the specific missing destination](handoff/logo-links-2026-11-11.md). The October 25 footer links use `/privacy-policy/`, `/terms-and-conditions/` and `/accessibility/`; those three local pages explicitly state that their content is being prepared. They contain no invented policy terms or conformance claims. Other production gaps remain in the handoff.

Navigation supports keyboard and touch-sized controls. The full-width category row shows four cards across on desktop, two on tablet and one on phones. Guy's latest revision removes visible motion and previous/next controls. Motion retains reduced-motion, offscreen and hidden-page handling; the category row also stops during hover or keyboard focus. No manual motion preference is stored. Inquiry fields validate locally; a valid attempt reports that message delivery is not connected. Fields remain disabled if their script does not initialize.

## Records and artwork

The Git repository includes the site sources, generated pages, runtime assets, extracted original artwork and handoff/review records. Duplicate ZIP packages, local preview logs and Python caches remain local and are ignored. The original intake archive is retained in the working folder; its extracted originals are versioned under `brand/source/`. Git preserves file bytes to keep artwork provenance checks stable across clones.

- [Historical completion and verification](handoff/review-summary.md): earlier delivered local scope, checks and limitations.
- [Current content/component brief](handoff/content-component-brief-2026-11-11.md): approved C01–C14 copy, destinations and theme-preservation scope for the November 11 local revision.
- [Shared component catalog](handoff/component-catalog.md): implementation locations, content inputs, variants, page coverage and reusable composition.
- [Logo link evidence](handoff/logo-links-2026-11-11.md): eight verified official destinations and unresolved HACCP issuer.
- [Implementation evidence](reviews/site-build-2026-10-24/implementation-verification.md): the 50 route/width checks, browser interactions and static-check commands.
- [October site-build plan](handoff/site-build-plan.md): historical approved tasks, route inventory, findings, content gaps and verification.
- [Elementor transfer map](handoff/elementor-map.md): native assembly responsibilities for the later WordPress phase.
- [Production open items](handoff/open-items.md): content, target environment and delivery decisions.
- [Review ledger](reviews/ledger.md): the four October 24 baseline reviews, separate from the five historical prototype sessions.
- `brand/brand-rules.md`, `brand/brand-exceptions.md`, `brand/asset-manifest.md`: brand decisions and provenance.
- `assets/`: web artwork, imagery, six editable pattern masters and licensed local Montserrat fonts.
- `brand/source/`: preserved supplied originals. The original ZIP remains unchanged in the full workspace.
- `handoff/pretzel-cutout-provenance.json`: provenance for two Imagegen-assisted reconstructed pretzel cutouts.
- `DeCocoa-Site-Build-Master-Brief.md`: earlier supplied build brief; the November 11 content/component brief governs its mapped replacements. `DeCocoa-Codex-Master-Brief.md` remains historical where superseded.

Earlier `DeCocoa-preview*.zip` packages and r3–r6 reports describe historical homepage builds. They are not evidence of the current site's completion or an Elementor import package.

The preview helper serves only public pages and runtime assets through `scripts/preview_server.py`. Unknown routes return the shared recovery page with HTTP 404. The layout is also available at `/404.html`. WordPress will need its own equivalent routing when transferred.

