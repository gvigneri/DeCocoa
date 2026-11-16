# DeCocoa Content Updates and Shared Component Library

Implement the confirmed content and navigation updates in the existing DeCocoa website. Preserve the current theme, use the approved client copy in this brief verbatim, and build on the existing code to establish a reusable component library across the site.

Reference site: https://gvigneri.github.io/DeCocoa/

This is an implementation brief for the existing repository. Inspect the actual repository before choosing files or implementation details. The reference site establishes the visual baseline; the approved client text in this brief establishes the replacement copy, including the explicitly authorized corrections in section 8. Do not rebuild the site in a different framework or introduce a new UI library.

## 1. Confirmed decisions

1. Preserve the existing theme: typography, palette, brand assets, buttons, image treatments, spacing conventions, and visual character. The approved hero and navigation changes below are the intended layout changes.
2. Every public page must use a full-width orange hero based on the current homepage hero. Desktop layout: text left, imagery right. Reuse the homepage's actual orange token, layout rules, typography, and responsive behavior. Do not select a new orange or reinterpret the design.
3. All 11 chocolate categories belong on one Our Chocolate page, with direct section links. Do not create 11 new category pages.
4. Reuse the existing B2B page for Partner Brands. Add a dedicated Décor page. Present all four business segments under Our Craft → Our Segments.
5. Make each primary navigation label a link to its main page, and provide large image-based dropdown menus on desktop hover. Use the existing theme for these menus.
6. Partner and certification logos link to the corresponding organization's official website in a new tab.
7. Reuse and consolidate existing components, styling, and interactions. Deliver a documented shared component library that can serve every page of the site.
8. Use the approved wording in this brief, including the authorized spelling, grammar, punctuation, and naming corrections. Use Tablet, Drink, and DeCocoa consistently. Preserve all remaining copy verbatim; no additional rewriting is authorized.

### Earlier suggestions superseded by the theme decision

Do not implement site-wide image-border removal, a new button-hover design, or a custom cocoa-pod cursor in this pass. Preserve existing styling outside the approved hero and menu changes. Do not copy Läderach's theme or build a separate visual direction from that reference.

## 2. Inspect and reuse before implementing

- Read the repository's applicable AGENTS.md and project documentation.
- Identify the current framework or static-site approach, build commands, route generation, header/footer assembly, content sources, shared CSS, breakpoints, and reusable JavaScript.
- Inventory every public page, including secondary pages, existing product-detail pages, contact, and legal pages. Apply the shared orange hero across that inventory.
- Identify existing reusable components and classes before adding anything. Extend or extract an existing pattern whenever it supports the required content.
- Record representative desktop and mobile baseline views before refactoring shared components. Use them to preserve unaffected styles.
- Work within the existing repository and build process. Keep GitHub Pages deployment under /DeCocoa/ working, including nested pages, image URLs, CSS, scripts, and hash links.
- Retain existing valid routes and page content unless this brief explicitly supplies a replacement or relocation. Changing navigation placement does not mean deleting a page.

## 3. Shared component library

Use the project's existing component, partial, template, or module mechanism. These are functional responsibilities, not prescribed filenames or framework-specific component names.

| Shared component | Responsibility and configurable content |
|---|---|
| Site header and navigation | One navigation source, logo, utility CTA, main-page links, menu groups, active states, desktop and mobile behavior |
| Image-based menu | Reusable themed menu panel, link groups, optional images, keyboard and touch interactions |
| Site footer | One shared footer with consistent destinations, retained secondary links, legal links, and existing styling |
| Orange page hero | Full-width homepage orange background, existing inner container, eyebrow/page label, heading, optional body copy and CTA, image or composition, alt text |
| Section container | Existing widths, vertical spacing, backgrounds, optional anchor target and heading |
| Image-and-text section | Existing split layout, optional image placement, editable copy and image data |
| Category block and card | Heading, tagline, complete description, imagery, destination, and existing visual treatment |
| Card grid | Existing responsive layout for categories, business segments, values, and related links, using appropriate existing variants |
| Logo collection | Partner and certification images, accessible names, verified URLs, and new-tab behavior |
| Timeline primitives | Date, heading where supplied, body, optional imagery, existing presentation and responsive behavior |
| Section navigation | In-page anchors with the correct sticky-header offset |
| Buttons and text links | Existing variants, styling, focus and hover behavior |

