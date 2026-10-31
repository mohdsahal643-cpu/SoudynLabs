# DESIGN-SYSTEM.md

Single source of truth for everything visual. Implement as `assets/css/tokens.css`, `base.css` and `components.css`. Never hard-code values in pages.

## 1. Design plan (why these choices)

- **Subject:** a software studio for small businesses. Audience: owners who are busy and skeptical of jargon. Job of the site: earn trust fast, then make it easy to start.
- **Palette** comes from the logo (white and silver on transparent), so the site is dark by default. The base is a clearly blue navy, not near-black. One warm amber works as the "indicator light" on a lab bench.
- **Typography** pairs a geometric display face that echoes the logo letterforms with a humanist text face for reading.
- **Signature shape:** a cut corner (one 45 degree clipped corner) borrowed from the angular logo mark. Used only on large non-interactive panels and hero media.
- **Boldness is spent in one place:** the hero settle (see `MOTION-AND-INTERACTION.md`). Everything else stays quiet.
- **Structure over cards:** content is organized with rows, dividers and whitespace. Cards are used only where an item is a self-contained object (a project, a product panel).

## 2. Color tokens

| Token | Name | Hex | Role |
|---|---|---|---|
| `--navy` | Lab Navy | `#0F1F3D` | Dark section background, text on light |
| `--navy-raised` | Raised Navy | `#162B52` | Panels and surfaces on dark |
| `--frost` | Frost | `#EEF2F8` | Light section background |
| `--white` | White | `#FFFFFF` | Text on dark, form fields, logo |
| `--silver` | Logo Silver | `#AFAFAF` | Muted text on dark, taken from the logo |
| `--mist` | Mist | `#C3CAD6` | Body text on dark |
| `--slate` | Slate | `#4B5B75` | Body text on light |
| `--amber` | Signal Amber | `#FFB03B` | Primary button fill, focus ring on dark, the one "done" dot |
| `--line-dark` | | `rgba(255,255,255,0.14)` | Dividers on dark |
| `--line-light` | | `rgba(15,31,61,0.14)` | Dividers on light |
| `--error` | Error | `#FF8A80` on dark, `#B3261E` on light | Form errors |
| `--success` | Success | `#7ED6A5` on dark, `#1B6B43` on light | Form success |

### Contrast (checked)

| Pair | Ratio | Use |
|---|---|---|
| White on Navy | 16.4 | Headings on dark |
| Mist on Navy | 9.9 | Body on dark |
| Silver on Navy | 7.5 | Secondary text on dark |
| Amber on Navy | 9.0 | Focus ring, dots |
| Navy on Amber | 9.0 | Primary button text |
| Navy on Frost | 14.6 | Headings on light |
| Slate on Frost | 6.1 | Body on light |
| Slate on White | 6.9 | Body in forms |
| Mist on Raised Navy | 8.5 | Body in panels |
| Silver on Raised Navy | 6.4 | Secondary in panels |

Rules:
- Amber is a fill or a ring, never text on a light background (it fails contrast there).
- Never use colors outside this table. No purple, no gradients.
- Never use pure black or a different dark.

### Section themes

```css
.theme-dark  { --bg: var(--navy);  --fg: var(--white); --fg-body: var(--mist);  --fg-muted: var(--silver); --line: var(--line-dark);  --focus: var(--amber); }
.theme-light { --bg: var(--frost); --fg: var(--navy);  --fg-body: var(--slate); --fg-muted: var(--slate);  --line: var(--line-light); --focus: var(--navy); }
.section { background: var(--bg); color: var(--fg-body); }
```

Sections alternate dark and light down the page. Header and footer are always navy. Never place two sections of the same theme next to each other unless separated by a `--line` border.

## 3. Typography

| Role | Family | Weights | Notes |
|---|---|---|---|
| Display and headings | Outfit | 600, 700 | Echoes the logo geometry. Tracking -0.02em on large sizes. |
| Body and UI | Source Sans 3 | 400, 600 | Humanist, reads well at small sizes. |

Self-host woff2 files (Latin subset) with `font-display: swap`. Preload the two weights used above the fold (Outfit 600, Source Sans 3 400). Fallback stacks:

```css
--font-display: "Outfit", "Segoe UI", system-ui, sans-serif;
--font-body: "Source Sans 3", "Segoe UI", system-ui, sans-serif;
```

### Type scale (fluid)

| Token | Size | Line height | Use |
|---|---|---|---|
| `--text-display` | `clamp(2.75rem, 6.2vw, 5rem)` | 1.02 | Home hero h1 |
| `--text-h1` | `clamp(2.25rem, 4.6vw, 3.75rem)` | 1.06 | Page h1 |
| `--text-h2` | `clamp(1.75rem, 3.4vw, 2.75rem)` | 1.12 | Section titles |
| `--text-h3` | `clamp(1.25rem, 2vw, 1.5rem)` | 1.25 | Row and panel titles |
| `--text-lead` | `clamp(1.125rem, 1.6vw, 1.3125rem)` | 1.55 | Intro paragraphs |
| `--text-body` | `1.0625rem` | 1.65 | Body |
| `--text-small` | `0.9375rem` | 1.5 | Captions, footer, form help |

