"""Author static pages by phase: python scripts/build-pages.py 2 (or all)."""
import sys
from site_helpers import ROOT, page, section, intro, cta, button, field, form


def rows(items):
    return '<div class="rows">'+''.join(f'<div class="row"><h3>{title}</h3><p>{body}</p></div>' for title, body in items)+'</div>'


def process():
    items = [("Listen", "We learn how your team actually works before we propose anything."),
             ("Design", "We design the simplest version that solves the problem and show it early."),
             ("Build", "We build it fast and test it on real phones and real connections."),
             ("Improve", "We stay on after launch and improve it based on what people actually use.")]
    return section('<h2>How we work</h2><ol class="process">'+''.join(f'<li><h3>{a}.</h3><p>{b}</p></li>' for a,b in items)+'</ol>')


def mock():
    return '''<figure class="concept"><div class="mock-window" aria-hidden="true"><div class="mock-top">Sample workspace / Bookings</div><div class="mock-body"><div class="mock-sidebar"><p>Sample customer 1</p><p>Sample customer 2</p><p>Sample customer 3</p></div><div class="mock-detail"><p>Sample booking</p><ul><li>Sample passport</li><li>Sample visa</li><li>Sample invoice</li></ul><p>Sample payment: due</p></div></div></div><figcaption>Concept preview</figcaption></figure>'''


FEATURES = ['Customer records and document collection','Visa and passport tracking','Quotations and invoices','Payment tracking and reminders','Team tasks and reports']


def product(theme='light', single=False):
    actions = button('Learn about TravelOS', '/travelos.html') if single else button('Join early access','/travelos.html#early-access')+button('About TravelOS','/travelos.html',True)
    return section(f'''<div class="product-panel theme-dark"><div class="split split-wide"><div><p class="status">In development</p><h2>TravelOS: one place to run a travel agency.</h2><p class="product-intro">Customers, passports, visas, quotations, payments and reminders in one quiet workspace. We are building it with travel agencies. Join early access and help shape it.</p><ul class="feature-list">{''.join('<li>'+x+'</li>' for x in FEATURES)}</ul><div class="actions">{actions}</div></div>{mock()}</div></div>''', theme)


def home():
    chips = ''.join([
        '<div class="chip" role="listitem">Websites</div>',
        '<div class="chip" role="listitem">Branding</div>',
        '<div class="chip" role="listitem">Digital growth</div>',
        '<div class="chip" role="listitem">Web applications</div>',
        '<div class="chip" role="listitem">Maintenance</div>',
        '<div class="chip chip-development" role="listitem">'
        '<span>Business software</span>'
        '<small>In development</small>'
        '</div>',
    ])
    hero = f'''<section class="section theme-dark hero"><div class="container-wide split hero-inner"><div><h1 class="text-display">Software that takes repetitive work off your team.</h1><p class="lead">Soudyn Labs designs and builds websites and business software for companies that would rather spend their time on customers.</p><div class="actions">{button('Start a project')}{button("See what we're building",'/products.html',True)}</div></div><div class="hero-visual" role="list" aria-label="Soudyn Labs services and products">{chips}</div></div></section>'''
    problem = section('<div class="split"><h2>Most businesses lose hours every week to work a computer should do.</h2><div class="stack"><p>None of it is hard. All of it adds up. We start by finding the task that costs you the most time, then build the simplest thing that removes it.</p>'+rows([
        ('Quotes and invoices typed again from scratch.','The same details, entered by hand every time.'),
        ('Customer details spread across chats, sheets and inboxes.','Nobody is sure which version is current.'),
        ('Follow-ups that depend on someone remembering.','Payments and documents slip until a customer asks.')])+'</div></div>')
    services = section('''<div class="section-heading"><h2>Two ways we work with you.</h2></div><div class="pair"><div><h3>Services.</h3><p>Websites, branding and digital growth for businesses that want to look established and be found. Fixed scope and a clear timeline.</p><a class="text-link" href="/services.html">Explore services</a></div><div><h3>Products.</h3><p>Focused software for one industry at a time, built from problems we see repeat. TravelOS, for travel agencies, comes first.</p><a class="text-link" href="/products.html">Explore products</a></div></div>''','dark')
    work = section('''<div class="section-heading"><h2>Recent work</h2><p>Websites we designed and built for businesses in different industries.</p></div><div class="empty-work"><p>[CONFIRM approved projects and screenshots]</p></div><div class="actions"><a class="text-link" href="/work.html">See all work</a></div>''','dark')
    page('index.html','Soudyn Labs | Websites and business software built to save time',hero+problem+services+product()+work+process()+cta(),home=True)


