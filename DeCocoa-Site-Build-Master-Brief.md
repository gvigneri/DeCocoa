DeCocoa Site Build: Master Brief and Codex Tasks
Date: October 24, 2026
Project owner: Guy Vigneri
Target platform: Existing WordPress / Elementor project
First milestone: Homepage and shared site components
Full scope: Homepage, main pages, and their approved subpages
1. Start here
We are moving DeCocoa from prototype exploration into the actual website build. The project, homepage, assets, and theme are already in place according to the project owner. Inspect that implementation and improve it. Do not restart the project or create a separate prototype application.

The primary visitor goal is:
Explore our products and get more information on how to work with us.

Use this brief to coordinate four reviewers, consolidate their findings, and then have one implementation owner build the agreed changes. The output must be one actionable backlog, followed by the implemented website and verification results. Four disconnected reports do not satisfy the brief.

This document replaces earlier prototype-first instructions where they conflict. Bonfire may remain a structural reference, but DeCocoa's current implementation, approved content, and brand rules take precedence. Do not copy Bonfire's visual identity or let an old reference dictate unnecessary changes.
Evidence boundary
This brief was prepared from the owner's current instructions and the supplied brand manual and asset filenames. The current website source, WordPress configuration, and rendered pages were not supplied with these attachments and have not been audited for this brief. The previous wireframe PDF is also absent from this attachment set. Find these in the actual project before drawing conclusions about its pages or implementation.

The tasks below are implementation instructions, not claims that defects were observed or that pages were already built. Do not treat a historical preview URL as the current baseline without checking it against the project configuration.
2. Shared brief
Item	Direction
Audience	People exploring DeCocoa products and people considering working with DeCocoa. Determine any specific customer or business segments from approved project content.
Primary action	Explore Our Products leading to the actual product overview.
Secondary action	Work With Us leading to useful information about working with DeCocoa, with a clear inquiry route.
Success	Visitors understand the offering, find relevant products, and understand how to make an inquiry without guessing or encountering dead ends.
Visual direction	Natural and organic in appearance, with restrained cocoa-pod and leaf illustration or motion where suitable. This is an aesthetic direction, not permission to make organic-product or sourcing claims.
Preserve	Working theme and project structure, approved assets and copy, successful homepage sections, existing useful URLs, and functioning integrations.
Improve	Clarity, product discovery, page hierarchy, shared components, responsive behavior, accessibility, and maintainability.
Scope boundary	Build the informational and inquiry journey. Do not add checkout, accounts, wholesale portals, or new business offerings unless already established in the project or explicitly approved. Preserve existing working commerce functionality if present.


Use direct, friendly language and “we” phrasing where appropriate. Avoid exaggerated benefits, vague superlatives, em dashes, and the words “streamline,” “seamless,” and “enhance.”
Content rules
- Use existing approved copy, product records, and client-provided information as the factual source.
- Separate existing approved copy from proposed revisions in the review package.
- Do not invent product varieties, ingredients, allergens, certifications, sourcing practices, production methods, customer names, testimonials, years in business, minimum orders, delivery times, or partnership capabilities.
- Packaging mockups are design assets. Their text and imagery do not establish that a product or service is available.
- Record missing facts in a content-gap list with the page, information needed, owner, and effect on completion.
- Draft around missing facts where possible. Keep unresolved placeholders internal and exclude them from public navigation and launch-ready pages.
- Do not leave approved main pages and subpages as empty shells and call the site complete.
3. Team and ownership
Role	Responsibilities	Required handoff
Lead / coordinator	Own the brief and baseline; assign review scope; reconcile conflicts; protect useful existing work; prioritize dependencies; maintain the single backlog.	One prioritized plan, decisions, content gaps, and implementation sequence.
Messaging reviewer	Check what DeCocoa offers, who the content addresses, product explanation, headlines, page flow, and calls to action. Identify unsupported claims.	Findings tied to exact content and locations, with proposed copy only where facts support it.
Design reviewer	Review brand fidelity, typography, palette, imagery, patterns, spacing, and consistency. Define a small reusable style system.	Findings and a recommended style/component specification grounded in the current site.
UI/UX reviewer	Review navigation, hierarchy, product discovery, mobile behavior, page relationships, and the path to inquiry.	Findings with steps to reproduce confusing or broken journeys and proposed changes.
Accessibility reviewer	Combine automated checks with manual checks of structure, keyboard use, focus, contrast, text alternatives, motion, and forms.	Evidence, affected interaction, relevant criterion where applicable, and testable correction.
Implementation owner	Implement only the consolidated, agreed plan in the existing project and Elementor. Own shared components and code changes.	Working pages, changed-file/template list, and verification evidence.


