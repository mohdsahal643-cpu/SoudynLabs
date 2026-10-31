# BUILD-PLAN.md

Ten phases. Give the agent **one phase at a time**. Each phase has a short prompt to paste. After each phase, review, give brief feedback, then move on.

Before phase 0, put all eleven `.md` files in the repo root and the logo in `assets/img/`.

---

## Phase 0 - Scaffold and tokens

Prompt:
> Read README.md, AGENTS.md, BRAND-FOUNDATION.md, DESIGN-SYSTEM.md and TECHNICAL-SEO-SPEC.md. Give me a 5 line plan. Then create the folder structure from README.md, `tokens.css` and `base.css` (reset, fonts with `@font-face`, type scale, section themes, focus styles, skip link), and a blank `index.html` that loads them. Prepare the logo: crop to the artwork plus padding, export a white SVG or WebP at 2x, and a mark-only file. Do not build any page content yet.

Done when: tokens match DESIGN-SYSTEM.md exactly, fonts load self-hosted, contrast table values are used, logo files exist.

## Phase 1 - Global components

Prompt:
> Read MOTION-AND-INTERACTION.md section 2 and DESIGN-SYSTEM.md section 5. Build `components.css` and the shared header, mobile menu, footer, buttons, final call to action block, form fields and FAQ accordion as static HTML on a `components-test.html` page (not linked, `noindex`). Include menu JavaScript with focus trap and Escape handling.

Done when: keyboard-only use works for menu and accordion, focus rings visible on dark and light themes.

## Phase 2 - Home page

Prompt:
> Read PAGE-SPECS.md (Home), CONTENT.md (Home) and MOTION-AND-INTERACTION.md section 1. Build `index.html` with all seven sections and the hero settle. Use CONTENT.md copy exactly. Use `[CONFIRM]` work items as visible placeholders only if no approved screenshots exist.

Done when: no-JS and reduced-motion show the final tidy list, hero text paints immediately, LCP element is the h1.

## Phase 3 - Services

Prompt:
> Build `services.html` from PAGE-SPECS.md and CONTENT.md (Services). Rebuild the Packages section using the data in CONTENT-CHECKLIST.md. If package data is missing, stop and ask me.

## Phase 4 - Products and TravelOS

Prompt:
> Build `products.html` and `travelos.html`. Build the TravelOS concept mock in HTML and CSS with obviously sample content and the "Concept preview" caption. Wire both forms to the shared form component.

Done when: the mock never implies real customers or metrics.

## Phase 5 - Work

Prompt:
> Build `work.html`. Only include the projects I mark as approved in CONTENT-CHECKLIST.md. Use my screenshots if provided, otherwise ask me to supply them. Do not generate fake screenshots.

## Phase 6 - About

Prompt:
> Build `about.html` from PAGE-SPECS.md and CONTENT.md (About). If no founder photo is provided, use the text-only layout.

## Phase 7 - Contact, Privacy Policy, 404

Prompt:
> Build `contact.html`, `privacy-policy.html` and `404.html`. Implement `form.js` per TECHNICAL-SEO-SPEC.md section 8 with validation messages from CONTENT.md, honeypot and success and error states. Use a placeholder endpoint from `config.js`. For the privacy policy, use the text I provide; if none, create a clearly marked draft and list the missing facts.

## Phase 8 - Polish pass

Prompt:
> Review every page against AGENTS.md banned patterns and DESIGN-SYSTEM.md. List violations first, then fix them. Check responsive layouts at 360, 390, 768, 1024, 1440. Remove any decoration that does not serve the brief. Do not add new features.

## Phase 9 - SEO, performance, accessibility

Prompt:
> Implement everything in TECHNICAL-SEO-SPEC.md: metadata per page, canonical, Open Graph, favicons, JSON-LD, sitemap, robots (staging `noindex`), `vercel.json`. Then run Lighthouse on all pages and fix until the targets are met. Report scores.

## Phase 10 - Launch

Prompt:
> Run the launch section of QA-CHECKLIST.md. List every remaining `[CONFIRM]` in the repo. After I resolve them, remove staging `noindex`, update robots and sitemap, and prepare the production deploy notes.

---

## Feedback style

Short and directional is fine ("hero feels crowded", "work section too heavy", "tighter spacing"). The agent should propose a specific fix, apply it, and show what changed.

## Optional later phases

- Case study pages for approved projects
- Blog or notes section
- TravelOS product site expansion once it has screenshots
- Pricing calculator
