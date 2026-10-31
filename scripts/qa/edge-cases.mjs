import { chromium } from '../../.tools/browser/node_modules/playwright-core/index.mjs';
import assert from 'node:assert/strict';
const browser = await chromium.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe', headless: true });
const base = 'http://127.0.0.1:4174';
const pages = ['/', '/services.html', '/products.html', '/travelos.html', '/work.html', '/about.html', '/contact.html', '/privacy-policy.html', '/404.html'];
const p = await browser.newPage();
const violations = [];
await p.addInitScript(() => {
  window.cspViolations = [];
  document.addEventListener('securitypolicyviolation', e => window.cspViolations.push(e.violatedDirective));
});
for (const path of pages) {
  const response = await p.goto(base + path);
  assert.match(response.headers()['content-security-policy'], /frame-ancestors 'none'/);
  await p.evaluate(() => { document.documentElement.style.zoom = '2'; });
  assert.equal(await p.evaluate(() => document.documentElement.scrollWidth > innerWidth), false, path + ' zoom overflow');
  violations.push(...await p.evaluate(() => window.cspViolations));
}
assert.deepEqual(violations, []);
const missing = await p.goto(base + '/does-not-exist/');
assert.equal(missing.status(), 404);
assert.equal(await p.locator('h1').textContent(), 'That page does not exist.');
await p.route('**/main.js*', route => route.abort());
await p.setViewportSize({ width: 390, height: 844 });
await p.goto(base + '/');
await p.waitForTimeout(4200);
assert.equal(await p.locator('#site-navigation').isVisible(), true);
assert.equal(await p.locator('.chip').first().evaluate(e => getComputedStyle(e).transform), 'none');
await browser.close();
console.log('PASS: 200% zoom, CSP/no violations, security headers, custom HTTP 404, failed-JS menu recovery and hero recovery');