### Implementation rules

- Separate page content and navigation data from shared presentation wherever the existing stack supports it.
- Keep one authoritative copy source for each supplied block. A homepage teaser and an interior page must reuse the same approved source when they display the same text.
- Do not duplicate the hero markup and CSS in every page. Do not duplicate the header, footer, menu logic, or category data.
- Keep reusable JavaScript in shared files or modules. Avoid page-specific copies of the same interaction.
- Consolidate equivalent CSS rules without changing their rendered appearance. Add narrowly scoped rules only when needed for the approved hero or menu behavior.
- Do not create a generic component for every individual sentence. Extract useful repeated layouts and controls with clear responsibilities.
- The family timeline and the existing chocolate-history experience may share underlying components without losing their different content, pacing, or established presentation.
- Add a component catalog in the repository using its documentation convention. Document each component's location, purpose, content inputs, existing variants, example usage, and pages that use it. Include a reusable page composition example. If a component preview facility already exists, update it; do not add a new tooling platform just for this work.

## 4. Hero requirements for every page

- Extract or reuse the homepage hero as the shared base. Preserve the current homepage hero's appearance.
- The orange background spans the full viewport width. Content aligns to the current site container.
- Desktop: text left and relevant existing imagery right. On small screens, use the site's established stacking and spacing conventions, with readable text and no overflow.
- Use semantic HTML text, not text embedded in an image. Preserve the supplied wording through line wrapping and responsive layout.
- Use existing page imagery and brand assets first. Do not generate new imagery or introduce a different art direction. For utility/legal pages without dedicated imagery, use an appropriate existing brandmark or pattern treatment.
- Ensure one semantic H1 per page. Page labels can act as eyebrows when a supplied tagline is the H1.
- Avoid arbitrary page-specific hero heights or new typography scales. Accommodate the actual copy within the shared layout.

| Page | Page label | Hero heading and copy treatment |
|---|---|---|
| Homepage | Existing | Retain the existing "Experience. Chocolate." hero and existing introductory text |
| Our Chocolate | Our Chocolate | "Experience. Chocolate."; do not invent new introductory copy |
| Our People | Our People | "Your Chocolate Crafters"; retain relevant existing introductory body copy where no replacement is supplied |
| Our Craft | Our Craft | "Crafting the Future"; retain relevant existing introductory body copy where no replacement is supplied |
| Experience Center | Existing appropriate label | "Experience Center" with the exact C03 introduction |
| Partner Brands | Partner Brands | "Crafting the Future" with all five opening sentences from C09 |
| Décor | Décor | "Chocolate as Art" with the corresponding paragraph from C08; place the remaining C08 text below the hero |
| Other existing pages | Existing page identity | Preserve the existing page title and relevant body copy unless a specific replacement is mapped below |

The image taglines in C07 are also the source for the homepage's corresponding Our Chocolate, Our People, and Our Craft introductions. Match those section headings to the supplied taglines while retaining the current section styling.

## 5. Navigation and destinations

### Main navigation

| Main label | Main-page destination | Menu contents |
|---|---|---|
| Our Chocolate | /products/ | The 11 category links in C01, in that order |
| Our People | /our-people/ | Existing Our Roots, Our Principals, Our Values, and Sweet Careers destinations |
| Our Craft | /our-craft/ | Promise, Focus, Sustainability, Food Safety, Our Segments, with access to business destinations and Wholesale |
| Experience Center | /experience-center/ | How It's Made, Museum & Virtual Exhibition, Tours and Classes, and Craft Your Own |

Paths in this brief are site-relative; respect the repository's /DeCocoa/ deployment base. Reuse existing paths and anchor IDs where possible.

