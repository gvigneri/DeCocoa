# Approved brand exceptions

## Full-width phone buttons and softer inner corners, October 25, 2026

Guy requested full-width primary/secondary buttons on phones, except compact Let's Talk buttons, plus slightly more rounded inner borders. Phone inner radii increase from 2px to 4px; outer radii stay 8px. Width follows the containing content area rather than the viewport. Desktop/tablet styling remains unchanged.

## Sticky phone Menu and closing motion, October 25, 2026

Guy requested the original phone Menu/Close row to stick at the top as its logo/contact row scrolls away, replacing the separate scrolling header on phones. The mobile drawer omits its duplicate Let's Talk link and bottom border. Drawer and accordion submenus move upward when closing, with immediate interaction removal and reduced-motion support. Phone pretzels gain modest spacing with the final piece lower. Phone primary/secondary buttons use tighter concentric corners; desktop buttons and supplied artwork remain unchanged.

## Full-height phone drawers and accordion states, October 25, 2026

Guy requested phone drawers to fill the viewport beneath the active header and open downward behind its chrome. Use internal drawer scrolling when links exceed the available height. Main accordion rows lose their permanent bottom borders; their active Orange line spans the entire row. Collapsing an accordion with a pointer clears the Orange hover treatment, while keyboard focus remains visible.

## Mobile accordion drawers and header-aware hero, October 25, 2026

Guy requested padding-free eyebrows, with 1rem type on phones. Both mobile headers use a logo/contact top row and a full-width Brown Menu/Close row with Cream text. The opening drawer contains main-group accordions and ordinary submenu links. The mobile hero accounts for the original header in its viewport-height composition; smaller pretzels settle higher and use a shorter falling entrance, retaining the same artwork and layered copy treatment.

Implementation adjustment for the smaller text: phone eyebrows on Primary Brown use a lighter Ripe #E05F49 (4.51:1 against #3A170D). This supports Guy's standing accessible-color preference at the new 16px size; he did not specify this hex directly. Keep light-surface Ripe, decorative shadows and the larger Craft summary headings unchanged.

## Mobile header spacing and layered viewport-height hero, October 25, 2026

Guy requested a centered Menu label and 16px edge alignment for the mobile scroll-header icon and contact action. Use the intact icon artwork. On phones, the hero copy card sits at the bottom of a viewport-height composition, with some falling pretzels passing behind it. Preserve the existing assets, fast eased entrance, static pattern and motion preferences; the card remains above the products for legibility. Let the hero grow when text or a short viewport requires it.

## People photo 50% enlargement, October 25, 2026

Guy requested the current padding-bleed image be 50% larger. Scale the exact mask/photo to 1.5 times its preceding dimensions, preserving stage/card height and outer rounded-card cropping. Keep the desktop left edge at the image column; center the stacked image horizontally and preserve its top clipping so copy/CTA stay clear. Source geometry and pixels remain unchanged.

## People image through card padding and Ripe Craft headings, October 25, 2026

Guy clarified that the People image remains in its column but ignores padding and crops at the outer card. Extend the exact masked photo through image-side padding without changing reserved stage/card height. Stacked layouts may extend through both side and bottom padding while keeping copy/CTA clear. This supersedes inset-stage clipping in the preceding column-width revision; original mask geometry and photography remain intact.

The three homepage Craft summary headings use Ripe-on-Brown #DC4B33, the existing contrasting dark-surface variant. Their body copy and links remain Cream.

## Full image-column People crop, October 25, 2026

Guy clarified that the People photo should fill its image column, not the whole card. The exact existing mask/photo use 100% of that column without the prior rightward offset. Reserved image-stage and card heights remain unchanged, with vertical centering and clipping confined to the image area. This supersedes preceding percentage scale and horizontal-offset treatments.

## Immediate card imagery, October 25, 2026

Guy removed the drop-in entrances from product/category-card imagery and More to Discover icons. These now appear directly in place at full opacity. Slider/hover effects and the separate hero pretzel entrance remain unchanged; background patterns stay static.

## Consistent display-heading tracking and Cream text, October 25, 2026

All `.heading-title` text, including bold spans, uses the shared -0.055em tracking value previously used by most section headings. Eyebrow tracking remains separate. Authored White text becomes brand Cream #F7EFE6, superseding the preceding White category-copy direction; supplied artwork and background colors are unchanged.

