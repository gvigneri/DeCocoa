# DeCocoa: Codex Master Brief

Version: 1.1 | Updated: October 11, 2026 | Project owner: Guy Vigneri

## 1. Mission and first deliverable

Act as the planning lead for a DeCocoa homepage prototype. Coordinate a coding agent and a separate design-review agent. Start by experimenting with the hero, then complete the homepage, main navigation, and footer. Deliver a working, responsive mockup for Guy to review after no more than five total design-review sessions.

The final website will be built in WordPress with Elementor. Every design and interaction should have a practical Elementor implementation path.

Creative direction: natural, organic, warm, refined, and distinctly DeCocoa. Use cocoa pods, leaves, chocolate, craft, and the supplied brand patterns thoughtfully. Movement should be light and deliberate.

The supplied wireframes and Bonfire website are guides. Guy explicitly wants a substantial improvement in design. Preserve useful content and structural intent while improving composition, hierarchy, spacing, imagery, navigation, and responsive behavior. Brand guidelines are mandatory unless Guy explicitly authorizes a specific exception.

Do not build interior pages, commerce, checkout, booking, account systems, or production integrations during this phase. Do not publish the site. Product and visitor journeys may be represented as prototype interactions with clearly documented destinations.

## 2. Decision hierarchy

Apply this order when sources disagree:

1. Guy's explicit project instructions and documented exceptions.
2. DeCocoa Brand Manual for visual identity and the supplied original assets for artwork.
3. This brief for scope, process, and implementation constraints.
4. DeCocoa wireframe PDF for content, destinations, and section intent.
5. Bonfire at https://fjujdwrk.elementor.cloud/ for structural inspiration.
6. Agent design judgment for decisions the above sources leave open.

Do not treat a visual treatment in a wireframe as permission to break the manual. Record unresolved contradictions and avoid representing a provisional choice as brand-approved.

## 3. Agent roles and recommended models

These are recommended runtime selections, not a claim that this Markdown file changes any model settings. The launching environment must actually select the models and reasoning levels. Check availability before spawning agents; report any fallback rather than silently substituting it.

| Role | Recommended model | Reasoning | Responsibility |
| --- | --- | --- | --- |
| Planning lead / coordinator | GPT-6 Astra (`gpt-6-astra`) | Extra High (`xhigh`) | Interpret sources, settle routine design and implementation decisions, write shared instructions, delegate work, maintain the review budget, and assemble the handoff. |
| Coding agent | GPT-6.1 Sol (`gpt-6.1-sol`) | High (`high`) | Prepare assets, build the prototype, implement responsive behavior and motion, run functional checks, and apply reviewer corrections. |
| Independent design-review agent | GPT-6 Astra (`gpt-6-astra`) | High (`high`) | Inspect the rendered experience and actual assets against the manual; review visual quality, brand fidelity, responsive behavior, and interaction. Return evidence-based findings. |

Use Astra for a coding task if Sol cannot resolve a concrete complex problem. If Sol is unavailable, Astra is an acceptable coding fallback. If Astra is unavailable, propose GPT-6.1 Sol with High or Extra High reasoning and disclose the change before claiming the requested configuration is active. Never block basic source inventory because a preferred model is unavailable.

The reviewer must be a separate agent from the implementer and must not edit implementation files. Supply the reviewer with the manual, this brief, relevant prototype pages, current render, and previous unresolved findings. Let it assess the result independently of the coding agent's explanation.

No additional agents are necessary by default. Asset preparation belongs to the coding agent. Keep review and revision sequential so the reviewer inspects a stable version. The lead owns shared instructions; the coding agent owns implementation; the reviewer owns review reports.

Model recommendations were checked against official OpenAI documentation on October 11, 2026: https://learn.chatgpt.com/docs/models. Availability and controls can vary by environment. In the documented guidance, Astra is the strongest option for demanding work, while GPT-6.1 Sol offers near-Astra capability at lower cost. The role assignments above are project recommendations.

## 4. Supplied source material and discovery