### Chocolate category anchors

| Menu label, exact | Copy heading, exact | Suggested anchor if a compatible anchor does not exist |
|---|---|---|
| Tablet | Tablet | /products/#tablet |
| Filled | Filled | /products/#filled |
| Covered | Covered | /products/#covered |
| Dipped | Dipped | /products/#dipped |
| Novelty | Novelty | /products/#novelty |
| Drink | Drink | /products/#drink |
| Wellness | Wellness | /products/#wellness |
| Assortment | Assortment | /products/#assortment |
| Snacking | Snacking | /products/#snacking |
| Gifting | Gifting | /products/#gifting |
| Entertaining | Entertaining | /products/#entertaining |

Use Tablet and Drink consistently in the menu, category headings, cards, links, and related copy. Use DeCocoa as the brand spelling throughout editable site text. Reuse existing logo artwork unchanged. Keep valid asset filenames and routes unchanged unless a deliberate route or filename change is required; do not break existing links just to normalize their spelling.

### Business and secondary destinations

- B2C Branded Chocolate (Retail): summary under Our Segments, linking to the Our Chocolate page. Retain the existing Wholesale page and make it accessible from the business area and footer.
- B2B Partner Brands (Private Label): summary under Our Segments, linking to the existing /b2b/ route with C09 replacement content. Update its navigation grouping, active state, relevant links, and breadcrumbs if present to Our Craft.
- Pro2Pro Décor (Chocolate Solutions): summary under Our Segments, linking to a dedicated Décor page. Reuse an appropriate route if one exists; otherwise follow repository conventions, with /decor/ as the proposed route.
- D2C Fulfillment (Logistics Services): full supplied summary in the Our Segments area, with a direct anchor. A separate fulfillment page is not required by this brief.
- Craft Your Own: retain /craft-your-own/ and place its primary menu access under Experience Center. Keep relevant Gifting links.
- Fundraising: retain /fundraising/ and its secondary/footer access. Do not remove the page.
- Gifting: retain /gifting/ as a supporting page. The Our Chocolate dropdown's Gifting item points to the category on the single Our Chocolate page. Use the supplied Gifting tagline and description on the existing Gifting page's hero; retain relevant supporting content.
- Preserve existing contact and legal destinations. Keep contact-topic routing aligned with renamed and moved content without changing form submission behavior.

### Menu interaction

- Clicking a primary label navigates to its main page and shared hero.
- Desktop hover opens the larger image-based dropdown. Reuse current colors, fonts, imagery, borders, and other style conventions.
- Provide an independent submenu toggle for keyboard and touch access so opening a menu does not require following the parent link.
- Support keyboard focus, Escape to close, appropriate expanded states, and a practical focus order. Keep menus open while moving from their trigger into the menu.
- Keep mobile navigation functional without hover. Use existing mobile patterns and avoid hover-only destinations.
- Do not add gratuitous menu copy. Use existing labels and the supplied labels/headlines where available.

## 6. Page-by-page content implementation

### Homepage

1. Preserve the existing hero visually and textually.
2. Update the Our Chocolate introduction and category previews using C01, C02, and C07. Every category must have its full description on /products/. Homepage cards may use the exact heading and tagline with a link; do not invent shortened descriptions or truncate supplied sentences to fit.
3. Move the current business-segment overview out of the Our Chocolate section and into the Our Craft portion of the homepage. Source its four segments from C13 and link to the appropriate destinations.
4. Update the Our People and Our Craft section headings using C07.
5. Keep Connections & collaboration / Our Partners as the partner-logo section and apply C11 in full. The Partner Brands business card must lead to /b2b/, not to the partner-logo section.
6. Use C03 for the Experience Center introduction, preserving its punctuation exactly.
7. Make partner and certification logos functional external links as specified in section 7.

### Our Chocolate

