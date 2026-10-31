# TECHNICAL-SEO-SPEC.md

## 1. Stack and build

- Static multi-page site: HTML, CSS, vanilla JS. No build step required. Optional: a tiny Node script to minify CSS and JS at deploy time. Do not add a framework.
- Shared header and footer markup is duplicated across pages (no JS includes, so pages work without JS). Keep the markup identical on every page.
- Config values (form endpoint, analytics ID, site URL) live in one file: `assets/js/config.js`. Never commit real secrets.

```js
window.SOUDYN = {
  siteUrl: "https://soudynlabs.com",   // [CONFIRM]
  formEndpoint: "",                     // [CONFIRM] e.g. Formspree or Web3Forms endpoint
  analytics: ""                         // [CONFIRM]
};
```

## 2. Performance budget (mobile, throttled 4G)

| Metric | Target |
|---|---|
| Largest Contentful Paint | under 2.0 s (the h1 is the LCP element) |
| Cumulative Layout Shift | under 0.05 |
| Interaction to Next Paint | under 200 ms |
| Total blocking time | under 100 ms |
| Lighthouse (mobile) | Performance 95+, Accessibility 100, Best Practices 100, SEO 100 |
| CSS (all files, gzipped) | under 30 KB |
| JS (all files, gzipped) | under 15 KB |
| Fonts | two families, Latin subset, woff2, under 100 KB total |
| Images above the fold | none except the logo SVG/WebP |

Rules:
- Preload Outfit 600 and Source Sans 3 400. `font-display: swap`. Match fallback metrics with `size-adjust` to prevent shift.
- Critical CSS inlined in `<head>` for the Home page only if the render-blocking CSS exceeds 14 KB; otherwise one blocking stylesheet.
- All images: AVIF with WebP fallback, explicit `width` and `height`, `loading="lazy"` below the fold, `decoding="async"`.
- No third-party scripts except the analytics slot (see section 7).

## 3. Per-page metadata

Titles under 60 characters, descriptions 140 to 160 characters. Brand suffix "Soudyn Labs".

| Page | Title | Meta description |
|---|---|---|
| Home | Soudyn Labs | Websites and business software built to save time | Soudyn Labs is a software studio in Kerala, India. We design and build websites and business software that take repetitive work off your team. |
| Services | Website design and development services | Soudyn Labs | Custom websites, branding and digital growth for businesses. Fast, accessible, built to be found, and delivered on a clear scope and timeline. |
| Products | Industry software products | Soudyn Labs | We build focused software for one industry at a time. TravelOS, a workspace for travel agencies, is in development. Join early access. |
| TravelOS | TravelOS: travel agency management software | Soudyn Labs | TravelOS brings customers, documents, visas, quotations and payments into one workspace for travel agencies. In development. Join early access. |
| Work | Selected work | Soudyn Labs | Websites designed and built by Soudyn Labs for businesses in facility management, construction, HR, travel and healthcare. [CONFIRM list] |
| About | About Soudyn Labs | Software studio in Kerala | Soudyn Labs is an independent software studio. We start from recurring business problems and build simple, well-made software and websites. |
| Contact | Contact Soudyn Labs | Start a project | Tell us about your website or software project. We reply within one working day. [CONFIRM] |
| Privacy | Privacy Policy | Soudyn Labs | How Soudyn Labs collects and uses information submitted through this website. |

Every page also has:
- `<link rel="canonical">` with absolute URL
- `<meta name="viewport" content="width=device-width, initial-scale=1">`
- `<meta name="theme-color" content="#0F1F3D">`
- Open Graph: `og:title`, `og:description`, `og:type` (`website`), `og:url`, `og:image`, `og:site_name`
- Twitter card `summary_large_image`
- Favicon set: SVG favicon (mark only), 32 px PNG, 180 px apple-touch-icon, 512 px PNG for manifest
- `lang="en"` on `<html>` (use `en-IN` in schema `inLanguage` if desired)

## 4. Open Graph image

1200 x 630, Lab Navy background, the white logo at left, the tagline "Elegant software for everyday business work." in Outfit 600, the hero chips in settled state at right. One shared image at launch; TravelOS may get its own.

