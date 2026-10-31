"""Shared authoring helpers. Output is plain HTML, with no runtime includes."""
from pathlib import Path
import html
import json
import os
import re

ROOT = Path(__file__).resolve().parent.parent
SITE_URL = os.environ.get('SOUDYN_SITE_URL', 'https://soudynlabs.com').rstrip('/')
FORM_ENDPOINT = os.environ.get('SOUDYN_FORM_ENDPOINT', '')
NAV = [("Services", "/services.html"), ("Products", "/products.html"),
       ("Work", "/work.html"), ("About", "/about.html"), ("Contact", "/contact.html")]
VOID_ELEMENTS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input", "link",
    "meta", "param", "source", "track", "wbr",
}


def format_html(document):
    """Indent generated markup so the authored pages remain easy to review."""
    tokens = re.findall(r"<!--.*?-->|<![^>]*>|<[^>]+>|[^<]+", document, re.S)
    lines = []
    indent = 0

    index = 0
    while index < len(tokens):
        token = tokens[index]
        value = token.strip()
        if not value:
            index += 1
            continue

        # Keep simple text elements together so formatting does not change
        # their textContent (for example, a navigation link or page heading).
        if value.startswith("<") and not value.startswith(("</", "<!", "<!--")):
            opening = re.match(r"<([a-zA-Z0-9-]+)(?:\s[^>]*)?>$", value)
            if opening and index + 2 < len(tokens):
                text = tokens[index + 1].strip()
                closing = tokens[index + 2].strip()
                expected_closing = f"</{opening.group(1)}>"
                if text and closing == expected_closing:
                    lines.append("  " * indent + value + text + closing)
                    index += 3
                    continue

        if value.startswith("</"):
            indent = max(0, indent - 1)

        lines.append("  " * indent + value)

        if not value.startswith(("</", "<!", "<!--")) and value.startswith("<"):
            tag_match = re.match(r"<([a-zA-Z0-9-]+)", value)
            is_self_closing = value.endswith("/>")
            tag_name = tag_match.group(1).lower() if tag_match else ""
            if not is_self_closing and tag_name not in VOID_ELEMENTS:
                indent += 1

        index += 1

    return "\n".join(lines) + "\n"


def button(text, href="/contact.html", secondary=False):
    return f'<a class="button{" button-secondary" if secondary else ""}" href="{href}">{text}</a>'


def logo():
    return '<a class="brand" href="/" aria-label="Soudyn Labs home"><img src="/assets/img/soudyn-logo-2x.webp" width="478" height="175" alt="Soudyn Labs" decoding="async"></a>'


def header():
    links = ''.join(f'<a href="{url}">{name}</a>' for name, url in NAV)
    return f'''<header class="site-header theme-dark"><div class="container header-inner">{logo()}
<button class="button menu-button" type="button" aria-expanded="false" aria-controls="site-navigation">Menu</button>
<nav class="site-nav" id="site-navigation" aria-label="Main navigation">{links}{button('Start a project')}</nav>
</div></header>'''


def footer():
    links = ''.join(f'<li><a href="{url}">{name}</a></li>' for name, url in [*NAV[:2], ("TravelOS", "/travelos.html"), *NAV[2:]])
    return f'''<footer class="site-footer theme-dark"><div class="container"><div class="footer-grid">
<div class="footer-brand">{logo()}<p class="footer-tagline">Elegant software for everyday business work.</p><p>Soudyn Labs designs and builds websites and business software from Kerala, India.</p></div>
<div><h2 class="footer-heading">Explore</h2><ul class="footer-links">{links}</ul></div>
<div><h2 class="footer-heading">Contact</h2><ul class="footer-links"><li><a href="mailto:hello@soudynlabs.com">hello@soudynlabs.com</a></li></ul><p class="confirm">[CONFIRM email]</p><p>Kerala, India</p><p class="confirm">WhatsApp [CONFIRM]<br>Social links [CONFIRM]</p></div>
</div><div class="footer-bottom"><p>&copy; 2026 Soudyn Labs.</p></div></div></footer>'''


def section(content, theme="light", extra="", id=""):
    return f'<section class="section theme-{theme} {extra}"'+(f' id="{id}"' if id else '')+f'><div class="container">{content}</div></section>'


def intro(title, lead, action="", extra=""):
    return section(f'<div class="page-intro stack">{extra}<h1>{title}</h1><p class="lead">{lead}</p>{action}</div>', "dark", "intro")


def cta(theme="dark"):
    return section(f'''<h2>Tell us what is eating your team's time.</h2><p>A short message is enough. We reply within one working day. [CONFIRM]</p><div class="actions">{button('Start a project')}</div>''', theme, "cta")


def field(name, label, type="text", required=True, autocomplete="", options=None):
    attrs = f'id="{name}" name="{name}" aria-describedby="{name}-error"'
    if required: attrs += ' required'
    if autocomplete: attrs += f' autocomplete="{autocomplete}"'
    if type == "textarea": control = f'<textarea {attrs} rows="5"></textarea>'
    elif options:
        control = f'<select {attrs}><option value="">Select an option</option>'+''.join(f'<option>{x}</option>' for x in options)+'</select>'
    else: control = f'<input {attrs} type="{type}">'
    if type == "email": control = control.replace(f'name="{name}"', 'name="email"')
    return f'<div class="field"><label for="{name}">{label}</label>{control}<p class="field-error" id="{name}-error" aria-live="polite"></p></div>'