1. Use the shared orange hero and C07 tagline.
2. Render all 11 C02 categories on one page, in the C01 menu order. Each includes its exact source heading, tagline, and complete description.
3. Relocate existing manufacturing-method content, including One Shot Depositing, Hollow Moulding, Mixing, and Dry Filling, to the capabilities material under Our Craft. Preserve useful existing copy and imagery; keep these separate from the 11 consumer categories.
4. Update homepage, menu, footer, and other internal links affected by these moves. Preserve existing external deep links to moved capability anchors with explicit compatibility behavior or an equivalent destination; avoid silently dropping them.
5. Retain existing product-detail routes and useful supporting pages. Apply the shared hero to them without creating new category pages or rewriting unrelated text.

### Our People

1. Use the shared orange hero with "Your Chocolate Crafters".
2. Replace the partial Our Roots story with C04 in full. Retain its supplied subheadings and paragraph order.
3. Add C05 as the family timeline within Our Roots. Keep all five years and complete sentences. This timeline is separate from the chocolate-history timeline in Experience Center.
4. If retaining the existing Our Principals mission, vision, and focus cards, source their sentences directly from C04. They may repeat the source sentences intentionally, but must not contain competing rewritten versions.
5. Replace existing Our Values titles and descriptions with C06, preserving its order.
6. Retain Sweet Careers and its existing content and links.

### Our Craft

1. Use the shared orange hero with "Crafting the Future".
2. Promise: use the first two sentences in C10, beginning "At DeCocoa Chocolate Crafters, we promise...". This is a placement change from the client's source grouping, not a copy edit.
3. Focus: use the complete focus sentence from C04 exactly. Source it once for reuse.
4. Sustainability: use the "How sweet are we" heading and all following C10 sustainability lines. Use Sustainability consistently in navigation and section labels. C10 includes the approved spelling and punctuation corrections.
5. Food Safety: retain the existing detailed section and functionality. Do not replace it with just the short Promise text.
6. Our Segments: use C13 in full, including the introduction and all four complete segment descriptions. Add working links to the detailed destinations.
7. Process & Capabilities: retain C14 exactly, with appropriate existing factory imagery and the relocated manufacturing-method information.
8. Keep the business content distinct from the Our Partners logo collection.

### Partner Brands

1. Reuse /b2b/ for the dedicated Partner Brands content.
2. Replace the generic current B2B introduction and placeholder-like project descriptions with C09 in full.
3. Use the shared orange hero with the C09 heading "Crafting the Future" and all five opening sentences.
4. Render the remaining C09 blocks in their supplied order, including all five What We Do items, the four How We Do It steps, and Built for Growth.
5. Reuse the existing relevant inquiry CTA and form-topic behavior. Avoid inventing promises, certifications, quantities, or capabilities beyond the supplied copy.

### Décor

1. Add a dedicated page using shared components and styling.
2. Use the C08 "Chocolate as Art" heading and its corresponding paragraph in the orange hero, with Décor as the page label.
3. Include the complete introductory C08 paragraph and all remaining C08 copy below the hero. Every supplied sentence must appear; place hero-used copy once unless reuse has a clear purpose.
4. Link the page from Our Craft → Our Segments → Pro2Pro Décor (Chocolate Solutions).
5. Use existing suitable images and inquiry components. Do not invent product data or a new catalog.

### Experience Center

1. Use C03's Experience Center introduction in the shared orange hero.
2. Place C03's exhibition and Green Screen Photo Room sentences under Museum & Virtual Exhibition. Remove the redundant second Experience Center heading currently introducing this museum copy.
3. Use the Tours and Classes block exactly as provided.
4. Preserve the existing How It's Made content and the chocolate-history experience, including their existing assets and animations. Do not replace them with the Vigneri family timeline.
5. Add or retain useful access to Craft Your Own without changing existing inquiry behavior.

### Other existing pages

Apply the shared hero and shared shell to contact, legal, fundraising, wholesale, craft-your-own, existing product-detail pages, and any other public pages found in the repository. Retain unrelated content and functionality. Keep the homepage visually stable except for the mapped content changes.

## 7. Partner and certification links