The coordinator may also be the implementation owner. This does not require a sixth concurrent agent.
Collaboration rules
1. Establish a single baseline before reviews: commit or source snapshot, staging URL, WordPress page/template identifiers where available, and timestamp. Note unsaved or uncommitted changes without overwriting them.
2. Give all four reviewers the same brief, page inventory, approved assets, and baseline. Begin with the homepage plus its shared header, footer, and linked product/inquiry paths.
3. Reviewers are read-only. They must not edit source, WordPress content, Elementor templates, styles, settings, or shared files.
4. Reviewers may work in parallel when independent read access is available. If they share one browser session, serialize browser interaction or assign separate tabs/sessions so actions do not interfere.
5. Each reviewer returns concise structured findings to the lead. The lead alone writes the consolidated plan.
6. Label unavailable checks Blocked or Not tested, with the reason. Do not substitute assumptions or a scanner score for observed behavior.
7. The lead removes duplicates, resolves contradictory recommendations, and separates confirmed defects from proposed improvements.
8. Present the consolidated changes, revised page flow, and key copy decisions to Guy before implementation, as requested. Prepare the concrete review package first. Previously approved decisions do not need approval again.
9. After approval, one implementation owner makes changes. Reviewers can inspect a stable implementation milestone, but do not make competing edits.
10. If separate agents are unavailable, perform the four review passes sequentially against the same baseline and disclose that limitation.
4. Site structure and page coverage
First inventory the pages, navigation, content, and wireframes already present. Preserve existing page names and URLs when they work. Use the structure below as a planning starting point, not as a verified inventory or instruction to invent content.
Page type	Purpose	Scope rule	Main next step
Homepage	Explain the offering and introduce both visitor paths.	Required first milestone.	Explore Our Products; Work With Us.
Products overview	Present the approved range clearly.	Required; retain the existing route where practical.	Open a relevant category or product.
Product category	Organize a meaningful group of products.	Build for each approved category when grouping helps visitors; skip an unnecessary intermediate layer.	View product details.
Product detail	Explain a specific product with approved imagery and information.	Build every approved product page in scope using a reusable layout.	Make a relevant inquiry or use an existing approved purchase action.
About / Our Story	Explain DeCocoa using verified company information.	Use the existing equivalent; include when supported by the approved sitemap/content.	Explore products or learn about working together.
Work With Us	Explain supported ways to work with DeCocoa and how to begin.	Required content destination; it may improve an existing equivalent page.	Start an inquiry.
Work With Us subpage	Explain a distinct, established offering or audience journey.	Build only for offerings evidenced in approved content. Do not invent wholesale, private label, gifting, or other programs.	Relevant inquiry.
Contact / Inquiry	Provide the existing approved contact route or form.	Use an existing page or integrate the inquiry into Work With Us if that is clearer. Avoid duplicate forms without a reason.	Submit an inquiry successfully.
Supporting pages	Maintain privacy and other existing required information, plus a useful not-found page.	Preserve existing content; request missing business/legal facts instead of inventing them.	Recover navigation or find information.