Locate these files in the actual working project. Do not hard-code paths from a different ChatGPT session or assume that attached files exist in a future Codex workspace.

### Authoritative documents

- `DeCocoa_BrandManual.pdf`: 30 pages; visual identity authority.
- `DeCocoa_BrandManual_Editable.ai`: editable manual source.
- `DeCocoa_BrandManual_OutlinedType.ai`: outlined manual source.
- `Decocoa 2026 Wireframe + Branded.pdf`: 9 pages; homepage and broader content reference.

### Additional supplied assets

- Pattern sources: `DeCocoa_BrandPatterns_All.ai` and individual Circles, FlowerOfLife, Growth, Luxury, Rings, and Stripes `.ai` files.
- Pattern previews: `DeCocoa_Circles_Pattern.jpg`, `DeCocoa_FlowerOfLife_Pattern.jpg`, `DeCocoa_Growth_Pattern.jpg`, `DeCocoa_Luxury_Pattern.jpg`, `DeCocoa_Rings_Pattern.jpg`, and `DeCocoa_Stripes_Pattern.jpg`.
- Logos: RGB Black Badge, Brandmark, Horizontal, and Vertical `.ai` files; CMYK master and Black, DarkBG, LightBG, and White variants in the supplied lockups.
- Mockups: `BagMockup.psd`, `Cap1.psd`, and `ChocolateBar.psd`.

In the preparation workspace, the four documents appeared in `upload/`, and additional assets appeared in `project_sources/` with numeric filename prefixes such as `08-` and `35-`. Some source filenames spell Horizontal as `Horiztonal`; match actual filenames and preserve them in the source manifest.

The six pattern JPGs were verified present and readable at 4800 × 2700 pixels, RGB, despite earlier missing-path messages. Recheck paths in the new workspace before declaring them missing. No `.ttf`, `.otf`, `.woff`, or `.woff2` files were found in the supplied workspace.

Sample AI files were confirmed PDF-compatible, including the six-page combined pattern file. This does not mean every AI asset or PSD has been fully inspected or exported. Inventory and validate each asset actually used.

### Source handling

Preserve originals. Prefer the dedicated logo and pattern sources over extracting artwork from manual pages. Use the manual only when a standalone source is unavailable. Do not redraw logos, trace a poor raster when a vector exists, or use image generation to reproduce brand artwork.

Render each selected export and compare it with the original. Check colors, proportions, clipping, transparency, bounds, strokes, and any outlined lettering. Export browser-ready SVG where faithful conversion is possible, with PNG fallbacks if necessary. Renaming an `.ai` file to `.svg` is not conversion.

Use color-managed conversion for CMYK assets and log the source profile and conversion when available. Do not manually recolor a logo to resolve a palette discrepancy. Do not assume a full-page JPG is a seamless repeat tile; test pattern edges before tiling.

## 5. Brand rules extracted from the manual

Page numbers below are one-based PDF page numbers. The manual remains the source of truth; inspect the visual pages as well as extracted text.

### Color system: page 17

| Name | Classification | Website HEX |
| --- | --- | --- |
| De Cocoa Orange | Primary | `#E87933` |
| Chocolate | Primary | `#512316` (illustrated brown, approved direction) |
| Cream | Primary | `#F7EFE6` |
| Sunrise | Secondary | `#FFBE4A` |
| Leaf | Secondary | `#327D4F` |
| Fresh | Secondary | `#A0B65C` |
| Blush | Secondary | `#F2C9C1` |
| Ripe | Secondary | `#DC4B33` |

**Resolved color direction, October 11, 2026:** Guy explicitly chose the illustrated brown over the printed charcoal HEX. Use `--color-chocolate: #512316` throughout the website. This digital value is derived from the actual vector fill on manual page 17: RGB fractions `0.318, 0.137, 0.086`, rounded to 8-bit RGB `81, 35, 22`. It is source-derived, not an estimate from a screenshot. The manual prints `#2E2E2E`, but that value is superseded for this project. Record Guy's instruction in `brand/brand-exceptions.md`; do not ask him to choose again. Preserve supplied logo artwork and color-manage exports. Separate CMYK artwork can convert to slightly different RGB values; flag material differences rather than silently recoloring the logos.

