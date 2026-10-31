# AGENTS.md - Rules for the AI coding agent

Read `README.md` first for the file index and precedence order. This file wins over every other document.

## Working style

- Work one phase at a time from `BUILD-PLAN.md`. Do not build ahead.
- Before each phase, state a 3 to 6 line plan, then build.
- After each phase, run the relevant checks in `QA-CHECKLIST.md` and report what passed and what did not.
- If something is unclear or two documents conflict, ask. Do not invent.

## Stack constraints

- Plain HTML, CSS and vanilla JavaScript only. No React, Next.js, Tailwind, jQuery or bundler.
- Shared styles live in `assets/css/`. Use CSS custom properties from `tokens.css`. Never hard-code a color, font or spacing value in a page.
- JavaScript is progressive enhancement. Every page must be readable and usable with JS disabled.
- No external scripts or CDNs except the analytics slot defined in `TECHNICAL-SEO-SPEC.md`. Fonts are self-hosted.
- All `.md` and source files use ASCII only. Use HTML entities for symbols in HTML.

## Content rules

- Use the copy in `CONTENT.md` exactly. Do not rewrite it, shorten it or add filler.
- Never invent statistics, client counts, testimonials, awards, logos, prices or timelines.
- Anything marked `[CONFIRM]` ships as a visible build-time placeholder only in staging. Before launch, none may remain. List them in your phase report.
- TravelOS is in development. Never describe it as live, launched or used by customers.
- Name usage: running text says "Soudyn Labs". The logo image shows "SoudynLabs". Do not retype the logo as text.

## Banned patterns (these read as generated)

- All-caps or letter-spaced eyebrow labels above headings
- Accenting one word in a headline with color, italic or bold
- A right arrow or chevron appended to button or link text
- Spaced em dash labels, or meta strings joined with middle dots
- Grids of identical rounded cards with the same soft grey shadow
- Gradient washes, glow blobs, purple or blue-violet accents
- Numbered markers on anything that is not a true sequence (only "How we work" is a sequence)
- Fade-and-slide-up reveal on every section, or hover lift on every card
- Stock photos of people shaking hands, laptops on desks or glowing globes
- Monospace type for decorative labels
- Lorem ipsum anywhere

## Required quality floor

- Responsive from 360 px to 1440 px and up, no horizontal scroll.
- Visible keyboard focus on every interactive element.
- `prefers-reduced-motion` respected. The hero settle renders in its final state.
- WCAG AA contrast minimum. Ratios for the palette are in `DESIGN-SYSTEM.md`.
- Semantic HTML: one `h1` per page, ordered headings, landmarks, labelled form fields.
- Images have `width`, `height` and meaningful `alt` text. Decorative images use `alt=""`.
- Meets the performance budget in `TECHNICAL-SEO-SPEC.md`.

## Definition of done for a page

1. Matches `PAGE-SPECS.md` section order and `CONTENT.md` copy.
2. Uses only tokens and components from `DESIGN-SYSTEM.md`.
3. Has title, meta description, canonical, Open Graph tags and correct structured data.
4. Passes the page-level checks in `QA-CHECKLIST.md`.
5. No console errors, no broken links, no leftover placeholder text except tracked `[CONFIRM]` items.

## Git hygiene

- One commit per phase with a clear message, for example `phase 2: home page`.
- Do not commit secrets. Form endpoint and analytics IDs go in the config noted in `TECHNICAL-SEO-SPEC.md`.
