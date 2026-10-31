import {chromium} from '../../.tools/browser/node_modules/playwright-core/index.mjs';
import assert from 'node:assert/strict';
const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
for(const options of [{},{javaScriptEnabled:false},{reducedMotion:'reduce'}]) {
 const context=await browser.newContext(options);const p=await context.newPage();
 await p.goto('http://127.0.0.1:4174/');
 if(!Object.keys(options).length) await p.waitForTimeout(2000);
 assert.equal(await p.locator('main > section').count(),7);
 assert.equal(await p.locator('h1').count(),1);
 assert.equal(await p.locator('.chip').count(),6);
 const chipLabels = (await p.locator('.chip').allTextContents()).map(text => text.replace(/\s+/g, ' ').trim());
 assert.deepEqual(chipLabels,['Websites','Branding','Digital growth','Web applications','Maintenance','Business software In development']);
 assert.equal((await p.locator('.chip-development small').textContent()).trim(),'In development');
 assert.equal(await p.locator('.chip').first().evaluate(e=>getComputedStyle(e).transform),'none');
 for(const width of [360,390,768,1024,1440,1920]) {
  await p.setViewportSize({width,height:1000});
  assert.equal(await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false,`overflow ${width}`);
 }
 if(!Object.keys(options).length) {await p.setViewportSize({width:1440,height:1100});await p.screenshot({path:'.tools/home-desktop.png',fullPage:true});}
 await context.close();
}
await browser.close();console.log('PASS: Home seven sections, one h1, six final chips, no-JS, reduced motion, six responsive widths');
