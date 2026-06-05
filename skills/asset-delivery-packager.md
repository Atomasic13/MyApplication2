# Skill: Asset Delivery Packager

## Purpose
Take all design output files and package them correctly — right format, right naming, right compression — then deliver them to the client via Telegram, WhatsApp, or email with a professional summary message.

## When to Use
- Design work is complete and ready to send to client
- Client requested files in a specific format
- Sending a mid-project update with partial deliverables
- Archiving a completed project

## File Naming Convention
Always follow this pattern:
```
[client-slug]_[deliverable-type]_[variant]_[size]_v[version].[ext]
```

Examples:
```
novafit_instagram-post_launch-day_1080x1080_v1.png
novafit_linkedin-banner_corporate_1200x627_v2.jpg
novafit_brand-guidelines_full_A4_v1.pdf
novafit_logo_primary_SVG_v1.svg
```

Rules:
- All lowercase, hyphens inside names, underscores between segments
- Never use spaces or special characters
- Always include version number (start at v1)
- Include dimensions for raster files

## Format Decision Tree

```
Is it a logo or icon?
  → Export SVG (vector) + PNG @2x (transparent background)

Is it a UI screen or mockup?
  → Export PNG @2x + PDF (for print if needed)

Is it a marketing banner or social post?
  → Export JPG at 90% quality (web delivery) + PNG master
  → If transparency needed: PNG only

Is it a brand guideline or presentation?
  → Export PDF (vector, press-ready)

Is it a website asset?
  → Export WebP + fallback JPG
  → Icons: SVG

Is it for print?
  → Export PDF with 3mm bleed, CMYK if possible
  → Minimum 300 DPI for raster elements
```

## Compression Guidelines
| Format | Tool / Setting | Target Size |
|--------|---------------|-------------|
| JPG | 90% quality | <500KB per file |
| PNG | Lossless (keep master), compress copies | <1MB web, master unlimited |
| WebP | 85% quality | <300KB |
| PDF | Compress for web if >5MB | <5MB for email delivery |
| SVG | Minify (remove metadata) | <100KB |

## Folder Structure for Delivery ZIP
```
[client-slug]_[project-name]_[date]/
├── 01_logos/
│   ├── SVG/
│   └── PNG/
├── 02_social/
│   ├── instagram/
│   ├── linkedin/
│   └── stories/
├── 03_marketing/
│   ├── banners/
│   └── print/
├── 04_ui/
│   ├── screens/
│   └── components/
├── 05_brand-guidelines/
│   └── [client]-brand-guidelines-v1.pdf
└── README.txt   ← always include this
```

## README.txt Template
```
[CLIENT NAME] — Design Deliverables
Project: [Project Name]
Date: [delivery date]
Delivered by: DECA / FORMA Studio

CONTENTS
--------
01_logos/       Logo files in SVG and PNG formats
02_social/      Social media posts, stories, covers
03_marketing/   Banners, ads, print-ready files
04_ui/          App/web screens and components
05_brand/       Brand guidelines PDF

FILE USAGE
----------
- SVG: Use for web, presentations, any scalable context
- PNG @2x: Use for screens, slide decks
- JPG: Web/social delivery
- PDF: Print, sharing with stakeholders

FONTS USED
----------
[List fonts used and where to download if not embedded]

QUESTIONS?
----------
[contact info]
```

## Delivery Messages by Channel

### Telegram
```
[Client name], here are your final files for [project name] 🎨

✅ [X] deliverables ready
📁 ZIP attached — see README.txt for file guide

Highlights:
• [key deliverable 1]
• [key deliverable 2]
• [key deliverable 3]

Let me know if you need any adjustments or additional formats.
```

### WhatsApp
```
Hi [name]! Your [project] files are ready. I'm sending the ZIP now.

Inside: [brief list of what's included]

README.txt explains each folder. Any questions just reply here.
```

### Email
Subject: `[Client Name] — [Project Name] Deliverables Ready`
```
Hi [name],

Please find attached the complete deliverables for [project].

[same content as Telegram message, professional tone]

The ZIP includes a README.txt with full file descriptions and font info.

Best,
[your name]
FORMA Studio
```

## Execution Steps

1. Collect all output files from the project's `output/` folder
2. Apply naming convention to every file
3. Organize into folder structure above
4. Generate README.txt with actual project details
5. Compress all to ZIP: `[client-slug]_[project]_[YYYYMMDD].zip`
6. Check ZIP size — if >50MB, upload to cloud storage and send link instead of attachment
7. Send via the client's preferred channel with the correct delivery message
8. Log delivery: append a line to `output/delivery-log.md`

## Delivery Log Format
```
| Date | Client | Project | Files | Channel | Status |
|------|--------|---------|-------|---------|--------|
| 2026-06-05 | NovaBrand | Social Pack | 12 files | Telegram | Delivered ✓ |
```

## Quality Checks Before Sending
- [ ] All files renamed to convention
- [ ] No working/WIP files included (no `-draft`, `-wip`, `-old` versions)
- [ ] README.txt is accurate and complete
- [ ] ZIP opens correctly and folder structure is clean
- [ ] Message is addressed to the right person by name
- [ ] Delivery logged
