# Typography, hero and footer revision

Guy's follow-up after homepage-r4 requests the following changes. The preceding package is preserved as `DeCocoa-preview-r4.zip`.

- Default text and button labels: 1rem. Main navigation: 1.25rem. Preserve these sizes on small screens by adjusting layout rather than shrinking labels.
- Button corner radii: 8px outside and 4px inside, retaining the existing double-border thicknesses. Add restrained animated hover feedback to primary and secondary buttons. Remove text underlining from all hover states.
- Let's Talk actions use secondary styling. Keep contrast legible on the Orange scrolling header and the dark hero/footer.
- Eyebrows use primary Orange and sit close above headings.
- Main footer uses primary Chocolate with the supplied badge-logo artwork suitable for a dark background; navigation titles use primary Orange.
- Hero uses a full-height source-pattern background on primary Chocolate. Remove the yellow circle, retain the falling entrance, and use two additional distinct dipped pretzels from the supplied artwork.

All source files, existing page content, section/contact destinations, icon mask and local-only contact behavior remain within the established scope. Continuous background animation retains its pause and reduced-motion behavior.

The hero artwork uses the intact three-piece core of `images/Pretzels.png`; only the detached faint duplicate is excluded. Preserving the original overlaps avoids inventing hidden edges. The three pieces fall in together as one group. The footer SVG comes from the original `DeCocoa_Logo_RGB_DarkBG_Badge.ai`; its #FA7110/#FAF0E6 source fills are preserved rather than remapped to website color tokens.

Four independent sessions were consumed before this change. Implementation self-checks and the fifth independent review are complete. Session 5 accepted the frozen homepage-r5 with no essential defects. All five sessions are consumed and the review loop is closed; any subsequent implementation corrections must be disclosed as not independently re-reviewed.