- Read each actual logo's identity and verify its official organization or program website before assigning a destination. Do not guess URLs or make every logo point to a generic page.
- The reviewed homepage includes Puratos, Wegmans, Chocolate.com, Blue Stripes, Cacao-Trace, Rainforest Alliance, SQF Institute, HACCP, and OU Kosher Dairy. Reconcile this list with the current repository assets.
- Use target="_blank" with rel="noopener noreferrer". Preserve clear accessible names, existing styling, and keyboard focus behavior.
- Maintain one shared data collection per logo group so the same logo and URL pair is consistent wherever reused.
- HACCP describes a system and may not uniquely identify a certifying organization. Determine the actual organization from the asset or project records; if it cannot be verified, report that specific missing destination rather than inventing one. Continue all independent work.

## 8. Approved copy rules

The C01–C14 blocks below are the source of truth for replacement copy. They incorporate the user's explicitly approved corrections. Their labels are implementation identifiers, not additional public copy.

### Approved terminology and corrections

- Use Tablet for both the menu label and category heading.
- Use Drink for both the menu label and category heading.
- Use DeCocoa consistently in editable brand references, including DeCocoa Chocolate Crafters and DeCocoa Decor™. Preserve existing logo artwork, valid asset filenames, and working routes.
- Use Sustainability.
- Use "cobblestoned streets".
- Use "is on a mission to".
- Use "your personalized finished product".
- Use "three generations of confectioners".
- Use "virtual self-guided exhibition".
- Use "an industry-leading chocolate brand".
- Use "Sustainability is more than a goal; it’s our way of doing business."

These changes are already applied to the copy blocks below. Use those corrected blocks verbatim rather than reverting to earlier versions of the client's text.

### Preserve the remaining wording

- Preserve all other words, capitalization, punctuation, spelling, and apostrophes in the approved copy exactly.
- Preserve full sentences and paragraphs. Do not make additional edits, polish, summarize, or generate marketing replacements.
- Presentation-only whitespace and line wrapping may change. Markdown emphasis, bullets, and source separators are formatting, not extra text to display. Zero-width formatting characters may be discarded.
- Keep other source-specific terms, including "Pro2Pro" and "Confection's", as supplied. Record any further wording concerns separately without changing them.
- Do not use implementation instructions, IDs, deferred design notes, or copy questions as public-facing website text.

## 9. Implementation order and acceptance

1. Inventory the repository, public routes, styles, assets, and existing components.
2. Extract or extend the shared shell, orange hero, section primitives, content data, and navigation components while preserving current appearance.
3. Apply the confirmed navigation and destination changes.
4. Implement the page-specific content from C01–C14 and update supporting links.
5. Apply the shared hero to all remaining public pages.
6. Complete the component catalog and page-composition example.
7. Run existing build/check commands and targeted browser verification. Fix regressions introduced by this work.

### Acceptance checklist

- [ ] Every public page in the repository inventory uses the shared full-width orange hero, with desktop text-left/image-right layout and working mobile stacking.
- [ ] The current theme and unaffected component styles remain visually consistent with the baseline; there is no new global border, button, cursor, font, or color redesign.
- [ ] Exactly 11 chocolate categories appear on one Our Chocolate page, in the supplied menu order, with complete verbatim approved copy.
- [ ] Primary labels navigate to their main pages; image-based dropdowns work with pointer, keyboard, and touch. Mobile navigation does not depend on hover.
- [ ] Partner Brands reuses /b2b/ and is grouped under Our Craft; Décor has a dedicated working page; all four business segments appear under Our Segments.
- [ ] Family history and chocolate history remain in their correct separate locations.
- [ ] Every mapped approved source block is rendered fully at its destination. Compare against the corrected C01–C14 blocks in this version. A targeted source-to-rendered-text comparison may normalize presentation whitespace only; it must catch altered punctuation, capitalization, omitted sentences, and unintended rewriting. Tablet, Drink, and DeCocoa are used consistently.
- [ ] Partner and certification links use verified destinations and open in new tabs. Any unresolved logo identity is named explicitly.
- [ ] Existing contact forms, topic routing, secondary pages, legal pages, assets, and established animations still work.
- [ ] All navigation and asset paths work from both the site root and nested pages under /DeCocoa/; anchor targets remain visible below the sticky header.
- [ ] Header, footer, hero, shared layouts, logo collections, and repeated interactions use reusable implementations with documented inputs and actual cross-page usage.
- [ ] The repository component catalog explains how to assemble a new page without copying page-specific markup and CSS.

