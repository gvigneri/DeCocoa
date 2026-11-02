# DeCocoa web asset export manifest

## Homepage People photo selection, October 25, 2026

Guy selected the existing `assets/images/chocolate-craft.webp` photo for the homepage People mask after viewing the full image. It is the unchanged 931 x 696 export of wireframe image `references/wireframe-images/P184-X17.jpg`, showing a person carrying a tray of chocolate. This replaces `people-at-work.webp` in the homepage card only; both assets and their original provenance remain. Keep the enlarged exact brandmark mask and fixed card/stage heights, with CSS photo framing for the visible crop.

## Compact header icon and static website patterns, October 25, 2026

The compact scrolling header now references the existing `assets/logos/decocoa-brandmark.svg`, preserving its exact source geometry and Brown #582011 artwork. A picture source switches to the unchanged desktop wordmark at1536px. No new logo export is created. Website pattern instances are regenerated without animation/highlight metadata; source/master paths and transforms are unchanged. All backgrounds retain fixed motif colors. The People photo/mask are unchanged assets displayed1.5× larger inside the preceding fixed-height card/stage, with additional clipping.

## Supplied Wegmans replacement, October 25, 2026

Guy supplied `C:/Users/guyta/Desktop/626950-h-media-logo-fyfga.webp` and requested it for Wegmans. The complete 1280×1000 WebP is preserved as `assets/source-external/user-attachments/626950-h-media-logo-fyfga.webp` and copied byte-for-byte to `assets/images/partner-wegmans-supplied-626950.webp` (58,794 bytes; SHA256 `46aa4f2538544f46aa9abd6627eae5ab132f8184b2feff7b81efad58564178fd`). No image editing, background removal, recoloring or cropping. The homepage uses this supplied image; its original background/alpha are retained. The earlier official PNG and provenance remain archival. The `wegmans-supplied` record in [trust-export-details.json](../assets/trust-export-details.json) records the new active asset.

## Homepage panels and factory animation, October 25, 2026

The supplied `C:\Users\guyta\Downloads\DeCocoa-Factory.gif` is preserved under `assets/source-external/user-attachments/` and copied byte-for-byte to `assets/images/decocoa-factory.gif`. It is a 1200×422 illustration with 160 frames at 50ms each, an eight-second cycle and infinite looping. No frame, palette, geometry or timing is changed. A lossless composited first-frame PNG, `decocoa-factory-still.png`, supplies the reduced-motion picture source. Dimensions, SHA256 hashes and operations are in [factory-media-details.json](../assets/factory-media-details.json). The entire illustrated frame appears left of the Experience Center copy in its borderless card; it does not establish the real facility's appearance or operating capabilities.

Three additional genuine Font Awesome Free 6.7.2 icons, `shield-heart`, `leaf` and `gears`, identify the homepage Craft themes. Original SVG geometry, attribution and CC BY 4.0 license are preserved; inline instances add presentation attributes and inherit Orange. Source URLs and hashes are in [icon provenance](../assets/icons/fontawesome-free-6.7.2/provenance.json). The supplied people photograph is unchanged and now uses the exact existing standalone brandmark mask inside the People card, as Guy explicitly requested. Horizontal positioning favors the face. The homepage Craft photograph and former Experience masked chocolate image are removed from those sections, while original assets and interior-page usage remain intact.

## Partner and certification refresh, October 25, 2026

The homepage separates Partners after Our People and Certifications after Our Craft, using larger individual marks on Cream. Runtime images are PNGs, with full source files, dimensions, alpha checks, SHA256 hashes and conversion details in [trust-export-details.json](../assets/trust-export-details.json). New downloads are preserved under `assets/source-external/trust/`; earlier wireframe crops remain unchanged. Source artwork is neither recolored nor redrawn. Vector sources are rendered faithfully to transparent PNGs.