## 5. Structured data (JSON-LD)

- Home: `Organization` (name, url, logo, sameAs links [CONFIRM], address country India, region Kerala) and `WebSite`.
- Services: `Service` entries for Websites, Branding, Digital growth, with `provider` pointing at the Organization.
- Contact: `ContactPage` plus `Organization` contactPoint [CONFIRM email].
- All pages: `BreadcrumbList` except Home.
- Do not add `Product` rich results for TravelOS (not released) and do not add review or rating schema.

Validate with Google's Rich Results Test.

## 6. Crawl files

`robots.txt`:
```
User-agent: *
Allow: /
Sitemap: https://soudynlabs.com/sitemap.xml
```
(replace the domain [CONFIRM]). During staging, deploy with `noindex` meta tag and a robots `Disallow: /`. The launch checklist removes both.

`sitemap.xml`: lists the seven indexable pages with `lastmod`. Excludes 404 and any thank-you states.

## 7. Analytics and consent

- Default: privacy-friendly, cookie-less analytics [CONFIRM provider, for example Plausible or Cloudflare Web Analytics] loaded `defer` from one tag in `config.js` driven injection. No cookie banner if no cookies are set.
- Google Search Console verification via DNS record.
- Track events: `start_project_click`, `form_submit_contact`, `form_submit_travelos`, `form_submit_idea`.

## 8. Forms

- Three forms: contact, TravelOS early access, idea. Same component and script (`form.js`), differentiated by hidden `form` field.
- Submit with `fetch` POST (JSON) to `SOUDYN.formEndpoint`. Fallback: normal HTML POST works if JS is off (use `action` and `method="post"`).
- Validation: native constraint validation plus custom messages from `CONTENT.md`. Errors announced with `aria-live="polite"`.
- Spam: hidden honeypot field `company_website`; reject if filled. Add rate limiting at the provider.
- Never expose personal email addresses in client JS other than the public contact address.
- Do not store form data in the repo or logs.

## 9. Security headers (`vercel.json`)

```json
{
  "cleanUrls": true,
  "trailingSlash": true,
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" },
        { "key": "X-Frame-Options", "value": "DENY" },
        { "key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=()" },
        { "key": "Content-Security-Policy", "value": "default-src 'self'; img-src 'self' data:; style-src 'self'; script-src 'self'; font-src 'self'; connect-src 'self' https://formspree.io https://api.web3forms.com; form-action 'self' https://formspree.io https://api.web3forms.com; base-uri 'self'; frame-ancestors 'none'" }
      ]
    },
    {
      "source": "/assets/(.*)",
      "headers": [{ "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }]
    }
  ]
}
```

Adjust `connect-src` and `form-action` to the form provider actually chosen and add the analytics domain. The inline `<head>` script for the hero settle needs a CSP hash or move it to a tiny external file loaded without `defer`. Prefer the external file.

## 10. Accessibility technical notes

- Landmarks: `header`, `nav` (labelled), `main`, `footer`.
- One `h1`; `h2` for sections; `h3` for rows and panels.
- Mobile menu: `button` with `aria-expanded` and `aria-controls`; trap focus; Escape closes; returns focus to the button.
- Accordion uses native `<details>` and `<summary>`.
- Form fields: `<label for>`, `aria-describedby` for help and errors, `autocomplete` attributes (`name`, `email`, `organization`).
- External links to client sites: add visually hidden text "(opens client website)" only if they open in a new tab; default is same tab.

## 11. Local and global SEO notes

- Primary location signal: Kerala, India in footer, About, Contact and schema.
- Target topics for content: website design and development for businesses, branding, business software, travel agency software. Do not stuff keywords.
- Add an internal link from every page to Contact and to at least two other pages.

## 12. Deployment

1. Create repo, connect to Vercel, deploy `main` to production and every branch to preview.
2. Staging on the Vercel preview URL with `noindex`.
3. Connect the production domain [CONFIRM], enforce HTTPS, redirect `www` to apex (or the reverse, pick one).
4. Add DNS records for email and Search Console.
5. Run `QA-CHECKLIST.md` launch section on the production URL.
6. Submit sitemap in Search Console.
