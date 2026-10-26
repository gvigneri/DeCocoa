# Separate pretzel entrances and rounded components

Guy requested that each pretzel enter separately with easing and a slight delay, like rain, plus 2px button inner borders, rounded eyebrows, and cards with 4px double borders (the second transparent) and 16px corners.

Three image elements now replace the single animated collage. The red-drizzle and chunky-sprinkle pretzels were separated with the built-in Imagegen tool, preserving their source appearance while reconstructing the small portions hidden behind other pretzels. These are edited images, not pixel-identical source exports. The beaded pretzel remains a direct export of the supplied separate PNG. Original source files remain unchanged. Exact prompts, inputs and output paths are recorded in `pretzel-cutout-provenance.json`.

Each image begins above the hero, with durations of 1.55, 1.65 and 1.7 seconds and delays of 0, 0.2 and 0.4 seconds. The complete sequence settles after 2.1 seconds. Mid-entry pause holds the current positions and resumes without restarting; a previously saved pause shows the settled composition on load. Reduced motion uses the static layout.

Buttons retain their 8px/4px corner radii, with both borders now 2px. Eyebrows use an 8px radius. Card frames use 16px outer corners, a 4px visible inset ring and a 4px transparent outer ring that exposes the section background. The exact source icon photo mask remains unchanged.

Guy explicitly stopped the design-review agent and will provide design reviews from this revision onward. Independent review session 5 applies to the preserved r5 build only. R6 receives implementation self-checks; no independent design-review acceptance is claimed. The preceding deliverable is saved as `DeCocoa-preview-r5.zip`.
