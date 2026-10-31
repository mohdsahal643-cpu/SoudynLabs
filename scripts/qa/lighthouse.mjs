import lighthouse from '../../.tools/browser/node_modules/lighthouse/core/index.js';
import {chromium} from '../../.tools/browser/node_modules/playwright-core/index.mjs';
import net from 'node:net';
import fs from 'node:fs';
const reservation=net.createServer();
await new Promise(resolve=>reservation.listen(0,'127.0.0.1',resolve));
const port=reservation.address().port;
await new Promise(resolve=>reservation.close(resolve));
const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true,args:[`--remote-debugging-port=${port}`]});
const selected=process.argv.slice(2);
try {
 for(const [name,path] of [['home','/'],['services','/services.html'],['work','/work.html'],['products','/products.html'],['travelos','/travelos.html'],['about','/about.html'],['contact','/contact.html'],['privacy','/privacy-policy.html'],['404','/404.html']]) {
  if(selected.length && !selected.includes(name)) continue;
  const result=await lighthouse('http://127.0.0.1:4174'+path,{port,output:'json',logLevel:'error',onlyCategories:['performance','accessibility','best-practices','seo']});
  fs.writeFileSync(`.tools/lighthouse-${name}.json`,result.report);
  const categories=Object.fromEntries(Object.entries(result.lhr.categories).map(([key,v])=>[key,Math.round(v.score*100)]));
  const metrics={lcp:result.lhr.audits['largest-contentful-paint'].numericValue,cls:result.lhr.audits['cumulative-layout-shift'].numericValue,tbt:result.lhr.audits['total-blocking-time'].numericValue};
  console.log(name,JSON.stringify({...categories,...metrics}));
 }
} finally { await browser.close(); }