## Compact mobile header and enlarged fixed-height People crop, October 25, 2026

Guy clarified "Keep static patterns": every background pattern remains visible in fixed colors without translation or highlight animation. Preserve the original paths and transforms.

The original mobile header places its full logo above the Menu/contact row. The compact scroll header may use the intact existing standalone Brown brandmark, keeping icon, Menu and Let's Talk on one line. Source geometry and colors remain unchanged; desktop retains the horizontal wordmark. Hero eyebrow uses the existing Ripe-on-Brown variant, with Cream copy/secondary text. Category copy panels become Primary Brown with White text while their image-panel colors remain.

The People masked image grows 50% from the preceding revision inside the same reserved-height area. Vertical centering and clipping may crop more of the exact mask/photo without changing either source or extending the card. Background-pattern movement and color cycling are removed; product entrance and carousel motion remain independent.

## Ripe shadows, smaller People crop and focus treatment, October 25, 2026

Guy restores decorative shadows to website Ripe #B83B28, superseding the Dark Brown direction below. Buttons retain transparent fills and their current structural double borders. Active/focused elements lose rectangular outlines and focus halo shadows; semantic and keyboard focus remain, with text/underline and field bottom-line treatments replacing perimeter indicators. This is a user-directed styling revision, not a conformance certification.

The People display heading wraps naturally without explicit line breaks. The current mask is reduced by 50% and shifted left by 25% of its resulting width; neither photo pixels nor original mask geometry are edited. The supplied `626950-h-media-logo-fyfga.webp` replaces Wegmans' earlier reference image with complete artwork and its original transparency. Shared inquiry labels use the supplied Montserrat 700 weight.

## Dark Brown shadows, transparent buttons and cropped People imagery, October 25, 2026

