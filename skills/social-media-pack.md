# Skill: Social Media Pack Generator

## Purpose
Produce a complete, correctly-sized, on-brand social media asset pack from a campaign brief — every platform, every format, named and organized for immediate publishing.

## When to Use
- Client needs launch/campaign posts across platforms
- Monthly content pack for a retainer client
- A single announcement that needs multi-platform adaptation
- Profile refresh (avatars, covers, highlight icons)

## Canonical Size Chart (2026)
Always generate at exactly these dimensions, @2x where raster:

| Platform | Format | Size (px) | Notes |
|---|---|---|---|
| Instagram | Feed post (square) | 1080×1080 | Safe margin 60px all sides |
| Instagram | Feed post (portrait) | 1080×1350 | Preferred by algorithm for reach |
| Instagram | Story / Reel cover | 1080×1920 | Keep text inside 1080×1420 center zone (UI overlays top/bottom) |
| Instagram | Profile avatar | 320×320 | Displays as circle — keep mark centered |
| LinkedIn | Feed post | 1200×627 | |
| LinkedIn | Square post | 1080×1080 | Works well for carousels |
| LinkedIn | Company cover | 1128×191 | Critical content in center 50% |
| LinkedIn | Carousel (PDF) | 1080×1080/page | Export as single PDF |
| X (Twitter) | In-feed image | 1600×900 | |
| X (Twitter) | Header | 1500×500 | |
| Facebook | Feed post | 1200×630 | |
| Facebook | Cover | 820×312 | Mobile crops to center 640×312 |
| TikTok | Video cover | 1080×1920 | Same safe zone as IG Story |
| YouTube | Thumbnail | 1280×720 | Text ≥ 5% of frame height to stay legible at small sizes |

## Pack Composition Rules

For a standard campaign, the default pack is:
- 3× Instagram feed (1 hero announcement, 1 benefit/feature, 1 social proof or CTA)
- 2× Instagram Story (1 announcement, 1 countdown/reminder)
- 2× LinkedIn (1 announcement adapted to professional tone, 1 insight/behind-the-scenes)
- 1× X in-feed
- Sized variants of the hero for any other platform the client uses

Scale up/down based on the brief — but always propose the composition before producing.

## Design Rules
1. **One message per asset.** If a post needs three sentences to land, it's two posts.
2. **Text hierarchy:** headline ≤ 7 words, subline ≤ 12 words, CTA ≤ 3 words.
3. **Brand tokens first:** pull colors/type from the client's design tokens (see brand-guidelines skill). Never introduce off-brand colors for "variety."
4. **Series coherence:** all assets in a pack share a visual system (same grid, same type treatment) with controlled variation — a feed of them should look like one campaign.
5. **Safe zones are hard constraints**, not suggestions. Story text outside the center zone gets covered by platform UI.
6. **Contrast check:** headline over image requires an overlay/scrim if contrast < 4.5:1.

## Copy Rules (per platform)
- **Instagram:** conversational, emoji acceptable if on-brand, hashtags in first comment not caption (list 10-15 researched tags separately)
- **LinkedIn:** professional but human, no hashtag spam (3-5 max), hook in first line (text before the fold decides the click)
- **X:** punchy, thread-ready if the message has depth
- Always deliver copy in a separate `copy.md` file per pack — caption, alt text, hashtags, suggested posting time

## File Naming & Export
Follow the Asset Delivery Packager convention:
```
[client]_ig-feed_hero_1080x1080_v1.png
[client]_ig-story_countdown_1080x1920_v1.png
[client]_li-post_announce_1200x627_v1.png
```
- Master: PNG. Delivery: JPG 90% for photo-heavy, PNG for flat graphics.
- Carousels: individual PNGs + assembled PDF for LinkedIn.

## Execution Steps
1. Read the campaign brief (or run Campaign Brief Parser first)
2. Load the client's design tokens / brand guidelines
3. Propose the pack composition (platforms × formats × count) — confirm if scope unclear
4. Write all copy first (headlines drive layout, not the other way around)
5. Produce the hero asset, get the visual system right, then derive the rest
6. Run quality checks per asset
7. Export with naming convention to `output/social/[client-slug]/[campaign-slug]/`
8. Write `copy.md` with captions, alt text, hashtags per asset
9. Hand off to Asset Delivery Packager for ZIP + client message

## Quality Checks (per asset)
- [ ] Exact canonical dimensions
- [ ] Text inside safe zone
- [ ] Headline contrast ≥ 4.5:1
- [ ] Brand colors and type only
- [ ] Alt text written (accessibility + SEO)
- [ ] No orphan words in headlines (manual line-break control)