Every main page and subpage must have a row in the final inventory with: title, URL, parent, page/template ID, purpose, source content, primary CTA, status, and blockers. Reconcile the final built pages against this inventory.
Homepage content sequence
Map the existing homepage into this sequence and retain sections that already serve it well. This is a flow to evaluate, not a requirement to replace every section.
1. Shared header: Recognizable brand, short navigation, product access, and a clear Work With Us route.
2. Hero: A clear statement of what DeCocoa offers, concise supporting copy, approved imagery, and the two main CTAs. Visitors should not need to scroll or wait for animation to understand the offering.
3. Product introduction: Useful approved product or category options with specific labels and descriptive links.
4. DeCocoa story or approach: A brief, factual explanation that supports the product presentation, with a link to fuller content if available.
5. Working with DeCocoa: Explain established options and the first step in a business relationship. Avoid presenting a bare contact button without context.
6. Supporting content: Include existing useful answers, evidence, or additional product information only where it helps a visitor decide. Do not add testimonials or claims to fill space.
7. Closing CTA: A concise invitation to explore further or start the relevant conversation.
8. Shared footer: Secondary navigation, approved contact details, and existing policy links.
Use clear CTA labels consistently. “Learn More” should not be the only explanation of where a link goes. Maintain access to both visitor paths throughout the site without repeating every CTA in every section.
5. Brand requirements and approved color updates
Sources: DeCocoa_BrandManual.pdf, particularly pages 17, 19, 21, 23, and 24, plus Guy's approved brown values supplied October 24, 2026. Numeric prefixes in the supplied attachment filenames are upload labels, not required project naming.
Colors
Use the following approved website palette. Guy confirmed Primary Brown as #3A170D and added Dark Brown as #170905. These values take precedence over the manual's printed Chocolate value and resolve the earlier color discrepancy. The remaining values come from page 17 of the manual.
Brand color	Approved HEX	Website role
De Cocoa Orange	#E87933	Primary
Primary Brown / Chocolate	#3A170D	Primary brand brown; headings, body text, and primary brown surfaces.
Dark Brown	#170905	Deeper background, footer, and interaction-state option where appropriate.
Cream	#F7EFE6	Primary
Sunrise	#FFBE4A	Secondary
Leaf	#327D4F	Secondary
Fresh	#A0B65C	Secondary
Blush	#F2C9C1	Secondary
Ripe	#DC4B33	Secondary


Approved correction: Replace the previous #2E2E2E Chocolate token with #3A170D wherever it represents the brand brown. Add #170905 as a separate Dark Brown token. Do not globally replace unrelated neutral colors or alter the original source artwork. No further color clarification is needed.

Define these values once in the existing shared style system and map them to Elementor global colors:
--decocoa-brown: #3A170D;
--decocoa-brown-dark: #170905;
Use Cream for readable text on either brown background. The two browns are too similar in luminance to serve as a readable foreground/background pair or as the sole distinction for an essential control boundary or focus indicator.

Use a restrained selection of approved colors for each page. The entire palette does not need to appear in every section. Create semantic tokens for text, surface, accent, border, action, and focus, and test actual pairings.

Calculated contrast examples using the approved sRGB values:
Pairing	Approximate ratio	Use implication
White on De Cocoa Orange	2.91:1	Fails the 4.5:1 normal-text and 3:1 large-text thresholds.
Primary Brown on De Cocoa Orange	5.51:1	Passes normal-text contrast using these exact colors.
Primary Brown on Cream	14.10:1	Strong body-text pairing; the reverse pairing also passes.
Cream on Dark Brown	17.11:1	Strong text pairing for dark sections and the footer.
Dark Brown on De Cocoa Orange	6.69:1	Passes normal-text contrast using these exact colors.
Primary Brown against Dark Brown	1.21:1	Insufficient for readable text or an essential visual indicator by itself.
Leaf on Cream	4.41:1	Fails normal-text contrast; do not round it up to a pass.