Rules:
- Max line length 68 characters (`max-width: 68ch`) for body and lead text.
- Headings: Outfit, sentence case, left aligned, `text-wrap: balance`.
- Body: `text-wrap: pretty`.
- Do not use all caps, letter-spaced labels or monospace for labels.
- Do not accent a single word in a headline.

## 4. Layout

- 12-column grid. Container `max-width: 1200px`, wide container `1360px` (hero only). Side padding `clamp(20px, 5vw, 48px)`.
- Alignment: **left aligned** text everywhere. Center only the final call to action on mobile if needed.
- Asymmetry is preferred: text takes 7 columns, supporting visual takes 5, offset.
- Section padding: `clamp(72px, 10vw, 144px)` top and bottom.
- Breakpoints: 480, 768, 1024, 1280 px (min-width, mobile first).

### Spacing scale

`--space-1: 4px; --space-2: 8px; --space-3: 16px; --space-4: 24px; --space-5: 32px; --space-6: 48px; --space-7: 72px; --space-8: 112px; --space-9: 160px;`

### Shape

| Token | Value | Use |
|---|---|---|
| `--radius-sm` | 6px | Buttons, inputs, chips |
| `--radius-md` | 14px | Work thumbnails |
| `--cut-sm` | 14px | Cut corner on large panels |
| `--cut-lg` | 28px | Cut corner on hero media |

Cut corner (top right) on large non-interactive panels only:

```css
.cut { clip-path: polygon(0 0, calc(100% - var(--cut-sm)) 0, 100% var(--cut-sm), 100% 100%, 0 100%); }
```

Never apply `clip-path` to focusable elements (it clips the focus ring). Buttons and inputs use `--radius-sm`.

### Elevation

No drop shadows. Separation comes from color change (Navy to Raised Navy) and 1 px lines.

## 5. Components

### Header
- Always Lab Navy, height 72 px, sticky, 1 px bottom line on scroll.
- Left: logo (white file, height 28 px). Right: nav links, then primary button "Start a project".
- Mobile: logo and a "Menu" button. The menu opens a full-height navy sheet with large links and the button. Focus is trapped while open. Escape closes it.
- Current page link has a 2 px amber underline offset 6 px.

### Buttons
| Type | Style |
|---|---|
| Primary | Amber fill, Navy text, Source Sans 3 600, 16 px, padding 14 x 24, radius 6. Hover: lighten fill 6 percent. Active: translateY(1px). |
| Secondary | 1 px border `currentColor` at 40 percent, text inherits. Hover: border 100 percent. |
| Text link | Underline 1 px, offset 4 px, thickness 2 px on hover. On light, underline is Navy. On dark, underline is Amber. |

Min tap target 44 x 44 px. No arrows or icons appended.

### Task chip (hero only)
Rounded 6 px, Raised Navy fill, 1 px `--line-dark` border, 15 px text Mist, padding 12 x 16, optional 8 px dot at left (Silver, Amber when done).

### Service row (Services page, Home)
Full-width row: title (h3) left in 4 columns, description and link in 8 columns. 1 px `--line` divider between rows. Padding 32 px vertical. No box, no icon grid.

### Product panel (TravelOS)
Raised Navy panel with `.cut`, padding 40 px. Contains a status line, h2, body, feature list with 1 px dividers, buttons. An HTML/CSS mock of the product UI sits beside it (see `PAGE-SPECS.md`).

### Work item
Screenshot (radius 14, 1 px border) above or beside title, industry, one line of what was done, and a text link "Visit site". Layout is a 2-column list, not identical equal cards: the first item is larger (span 2 columns on desktop).

### Process sequence (true sequence, numbering allowed)
Four steps with numerals set in Outfit 600, 1 px vertical line connecting them on desktop (horizontal), stacked on mobile.

### Forms
- Labels above fields, 600 weight, 15 px. Never placeholder-only labels.
- Inputs: height 48 px, White fill, Navy text, 1 px border `#B8C2D3`, radius 6. Focus: 3 px ring (`--focus`) with 2 px offset.
- Error: text below field in `--error`, plus `aria-invalid` and `aria-describedby`. Message says what is wrong and how to fix it.
- Honeypot field hidden off-screen. Submit button shows "Sending" state, disabled.
- Success replaces the form with a confirmation block (focus moves to it).

### Footer
Navy, 1 px top line. Three columns: logo and tagline; navigation; contact. Bottom row: copyright and Privacy Policy link.

### Focus
Dark sections: 3 px Amber outline, offset 3 px. Light sections: 3 px Navy outline, offset 3 px. Never `outline: none` without a replacement.

## 6. Imagery and icons

- No stock photography. Visuals are built from HTML/CSS product mocks, real project screenshots, and the angular geometry of the logo mark (used as a large, low-contrast background shape in at most two places: hero and final call to action).
- Icons: inline SVG, 1.5 px stroke, 24 px grid, `currentColor`. Used sparingly (menu, close, check, external link).
- Project screenshots are shown in a plain 1 px bordered frame. No device mockups.

## 7. Accessibility baseline

- Contrast per table above.
- Focus order follows visual order. Skip link "Skip to content" as first focusable element.
- Touch targets at least 44 px.
- No information by color alone (status dots always have text).
- Motion rules in `MOTION-AND-INTERACTION.md`.
