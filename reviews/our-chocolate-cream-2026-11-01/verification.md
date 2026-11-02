# Our Chocolate Cream card revision

November 1, 2026. Scope: the five homepage category cards. Their image and copy surfaces use Cream, with Primary Brown text and Ripe action hover/focus. Copy, media, destinations, sizing and carousel behavior remain unchanged. More to Discover and the dedicated Products page retain their existing surfaces.

Hidden-browser checks at 1440px and 390px confirm Cream (`#F7EFE6`) on all five card, image and copy surfaces, Primary Brown text, and no horizontal overflow. The offscreen fifth image remains normally lazy-loaded. Keyboard focus changes the action to Ripe and retains its underline. More to Discover retains its three original colors. Viewed screenshots: [desktop](desktop-final.png), [phone](phone.png); [computed styles and focus evidence](browser-checks.json).

Build, static and deterministic checks pass. The refreshed local Pages artifact passes 1,688 reference checks and 143 HTTP cases with no errors. No changes to assets, content, layout or JavaScript. This is an implementation check, not an independent review or public deployment.