Build the base page around the primary colors. Use secondary colors selectively for botanical details, accents, and purposeful sections. The visual balance is a design recommendation, not a quantified brand rule. Do not add arbitrary browns, beiges, gradients, or new UI colors. Use black/white logo variants in their approved contexts. Test contrast using actual combinations; choose another approved pairing if a combination fails.

### Typography: pages 19-21

- Consumer-facing headline choices on page 19: Montserrat Bold, Montserrat Light, and Susa Regular.
- Body choices: Montserrat Regular and Montserrat Light.
- Proposed website default: Montserrat Bold for the main hierarchy, Montserrat Regular for body and controls, and Montserrat Light for selected large supporting text. Use Susa Regular sparingly as an expressive accent only when a properly licensed webfont is available.
- Page 21 names Avenir Bold, Light, and Book as fallback/system typography. Do not assume Avenir is installed on every visitor's device or available for web embedding merely because the manual describes it as a system font.
- Obtain legitimate webfont files or an authorized delivery method. Do not extract embedded PDF font subsets and treat them as licensed webfonts. Document actual loaded weights and avoid synthetic bold or light styles.
- The wireframes use visible serif headings. Those headings do not override the manual. Do not carry that serif style into the site without an explicit exception from Guy.
- If Susa is unavailable, proceed with approved Montserrat choices and record the missing accent font. If Montserrat cannot be loaded, treat typography as provisional and do not pass brand typography review until resolved.

### Logos and clear space: pages 3-7 and 23-24

- The brandmark combines six cocoa pods into the Flower of Life, representing creation, connection, unity, balance, harmony, and responsibility (page 3).
- Use supplied light-background, dark-background, white, or black variants as appropriate (pages 4-7).
- Use page 23's clear-space construction. The standalone brandmark uses the illustrated X measure; badge, vertical, and horizontal logos use Y. Inspect the diagram and measure against the relevant artwork. Do not invent a universal pixel margin or percentage and call it the official rule.
- Page 24 prohibits rotation, stretching, squishing, changing logo colors or font, rearranging elements, placing the logo on a pattern, and inserting the full logo into a sentence or headline.
- Keep header/footer logos on solid, quiet backgrounds with clear space. Do not animate the logo or use its components as independently moving decorative objects. Botanical motion must use separate decorative artwork.
- Do not crop the brandmark into a photographic mask simply because the wireframe does so; confirm any such treatment against the manual or obtain an explicit exception.

### Patterns: pages 8-14

Use the supplied six pattern families. Control their placement, visual density, and scale so content stays readable. Use source colors and approved treatments; do not silently recolor or distort the pattern. Record any proposed tint or opacity treatment as a design proposal if it is not shown in the manual. Never place a logo directly over a pattern.

### Brand exceptions

Keep `brand/brand-exceptions.md`. Each exception needs the exact rule, the requested treatment, Guy's explicit approval, and the affected components. Seed it with the October 11, 2026 approval to use the illustrated Chocolate brown, represented by source-derived `#512316`, instead of printed `#2E2E2E` for website color tokens. An agent's aesthetic preference is not approval.

## 6. Homepage content and navigation

Wireframe pages 1-2 are homepage references. Pages 3-9 help explain destinations and voice; they do not expand the build scope.

### Starting navigation

- Our Chocolate
- Our People
- Our Craft
- Experience Center
- Let's Talk

The Our Chocolate submenu references Products, Gifting, Craft Your Own (Chocolate Bar and Basket), Fundraising, Wholesale, and B2B. Preserve these as candidate destinations. Document possible Wholesale/B2B overlap rather than inventing a distinction. Do not create working commerce flows during this phase.

Design desktop and mobile navigation deliberately. Dropdowns must open through click/tap and keyboard interaction, with visible focus, appropriate expanded state, Escape handling, and predictable focus return. Mobile menu state and scrolling must behave correctly. Hover may supplement interaction but cannot be the only way to open a menu.