Guy corrected the decorative shadow token to `--decocoa-brown-dark` (#170905). This supersedes the prior Primary Brown shadow selection while retaining solid offsets, button/card lift and staged submenu motion. Contrasting keyboard-focus separation rings remain distinct from decorative shadows.

Primary and secondary button fills, including the inset rectangle, are transparent in both rest and hover states. Their Orange double borders remain; text uses Brown on light surfaces or Cream on Brown surfaces. The scrolling-header Let's Talk action is a special transparent variant with Primary Brown double borders and text. Retain visible focus and avoid a hover text color that disappears against the underlying surface.

The People paragraph loses its maximum width, and its unchanged photo/mask is doubled in scale with the right half intentionally clipped beyond the shared card's right edge. This directly authorizes the new crop while preserving source artwork and mask geometry. Craft's exterior becomes Orange with Primary Brown motifs; its Brown copy card and Cream text remain.

Inquiry labels, bottom borders and dropdown arrows use Orange on hover/focus, while entered/selected text remains Brown and a separate contrasting focus outline is retained. The same treatment applies to both shared inquiry instances. These are user-directed visual revisions, not a whole-site accessibility certification.

## Borderless homepage cards and Primary Brown shadows, October 25, 2026

Guy requested a shared borderless Cream card for Our People copy and photography, explicitly using the existing `experience-photo` treatment. The unchanged supplied people photograph may now use the exact standalone brandmark silhouette. Preserve the mask geometry and position the photograph to retain the person's face; this supersedes the previous unmasked People-photo direction without changing the header/footer identities.

Our Craft uses one Brown card for all summary copy, with title/introduction/CTA on the left and three FontAwesome-led linked themes on the right; its homepage photo is removed. Experience Center uses a full-container-width borderless Cream card with the supplied factory GIF on the left of its copy/CTA, replacing the chocolate photo. Preserve the GIF's entire illustrated frame and source colors, with a still alternative for reduced-motion preferences.

All decorative shadows previously colored Ripe now use Primary Brown #3A170D. Retain their solid unblurred appearance, up-left hover motion and staged submenu entrance. Ripe eyebrow/link colors and contrasting keyboard-focus rings are unchanged. These scoped directions supersede earlier card borders, separated imagery and Ripe-shadow requirements.

## Larger footer badge and Orange link treatment, October 25, 2026

Guy requested removal of the footer tagline, a larger intact badge logo, Orange footer link hover and an animated 2px bottom line matching the main navigation. Preserve original logo colors/geometry and proportional clear space. Footer text links keep a transparent background; the line grows left to right and also supports keyboard focus. The copyright row has an Orange top divider and legal links that wrap on narrow screens. Reduced motion removes the line transition.

## Diagonal submenu entrance, October 24, 2026

Guy requested that submenus in both headers move up and left, followed by the shadow in the same direction. Apply the shared diagonal panel entry before the hard Ripe shadow appears and moves up-left to its settled offset. Preserve the borderless Cream panels, safe hover path, keyboard controls and static reduced-motion treatment. This replaces the earlier vertical entry and shadow growing from zero.

## Static Orange/Brown hero, October 24, 2026

Guy's subsequent revision replaces the Blush/Cream hero with an Orange background and static Primary Brown source-pattern motifs. Disable all hero-pattern row/highlight animation while preserving original geometry and other sections' animation. The borderless copy card is Brown with Cream text, including its eyebrow, and its single CTA uses the existing secondary button style. Retain enlarged pretzels and their falling entrance. This supersedes the immediately preceding color/button treatment below.

## Blush hero and White copy card, October 24, 2026

Guy directly requested a Blush hero background and Cream pattern. Recolor only the website pattern instance; preserve the faithful source exports and geometry. The copy card is White with Primary Brown text and no border. Its eyebrow uses accessible Ripe for a light surface. One primary CTA reads “Let’s Craft Something Together”. Enlarged pretzels may extend beyond the hero edges after their smooth falling entrance; keep the text and CTA clear. This supersedes the Brown hero, Cream card ring, Orange pattern and two-action treatment in earlier records. Reduced-motion and visibility behavior remain required.

## Header scale and paired headings, October 24, 2026

Guy requested a 360px desktop main-header logo and 1rem Let's Talk type in both headers. Apply the logo width from 1200px, retain proportional clear space and the compact scroll/footer/mobile variants. The horizontal scroll menu fills the middle container with equal gaps, left-aligned labels and underlines starting at the same edge as their text.

Eyebrow/title pairs now share one correctly ranked semantic heading, with separately styled spans for the 1.25rem eyebrow and large display title. Preserve existing IDs, heading hierarchy, colors and visual line breaks. This gives assistive technology one complete section heading and addresses the reported short, large paragraph heuristic without adding redundant headings. Reference: [W3C headings guidance](https://www.w3.org/WAI/tutorials/page-structure/headings/).

## Accessible Ripe, desktop type and linked cards, October 24, 2026

Guy requested an accessible Ripe on Cream and use of the new shade for product Explore hover. The selected website Ripe is #B83B28, with calculated WCAG contrast 4.99258:1 on Cream #F7EFE6 and 5.68444:1 on White. This exceeds the normal-text AA threshold of 4.5:1. Keep original Ripe #DC4B33 for the Brown hero eyebrow, where 20px bold text has 3.89624:1 contrast and exceeds the large-text threshold of 3:1. Artwork retains source colors. Reference: [W3C Understanding Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html). These ratios do not certify the complete site.

Desktop ordinary text and controls use 1.25rem from 1200px up, retaining the 16px root and existing larger headings. Eyebrows and submenu links use 1.25rem throughout. The horizontal scroll navigation expands between logo and CTA with left-aligned links.

Category image panels regain their varied nonprimary palette colors while copy areas remain White. Each full card becomes one anchor; its Explore label and arrow are part of that link and turn the new Ripe on hover/focus, without text or arrow shadows. These changes supersede the all-White image panels and nested Explore-link treatment below.

## Ripe accents and borderless cards, October 24, 2026

Guy's latest direct revision uses Ripe #DC4B33 for eyebrow text and primary/secondary button shadows. Let's Talk CTAs on Cream surfaces use primary styling. Button hover fills the inset rectangle Orange and changes text to Brown while retaining the established concentric double borders and up-left movement. The outer margin between borders keeps its primary/secondary base fill.

Submenus now open on pointer hover as well as click/tap/keyboard, with panel entry followed by shadow entry. Remove their outside border and each anchor's bottom border. The Orange horizontal scrolling navigation returns to Brown text without a group background and uses Cream text/underline on hover. Cream submenu surfaces retain Orange sublink hover.

Our Chocolate cards lose their perimeter and use White backgrounds, with the same Ripe hard-shadow hover lift as buttons. White is explicitly authorized for these cards. More to Discover cards lose their borders and use distinct nonprimary palette backgrounds, with the same hover effect. These directions supersede conflicting border, shadow, color and hover details in the historical revisions below.

## Navigation and buttons, October 24, 2026

Guy's direct revision replaces Blush navigation hover backgrounds with Orange text and a 2px bottom line that grows left to right. Submenus have a restrained entrance, rounded corners and a 2px Primary Brown border; sublinks turn Orange on hover without a background change. Preserve click/tap, keyboard, Escape and focus-return behavior.

Primary buttons now use Cream fill, Primary Brown text and Orange double borders. Secondary buttons use Primary Brown fill, Cream text and Orange double borders. The implementation uses a 12px outer radius, 2px outer border, 4px inner inset from the padding edge and 6px inner radius, producing concentric curves. Both lift 4px up and left over a hard 6px offset Orange shadow; the Orange scrolling header uses a Brown shadow for visibility. The desktop scrolling navigation has a quiet Cream backdrop so Orange hover text stays visible. These implementation choices preserve the requested palette. These instructions supersede the October 11 button colors, radii and hover treatment. Reduced-motion and visible keyboard-focus behavior remain required.

## Our Chocolate category cards, October 24, 2026

Latest direct refinement: the slider is full viewport width with four equal desktop columns, responsive to two/one columns on smaller screens. The intro changes from 600px maximum to a 650px desktop minimum, constrained on mobile. Category hover links now have a hard Primary Brown text shadow with Orange text, no blur and no box shadow/background chip. More to Discover becomes whole-card links with centered icons/headings and a solid Orange hover box shadow. Explore Our Products in the section intro uses the primary button. All eyebrow backgrounds are removed. Guy explicitly removed global/local pause-motion and previous/next buttons; reduced-motion, interaction stops and offscreen/hidden handling remain. These directions supersede conflicting details in the first revision below.

Guy explicitly requested a 2px Primary Brown border around each whole category card, equal image-panel heights, a slow left-to-right row and downward product entrances. This overrides the historical 4px double-ring card treatment for these cards. The section introduction is centered, stacked and limited to 600px.

Category CTA links use Primary Brown text and a FontAwesome right arrow, with an Orange hover treatment and a hard Primary Brown offset shadow. This is a scoped exception to the earlier no-CTA-arrow instruction. Preserve keyboard focus and adequate text contrast. More to Discover uses three large FontAwesome icon cards with downward entrances. Existing source artwork, logos and the remaining button system retain their established treatment.

## Current website brown values, October 24, 2026

Guy's new site-build brief approves Primary Brown / Chocolate #3A170D and Dark Brown #170905. Use separate shared tokens `--decocoa-brown` and `--decocoa-brown-dark`. This supersedes the October 11 website token #512316 as well as the manual's printed #2E2E2E. No clarification is needed. Do not recolor original artwork. Review-phase source is frozen; token implementation follows the agreed review checkpoint.

The historical approvals below remain valid where they do not conflict with this update.

## Historical website brown approval

Source: Guy's October 11, 2026 direction documented in the supplied master brief, accepted as the project plan.

Rule: Manual page 17 prints Chocolate as #2E2E2E.
Approved treatment: Use illustrated Chocolate brown #512316 for website color tokens (RGB 81,35,22; vector fill 0.318,0.137,0.086).
Affected components: All website CSS using Chocolate, including headings, backgrounds, borders, and controls.
Original artwork is not recolored to force a token match.

## Logo icon as a photographic mask

Approval: Guy's direct revision request, October 11, 2026: "Want to start using the logo icon as an image mask as well".

Earlier rule: the working brief prohibited logo-photo masks and required unchanged brandmark treatments under manual pp. 23-24.

Approved treatment: use the exact supplied standalone icon geometry as a photographic mask in homepage imagery. Preserve the original vector outline and proportions. Header identities and the user-requested footer badge remain complete, unmodified and static; the approval does not imply permission to crop or mask the wordmark.

## Pattern backgrounds and motion

Approval: Guy's direct revision request, October 11, 2026: incorporate patterns into section background covers, convert AI patterns to SVG, and allow "pod rows can move slowly or different pods highlight different colors randomly."

Earlier rule: preserve static source colors and avoid unapproved tint/recolor treatments.

Approved treatment: faithful SVG master exports plus website instances with subtle row motion and individual highlights using the established palette. Keep source files unchanged. Preserve pattern geometry and provide static reduced-motion and pause states. No new brand colors or arbitrary alteration of the identity wordmark is authorized.
