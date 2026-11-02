# Our Craft copy and navigation revision

November 1, 2026. Source: [user copy transcription](../../handoff/our-craft-copy-2026-11-01.json). The Craft page uses its new title, two introduction paragraphs, Promise, Focus, Sustainability, Food Safety list and three segment descriptions. The homepage Craft intro uses those same two paragraphs. Standing DeCocoa spelling is applied and Fullfilment is corrected to Fulfillment; all other supplied copy is preserved.

Page jump links move above the section content using the existing Our People/Experience pattern. Existing photo, fragment targets and page actions remain. Guy explicitly deferred Alex's video and the three PDFs: "Don't worry about those for now." No media controls or visitor-facing production notes are included in this revision.

Browser DOM comparison confirms one Our Craft h1, exact introduction paragraphs, every supplied section paragraph, all four Food Safety list items and all three segment headings/descriptions. The homepage introduction exactly matches the same transcription. No Video of Alex / Download PDF production notes are rendered. The source renderer safely escapes each optional bullet and emits a real ul/li list.

Hidden-browser responsive checks pass at 1920, 1440, 768, 390 and 320 CSS pixels: no horizontal overflow, contained content, and wrapping jump links above the section content. Activating Food Safety reaches its fragment and focuses the Food Safety heading. Existing aliases remain present.

Viewed screenshots: [desktop introduction and jumps](desktop-intro.png), [Food Safety list](desktop-food-safety.png), [phone introduction/jumps](phone-intro.png), [phone segments](phone-segments.png), [homepage desktop](homepage-desktop.png), [homepage phone](homepage-phone.png). [Exact copy and layout evidence](browser-checks.json).

Build/static/deterministic and whitespace checks pass. The local Pages artifact passes 1,689 references and 144 HTTP cases across 118 files. CSS and JavaScript are unchanged. No public deployment is included.