Use the project's existing test tools. Prioritize the navigation, shared-component behavior, route integrity, exact content, and visual regressions; do not add redundant tests for every static sentence. Report the changed files, component reuse, page coverage, validation results, and any remaining specific issue. Follow the repository's normal delivery workflow and do not publish merely because this brief has been provided.

## 10. Approved client copy source

### C01 Our Chocolate dropdown

```text
Tablet
Filled
Covered
Dipped
Novelty
Drink
Wellness
Assortment
Snacking
Gifting
Entertaining
```

### C02 Chocolate category copy

Arrange these blocks in C01 menu order. Each block contains its source heading, tagline, and complete description.

```text
Tablet
Pure Chocolate. Endless Desire.
Beautifully crafted bars in captivating shapes and designs. Timeless indulgence, made extraordinary.
```

```text
Filled
The Magic Is Within.
Delicate chocolate shells embrace luscious centers, revealing a delicious surprise in every bite.
```

```text
Covered
Wrapped in Chocolate. Made to Crave.
Delicious centers enveloped in velvety chocolate. A perfect marriage of flavor and texture.
```

```text
Dipped
One Dip. Pure Temptation.
Beautifully dipped creations, dressed in silky chocolate and finished to perfection.
```

```text
Novelty
Where Imagination Becomes Chocolate.
Whimsical shapes, exquisite details, and irresistible creations that enchant before the first bite.
```

```text
Drink
Sip Into Something Wonderful.
Rich chocolate creations designed to melt, mingle, and transform every sip into indulgence.
```

```text
Wellness
Indulgence with Intention.
The pleasure of fine chocolate meets thoughtfully chosen functional ingredients. Feel-good indulgence, beautifully crafted.
```

```text
Assortment
A Symphony of Sweet Sensations.
An enchanting collection of flavors, textures, and tempting little discoveries in every bite.
```

```text
Snacking
Little Bites. Big Love.
Irresistible moments of chocolate bliss, made to satisfy cravings and sweeten everyday life.
```

```text
Gifting
Give Chocolate. Share Love.
Beautifully crafted chocolate that speaks from the heart, turning thoughtful gestures into unforgettable moments.
```

```text
Entertaining
Made to Share. Meant to Impress.
Exquisite chocolate creations that spark conversation, bring people together, and make every gathering memorable.
```

### C03 Experience Center

```text
Experience Center
Visit our Craft your own Chocolate Bar and experience a world of chocolate.
Let our Chocolate Crafters introduce you to the art of the chocolatier.
Be sure to craft your own chocolate bar and build your own Gift Box

Museum & Virtual Exhibition
Experience our virtual self-guided exhibition to learn interesting facts about the History of Chocolate and how it is made.
Be sure to experience our Green Screen Photo Room and choose a selection of backdrops to choose from

Tours and Classes
Book for a Factory tour or Chocolate Crafting Classes & tasting sessions and let our Chocolate Crafters introduce you to the art of Chocolate Crafting.
```

### C04 Our Roots and organizational statements