| Web PNG | Source | Status |
| --- | --- | --- |
| `partner-wegmans-official.png` | [Wegmans photo/logo gallery](https://www.wegmans.com/news-media/photo-logo-gallery), color PNG with alpha | Unmodified official download, 1000×379. Replaces the White-backed wireframe crop. |
| `certification-sqf.png` | [SQFI website](https://www.sqfi.com/integrity-program/logo-rules-of-use), complete official SQF Institute header vector | Transparent PNG export, 640×280. Organization identity, not an SQF Quality Shield; alt text identifies SQF Institute. |
| `certification-ou-kosher.png` | [Commons Ou kosher.svg](https://commons.wikimedia.org/wiki/File:Ou_kosher.svg) | Transparent PNG export, 654×651 after trimming empty alpha canvas and adding 40px transparent padding; mark geometry and colors unchanged. Third-party vector recreation, not an issuer master; PD-textlogo/trademark notice retained in provenance. Replace with approved issuer artwork before production. |
| `certification-haccp.png` | [Plants2Market quality page](https://www.plants2market.com/en/qualitatsmanagement), generic HACCP badge | Unmodified transparent PNG, 690×706. Explicitly authorized temporary online reference; no issuer identified. Replace later as Guy requested. |
| `certification-rainforest-alliance.png` | [Rainforest Alliance logo/seal guidance](https://www.rainforest-alliance.org/business/marketing-sustainability/using-our-logo-and-seal/), official navigation seal vector | Transparent PNG export, 640×640. Standard People & Nature seal, not the separate Regenerative or Forest Allies mark. |
| `certification-cacao-trace.png` | [Cacao-Trace](https://www.cacaotrace.com/), inline header vector | Transparent PNG export, 640×519; geometry, colors and proportions preserved. |
| `partner-puratos.png`, `partner-guittard.png` | Existing supplied wireframe exports | Unchanged PNGs; their raster backdrop is exactly website Cream #F7EFE6, so it blends without background removal. |

Logo sourcing does not establish DeCocoa's certification, partnership, product scope or permission for public use. Existing production confirmation requirements remain. The local draft is not published. Candidate files with opaque backdrops, White lettering, unrelated social icons or an unsupported HACCP issuer were rejected and are not runtime assets.

October 24 category revision: Wellness reuses the Wellness.png export; One Shot Depositing reuses Bark filled.png; Hollow Moulding adds a proportional alpha-cropped WebP from Bunny 2.png; Mixing reuses Nuts Upscale.png; Dry Filling reuses Chocolate Powder.png. Original sources remain unchanged. Dimensions, operations and SHA256 hashes are recorded in [category-export-details.json](../assets/category-export-details.json). Image selection is illustrative draft mapping, not ingredient or availability confirmation.

Four genuine Font Awesome Free 6.7.2 SVGs (arrow-right, gift, wand-magic-sparkles and handshake) are bundled locally, with original geometry/attribution and presentation-only attributes on embedded instances. See [icon provenance](../assets/icons/fontawesome-free-6.7.2/provenance.json) and [license](../assets/icons/fontawesome-free-6.7.2/LICENSE.txt). No external icon/font script is loaded at runtime.

Prepared October 11, 2026. Originals remain under `brand/source/Decocoa Get Started/`. Conversion is reproducible through `scripts/prepare_assets.py` plus the Poppler commands below. Current redesign uses the corrected horizontal logo, three separately animated pretzels (two Imagegen-assisted cutouts and one original source export), supplied dark-background badge, three product cutouts, three inline editable pattern covers, two supplied people/craft photos, supplied trust reference marks and the exact brandmark exterior as a chocolate photo mask. Earlier stage history below is archival; homepage-r6 notes supersede its usage and treatment descriptions.

| Export | Original | Export details | Usage and validation |
| --- | --- | --- | --- |
| `assets/logos/decocoa-horizontal.svg` | `DeCocoa_Logo_RGB_LightBG_Horiztonal.ai`, page 1 | True SVG, 9 outlined paths. Original path coordinates transformed from PDF into SVG coordinates; tight viewBox 3537.758 Ã— 918.851. Source RGB fill 0.345/0.125/0.067 â†’ #582011. ICC-based source profile is RGB; matching Poppler raster sample #582011. No manual recoloring. | Header on solid cream. Source raster inspected at 1800px. The r4 exporter preserves the filled underline rectangle and artboard clipping. Source-to-SVG browser comparison verified the complete wordmark including underline. Earlier path-count validation alone did not detect the missing rectangle. Source fill differs from site Chocolate #512316 and is deliberately preserved. |
| `assets/logos/horizontal-source-render.png` | Same | Poppler, 1800 Ã— 801, white raster background, original complete artboard | Source export comparison evidence only. |
| `assets/logos/horizontal-source-cropped.png` | Same | Tight crop of source render with 2px bleed | Comparison evidence only; not the web identity asset. |
| `assets/images/filled-chocolate.webp` | `images/Bark filled.png` | 872 Ã— 496, RGBA WebP quality 94. Cropped to existing alpha bounds. No retouching, recoloring, or new background. | Products and Experience masked composition in r4. Original inspected, including actual compositing on cream to verify transparency. Represents supplied chocolate; product/flavor name intentionally not inferred. |
| `assets/images/chocolate-bar.webp` | `images/Bark.png` | 905 Ã— 1500, RGBA WebP quality 94. Alpha-bounds crop and proportional resize. | Products; not used in stage 1. |
| `assets/images/cocoa-powder.webp` | `images/Chocolate Powder.png` | 1500 Ã— 642, RGBA WebP quality 94. Alpha-bounds crop and proportional resize. | Prepared; not used in stage 1. |
| `assets/images/nuts-and-chocolate.webp` | `images/Nuts Upscale.png` | 1500 Ã— 876, RGBA WebP quality 94. Alpha-bounds crop and proportional resize. | Prepared; not used in stage 1. |
| `assets/images/chocolate-drizzle.webp` | `images/Wellness.png` | 1500 Ã— 1486, RGBA WebP quality 94. Alpha-bounds crop and proportional resize. | Products; not used in stage 1. No wellness claim adopted from filename. |
| `assets/patterns/stripes.png` | `DeCocoa_BrandPatterns_Stripes_Pattern.ai`, page 1 | Poppler PNG at 1400px longest edge, source RGB colors, full artboard | Hero decorative panel with proportional `object-fit: cover`. No tiling, recoloring, opacity, animation, or logo overlay. All six source pattern previews inspected together before selection. |
| `assets/patterns/*source-render*`, `DeCocoa*png`, `pattern-contact-sheet.jpg` | Six standalone pattern AI sources | Diagnostic PNG/JPG previews | Inspection evidence, not web assets. No repeat-seam claim. |
| `assets/fonts/montserrat.css` and five `.woff2` files | Google Fonts Montserrat, coordinator-prepared local files | Local 300, 400, 700 font faces; provenance and OFL retained in same folder | All text. `font-synthesis: none`. Susa omitted because unavailable. |

Pattern rendering command: `pdftoppm -scale-to 1400 -png -singlefile "brand/source/Decocoa Get Started/DeCocoa_BrandPatterns_Stripes_Pattern.ai" "assets/patterns/stripes"`.

No brandmark components were extracted as botanical decoration. No generated imagery, third-party stock, partner marks, certifications, or wireframe photography is used in stage 1. Product cutouts are original supplied assets, with no claim about current availability.

## Complete homepage additions, homepage-r2

| Export | Original / extraction path | Export details and validation |
| --- | --- | --- |
| `assets/images/people-at-work.webp` | Wireframe page 2 `/Resources/Pattern/P179/Resources/XObject/X4`; unchanged extracted JPEG in `references/wireframe-images/P179-X4.jpg` | 1229 Ã— 697, RGB WebP quality 92; source framing and colors preserved. Original and export inspected. Used with full original framing and a quiet cream frame in People in r4; face remains complete. Photography is provisional for production usage. |
| `assets/images/chocolate-craft.webp` | Wireframe page 2 `/Resources/Pattern/P184/Resources/XObject/X17`; unchanged extracted JPEG `references/wireframe-images/P184-X17.jpg` | 931 Ã— 696, RGB WebP quality 92; source framing and colors preserved. Original and export inspected. Used with CSS cover crop in Craft. Provisional production rights/approval. |
| `assets/images/partner-puratos.png` | Wireframe page 2, page-coordinate bounds x44/y2710/x272/y2870 from top-left | PDFium render at 2Ã—, exact 456 Ã— 320 crop. Full mark, tagline, source colors and quiet original cream preserved. Viewed export. One occurrence only. |
| `assets/images/partner-wegmans.png` | Wireframe page 2, bounds x304/y2710/x550/y2870 | PDFium 2Ã—, exact 492 Ã— 320 crop. Full mark/tagline and original white block preserved. Viewed export. One occurrence only. |
| `assets/images/partner-guittard.png` | Wireframe page 2, bounds x568/y2710/x838/y2870 | PDFium 2Ã—, exact 540 Ã— 320 crop. Full mark/tagline, source colors and quiet original cream preserved. Viewed export. One occurrence only. |
| `assets/images/certification-reference-a.jpg` | Wireframe page 2 `/Resources/XObject/X233/Resources/XObject/X224/Resources/XObject/X223/Resources/Pattern/P80/Resources/XObject/X77` | Exact decoded embedded JPEG bytes, 558 Ã— 154. OU Kosher/SQF/HACCP source grouping, no individual alteration. Viewed export. |
| `assets/images/certification-reference-b.jpg` | Wireframe page 2 `/Resources/XObject/X233/Resources/XObject/X226/Resources/XObject/X225/Resources/Pattern/P85/Resources/XObject/X83` | Exact decoded embedded JPEG bytes, 325 Ã— 130. Rainforest Alliance/Cacao-Trace source grouping, no individual alteration. Viewed export. |

Reference mark extraction is reproducible through `scripts/prepare_reference_marks.py`. In r4, reference caveats are documented here and in the handoff, per the user’s request for clean public-facing page copy. Relationships, certification status and usage approval remain unverified and must be confirmed before production. These exports are layout material, not certification or relationship verification. Production should replace reference crops with current approved individual originals.

Excluded asset: `references/wireframe-images/X201-P57-X55.jpg` has a visible iStock watermark. It is not included in website assets or used in the prototype; no watermark removal was attempted. Experience Center in r4 uses a typographic invitation, full Growth pattern cover, original filled chocolate inside the source brandmark exterior, and a contact anchor. It makes no claim about opening hours, visit availability or facility appearance.

Products section uses the previously prepared filled chocolate, bar, and drizzle cutouts. Descriptive headings are draft mood copy, not a finalized catalog taxonomy. Source capability labels Mixing, One Shot Depositing, and Hollow Moulding are moved into Craft with short draft explanatory copy. No sourced sustainability, food-safety or sourcing claims are adopted.

Homepage-r3 adjusts the wide-desktop Craft image to the original 931:696 aspect ratio, preserving the entire face and tray with no crop or retouching. Other responsive crops remain as reviewed. The export file and source provenance are unchanged.

Header clear space: SVG is trimmed to ink plus approximately 2 raster pixels. At 220px web width the flower is approximately 57px high; manual page 23 Y is approximately half that height. The link reserves 29px around the image, 25px at 190px logo width, 24px at 180px, 22px at 166px, and 20px at 150px. This is a practical measurement of the supplied diagram, not a new universal brand rule.


## Current redesign exports, homepage-r4

The revised user authorization permits animated/recolored website pattern copies in the approved palette and an exact logo-icon photo mask. Master pattern colors and header/footer identity artwork remain untouched. Patterns are full supplied panels, not assumed seamless tiles. No opacity tricks, raster embedding or redrawn geometry is used.

| Export | Source and preparation | Current use |
| --- | --- | --- |
| `assets/patterns/circles-master.svg` | Circles AI, 1600 × 900, 867 painted paths, 2 clipping paths. Source colors #512316/#E87933/#F4F4EF/#FFFFFF preserved. | Editable standalone master; not used on page. |
| `assets/patterns/floweroflife-master.svg` | FlowerOfLife AI, 1600 × 900, 56 painted paths, 1 clip. Source chocolate/orange preserved. | Full People section cover; website copy has scattered independently timed sunrise highlights and subtle path movement. |
| `assets/patterns/growth-master.svg` | Growth AI, 1600 × 900, 173 painted paths, 1 clip. Source chocolate/orange/cream preserved. | Full Experience section cover, with the same approved motion treatment. |
| `assets/patterns/luxury-master.svg` | Luxury AI, 1600 × 900, 154 painted paths, 1 clip. Source chocolate/orange preserved. | Editable standalone master; not used on page. |
| `assets/patterns/rings-master.svg` | Rings AI, 1600 × 900, 136 painted paths, 3 clips. Source chocolate/orange preserved. | Editable standalone master; not used on page. |
| `assets/patterns/stripes-master.svg` | Stripes AI, 1600 × 900, 187 painted paths, 1 clip. Source chocolate/cream preserved. | Broad hero separator, subtle movement without highlights. |
| `assets/patterns/{floweroflife,growth,stripes}-website.svg` | Built from masters by `scripts/build_homepage.py`; IDs and clip references uniquely prefixed per instance. Individual path styles use deterministic scattered phases/durations, varying the changing pods independently. | Embedded in `prototype/index.html` at build time; no runtime network loading. |
| `assets/logos/decocoa-brandmark.svg` | Complete outlined source `DeCocoa_Logo_RGB_LightBG_Brandmark.ai`. Tight viewBox 1309.676 × 1511.664, source #582011, 1 painted compound path, 1 clip. | Editable identity export; not used as altered header/footer logo. |
| `assets/logos/decocoa-brandmark-silhouette.svg` | Exact final closed exterior contour of that source compound path. No redrawing; white mask fill only. | CSS mask for original filled-chocolate photograph in Experience, per explicit user exception. No wordmark is masked. |
| `assets/images/dipped-pretzel.webp` | `images/Pretzel + RedGreen sprinkles.png`; crop to original alpha bounds, 1326 × 1138 RGBA, quality94 WebP. | Hero main piece and two decorative smaller instances. Only CSS position/scale/rotation and finite entrance motion; no source image editing. |
| `assets/images/dipped-pretzels.webp` | `images/Pretzels.png`; alpha-bounds crop and max1500 proportional resize. | Prepared but unused. Collage’s hidden-alpha composition was less suitable than the clean single original. |

Reproduction: run `scripts/prepare_assets.py`, `scripts/prepare_reference_marks.py` if reference marks need regeneration, then `scripts/build_homepage.py`. The strict vector converter in `scripts/export_vectors.py` owns all identity/pattern geometry; the legacy incomplete logo converter has been removed, so rerunning preparation cannot lose the underline. Filled `re` rectangles and clipping `re` rectangles are handled according to their subsequent PDF paint/clip operators.

Visual comparison on October 11: viewed all six original AI raster renders beside their SVG masters in Chrome at 1440px. Patterns matched source composition, clipping, geometry and colors; source raster antialiasing differed naturally. Viewed horizontal source/updated SVG including underline, full source brandmark/SVG, and extracted exterior silhouette. The outline matches. Diagnostic gallery: `scripts/vector-qa.html`.

The revised page removes prototype/provisional explanations, planned-route dialogs, initial contact status and unbuilt legal links. All visible journeys either anchor to implemented sections or preselect a useful contact topic. Source provenance, draft-copy status and trust-mark approval limitations remain in project documentation. No contact data is transmitted or persisted; only the allowed motion pause flag is stored locally. Source form fields are disabled until local handlers are safely installed, and have no native form owner.

## Current exports and treatment, homepage-r5

| Export | Source and preparation | Current use and verification |
| --- | --- | --- |
| `assets/images/dipped-pretzel-trio.webp` | Original `images/Pretzels.png`, 3232 × 4576 RGBA. `scripts/prepare_pretzel_trio.py` excludes only the detached faint small duplicate in the upper right. It preserves the three overlapping core pretzels, original transparency, overlap and all exterior edges, crops alpha bounds [223,562,3166,4397], then proportionally resizes to 1305 × 1700 and saves quality94 WebP. Measured selection polygon is recorded in `assets/pretzel-trio-export-details.json`. | One hero image; three distinct supplied pieces, with one finite two-second group entrance. No painted or invented hidden edges. Settled rotated composition inspected at all five required widths; all outer edges remain visible at 390 and 320. Source/export proof is `assets/images/pretzel-trio-export-proof.jpg`. The previously attempted isolated pair had cut edges and was rejected; that unused export/helper was removed. |
| `assets/logos/decocoa-dark-badge.svg` | Original `DeCocoa_Logo_RGB_DarkBG_Badge.ai`, strict outlined vector conversion, 31 painted paths and 1 clipping path. Tight viewBox 283.6911 283.6911 1432.618 1432.618. Original source colors #FA7110 and #FAF0E6 preserved exactly. | Static intact footer badge on solid site Chocolate. Source colors intentionally remain distinct from site tokens. Browser comparison against the original PDF-compatible AI rendered on Brown verified shape, lettering, three circles and color. Proof `prototype/qa-r5/badge-source-comparison.jpg`; source-render evidence retained beside export. |
| `assets/patterns/stripes-website.svg` | Source Stripes master geometry and clipping retained; approved website copy maps background to primary Chocolate and motifs to primary Orange. | Full-height hero cover. Brown quiet copy panel gives readable Cream text. No yellow disc. Source master remains in original colors. |

The previous single-pretzel export remains available as a source-derived asset but is no longer instantiated in the hero. Existing six SVG masters, horizontal identity with underline, icon mask, product exports, photographs and reference marks retain their preceding geometry and provenance.

R5 uses 1rem ordinary text and button type, 1.25rem main navigation, 8px outer/4px inner button radii and restrained animated hover fills/lift without underlines. Orange eyebrows use minimal solid Chocolate backing adjacent to headings to preserve contrast. Header Let's Talk links are secondary; the Orange scroll header gives its secondary CTA an intentional Cream backing. Footer navigation headings are Orange on Chocolate. Responsive menus preserve the requested type sizes by changing layout at 900px (original header) and 1199px (scroll header); menu height follows the actual measured header height.

Reproduction is unchanged: `prepare_assets.py` invokes the strict vector converter and the intact trio helper, followed by `build_homepage.py`. No source files are modified. R5 inspection and behavior coverage is recorded in `prototype/implementation-checks-r5.md`; static results and frozen implementation hashes are in `prototype/source-checks.json`.

## Current asset and motion treatment, homepage-r6

The user requested three independently falling pieces. The red-drizzle and chunky-sprinkle originals overlapped other pieces in the supplied collage. The coordinator used Imagegen to separate them and reconstruct their small occluded edges. These two are assisted reconstructions, **not pixel-identical original exports**. Prompts and provenance are retained in `handoff/pretzel-cutout-provenance.json`; the supplied source artwork remains unchanged.

| Current hero asset | Preparation and provenance |
| --- | --- |
| `assets/images/pretzel-red-drizzle-r6.webp` | Mechanical quality94 WebP compression of coordinator-provided `pretzel-red-drizzle-r6.png`, actual dimensions 1230 × 1278, 298158 bytes. No crop, resize, recolor, alpha edit or further retouch. Alpha channel compared byte for byte with PNG and is identical, range0..255. |
| `assets/images/pretzel-chunky-sprinkles-r6.webp` | Mechanical quality94 WebP compression of coordinator-provided `pretzel-chunky-sprinkles-r6.png`, actual dimensions 1230 × 1278, 495236 bytes. Same unchanged framing and verified exact alpha. |
| `assets/images/dipped-pretzel.webp` | Existing source-derived red/green sugar-pearl pretzel, 1326 × 1138. Unchanged original source export. |

Both generated PNGs remain retained as reproducible compression inputs. `scripts/prepare_r6_cutouts.py` exports the WebPs and records dimensions, alpha checks and PNG hashes in `assets/r6-cutout-export-details.json`. It is invoked by `prepare_assets.py`. The earlier intact trio remains archival and is unused in the current homepage.

Three separate image nodes have independent eased drop wrappers, durations1.55/1.65/1.7s and delays0/.2/.4s. They start1100px above settled positions, settle with subtle individual tilts, and finish by2.1s. Saved pause preference starts a complete static composition; a pause during entry holds the current animation frame and resume continues it. Reduced-motion, hidden/offscreen pauses and pattern motion controls remain supported.

Buttons retain outer2px and now use inner2px borders at8/4px radii. Eyebrows use8px corners. Eight shared card surfaces use a visible4px contextual Cream/Orange ring inside a transparent4px perimeter with16px outer corners; background clipping leaves the outer ring transparent, and images round inside the card. The exact icon mask and all header/footer identities remain untouched. R6 is implementation-self-checked only: the five independent review slots are exhausted and the user took over design review.
