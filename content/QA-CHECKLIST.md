# QA-CHECKLIST.md

Run the relevant sections after every phase. Run everything before launch.

## A. Visual and design system

- [ ] Only tokens from `tokens.css` used (search for stray hex values and px font sizes)
- [ ] Sections alternate dark and light, header and footer navy
- [ ] No banned patterns from `AGENTS.md` (all-caps eyebrows, single-word headline accents, arrow suffixes, identical shadowed card grids, gradients, hover-lift)
- [ ] One h1 per page, sentence case headings, left aligned
- [ ] Cut corner used only on large non-interactive panels
- [ ] Amber never used as text on light backgrounds
- [ ] Logo only on navy, clear space respected, never retyped

## B. Responsive

Check at 360, 390, 768, 1024, 1440 px and one very wide (1920 px).

- [ ] No horizontal scroll at any width
- [ ] Two-column splits collapse in the right order (text first)
- [ ] Hero chips stay inside the container on mobile
- [ ] Tap targets at least 44 x 44 px
- [ ] Mobile menu opens, closes, traps focus, restores focus
- [ ] Forms usable with the on-screen keyboard open (no hidden submit button)

## C. Accessibility

- [ ] Keyboard only: every link, button, field and accordion is reachable and operable
- [ ] Visible focus on dark and light themes
- [ ] Skip link works
- [ ] Heading order correct on every page
- [ ] Contrast meets the table in `DESIGN-SYSTEM.md`
- [ ] All images have correct `alt`; decorative ones `alt=""`
- [ ] Form labels, errors and success announced by a screen reader (test with VoiceOver or NVDA)
- [ ] `prefers-reduced-motion`: hero shows final state, no transitions
- [ ] Page works at 200 percent zoom
- [ ] axe or Lighthouse accessibility score 100

## D. Motion

- [ ] Hero settle runs once, about 1.7 s, no loop, no replay
- [ ] Hero text is visible immediately
- [ ] No other autonomous animation on any page
- [ ] With JS disabled, hero shows the tidy final list

## E. Content

- [ ] Copy matches `CONTENT.md` exactly
- [ ] No lorem ipsum, no invented numbers, testimonials or logos
- [ ] TravelOS described only as in development, mock labeled "Concept preview"
- [ ] Only approved projects shown
- [ ] ASCII only in `.md` files; HTML entities used for symbols in HTML
- [ ] "Soudyn Labs" in text; logo image for the wordmark

## F. Performance

- [ ] Lighthouse mobile: Performance 95+ on Home, Services, Work
- [ ] LCP under 2.0 s, CLS under 0.05, INP under 200 ms
- [ ] CSS under 30 KB and JS under 15 KB gzipped
- [ ] Fonts preloaded, no layout shift on swap
- [ ] Images AVIF/WebP with dimensions, lazy below the fold

## G. Forms

- [ ] Contact, TravelOS and idea forms submit to the real endpoint in preview
- [ ] Empty and invalid submissions show the exact error text from `CONTENT.md`
- [ ] Honeypot rejects filled submissions
- [ ] Success block replaces the form and receives focus
- [ ] Network failure shows the send-failure message and keeps the entered data
- [ ] Notification email arrives and contains the form name

## H. SEO and technical

- [ ] Unique title and meta description on every page (see table)
- [ ] Canonical, Open Graph, Twitter tags present and correct
- [ ] Favicons and `theme-color` present
- [ ] JSON-LD validates in Rich Results Test, no TravelOS Product schema
- [ ] `sitemap.xml` lists only live indexable pages
- [ ] 404 page returns 404 status
- [ ] No broken internal or external links (run a link checker)
- [ ] Security headers present (check securityheaders.com)

## I. Launch (production only)

- [ ] All `[CONFIRM]` items resolved (search the repo for the string `CONFIRM`)
- [ ] Staging `noindex` meta and robots `Disallow` removed
- [ ] Production domain, HTTPS, single canonical host (www or apex) enforced
- [ ] Privacy Policy published and linked in footer
- [ ] Analytics receives a test pageview and the four events
- [ ] Search Console verified, sitemap submitted
- [ ] Form notifications go to the correct inbox
- [ ] Share the home page URL in a messaging app and confirm the preview image and title
- [ ] Test on one real iPhone and one real Android phone on mobile data
