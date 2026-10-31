"""Dependency-free static acceptance checks for the finished staging website."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import json
import gzip
import re
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parent.parent
PAGES=['index.html','services.html','products.html','travelos.html','work.html','about.html','contact.html','privacy-policy.html','404.html','components-test.html']


class Document(HTMLParser):
    def __init__(self,text):
        super().__init__();self.elements=[];self.feed(text)
    def handle_starttag(self,tag,attrs): self.elements.append((tag,dict(attrs)))


docs={name:Document((ROOT/name).read_text(encoding='ascii')) for name in PAGES}
for name,doc in docs.items():
    assert sum(tag=='h1' for tag,attrs in doc.elements)==1,name
    ids=[a['id'] for t,a in doc.elements if 'id' in a]
    assert len(ids)==len(set(ids)),f'Duplicate IDs: {name}'
    for t,a in doc.elements:
        if t=='img': assert all(k in a for k in ['width','height','alt']),name
        if t=='label': assert a.get('for') in ids,name
        if 'aria-describedby' in a: assert all(i in ids for i in a['aria-describedby'].split()),name
        for attr in ['href','src']:
            value=a.get(attr)
            if not value: continue
            url=urlsplit(value)
            if url.scheme or url.netloc: continue
            target=(ROOT/url.path.lstrip('/')) if url.path else ROOT/name
            if target.is_dir():target=target/'index.html'
            assert target.exists(),f'{name}: broken link {value}'
            if url.fragment and target.suffix=='.html':
                target_ids=[a.get('id') for t,a in docs.get(str(target.relative_to(ROOT)).replace('\\','/'),Document(target.read_text())).elements]
                assert url.fragment in target_ids,f'{name}: broken fragment {value}'
    metas={a.get('name',a.get('property')):a.get('content') for t,a in doc.elements if t=='meta'}
    assert metas.get('description') and 'noindex' in metas.get('robots',''),name
    assert metas.get('og:title') and metas.get('og:image') and metas.get('twitter:card'),name
    text=(ROOT/name).read_text(encoding='ascii')
    assert not re.search(r'lorem ipsum|https://.*(?:unpkg|cdn\.jsdelivr)',text,re.I),name
    for schema in re.findall(r'<script type="application/ld\+json">(.*?)</script>',text,re.S):
        graph=json.loads(schema)['@graph'];assert all(x['@type'] not in ['Product','Review','AggregateRating'] for x in graph),name
css=(ROOT/'assets/css/site.css').read_bytes()
js=b'\n'.join(p.read_bytes() for p in (ROOT/'assets/js').glob('*.js'))
assert len(gzip.compress(css))<30000
assert len(gzip.compress(js))<15000
assert sum(p.stat().st_size for p in (ROOT/'assets/fonts').glob('*.woff2'))<100000
assert (ROOT/'assets/js/hero-settle.js').stat().st_size<1024
assert 'Disallow: /' in (ROOT/'robots.txt').read_text()
assert len(ET.parse(ROOT/'sitemap.xml').getroot())==7
config=json.loads((ROOT/'vercel.json').read_text())
assert config['cleanUrls'] and config['trailingSlash']
print(f'PASS: {len(PAGES)} HTML documents; IDs, landmarks/headings, labels, local links/fragments, metadata, schema, staging controls and asset budgets')
print(f'CSS gzip {len(gzip.compress(css))} bytes; JS gzip {len(gzip.compress(js))} bytes; fonts {sum(p.stat().st_size for p in (ROOT/"assets/fonts").glob("*.woff2"))} bytes')