def services():
    # Pull exact descriptions and FAQ answers from the approved copy source.
    source = (ROOT/'content'/'CONTENT.md').read_text()
    body = source.split('## SERVICES')[1].split('## PRODUCTS')[0]
    import re
    entries = re.findall(r'^\| ([^|]+) \| ([^|]+) \|$', body, re.M)[1:]
    service_rows = ''
    for title, text in entries:
        text = text.replace('Link: See our products','<a class="text-link" href="/products.html">See our products</a>')
        service_rows += f'<div class="row service-row"><h3>{title}</h3><p>{text}</p></div>'
    content = intro('Websites and digital work that make a business look as good as it is.', 'We design and build the website, the brand around it and the steady improvements that keep enquiries coming. One team, one point of contact. [CONFIRM scope]', '<div class="actions">'+button('Start a project')+'</div>')
    content += section('<h2 class="visually-hidden">Services</h2><div class="rows">'+service_rows+'</div>')
    content += section('''<h2>Packages</h2><p>Clear starting points. We adjust each one to the business. [CONFIRM]</p><div class="packages">'''+''.join(f'<div class="package"><h3>{name}</h3><p class="confirm">[CONFIRM features, price and recommendation]</p></div>' for name in ['Starter','Standard','Premium'])+'</div><div class="actions">'+button('Ask about a package')+'</div>','dark')
    content += process()
    faq = re.findall(r'\d+\. \*\*([^*]+)\*\* ([^\n]+)',body)
    content += section('<div class="section-heading"><h2>FAQ</h2><p class="confirm">[CONFIRM all answers before launch]</p></div>'+''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faq),'dark')
    content += cta('light')
    page('services.html','Website design and development services | Soudyn Labs',content)


def products():
    content = intro('Software built for one industry at a time.','General tools try to fit everyone. We pick one industry, learn how it actually works, and build software around its daily tasks.')
    content += section('<h2 class="visually-hidden">Our approach</h2>'+rows([
        ('One industry at a time.','Deep knowledge beats a long feature list.'),
        ('Built from repeated problems.','We build what businesses keep asking for.'),
        ('Simple by default.','You should understand it within minutes, not after training.')]))
    content += product('dark',True)
    idea = field('industry','Your industry')+field('task','The task that costs the most time','textarea')+field('idea-email','Email (optional)','email',False,'email')
    content += section('<div class="split"><div class="stack"><h2>What should we build next?</h2><p>Tell us which repetitive task costs your business the most time. We read every answer.</p></div>'+form('idea',idea,'Send idea','Thank you. We have your idea.')+'</div>')
    page('products.html','Industry software products | Soudyn Labs',content+cta())
    content = section(f'''<div class="split split-wide"><div class="stack"><p class="status">In development</p><h1>TravelOS: run your travel agency from one workspace.</h1><p class="lead">One place for customers, documents, visas, quotations and payments, with reminders that go out on time. Built with travel agencies, in development now.</p><div class="actions">{button('Join early access','#early-access')}</div></div>{mock()}</div>''','dark','intro')
    content += section('<div class="section-heading"><h2>Travel agencies run on scattered details.</h2></div>'+rows([
        ('Passports and documents arrive in chats.','Someone has to find, rename and file them.'),
        ('Visa status lives in a spreadsheet.',"Or in one person's head."),
        ('Quotes and invoices are typed again.','Every booking starts from zero.'),
        ('Payment follow-ups are manual.','Reminders depend on memory.')]))
    content += section('<div class="section-heading"><h2>What TravelOS will do</h2></div>'+rows([
        ('Customers and documents','Keep every customer record and document in one place and see what is missing at a glance.'),
        ('Visas and passports','Track each application step and get reminded before anything expires.'),
        ('Quotations and invoices','Create them from saved details instead of retyping.'),
        ('Payments and reminders','See who has paid, who has not, and send reminders from the same screen.'),
        ('Team and reports','Assign tasks, see what is pending and review the month without a spreadsheet.')]),'dark')
    content += section('<div class="section-heading"><h2>How we are building it</h2></div>'+rows([
        ('Quiet automation.','Software reads documents and drafts reminders so your team does not retype.'),
        ('Few clicks.','Each task should take the fewest steps possible.'),
        ('Built with agencies.','We design it around how agencies actually work. Early access members shape what comes next.')]))
    fields = field('name','Your name',autocomplete='name')+field('agency','Agency name',autocomplete='organization')+field('email','Email','email',autocomplete='email')+field('staff','Number of staff',options=['1 to 3','4 to 10','11 or more'])+field('headache','Biggest daily headache (optional)','textarea',False)
    content += section('<div class="split"><div class="stack"><h2>Join early access</h2><p>Tell us about your agency. We will contact you when early access opens.</p></div><div class="form-panel">'+form('travelos',fields,'Join early access','You are on the list. We will email you when early access opens.')+'</div></div>','dark',id='early-access')
    page('travelos.html','TravelOS: travel agency management software | Soudyn Labs',content)