These are planning checks of solid colors, not results from the current website. Test rendered text, overlays, opacity, hover/focus states, and image backgrounds separately.
Typography
- Page 19 identifies Montserrat Bold, Montserrat Light, and Susa Regular in the headline-font section, and Montserrat Regular and Light for body copy.
- Establish a readable hierarchy from these approved families. Prefer Montserrat Regular for sustained body copy and navigation. Use Susa selectively where the existing approved direction supports it and it remains legible.
- The manual also lists Avenir as a fallback on page 21. Do not assume it is installed on every visitor's device or that font redistribution rights are included.
- Check available font files and web licensing. If a font is missing, document the gap and use a deliberate temporary fallback. Do not introduce an unrelated brand typeface.
- Define sizes, weights, line heights, content widths, and mobile behavior once in the shared style system.
Logos, illustrations, and assets
- Use supplied logo variants suitable for light or dark backgrounds. Preserve proportions and the clear-space rules illustrated on page 23.
- Page 24 prohibits rotating, stretching, recoloring, changing the font, rearranging logo elements, placing the logo on a pattern, or embedding the full logo in a sentence/headline.
- Keep the logo stationary. Decorative pod/leaf motion must not distort or animate the logo itself.
- Use existing web-ready exports first. Source assets include AI logo files, six pattern families in AI/JPG formats, and PSD mockups. Do not serve AI or PSD source files as page images.
- Export only missing web assets, preserving original source files. Verify color, crop, proportions, and transparency. Sanitize SVG exports and remove unnecessary embedded data before integration.
- Keep pattern use restrained and separate from logo clear space and readable text areas.
- Retain the earlier illustrated-brown direction where it already appears in approved assets. Do not create a competing illustration style.
6. Implementation architecture
Use the existing WordPress/Elementor architecture. Inspect the theme, child theme, plugins, Elementor capabilities, and any repository/build process before choosing file locations. Do not introduce React, another framework, a new theme, or a second build system merely to create components.
Master header and footer
- Maintain one authoritative Master Header and one authoritative Master Footer, each independently editable and used by all applicable pages.
- When the installed Elementor configuration supports Theme Builder, use header and footer site-part templates with explicit display conditions. Verify the selected page layouts actually render them. [1]
- If the project already uses theme-managed components, reuse its supported header/footer partials and integration. Do not render both a theme header and an Elementor header.
- Do not paste header/footer markup into each page. Do not mistake detached copies of saved templates for synchronized global components.
- Keep menus in the existing WordPress navigation source where practical. Mobile and desktop navigation must reflect the same approved destinations.
- Record the authoritative template IDs or source files and the mechanism that includes them.
Reusable styles and JavaScript
- Store reusable JavaScript in dedicated source files. No repeated script blocks in page HTML widgets, no inline event handlers, and no separate copy of the same behavior for each page.
- A single site.js file is sufficient if the behavior is small. Split into focused files such as navigation.js, motion.js, and forms.js only when those custom behaviors are actually required.
- Prefer working native Elementor/widget behavior. Do not attach a second controller to a menu, accordion, or form already managed by the platform.
- Load custom styles and scripts through the existing WordPress enqueue mechanism, with unique handles, appropriate dependencies, and asset versioning. Load page-specific behavior only where needed. [2]
- Use stable classes or data-* attributes for custom behavior. Avoid brittle selectors tied to generated Elementor element IDs.
- Initialization must be safe when elements are absent or rendered again in the editor. Prevent duplicate listeners and duplicated initialization.
- Keep core content and links usable without animation or optional custom JavaScript. Follow the existing project convention for build output and source control.
- Define global styles through the project's established Elementor global settings and shared CSS. Document which source owns each token so competing values do not drift.
- Use consistent button, card, section, heading, form, and image treatments. Add component variants only when they serve a real content need.
- Keep ordinary page copy, images, and links editable in Elementor or the established content fields. Avoid turning whole pages into giant HTML widgets.
Illustrative responsibilities, to map onto the existing repository rather than impose verbatim:
Responsibility	Possible location
Global styles and tokens	Existing Elementor global settings plus theme assets/css/site.css
Reusable custom behavior	Theme or existing site plugin assets/js/site.js and necessary modules
Script/style registration	Existing enqueue function or inc/enqueue-assets.php
Master header/footer	Elementor site-part templates, or the existing theme's header/footer component files
Reusable page layouts	Existing Elementor templates/loop items and established content fields
Build records	Project documentation for page inventory, component mapping, backlog, and QA


Motion
Use subtle motion only after the page reads clearly without it. Decorative pods and leaves must not overlap controls, block text, introduce layout shifts, capture pointer input, or delay content visibility. Respect prefers-reduced-motion. Prefer short motion that settles; provide appropriate pause/stop behavior for persistent automatic motion where required. Keep small-screen motion restrained.
7. Consolidated finding and task format
Each reviewer submits the same fields:
Field	Requirement
ID and discipline	Unique finding ID plus Messaging, Design, UX, or Accessibility.
Location	Page URL or ID, section, element, and viewport.
Evidence	What was actually observed, exact copy or interaction, and reproduction steps where relevant.
User impact	How it affects understanding, discovery, inquiry, or access.
Proposed change	Specific correction that preserves useful existing work.
Priority	P0, P1, P2, or P3 using the definitions below.
Dependencies	Content, design, technical, or approval dependencies.
Acceptance check	Observable condition that establishes completion.
Status	Confirmed finding, proposed improvement, blocked, or not tested.