### Homepage section intent

| Section | Reference intent | Design direction |
| --- | --- | --- |
| Hero | Page 2 uses “Experience. Chocolate.” and “Experience With Us.” | Use these as source copy to test first. Create a stronger composition with readable typography, a clear CTA, product appetite, and restrained botanical details. |
| Our Products | Product imagery, capability-style cards, “Take a Bite.” | Create a clear product introduction; flag that One Shot Depositing, Hollow Moulding, and Mixing are process/capability labels rather than necessarily product categories. Do not fabricate a final taxonomy. |
| Our People | Human story and “Meet Us.” | Give the family, people, and craft narrative space and authentic imagery. |
| Our Partners | Partner marks | Use supplied reference marks provisionally; request confirmation of current relationships and approved assets before production. |
| Our Process | Craft/process introduction, “Learn With Us.” | Make the process understandable and visually engaging without copying the oversized logo-mask treatment. |
| Certifications | Trust marks | Use only verified supplied marks in their proper form; flag currency and usage approval for confirmation. |
| Experience Center | Visitor experience, “Visit Us.” | Distinguish the in-person experience from product browsing and provide a clear next step. |
| Let's Talk | Contact invitation/form | Design clear fields, labels, validation, and a prototype response. Do not transmit data. |
| Footer | Social/contact, Customer Service, About Us, Legal | Improve hierarchy, spacing, and mobile layout while retaining useful destinations. |

Sections may be reordered or combined when it improves the story. Explain significant changes briefly in the handoff. Avoid excessive carousels and repetitive split panels. Do not duplicate partner marks simply to fill a row.

The reference footer includes Contact Us, Accessibility Statement, FAQ, Jobs & Career, Corporate Gifts, Terms & Conditions, Privacy Policy, Cookie Policy, and Legal Notice. Treat these as planned destinations, not completed pages. Correct obvious typos such as “Customer Rervice” and “Inquary reason.”

Do not promote placeholder phone numbers such as `+585 000 0000` into real contact information. Mark contact details, social destinations, partner/certification status, booking availability, and unverified claims for confirmation. Source copy about sourcing, sustainability, food safety, or operating status is draft content until approved; do not embellish it with invented claims.

Use short, natural, customer-facing copy. Avoid em dashes and the words “streamline,” “seamless,” and “enhance.” Keep proposed copy changes visible in the handoff.

## 7. Hero and motion direction

Develop a clear hero direction before expanding the page. Explore compositions internally, choose the strongest brand-consistent option, and bring that option into the review loop. Do not consume separate reviewer sessions for many speculative variants.

- Emphasize whitespace, considered scale, appetite, material texture, and a strong headline/CTA relationship.
- Combine separate cocoa pod or leaf artwork with chocolate/product imagery when suitable assets are available. Use supplied assets first. If new imagery is needed, document its provenance and distinguish illustrative concepts from actual products or facilities.
- Keep botanical decoration away from the headline, controls, and logo clear space.
- Animate only decorative artwork. Favor small, slow transforms with restrained easing. Avoid bouncing, rapid spins, aggressive parallax, scroll hijacking, and heavy animation dependencies.
- Start with a brief entrance or one finite gentle sway, then settle. If continuous automatic movement lasts over five seconds alongside content, provide an accessible pause control and respect its saved state.
- Respect `prefers-reduced-motion`; show a composed static layout. A user must never need animation to understand the page.
- Keep the static mobile hero strong. Reduce or omit decoration when space is limited. Prevent horizontal overflow and layout shifts.

New illustration style, animation timing, spacing, and composition are design decisions. They do not authorize new logo treatments, fonts, or colors.

## 8. Implementation approach and Elementor handoff

Inspect the supplied repository and instructions before choosing tooling. For a new isolated mockup, default to portable HTML, CSS, and minimal JavaScript. Do not add React, a UI framework, or a component library solely for convenience. If the established project already uses a framework, keep the design transferable and document its Elementor equivalents.