def form(kind, fields, submit, success):
    return f'''<form class="form-grid" data-form="{kind}" action="{html.escape(FORM_ENDPOINT or '/contact.html', quote=True)}" method="post" data-success="{html.escape(success, quote=True)}">
<input type="hidden" name="form" value="{kind}"><div class="honeypot" aria-hidden="true"><label for="{kind}-website">Leave this field empty</label><input id="{kind}-website" name="company_website" tabindex="-1" autocomplete="off"></div>
{fields}{'' if FORM_ENDPOINT else '<p class="form-note">[CONFIRM form provider] This staging form is not connected yet.</p><noscript><p>Forms are not connected on staging. Please use the email link to contact us.</p></noscript>'}
<p class="form-error" role="status" aria-live="polite"></p><div><button class="button" type="submit"{'' if FORM_ENDPOINT else ' disabled'}>{submit}</button></div></form>'''


def page(path, title, content, home=False):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    settle = '<script src="/assets/js/hero-settle.js"></script>' if home else ''
    names={'index.html':'Home','services.html':'Services','products.html':'Products','travelos.html':'TravelOS','work.html':'Work','about.html':'About','contact.html':'Contact','privacy-policy.html':'Privacy'}
    key=names.get(path)
    descriptions={}
    for line in (ROOT/'content'/'TECHNICAL-SEO-SPEC.md').read_text().splitlines():
        if line.startswith('| '):
            cells=[x.strip() for x in line.strip('|').split('|')]
            if cells[0] in names.values(): descriptions[cells[0]]=cells[-1]
    description=descriptions.get(key, 'Shared website components.' if 'components' in path else 'The link may be old or mistyped. Return to the Soudyn Labs home page.')
    url=SITE_URL+('/' if home else '/'+path)
    org={'@type':'Organization','@id':SITE_URL+'/#organization','name':'Soudyn Labs','url':SITE_URL+'/', 'logo':SITE_URL+'/assets/img/soudyn-logo-2x.webp','address':{'@type':'PostalAddress','addressRegion':'Kerala','addressCountry':'IN'}}
    graph=[]
    if home: graph=[org,{'@type':'WebSite','@id':SITE_URL+'/#website','url':SITE_URL+'/','name':'Soudyn Labs','inLanguage':'en-IN'}]
    elif key:
        crumbs=[{'@type':'ListItem','position':1,'name':'Home','item':SITE_URL+'/'}]
        if key=='TravelOS': crumbs.append({'@type':'ListItem','position':2,'name':'Products','item':SITE_URL+'/products.html'})
        crumbs.append({'@type':'ListItem','position':len(crumbs)+1,'name':'Privacy Policy' if key=='Privacy' else key,'item':url})
        graph=[{'@type':'BreadcrumbList','itemListElement':crumbs}]
        if key=='Services':
            graph.append(org)
            graph += [{'@type':'Service','name':name,'provider':{'@id':SITE_URL+'/#organization'}} for name in ['Websites','Branding','Digital growth']]
        if key=='Contact': graph += [org,{'@type':'ContactPage','url':url,'name':'Contact Soudyn Labs','mainEntity':{'@id':SITE_URL+'/#organization'}}]
    schema='<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org','@graph':graph},separators=(',',':')).replace('<','\\u003c')+'</script>' if graph else ''
    metadata=f'''<meta name="description" content="{html.escape(description, quote=True)}"><link rel="canonical" href="{url}"><meta property="og:title" content="{html.escape(title, quote=True)}"><meta property="og:description" content="{html.escape(description, quote=True)}"><meta property="og:type" content="website"><meta property="og:url" content="{url}"><meta property="og:site_name" content="Soudyn Labs"><meta property="og:image" content="{SITE_URL}/assets/img/og-image.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Soudyn Labs. Elegant software for everyday business work."><meta name="twitter:card" content="summary_large_image"><link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml"><link rel="icon" href="/assets/img/favicon-32.png" sizes="32x32"><link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest">{schema}'''
    document = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex, nofollow"><meta name="theme-color" content="#0F1F3D"><title>{title}</title>{metadata}
<link rel="preload" href="/assets/fonts/outfit-latin-600.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/assets/fonts/source-sans-3-latin-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css"><script src="/assets/js/menu-init.js"></script>{settle}<script src="/assets/js/config.js" defer></script><script src="/assets/js/main.js" defer></script><script src="/assets/js/form.js" defer></script></head>
<body class="theme-dark"><a class="skip-link" href="#main-content">Skip to content</a>{header()}<main id="main-content" tabindex="-1">{content}</main>{footer()}</body></html>
'''
    target.write_text(format_html(document), encoding="ascii")


if __name__ == "__main__":
    content = intro("Component reference", "Shared website components. Staging only.")
    for theme in ("light", "dark"):
        content += section(f'''<div class="stack"><h2>{theme.title()} theme</h2><div class="actions">{button('Start a project')}{button('Explore products', '/products.html', True)}</div><p><a class="text-link" href="/services.html">Explore services</a></p>
<details><summary>How do we start?</summary><p>Send a short message. We reply within one working day and suggest next steps. [CONFIRM]</p></details>
{field('name-'+theme, 'Name', autocomplete='name')}{field('email-'+theme, 'Email', 'email', autocomplete='email')}</div>''', theme)
    content += cta()
    page("components-test.html", "Components | Soudyn Labs", content)