def work():
    content = intro('Selected work','Websites we designed and built, across different industries.')
    content += section('<h2 class="visually-hidden">Project list</h2><div class="empty-work"><p>[CONFIRM approved projects, live URLs and 1440 px screenshots]</p></div>')
    page('work.html','Selected work | Soudyn Labs',content+cta())


def about():
    content = intro('We build software that stays out of the way.','Soudyn Labs is an independent software studio in Kerala, India. We make websites for businesses today and focused software products for specific industries next.')
    content += section('''<div class="split"><h2>Problems first.</h2><div class="stack"><p>Soudyn Labs started with websites, because building them taught us how businesses really run: the same tasks, done by hand, again and again. That is where our products come from.</p><p>We do not start with "what should we build?" We start with "what recurring problem costs a business time or money?" Only then do we design, and we design the simplest thing that works.</p></div></div>''')
    content += section('<div class="section-heading"><h2>Principles</h2></div>'+rows([
        ('Problems first.','We start from a recurring problem, not a feature list.'),
        ('Simplicity over complexity.','Clean, few clicks, little training.'),
        ('Quality over quantity.','Fewer things, finished well: design, speed, accessibility, reliability.'),
        ('Long-term thinking.','We would rather build something that lasts than something quick.'),
        ('Keep improving.','Nothing is ever finished. Customer feedback shapes what we change.')]),'dark')
    content += section('<div class="split"><h2>How we use AI</h2><p>We use AI to build faster and to remove busywork inside our products, such as reading documents or drafting reminders. It works in the background. People still make the decisions, and we review everything we ship.</p></div>')
    content += section('<div class="split"><h2>Founder</h2><p>Sahal founded Soudyn Labs and leads product, design and development. [CONFIRM short bio and photo]</p></div>','dark')
    page('about.html','About Soudyn Labs | Software studio in Kerala',content+cta('light'))


def contact_pages():
    fields = field('name','Name',autocomplete='name')+field('email','Email','email',autocomplete='email')+field('company','Company (optional)',required=False,autocomplete='organization')+field('need','What do you need?',options=['Website','Branding','Digital growth','Web application','Something else'])+field('message','Message','textarea')
    contact = section('''<div class="split contact-layout"><div class="stack"><h1>Tell us about your project.</h1><p class="lead">A few lines is enough. We reply within one working day. [CONFIRM]</p><a class="text-link" href="mailto:hello@soudynlabs.com">hello@soudynlabs.com</a><p class="confirm">[CONFIRM email]</p><p>Kerala, India</p></div><div class="form-panel">'''+form('contact',fields,'Send message','Thanks. We have your message and will reply within one working day.')+'</div></div>','dark','intro')
    contact += section('''<div class="split"><h2>Other ways to reach us</h2><div class="stack"><p>Email: <a class="text-link" href="mailto:hello@soudynlabs.com">hello@soudynlabs.com</a> [CONFIRM]</p><p>WhatsApp [CONFIRM]</p><p>Location: Kerala, India</p><p class="confirm">Book a call [CONFIRM]</p></div></div>''')
    page('contact.html','Contact Soudyn Labs | Start a project',contact)
    draft = '''<article class="policy"><h1>Privacy Policy</h1><p><strong>Draft for review. [CONFIRM] This policy is not ready for publication.</strong></p><h2>Who is responsible</h2><p>Soudyn Labs, Kerala, India. [CONFIRM legal entity, address and privacy contact]</p><h2>Information submitted through this website</h2><p>The contact form asks for your name, email, optional company, project type and message. The TravelOS early access form asks for your name, agency name, email, number of staff and an optional description of your daily work. The idea form asks for your industry, a repetitive task and an optional email.</p><h2>How information is used</h2><p>[CONFIRM] Proposed purposes are replying to enquiries, reviewing product ideas and contacting people about TravelOS early access. Confirm the lawful basis and final data practices before publication.</p><h2>Service providers and storage</h2><p>[CONFIRM form provider, storage location, recipients, security measures and international transfers] Staging forms are not connected to a provider.</p><h2>Retention and data requests</h2><p>[CONFIRM retention periods, deletion process and grievance contact] Proposed contact: hello@soudynlabs.com [CONFIRM].</p><h2>Analytics and cookies</h2><p>[CONFIRM analytics provider or none, collected data and cookie practices] No analytics is enabled in this staging build.</p><h2>Policy updates</h2><p>[CONFIRM effective date and how policy changes will be communicated]</p></article>'''
    page('privacy-policy.html','Privacy Policy | Soudyn Labs',section(draft))
    page('404.html','Page not found | Soudyn Labs',intro('That page does not exist.','The link may be old or mistyped.','<div class="actions">'+button('Go to the home page','/')+'</div>'))


if __name__ == '__main__':
    phases={'2':home,'3':services,'4':products,'5':work,'6':about,'7':contact_pages}
    if sys.argv[1] == 'all':
        for build in phases.values(): build()
    else: phases[sys.argv[1]]()
