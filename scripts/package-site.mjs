// Deployment copies the ready-to-serve website, excluding project documents.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const output = path.resolve(root, 'dist');
if (path.dirname(output) !== root || path.basename(output) !== 'dist') throw new Error('Invalid output directory');
if (fs.existsSync(output) && fs.lstatSync(output).isSymbolicLink()) throw new Error('Output cannot be a symbolic link');
fs.mkdirSync(output, { recursive: true });
const files = ['index.html', '404.html', 'components-test.html', 'services.html', 'products.html', 'travelos.html', 'work.html', 'about.html', 'contact.html', 'privacy-policy.html', 'robots.txt', 'sitemap.xml', 'site.webmanifest'];
for (const file of files) {
  const target = path.join(output, file);
  fs.mkdirSync(path.dirname(target), { recursive: true });
  fs.copyFileSync(path.join(root, file), target);
}
fs.cpSync(path.join(root, 'assets'), path.join(output, 'assets'), {
  recursive: true, filter: source => !source.endsWith('.gitkeep') && !source.endsWith('soudyn-logo-source.webp')
});
console.log('Static website packaged in dist/');
