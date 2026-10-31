import fs from 'node:fs';
import {chromium} from '../../.tools/browser/node_modules/playwright-core/index.mjs';
import assert from 'node:assert/strict';
const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
for(const path of process.argv.slice(2)) {
 const p=await browser.newPage();const errors=[];p.on('pageerror',e=>errors.push(e.message));
 const response=await p.goto('http://127.0.0.1:4174'+path);assert.equal(response.status(),200);
 assert.equal(await p.locator('h1').count(),1);
 for(const width of [360,390,768,1024,1440,1920]) {
  await p.setViewportSize({width,height:1000});
  assert.equal(await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false,`${path} overflow ${width}`);
  if(width===1440) assert.equal(await p.locator('.menu-button').isVisible(),false);
 }
 await p.evaluate(fs.readFileSync('.tools/browser/node_modules/axe-core/axe.min.js','utf8'));
 const violations=await p.evaluate(async()=>{const r=await axe.run();return r.violations.map(v=>({id:v.id,targets:v.nodes.map(n=>n.target)}));});
 assert.deepEqual(violations,[],path);assert.deepEqual(errors,[],path);
 console.log(`PASS ${path}: six widths, one h1, desktop menu hidden, axe, JS errors`);
 await p.close();
}
await browser.close();