Priority definitions:
- P0: Essential journey is unusable, required content is inaccessible, or a critical failure prevents use. Fix before release.
- P1: Material clarity, navigation, product/inquiry, accessibility, or maintainability issue needed for the agreed build.
- P2: Meaningful refinement that improves consistency or usability after core journeys work.
- P3: Optional future work; exclude from this implementation unless explicitly adopted.
Keep severity separate from sequence. A P1 structure decision may need to precede several P1 page changes. Do not label all visual preferences P1. Unresolved applicable accessibility failures cannot be waived simply by moving them to a lower priority.

Convert approved findings into tasks with a DevOps-ready title, description, requirements, dependencies, acceptance criteria, implementation owner, and status. Each task should reference its originating finding IDs. The baseline tasks below are planned work and must not be presented as observed defects.
8. Ordered Codex backlog
DC-01: Establish the current project baseline and page inventory
Priority: P1. Owner: Coordinator. Dependencies: None.

Inspect project instructions, repository status, theme and plugin setup, available assets, current homepage, navigation, and actual page routes. Locate existing copy and any earlier approved wireframes. Identify the authoritative source for WordPress content and for repository code. Record the current environment and preserve unrelated work.

Acceptance criteria: All known main pages and subpages are inventoried; the same baseline can be opened by each reviewer; current header/footer and custom scripts are located; missing access or content is stated explicitly. No implementation edits occur during this task.
DC-02: Review the homepage and connected journeys in four disciplines
Priority: P1. Owner: Four reviewers. Dependencies: DC-01.

Review the homepage, shared header/footer, product entry point, and Work With Us/inquiry route using the role definitions above. Check desktop and mobile. Review linked pages sufficiently to understand whether homepage CTAs deliver what they promise. Use the shared finding format.

Acceptance criteria: Each discipline returns evidence-based findings and notes what already works and should be retained. All findings identify the shared baseline. Missing checks are labeled. No reviewer edits source or site content.
DC-03: Consolidate priorities, messaging, and page structure
Priority: P1. Owner: Coordinator. Dependencies: DC-02.

Merge duplicate findings, resolve conflicts, map current sections to the proposed homepage flow, and settle CTA labels and destinations. Produce the full page inventory, proposed copy changes, content gaps, and ordered implementation tasks. Explain major removals or changes instead of assuming a redesign is required.

Acceptance criteria: Guy receives one concrete review package with priorities, proposed changes, and decisions required. Every change has an acceptance check. Record approval or requested revisions before implementation. No four separate final reports.
DC-04: Establish shared styles and reusable code ownership
Priority: P1. Owner: Implementation owner. Dependencies: Approved DC-03.

Map approved typography, colors, spacing, controls, and image treatments into the existing shared style system. Apply Primary Brown #3A170D and Dark Brown #170905 as separate global tokens, following the resolved color direction in section 5. Move duplicated reusable behavior to external files where duplication is confirmed. Register assets through the existing WordPress mechanism and document ownership.

Acceptance criteria: Shared styles have one documented source per responsibility; the Primary Brown and Dark Brown tokens match the approved HEX values and are mapped consistently into Elementor; reusable custom JS is external; relevant files load without duplicate handlers or console errors; approved content remains editable; existing working behavior is preserved.
DC-05: Implement the Master Header and Master Footer
Priority: P1. Owner: Implementation owner. Dependencies: DC-04.

Create or refine the two authoritative shared components, using the existing integration. Apply them to the agreed page scope. Implement approved navigation, active states, mobile behavior, footer links, and brand presentation.

Acceptance criteria: Each page renders one header and one footer; a master edit propagates without page-by-page changes; navigation works with touch and keyboard; focus is visible; mobile navigation opens/closes correctly; all links resolve; logo clear space is retained.
DC-06: Build the homepage in the actual site
Priority: P1. Owner: Implementation owner. Dependencies: DC-05 and approved homepage content.