Represent the page as reusable sections with scoped styles and shared tokens for approved colors, typography, spacing, container widths, and responsive behavior. Keep text editable and separate from decorative imagery.

Create an Elementor mapping for each section identifying:

- Container structure and flex/grid intent.
- Native widgets and any Elementor Pro dependencies.
- Global color/type assignments and shared styles.
- Responsive stacking and visibility behavior.
- Custom CSS/JavaScript required, its scope, and how reduced motion works.
- Source assets and recommended export formats.

Do not assume Elementor Pro is available. Identify dependencies and alternatives. An HTML/CSS mockup is not an importable Elementor template; do not claim otherwise. Native Elementor assembly or a tested import package is a later deliverable unless Guy expands the scope.

Use semantic headings, accessible names, meaningful image alternatives, decorative empty alt text where appropriate, visible keyboard focus, and legible type. Measure text and UI contrast against WCAG AA criteria; this is an implementation check, not a legal compliance certification. Optimize image dimensions and formats without compromising the logo or artwork. Keep links and form interactions honest about prototype status.

## 9. Working project structure

Create these folders as needed. These are deliverables for the implementation phase, not assets already extracted by this brief.

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Concise shared scope, ownership, source hierarchy, and five-review cap; link to this master brief. |
| `brand/source/` | Preserved original manuals and artwork. |
| `brand/brand-rules.md` | Verified rules with page references and provisional decisions. |
| `brand/brand-exceptions.md` | Explicitly approved exceptions. |
| `brand/asset-manifest.md` | Source filename, variant/artboard, export filename, dimensions, color mode, usage, and validation status. |
| `assets/logos/` | Validated web logo exports. |
| `assets/patterns/` | Validated pattern exports. |
| `assets/illustrations/` | Separate botanical/decorative artwork. |
| `assets/images/` | Product, people, process, and experience imagery. |
| `assets/fonts/` | Authorized webfont files and license/source notes. |
| `references/prototype-screens/` | Wireframe source and useful reference renders. |
| `references/bonfire/` | Confirmed URL `https://fjujdwrk.elementor.cloud/`, dated screenshots, and structural observations once reviewed. |
| `prototype/` | Working homepage and supporting source. |
| `reviews/` | Session reports, screenshots, review ledger, and issue status. |
| `handoff/` | Run instructions, Elementor map, final screenshots, unresolved items, and copy notes. |

Keep source originals distinct from optimized exports. Use stable, descriptive filenames and relative asset paths. Preserve an existing repository's conventions when they already serve these purposes.

## 10. Five-session review contract

Maximum: five total design-review sessions across the hero and complete homepage, before Guy's review. This is a ceiling, not a required quota.

A session means one independent reviewer invocation against a named, frozen implementation version. Desktop/mobile views in that same invocation form one session. A new reviewer pass after changes consumes the next session. Renaming a review “verification,” “QA,” or “hero check” does not exempt it. Count a launched reviewer session even if it returns incomplete; report the limitation rather than hiding retries.

Initialize the ledger at 0/5. Source inventory, implementation self-checks, and preparation of this brief are not independent design-review sessions. Do not run an uncounted aesthetic review through the coordinator after the cap.

Suggested allocation:

| Session | Focus |
| --- | --- |
| 1 | Hero, header, brand fidelity, and initial responsive direction. |
| 2 | Complete homepage, navigation, footer, and narrative flow. |
| 3 | Desktop/tablet/mobile behavior, keyboard interactions, and motion. |
| 4 | Remaining corrections and page-wide consistency. |
| 5 | Final inspection of the version to hand to Guy. |

Consolidate findings per session. Prioritize brand violations, broken interactions, inaccessible content, and major layout failures ahead of optional polish. The coding agent applies corrections before the next session. Stop early once criteria are met.

At the end of session five, stop the review loop and hand over the reviewed version with unresolved findings. If an essential fix is made afterward, disclose that it has not had another independent design review. Never start session six without Guy explicitly changing the cap.

