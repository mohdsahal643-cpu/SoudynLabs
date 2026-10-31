# Soudyn Labs Website - Project README

Build package for the Soudyn Labs company website. Written for an AI coding agent (Codex CLI, Claude Code) and for Sahal as reviewer.

## Goal

A website that makes Soudyn Labs read as a software studio and product company, not a template web agency, while still converting website clients today. Services pay the bills now; products (TravelOS first) are the long-term story.

One-line promise: **Software that takes repetitive work off your team.**

## Decisions already made

| Topic | Decision |
|---|---|
| Stack | Plain HTML, CSS and vanilla JS. No framework, no Tailwind, no bundler. Multi-page static site. |
| Hosting | Static deploy (Vercel). Clean URLs. |
| Look | Dark Lab Navy and Frost sections alternating, one amber signal accent. Matches the white and silver logo. |
| Memorable element | The hero "settle": the studio's services (websites, branding, digital growth, web applications, maintenance, business software) drift into one tidy list, once, on load. Nothing else animates on its own. |
| Fonts | Outfit (display) and Source Sans 3 (body), self-hosted woff2. |
| TravelOS | Featured honestly as "in development" with an early access form. No fake users, no fake metrics. |
| Pages | Home, Services, Products, TravelOS, Work, About, Contact, Privacy Policy, 404. |

Open items that need Sahal's input are in `CONTENT-CHECKLIST.md`. Anything unconfirmed in the copy is marked `[CONFIRM]`.

## File index and reading order

Agents must read in this order before writing code.

1. `AGENTS.md` - rules, banned patterns, definition of done
2. `BRAND-FOUNDATION.md` - positioning, voice, logo rules
3. `DESIGN-SYSTEM.md` - tokens, type, components, layout
4. `MOTION-AND-INTERACTION.md` - the hero settle and all other motion
5. `SITE-ARCHITECTURE.md` - sitemap, navigation, URLs, user journeys
6. `PAGE-SPECS.md` - section by section build spec for every page
7. `CONTENT.md` - all page copy
8. `TECHNICAL-SEO-SPEC.md` - structure, performance, SEO, forms, deploy
9. `BUILD-PLAN.md` - phased prompts, one phase at a time
10. `QA-CHECKLIST.md` - acceptance checks per phase and before launch
11. `CONTENT-CHECKLIST.md` - assets and facts still needed from Sahal

## Precedence when documents disagree

1. `AGENTS.md`
2. `DESIGN-SYSTEM.md` for anything visual
3. `SITE-ARCHITECTURE.md` for structure and URLs
4. `CONTENT.md` for wording
5. `PAGE-SPECS.md` for layout of a section

If two documents conflict, stop and ask Sahal. Do not guess.

## Target folder structure

```
/
  index.html
  404.html
  services.html
  products.html
  travelos.html
  work.html
  about.html
  contact.html
  privacy-policy.html
  assets/
    css/        tokens.css, base.css, components.css, pages.css
    js/         main.js, hero-settle.js, form.js
    fonts/      outfit-*.woff2, source-sans-3-*.woff2
    img/        logo, mark, work screenshots, og image
  sitemap.xml
  robots.txt
  vercel.json
```

## File conventions

- All `.md` files are ASCII only. No smart quotes, em dashes or arrows.
- Mobile first. Test at 360, 390, 768, 1024 and 1440 px.
- Every build phase ends with the checks in `QA-CHECKLIST.md`.