```text
Our Roots
Our story begins in the cobblestoned streets of a Sicilian patisserie, where the Vigneri family first fell in love with the art of confection. In the scent of warm pastries and the flicker of old ovens, a legacy of sweetness began to rise. With hands guided by tradition and hearts full of dreams, the Vigneri name became known for its devotion to the craft.

The Journey to America
Drawn by possibility and passion, The Vigneri Family brought their treasured recipes across the sea, planting roots in Rochester, New York. There, the legacy flourished blending Old World elegance with American spirit.

The Birth of DeCocoa
DeCocoa was born from Vigneri Chocolate as a tribute to the cocoa bean, the soul of chocolate, and to generations of craft and care. From bean to bite, we honor that legacy by creating chocolate that stirs memory, emotion, and delight.

Today,
DeCocoa Chocolate Crafters is on a mission to passionately handcraft the highest-quality chocolates and deliver the sweetest, most memorable experiences to our customers.

Our vision is to be an industry-leading chocolate brand known for craftsmanship, creativity, and care while building a farmers-first, sustainable future through ethical sourcing and responsible practices.
Our focus is to combine passionate people, innovative craft, and sustainable practices to create chocolate with purpose and care
```

### C05 Timeline for our roots

```text
1951- Nonno Gaetano Vigneri opened a pastry shop in Realmonte, Sicily.

1967- Filippo Vigneri moves to America and buys a European Bakery in Rochester, New York.

1971 – Vigneri Confection's brand is registered and Italian Specialties are sold wholesale nationwide.

2014 – Alex Vigneri restructures into Vigneri Chocolate, fulfilling three generations of confectioners.

2024- Alex Vigneri rebrands Vigneri Chocolate into DeCocoa Chocolate Crafters.
```

### C06 Values

```text
INTEGRITY — ACT RIGHT
Be honest. Be safe. Do the right thing.
INGREDIENTS — CHOOSE QUALITY
Use the best. Do good work. Care about the details.
INVEST — GROW TOGETHER
Help each other. Learn. Grow as a team.
INSPIRE — LIFT OTHERS
Be positive. Be helpful. Set a good example.
INNOVATION — PUSH FORWARD
Try new things. Solve problems. Find a better way.
```

### C07 Image taglines

| Source placement | Exact tagline |
|---|---|
| Our Craft Tag Line for image | Crafting the Future |
| Our People Tag Line for image | Your Chocolate Crafters |
| Our Chocolate TagLine for image | Experience. Chocolate. |

### C08 Décor

```text
Décor
Gourmet decorating products catered to the Professional Chef. Artisanal chocolate décor innovations and customizable products serve food service channels; from bakeries to manufacturers.

Chocolate as Art
At DeCocoa, chocolate is craft. Each piece is handmade, shaped by tradition, refined by modern technique. Pure ingredients. Clean design. Honest flavor. A sensory experience in every bite.

Created by professionals, for professionals,
DeCocoa Decor™ offers innovative, customizable, and luxurious chocolate décor from precision ingredients to exquisitely finished decorative expressions.
Rooted in cocoa and inspired by design, our creations reveal themselves in graceful silhouettes, layered color, and refined detail where collaboration awakens creativity and
chocolate becomes an art of emotion.
```

### C09 Partner Brands

```text
Partner Brands

Crafting the Future
We know chocolate. Our work is guided by consumer and market insight.
Our chocolate crafters bring hands-on experience. We develop and test integrated solutions.
The result is chocolate people enjoy.

Driving Your Brand is our mission.
Contract manufacturing, co-packing and fulfillment for private label chocolate goods. We deliver cost-effective
quality, innovation, and all natural ingredients to your personalized finished product; generating added value and widening your profit margins.
Your Brand is our top priority and we ensure your success with unmatched quality products since 1971. Our focus and experience is in mass producing both small batch and high volume production of quality chocolate products created under the strictest industry standards. Vigneri Chocolate sets itself apart with innovative artisan chocolates for the everyday and holiday category.
We have a full range of off the shelf items and the capability to customize the flavor and shape of any finished product to bring excitement to your Private Label needs.

Why Partner with DeCocoa
We do more than make chocolate.
We control the process from idea to delivery.
This means consistent quality.
It means efficiency at scale.
It means a partner that meets you where you sell.

What We Do
•Product Development
•Ingredient sourcing and validation
•Format and tooling support
•End-to-end chocolate production and packaging
•Scalable solutions with consistent quality

How We Do It
Align
We define specifications, volumes, quality standards, and timelines.
Prepare
We review ingredients, allergens, formats, and tooling.
Produce
We manage the full process in our integrated facility.
From blending and refining to molding and packaging.
Deliver
We plan production and support efficient, reliable delivery as you scale

Built for Growth
We source responsibly.
We choose ingredients with care.
We work across the value chain to reduce impact.
Our supply strategies are dependable and flexible.
We scale with you without compromising quality.
```