Refine the current homepage using the agreed flow and shared components. Preserve effective sections. Implement product discovery and Work With Us CTAs, readable approved copy, responsive imagery, and any agreed decorative treatment.

Acceptance criteria: The homepage renders in WordPress/Elementor, not only in a standalone preview; both visitor paths have meaningful working destinations; desktop/mobile layouts are usable; no invented claims or unresolved public placeholders remain; content is editable; optional motion is nonessential and reduced-motion behavior works.
DC-07: Recheck the homepage milestone
Priority: P1. Owner: Coordinator and reviewers; fixes by implementation owner. Dependencies: DC-06.

Review the implemented homepage against the accepted findings and criteria. Present the working page to Guy with a short account of changes and unresolved decisions. Confirm the shared patterns before extending uncertain design/content decisions throughout the site. Continue independent work on already agreed requirements.

Acceptance criteria: Findings are marked fixed, still open, or blocked with evidence; key journeys are retested; shared component changes do not regress navigation or footer behavior. The milestone is a real site page, not another round of alternative mockups.
DC-08: Build the Products overview and approved category pages
Priority: P1. Owner: Implementation owner. Dependencies: DC-07 and approved product taxonomy/content.

Create or refine the overview and each approved category using shared layouts. Use actual product imagery, meaningful labels, and descriptive links. Add filters or search only when the known catalog and existing project justify them.

Acceptance criteria: Every approved category is represented correctly; navigation and parent/child relationships are clear; cards lead to real destinations; empty categories and unsupported offerings are excluded; mobile discovery works.
DC-09: Build reusable product detail pages and populate the approved products
Priority: P1. Owner: Implementation owner. Dependencies: DC-08 and approved product information.

Use the existing content model where practical. Create a consistent detail layout, then populate all product pages in scope. Show only approved product names, descriptions, images, and factual information. Link to relevant inquiry or existing purchase behavior.

Acceptance criteria: Every product in the approved inventory has a completed page or a specific documented blocker; the shared layout updates consistently; missing optional facts do not leave empty headings; product context carries into the inquiry where supported; no mockup text is treated as verified product data.
DC-10: Build remaining main pages and approved subpages
Priority: P1. Owner: Implementation owner. Dependencies: DC-07 and approved page content.

Complete About/Our Story if in scope, Work With Us, distinct established offering pages, and the other main/subpages in the approved inventory. Reuse the shared style and layout patterns. Keep each page purposeful and avoid splitting thin content into unnecessary pages.

Acceptance criteria: Every approved main page and subpage is complete or explicitly blocked; each has a clear purpose, useful content, correct parent relationship, and relevant next action; navigation matches the actual pages; shared components remain consistent.
DC-11: Complete the inquiry journey
Priority: P1. Owner: Implementation owner. Dependencies: DC-09/DC-10 as applicable and confirmed existing form configuration.

Connect product and Work With Us pages to the approved inquiry route. Use the existing form system where practical. Include only necessary fields and provide clear labels, required-field guidance, validation, success, and failure states. Carry relevant product or offering context without exposing private data in URLs.

Acceptance criteria: Visitors can reach and use the inquiry route with keyboard and mobile input; errors identify the affected fields; server-side handling is not replaced by client-only validation; success appears only after actual success; approved routing is retained. Test delivery with an existing test sink or local capture. If delivery cannot be verified, label it unverified rather than claiming completion. Do not send test messages to live recipients without explicit authorization.
DC-12: Verify all pages and shared components
Priority: P1. Owner: Reviewers and coordinator; fixes by implementation owner. Dependencies: All implemented page tasks.

Run the verification matrix below. Check every in-scope URL for content, links, shared components, and responsive rendering. Exercise every distinct interactive component and the complete product-to-inquiry journey. Recheck affected shared components after fixes.

Acceptance criteria: No open P0 or agreed release-blocking P1 issue remains; manual and automated results are distinguished; blocked checks are explicit; regression fixes are verified; the final page inventory matches what was built. Do not declare broad accessibility conformance from this limited review alone.
DC-13: Deliver the completed site handoff
Priority: P1. Owner: Coordinator. Dependencies: DC-12.