### Review evidence and report format

Review the rendered page, not just source code. Use 1920 × 1080 for the primary desktop view, a 1440-pixel-wide desktop check, tablet around 768 pixels, and mobile around 390 pixels. Also check 320-pixel width for overflow. Inspect full-page flow and important viewport details; exercise menus, focus, form states, and motion/reduced-motion modes.

Each review report must identify the session number, implementation version/commit, viewports, assets/fonts loaded, tested states, findings, and verdict. Each finding needs:

1. Stable issue ID and category: brand, design, interaction, responsive, accessibility, or content.
2. Severity: blocker, major, or minor.
3. Exact section/element and screenshot or reproducible evidence.
4. Relevant manual page when it is a brand finding; label subjective preferences as design judgment.
5. Specific requested correction and status on the next review.

If the reviewer cannot see rendered screenshots or operate the page, report the limitation. Do not claim a visual or interaction pass based on code inspection alone.

## 11. Acceptance criteria and delivery

- Complete homepage, navigation, and footer; no accidental interior-page scope expansion.
- Typography and colors follow verified rules, including the approved illustrated Chocolate brown (`#512316`); any missing fonts are disclosed.
- Logos preserve approved geometry, colors, background treatment, and clear space.
- Patterns and photography support the page without reducing readability.
- Hero remains attractive and understandable when animation is disabled.
- Desktop and mobile hierarchy are intentional; no clipped content or horizontal scrolling.
- Menus work with pointer, touch, and keyboard; focus behavior is clear.
- Contact UI has labels and useful feedback; no real submission or deceptive success state.
- The design improves on the wireframes without copying their unapproved serif typography or questionable logo masks.
- Assets are organized and traceable; the Elementor mapping is practical.
- Review count is recorded and does not exceed five.

Hand Guy the working preview and source, organized web assets, desktop/mobile screenshots, Elementor section map, concise review summary, and a clearly prioritized list of unresolved items. State the actual models used, sessions consumed, and anything not verified. Do not describe an unresolved brand discrepancy as approved or the prototype as production-ready.

## 12. Startup sequence and open inputs

When Guy supplies this file to Codex to begin implementation:

1. Read this brief and existing repository instructions. Confirm the initial deliverable is the homepage prototype.
2. Locate and inspect sources; build the asset inventory and extract brand rules before designing. Review the confirmed Bonfire reference at https://fjujdwrk.elementor.cloud/ for structure, navigation, reusable section patterns, and footer organization.
3. Confirm actual agent model selections and establish file ownership and the 0/5 review ledger.
4. Create shared instructions and approved design tokens; label unresolved decisions.
5. Prepare the hero, run the first counted review, and continue through the full homepage within the remaining budget.
6. Deliver the first mockup to Guy at or before session five. Do not publish it.

### Confirmed decisions

- **Bonfire URL:** https://fjujdwrk.elementor.cloud/ is the reference supplied by Guy. Use it as a structural guide while improving the design and applying DeCocoa branding. A text-fetch attempt during brief preparation timed out; no visual audit of Bonfire has been completed as part of this brief. Inspect it in the implementation environment, and report an access limitation if it remains unavailable. Do not guess a substitute site or claim it was reviewed.
- **Chocolate color:** Guy chose the illustrated brown. Use source-derived `#512316`; the printed charcoal value is superseded. This decision is settled.

### Remaining inputs

The following inputs remain open. They do not prevent source preparation or drafting the mockup:
- **Fonts:** Obtain authorized Montserrat webfonts/delivery and Susa Regular if used. No standalone font files were supplied in the inspected workspace.
- **Final content/assets:** Confirm real contact/social links, current product categories, approved partner/certification marks, suitable photography, and Experience Center availability before production.
- **Build environment:** Identify the target repository or prototype workspace. Confirm Elementor edition and site access when native WordPress implementation begins; access is not required for the standalone mockup.

Ask only focused questions that affect the current step. Continue useful work while awaiting answers. Do not repeatedly request approval for routine, reversible implementation choices already covered by this brief.
