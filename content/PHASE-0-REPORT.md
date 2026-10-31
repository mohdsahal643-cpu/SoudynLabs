# Phase 0 - Scaffold and tokens

## Delivered

- Root copies of the build documents, with original content/ files retained.
- Page directories and assets/css, assets/js, assets/fonts and assets/img.
- tokens.css with the specified palette, type, spacing, shape and layout values.
- base.css with reset, local font faces, typography, themes, focus styles,
  skip-link support and reduced-motion defaults.
- Blank staging index.html with noindex, two font preloads and an empty main.
- Four Latin WOFF2 files, font licenses and measured Segoe UI fallback metrics.
- Source logo plus transparent, lossless logo and mark exports. Exports retain
  44 source pixels of padding, half the 87 px mark height rounded up. Use the
  2x exports at half their intrinsic dimensions or smaller.
- scripts/prepare-assets.py for repeatable asset preparation. It requires
  Pillow, fontTools and Brotli; dependencies were installed only in .tools/.

## Checks passed

- Source files are ASCII and document copies match their originals.
- All CSS imports and font references resolve locally.
- Font files parse as WOFF2 and contain the required Latin characters.
- Chrome loaded all four font weights successfully.
- Theme backgrounds and 3 px focus styles match the prescribed tokens.
- Focusing the skip link makes it visible.
- No horizontal overflow in the typography/container fixture at six iframe
  widths of 360, 390, 768, 1024, 1440 and 1920 px. Iframe borders reduce their
  actual content viewports by 4 px.
- All prescribed text/background pairs exceed WCAG AA; minimum ratio 6.12.
- Combined CSS: 7012 bytes, 2001 bytes gzipped. Fonts: 50316 bytes total.
- Logo and mark exports have transparency and were visually checked on navy.

## Pending and scope limits

- Cropped logo and mark approval, plus original brand silver confirmation,
  remain open in CONTENT-CHECKLIST.md. Asset preparation does not approve them.
- No [CONFIRM] placeholders are rendered in the blank page.
- Page-level heading, content, component, form, motion, SEO and Lighthouse
  checks are deferred to their build phases. No page content exists yet.
- Font swap layout shift needs checking again with the actual page content.
- No deployment or external service setup was performed.
- No framework, bundler, runtime dependency or page JavaScript was added.
