# Heading and adjacent-link review

November 15, 2026. Local preview: http://127.0.0.1:4174/.

## Corrections

- Category names and taglines share one semantic heading: h3 on homepage cards, h2 in the product category sections. Existing IDs, typography and copy are retained.
- Segment names and audience labels share their h3. Product example captions and names share their h3.
- The four supporting mega-menu photos are decorative images, with empty alternative text and no link. Each main navigation label remains the destination link. This removes eight duplicate photo links per page across the two headers.
- Both drawers no longer render an extra contact link. The contact action remains in each header.

Across 22 generated pages, 35 heading-like paragraphs now belong to their existing headings. No extra heading levels were introduced. The generated pages contain 220 fewer redundant anchors in total.

## Verification

- Reproduced the supplied short-paragraph/font-size rule against the rendered DOM at 1600px: 45 candidates before, 10 after. This is a local reproduction of the supplied rule, not a claim that the WAVE extension was run.
- All 22 pages retain one h1, correct heading ancestry for the 35 changed elements, and no horizontal overflow at the checked desktop width.
- No consecutive same-destination anchors remain within the same navigation/content section. Repeated inquiries in separate product sections, global navigation and footer destinations are retained in their distinct contexts.
- Keyboard test: Tab from the expanded Our People toggle reaches Our Roots directly. Escape closes the menu and returns focus to its toggle. The 429px square supporting photo remains intact.
- At 390px, segment headings and labels retain their styling, the cards stack, and no horizontal overflow appears.
- Static checks pass: 3,203 local references, 57 protected artwork records, deterministic rebuild, shared partial propagation. All 718 retained-copy checks pass. Navigation state checks pass. Whitespace checks pass.

Evidence: `semantics-before.json`, `semantics-after.json`, `semantic-link-contexts.json`, `semantic-menu-keyboard.jpg`, `semantic-headings-desktop.jpg` in this directory.

## Reviewed body-copy matches

These remain real paragraphs. Their length and 24px desktop size match the supplied heuristic, but they describe existing sections or give form instructions. Promoting them to headings would misrepresent the document outline. Copy and typography were preserved.

| Page | Paragraph |
| --- | --- |
| Homepage, Partners | Good chocolate brings people together. |
| Homepage, inquiry | A question, an idea, a chocolate possibility. |
| Our People, Values | Be honest. Be safe. Do the right thing. |
| Our People, Values | Help each other. Learn. Grow as a team. |
| Our People, Values | Be positive. Be helpful. Set a good example. |
| Our Craft, Sustainability | We source cacao responsibly. |
| Our Craft, Sustainability | We choose only clean label ingredients. |
| Our Craft, Sustainability | We use eco-friendly packaging. |
| Our Craft, Food Safety | We ensure: |
| Let's Talk, inquiry | Choose a topic and add your questions below. |
