import {chromium} from '../../.tools/browser/node_modules/playwright-core/index.mjs';
import assert from 'node:assert/strict';
const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
const base='http://127.0.0.1:4174';
const p=await browser.newPage();await p.goto(base+'/contact.html');
await p.getByRole('button',{name:'Send message',exact:true}).click();
assert.equal(await p.locator('#name-error').textContent(),'Enter your name.');
assert.equal(await p.locator('#email-error').textContent(),'Enter a valid email address, for example name@company.com.');
assert.equal(await p.locator('#message-error').textContent(),'Tell us a little about what you need.');
assert.equal(await p.evaluate(()=>document.activeElement.id),'name');
const forms=[['/contact.html','contact',{name:'Test Person',email:'test@example.com',need:'Website',message:'Test enquiry'}],['/products.html','idea',{industry:'Travel',task:'Test task','idea-email':'test@example.com'}],['/travelos.html','travelos',{name:'Test Person',agency:'Test Agency',email:'test@example.com',staff:'1 to 3'}]];
for(const [path,kind,values] of forms) {
 await p.goto(base+path);
 for(const [id,value] of Object.entries(values)) {
  const el=p.locator('#'+id);if(await el.evaluate(e=>e.tagName==='SELECT')) await el.selectOption({label:value});else await el.fill(value);
 }
 const submit=p.locator('form button[type="submit"]');await submit.click();
 assert.match(await p.locator('.form-error').textContent(),/not connected/);
 await p.evaluate(()=>window.SOUDYN.formEndpoint='/qa-endpoint');
 let requests=0;
 await p.route('**/qa-endpoint',route=>{requests++;return route.fulfill({status:503,body:'failure'});});
 await p.locator('[name=company_website]').evaluate(e=>e.value='spam');
 await submit.click();assert.equal(requests,0);
 await p.locator('[name=company_website]').evaluate(e=>e.value='');
 await submit.click();await p.waitForFunction(()=>document.querySelector('.form-error').textContent.startsWith('The message did not send.'));
 assert.equal(await p.locator('#'+Object.keys(values)[0]).inputValue(),Object.values(values)[0]);
 assert.equal(await submit.isDisabled(),false);
 await p.unroute('**/qa-endpoint');
 let payload;
 await p.route('**/qa-endpoint',async route=>{payload=route.request().postDataJSON();await new Promise(r=>setTimeout(r,200));await route.fulfill({status:200,contentType:'application/json',body:'{"success":true}'});});
 await submit.click();assert.equal(await submit.textContent(),'Sending');assert.equal(await submit.isDisabled(),true);
 await p.locator('.form-success').waitFor();
 assert.equal(payload.form,kind);assert.equal(payload.email,'test@example.com');
 assert.equal(await p.evaluate(()=>document.activeElement.className),'form-success');
 assert.equal(await p.locator('form').count(),0);
 console.log('PASS '+kind+': missing endpoint, honeypot, failure preservation, sending, JSON payload, success/focus');
}
const nojs=await browser.newPage({javaScriptEnabled:false});await nojs.goto(base+'/contact.html');
assert.equal(await nojs.locator('form button').isDisabled(),true);
await browser.close();console.log('PASS exact contact validation messages, first-invalid focus, no-JS staging guard');
