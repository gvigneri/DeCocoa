# Experience Center copy revision

November 1, 2026. Scope: the dedicated Experience Center page. The authoritative transcription is `handoff/experience-center-copy-2026-11-01.json`. Guy requested word-for-word copy and explicitly excluded Museum & Virtual Exhibition from changes.

Keep the current photograph, existing section IDs and aliases, top jump navigation, Explore Our Craft action and tour inquiry action. Use one plain Experience Center h1, the supplied three opening sentences, a separate Experience Center h2 and its two paragraphs, How its Made with seven semantic numbered steps, and the exact supplied Tours and Classes paragraph. Spelling and punctuation are deliberately retained as supplied.

The former generated page is frozen in `before.html`; timeline source/style/script hashes are in `history-before-hashes.json`. Verify the full rendered Museum & Virtual Exhibition section is byte-identical after rebuilding, along with unchanged timeline resources.

Guy explicitly confirmed: “Start with the seven steps; leave the intro for later.” The planning note is omitted and no new process introduction was drafted.

The complete generated Museum & Virtual Exhibition section is byte-identical (40,866 bytes). Timeline JSON, chapter template, CSS and JavaScript hashes remain unchanged. Rendering adds only an optional escaped `ordered_steps` collection, with semantic ol/li, h3 and p elements. Five scoped process-spacing rules were added to the shared stylesheet; its cache version is now 18.

Hidden-browser checks at 1920, 1440, 768, 390 and 320 CSS pixels pass exact-copy comparisons for the heading, introduction, overview, all seven steps and Tours and Classes. There is one h1, all process titles are h3 elements in a native ordered list, all four jump targets exist, all ten timeline items remain, the existing photo loads, and no horizontal overflow occurs. The actual mobile How its Made jump focuses its heading and leaves it visible beneath the sticky Menu row. See [browser evidence](browser-checks.json), [desktop introduction](desktop-intro.png), [desktop steps](desktop-steps.png) and [phone steps](phone-steps.png). All listed screenshots were viewed.

Build/static/deterministic checks pass for 18 pages, with no errors. The local Pages export passes with 76 runtime resources, 118 files, 1,692 references and 144 HTTP cases. Git whitespace checks pass. The local preview remains available on port 4174; no public deployment was performed.
