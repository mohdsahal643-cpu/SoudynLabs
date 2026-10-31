# MOTION-AND-INTERACTION.md

Principle: **one orchestrated moment, everything else answers the user.** The page does not animate on its own except the hero settle on the Home page, once.

## 1. The hero settle (Home only)

### Idea
The hero shows the whole studio as one picture: six scattered pieces of a business's digital needs drift into one clean, aligned list under a single team. The last chip is the next chapter of the company (business software), marked with an amber dot and the words "In development".

### Content (chips, in final order top to bottom)
1. Websites
2. Branding
3. Digital growth
4. Web applications
5. Maintenance
6. Business software (with a small muted "In development" label inside the chip)

The chips must match the service rows on `/services.html` and the Products approach. If a service is added or removed there, change it here.

### States
- **Start state (JS on):** chips are offset and rotated by per-chip values. Final state is the default CSS, so no-JS users and reduced-motion users see the tidy list.
- **End state:** chips stacked in a single column, 12 px gap, left aligned, rotation 0, offset 0. The 6th chip's dot turns Amber.

### Per-chip start values (CSS custom properties)

| Chip | `--x` | `--y` | `--r` |
|---|---|---|---|
| 1 | 36px | -28px | -5deg |
| 2 | -44px | 18px | 4deg |
| 3 | 58px | 40px | -3deg |
| 4 | -30px | -14px | 6deg |
| 5 | 48px | 26px | -6deg |
| 6 | -52px | 34px | 3deg |

On screens under 768 px halve these values so chips stay inside the container.

### Timeline
- t = 0 ms: page renders in start state (only if JS added `.js-settle` to `<html>` in the document head before first paint).
- t = 350 ms: `.is-settled` added to the hero visual.
- Each chip transitions `transform` over 1100 ms, `cubic-bezier(0.2, 0.8, 0.2, 1)`, with 80 ms stagger (chip 1 first).
- t = 1700 ms: chip 6 dot changes to Amber (150 ms color transition). The dot marks "what we are building next"; the meaning is carried by the visible "In development" text, not by color alone.
- Nothing loops. Nothing replays on scroll.

### Rules
- Animate `transform` and `opacity` only.
- Add the `.js-settle` class with an inline script in `<head>` and guard it:

```html
<script>
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.documentElement.classList.add('js-settle');
  }
</script>
```

- CSS:

```css
.chip { transform: none; transition: transform 1100ms cubic-bezier(0.2,0.8,0.2,1); transition-delay: calc(var(--i) * 80ms); }
.js-settle .hero-visual:not(.is-settled) .chip { transform: translate(var(--x), var(--y)) rotate(var(--r)); }
@media (prefers-reduced-motion: reduce) { .chip { transition: none; transform: none !important; } }
```

- `hero-settle.js` adds `.is-settled` after `DOMContentLoaded` plus 350 ms. If JS fails, a `<noscript>` rule or the absence of `.js-settle` shows the final state.
- Chip text is real text in the DOM, in final order, so screen readers read a sensible list. The visual wrapper has `role="list"` and each chip `role="listitem"`. Dot has no text and `aria-hidden="true"`; the 6th chip text carries the meaning.
- The hero text (h1, lead, buttons) is visible immediately. It must never wait for the animation. LCP element is the h1.

### Hero background geometry
A large, low-contrast copy of the logo mark geometry (SVG, stroke `--line-dark`, no fill) sits behind the right column, partly cropped by the viewport edge. Static. No parallax.

## 2. Motion that answers a person's action

| Interaction | Behavior | Duration |
|---|---|---|
| Link hover (nav) | Underline grows from left | 160 ms |
| Button hover | Fill lightens | 120 ms |
| Button press | translateY(1px) | 80 ms |
| Mobile menu open and close | Sheet slides in from top, links appear without stagger | 220 ms |
| FAQ accordion | Height and chevron rotate, uses `<details>` | 200 ms |
| Form submit | Button text changes to "Sending", then success block replaces form | instant |
| Form error | Field border color changes, message appears, focus goes to first invalid field | instant |
| Header on scroll | 1 px bottom line fades in after 8 px scroll | 150 ms |

## 3. What is not allowed

- Scroll-triggered reveals on sections, headings or cards
- Hover lift or shadow growth on cards
- Parallax, scroll jacking, cursor followers, custom cursors
- Looping or autoplaying decorative animation
- Page transition effects
- Lottie, video backgrounds, particle fields

## 4. Reduced motion

Under `prefers-reduced-motion: reduce`: hero shows final state immediately, menu and accordion switch with no transition, hover effects are color changes only.

## 5. Performance

- No animation library. CSS transitions only. JS for the settle is under 1 KB.
- No layout shift: chip container has fixed min-height equal to its final height so the list does not push content.
