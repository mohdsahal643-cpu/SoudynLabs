# SITE-ARCHITECTURE.md

## 1. Sitemap and URLs

Clean URLs, trailing slash, lowercase, hyphenated. Each page is `folder/index.html`.

| Page | URL | Purpose | Primary CTA | In nav |
|---|---|---|---|---|
| Home | `/` | Pitch, route visitors | Start a project | Logo |
| Services | `/services.html` | Explain and sell services | Start a project | Yes |
| Products | `/products.html` | Product approach and TravelOS entry | Join early access | Yes |
| TravelOS | `/travelos.html` | Product page and early access | Join early access | Via Products |
| Work | `/work.html` | Proof of quality | Start a project | Yes |
| About | `/about.html` | Story, principles, founder | Start a project | Yes |
| Contact | `/contact.html` | Project enquiry | Send message | Yes |
| Privacy Policy | `/privacy-policy.html` | Legal | None | Footer only |
| 404 | `/404.html` | Recovery | Go to home page | No |

Not in launch scope: blog, careers, case-study detail pages, pricing calculator, client login. They can be added later without changing the structure.

## 2. Navigation

### Header (desktop)
`[Logo]   Services   Products   Work   About   Contact   [Start a project]`

- Products is a plain link to `/products.html`. No dropdown at launch (only one product).
- "Start a project" always goes to `/contact.html`.

### Header (mobile)
`[Logo]                    [Menu]`

Sheet contains the same five links stacked and the button.

### Footer
- Column 1: logo, tagline, one-sentence description
- Column 2: Services, Products, TravelOS, Work, About, Contact
- Column 3: email, WhatsApp [CONFIRM], location "Kerala, India", social links [CONFIRM]
- Bottom: "(c) 2026 Soudyn Labs" and Privacy Policy

## 3. Conversion paths

Two clear paths, never more than two buttons in view at once.

| Path | Who | Entry points | Destination | Success |
|---|---|---|---|---|
| Project enquiry | Anyone needing a site or software | Header button, hero, final CTA on every page | `/contact.html` form | Confirmation block |
| TravelOS early access | Travel agencies | Home spotlight, Products, TravelOS page | Early access form on `/travelos.html` | Confirmation block |

Secondary: "What should we build next?" idea form on `/products.html` (validates future products).

## 4. User journeys

1. **Owner needs a website:** Home hero -> Services -> Work -> Contact.
2. **Owner with manual work:** Home problem section -> Products approach -> Contact (describes the task).
3. **Travel agency:** Home TravelOS spotlight -> TravelOS page -> early access form.
4. **Referral or curious visitor:** Home -> About -> Work.

Every page ends with the same final call to action block, except Contact (the form is the call to action) and TravelOS (early access form).

## 5. Page inventory by section (summary)

Detailed layouts are in `PAGE-SPECS.md`.

| Page | Sections in order |
|---|---|
| Home | Hero, Problem, What we do, TravelOS spotlight, Selected work, How we work, Final call to action |
| Services | Page intro, Service rows, Packages, How we work, FAQ, Final call to action |
| Products | Page intro, Our approach, TravelOS panel, Idea form, Final call to action |
| TravelOS | Intro and status, The problem, What it will do, Principles, Early access form |
| Work | Page intro, Project list, Final call to action |
| About | Page intro, Story, Principles, How we use AI, Founder, Final call to action |
| Contact | Page intro and form, Other ways to reach us |
| Privacy Policy | Policy text |
| 404 | Message and link |

## 6. Cross-linking rules

- Home "What we do" links to Services and Products.
- Services "Web applications" row links to Products.
- Work items link out to live sites only when the client approved it. Links use `rel="noopener"` and open in the same tab.
- Footer links are the same on every page.

## 7. Content governance

- One h1 per page, written in `CONTENT.md`.
- Page titles and descriptions are in `TECHNICAL-SEO-SPEC.md`.
- Anything shown as a project must be approved (see `CONTENT-CHECKLIST.md`).
