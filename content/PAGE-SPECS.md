# PAGE-SPECS.md

Section by section build spec. Copy lives in `CONTENT.md`; tokens and components in `DESIGN-SYSTEM.md`. Themes alternate dark and light. Header and footer are always navy.

Wireframe key: `[ ]` button, `====` divider, `{chip}` task chip, `( )` image or mock.

---

## HOME `/`

### 1. Hero - dark (wide container 1360)
- Left, 7 columns: h1 (display size), lead (max 52ch), two buttons (primary "Start a project", secondary "See what we're building").
- Right, 5 columns: hero visual with the six task chips (see motion spec) over the static mark geometry.
- Min height `min(88vh, 820px)`. Vertical alignment: center.

```
+------------------------------------------------------------+
| Software that takes              {Websites}                |
| repetitive work off              {Branding}                |
| your team.                       {Digital growth}          |
|                                  {Web applications}        |
| lead paragraph                   {Maintenance}             |
| [Start a project] [See ...]      {Business software}       |
+------------------------------------------------------------+
```

### 2. Problem - light
- h2 left (5 columns). Right (7 columns): intro paragraph then a list of three recurring problems separated by dividers (plain rows, no icons).

### 3. What we do - dark
- h2, then two large side-by-side blocks separated by a vertical 1 px line: Services and Products. Each block: h3, paragraph, text link. No card fill.

### 4. TravelOS spotlight - light
- Raised Navy panel with cut corner (`--cut-sm`), 7 / 5 split inside.
- Left: status line "In development", h2, paragraph, five-item feature list with dividers, two buttons.
- Right: product mock built in HTML/CSS (see TravelOS mock below).

### 5. Selected work - dark
- h2 and intro. Work list: first item spans two columns, the rest in a 2-column grid. Maximum 4 items on Home. Link "See all work" to `/work.html`.
- Show only approved projects. If fewer than 3 are approved, show a single large feature item.

### 6. How we work - light
- h2 left. Four-step sequence (true sequence, numerals allowed): Listen, Design, Build, Improve. Horizontal on desktop, stacked on mobile.

### 7. Final call to action - dark
- Large geometry shape at low contrast behind. h2, one paragraph, one primary button. Left aligned on desktop, left aligned on mobile.

---

## SERVICES `/services.html`

1. **Intro - dark:** h1, lead, primary button.
2. **Service rows - light:** Websites, Branding, Digital growth, Web applications, Maintenance, Automation (marked "Coming soon"). Row component, no icons.
3. **Packages - dark:** Starter, Standard, Premium. Rebuild from the existing Soudyn Labs packages graphic (content in `CONTENT-CHECKLIST.md`). Three columns on desktop, stacked on mobile. Highlight the recommended plan with an Amber top border (not a badge). Prices only if confirmed.
4. **How we work - light:** same four-step sequence as Home.
5. **FAQ - dark:** `<details>` accordion, 5 to 6 items.
6. **Final call to action - light variant:** same block, light theme.

---

## PRODUCTS `/products.html`

1. **Intro - dark:** h1, lead.
2. **Our approach - light:** three short statements as rows: one industry at a time, built from repeated problems, simple by default.
3. **TravelOS panel - dark:** the same panel as Home, with a button to `/travelos.html`.
4. **Idea form - light:** "What should we build next?" Fields: industry, the task that costs most time, email (optional). Posts to the form endpoint with `form=idea`.
5. **Final call to action - dark.**

---

## TRAVELOS `/travelos.html`

1. **Intro and status - dark:** status line "In development", h1, lead, primary button "Join early access" (anchors to form), TravelOS mock on the right.
2. **The problem - light:** what agencies do by hand today, as rows.
3. **What it will do - dark:** feature groups as rows: Customers and documents, Visas and passports, Quotations and invoices, Payments and reminders, Team and reports. Each with one sentence.
4. **Principles - light:** three short rows: quiet automation, minimal clicks, built with agencies.
5. **Early access - dark:** form (name, agency name, email, number of staff select, biggest daily headache textarea optional). Success block replaces form.

### TravelOS mock (HTML/CSS, no images)
A simplified two-pane window on Raised Navy: left list of "Bookings" with customer names (obviously fictional, e.g. "Sample customer 1"), right pane with a checklist of document items and a payment status line. Every text node in the mock must be clearly sample content, and the mock has `aria-hidden="true"` with a visible caption "Concept preview". No metrics, no real names, no fake logos.

```
+---------------------------+
| Bookings   | Sample booking|
| [x] item   | Documents     |
| [ ] item   |  [x] Passport |
| [ ] item   |  [ ] Visa     |
|            | Payment: due  |
+---------------------------+
   Concept preview
```

---

## WORK `/work.html`

1. **Intro - dark:** h1, one paragraph.
2. **Project list - light:** each item = screenshot, name, industry, one-line description of what was delivered, "Visit site" link. First item large.
3. **Final call to action - dark.**

Rules: only approved projects. Screenshots are full-width page captures at 1440 px, cropped to 16 by 10, exported WebP/AVIF. No client logos unless approved.

---

## ABOUT `/about.html`

1. **Intro - dark:** h1, lead.
2. **Story - light:** two paragraphs in a 7-column text column with a pull sentence in h3 size.
3. **Principles - dark:** five principles as rows (Problems first, Simplicity over complexity, Quality over quantity, Long-term thinking, Keep improving).
4. **How we use AI - light:** short, plain explanation, no badges.
5. **Founder - dark:** Sahal, role, short bio, photo if provided [CONFIRM]. If no photo, text only.
6. **Final call to action - light.**

---

## CONTACT `/contact.html`

1. **Intro and form - dark:** two columns. Left: h1, lead, response expectation, direct contacts. Right: form on a Raised Navy panel (no cut corner on forms).
   Fields: Name, Email, Company (optional), What do you need (select: Website, Branding, Digital growth, Web application, Something else), Message. Honeypot hidden.
2. **Other ways to reach us - light:** email, WhatsApp [CONFIRM], location, optional "Book a call" link [CONFIRM].

---

## PRIVACY POLICY `/privacy-policy.html`

Single column, light theme, 68ch. Content drafted separately after legal entity and data practices are confirmed. Until then the page is not linked in the footer on staging builds and must exist before launch.

## 404 `/404.html`

Dark theme. h1, one sentence, primary button "Go to the home page". Includes header and footer.

---

## Responsive rules (all pages)

- Two-column splits collapse to one column under 768 px, text first, visual second.
- Hero visual sits below the buttons on mobile. Chip offsets halve.
- Work list becomes a single column. First item is not larger on mobile.
- Packages stack, recommended plan first.
- Header becomes logo plus Menu button under 900 px.