### C10 Sustainability source grouping

The first two sentences are mapped to Promise. The remaining block, beginning "How sweet are we", is mapped to Sustainability.

```text
Sustainability

At DeCocoa Chocolate Crafters, we promise to craft every chocolate with care, creativity, and integrity.
We always meet the highest standards of quality and food safety so you can taste and trust every bite

How sweet are we
Sustainability is more than a goal; it’s our way of doing business.
We make chocolate with care for people and the planet.
We source cacao responsibly.
We choose only clean label ingredients.
We use eco-friendly packaging.
Our chocolate is made with 100% sustainable hydro energy power from The Niagara Falls.
The result is a lighter footprint and chocolate made with integrity.
```

### C11 Connections & collaboration

```text
Connections & collaboration
Our Partners
Good chocolate brings people together.
Crafting World-Class Chocolate with World-Class Brands, Powered by Exceptional People.
Discover the ingredient specialists and food brands connected to DeCocoa’s chocolate craft.
```

### C12 Original interaction notes and their disposition

These are source notes for traceability, not public copy. The confirmed decisions in section 1 control implementation.

| Original note | Disposition |
|---|---|
| No borders around pics (clean) | Deferred under the confirmed theme-preservation requirement |
| B2B that is now in "Our Chocolate" moves to Our Craft under Our Segments and Pro 2 Pro gets added also for DeCor Our Craft under Our Segments B2B | Implement the approved business hierarchy in section 5; use the exact C13 segment names |
| Simplify the buttons so when you hover over only the outline/line of box bolds (see Laderach) | Deferred; preserve existing button styling |
| Make it When you click on the main Our Chocolate, Our people , Our Craft etc it takes you to a header main pic | Implement main-page links and the approved shared orange heroes |
| Make it When you hover on main button like Our Craft a large drop down appears with image to select from (see Laderach) | Implement image-based dropdowns using the existing theme |
| Can you make the cursor a cocoa pod from the logo instead of an arrow | Deferred; preserve the existing cursor |
| Can the certifications and our partners take to a link of their pages | Implement official website links in new tabs, subject to destination verification |

### C13 Our Key Business Segments

```text
Our Key Business Segments
DeCocoa is a vertically integrated chocolate company.
We operate across the full value chain.
This gives us control, efficiency, and the ability to serve retail, professional, and direct-to-consumer customers.

B2C Branded Chocolate (Retail)
DeCocoa delivers bold, modern chocolate built on craftsmanship and quality.
Each product is developed end to end—from sourcing and formulation to design and story.
This control builds loyalty, strengthens the brand, and supports long-term growth.

B2B Partner Brands (Private Label)
We help brands succeed in chocolate.
We create private-label and co-branded products for retailers, global brands, and startups.
We handle development, production, and packaging—so our partners can grow without manufacturing complexity.

Pro2Pro Décor (Chocolate Solutions)
Our décor division serves professional kitchens and bakeries.
We create chocolate decorations that deliver beauty, consistency, and speed.
Chefs and bakers trust us to elevate desserts while saving time and labor.

D2C Fulfillment (Logistics Services)
Fulfillment powers our ecosystem.
We manage packing, storage, inventory, and shipping.
Our chocolate-specific, temperature-controlled logistics ensure speed, quality, and a smooth path from production to doorstep.
```

### C14 Factory location

```text
Based in Rochester, New York a historic center of food manufacturing
and innovation, our factory continues a legacy of ingenuity,
craftsmanship, and making things with purpose.
```