Provide one concise completion record: built pages, changed templates and files, master-component edit locations, JS/style ownership, test results, content gaps, and remaining tasks. Include any existing export/deployment instructions needed by the project.

Acceptance criteria: Another developer can identify where to edit shared components and behaviors; Guy can review each completed page; unfinished items are specific and not hidden behind a generic “done” status. Production publishing follows the project's existing authorization and release process.
9. Verification matrix
Target WCAG 2.2 Level AA for applicable implemented content and interactions. Use automated checks plus manual evaluation; a score alone is not proof. [3]
Area	Required check
Page coverage	Open every approved route and verify content, title, primary heading, parent relationship, links, and both master components.
Responsive layout	Desktop at 1920 × 1080; a representative tablet width; mobile at 390 px; narrow reflow at 320 CSS px. Check content and navigation, not screenshots alone.
Browser coverage	Use available Chromium and WebKit/Safari coverage; state actual browser/device or emulation. Mark unavailable environments untested.
Navigation	Product/inquiry routes work; active states are understandable; dropdowns are not hover-only; no dead ends or overlapping click targets.
Keyboard and focus	Tab/Shift+Tab order, Enter/Space activation, appropriate Escape behavior, skip link, visible focus, and no traps. Sticky content must not obscure focus.
Structure and names	Meaningful headings/landmarks, descriptive link/button names, appropriate alt text, decorative images ignored, and correct accessible names/states.
Contrast and resizing	Test rendered text and essential controls in all states. Check 200% text resizing and reflow. Text targets: 4.5:1 normally; 3:1 for qualifying large text.
Touch targets	Aim for comfortable 44 px controls where practical; meet the applicable 24 × 24 CSS px minimum or documented WCAG spacing/other exception.
Forms	Labels, required fields, keyboard use, invalid/valid states, error association, status announcements, submission failure, and verified test delivery where available.
Assistive technology	Smoke-test navigation, a product page, and inquiry with an available screen reader. State the screen reader/browser combination or record the limitation.
Motion	Reduced-motion preference, no hidden essential content, no layout shifts from decoration, and appropriate pause/stop behavior for persistent animation.
Content accuracy	Approved copy/assets only; no unverified certifications, benefits, contact details, product facts, or mockup-derived claims.
Technical behavior	No broken media or custom-script errors; no duplicated scripts/listeners; assets have dimensions and suitable sizes; critical content appears promptly.
Maintainability	Confirm shared header/footer propagation, reusable page-layout behavior, and ordinary content editing in the established editor.


Fix common causes in shared components rather than applying many isolated page patches. Use focused automated tests where behavior warrants them; do not build tests that merely repeat CSS declarations or low-impact content edits.
10. Final deliverable and definition of done
Maintain one master plan/backlog in the existing project documentation. Link necessary evidence and component records from it rather than creating four competing reports.

The overall build is complete when the approved homepage, main pages, and subpages are implemented in the actual WordPress/Elementor site; the master header and footer are shared; reusable custom JavaScript lives in dedicated files; content and styles follow the agreed sources; and the core product-discovery and inquiry journeys pass the recorded desktop, mobile, and accessibility checks.

If something cannot be completed, identify the exact page/interaction, the reason, and the next action. Do not mark an unfinished website complete because the homepage looks finished.
11. Initial instruction to Codex
Read this master brief and the project's existing instructions. Begin with DC-01 through DC-03: inspect the current project, establish one baseline, run the four read-only reviews, and return one consolidated prioritized backlog with the proposed homepage flow, full page inventory, content gaps, and shared-component approach. Preserve useful existing work. Do not create a new prototype or make implementation edits during the review. After the agreed review checkpoint, use one implementation owner to build the actual homepage, shared header/footer, external reusable JavaScript, main pages, and approved subpages, then verify the complete site.

References
Local sources: supplied DeCocoa_BrandManual.pdf, pages 17, 19, 21, 23, and 24; supplied asset filenames; Guy's October 24, 2026 approval of Primary Brown #3A170D and Dark Brown #170905, which supersedes the manual's printed Chocolate HEX value. The current site must still be inspected as described in DC-01.

Technical references checked October 24, 2026:
1. Elementor: Set conditions for site part templates
2. WordPress: Including Assets
3. W3C: Web Content Accessibility Guidelines 2.2