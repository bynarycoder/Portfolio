"""Builds the one-page portfolio site: /home/user/portfolio-site/index.html

Edit the PROJECTS data or the copy below, then run:  python3 build_site.py
The site is fully static (no build step, no dependencies) so it can be dropped
straight onto Vercel, Netlify or GitHub Pages.
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

ME = dict(
    name='Abdulwahab Abdulyekeen',
    role='Software Developer & UI/UX Designer',
    city='Kaduna, Nigeria',
    email='Abdulwahababdulyekeen1@gmail.com',
    phone='+234 704 518 7666',
    gh='https://github.com/bynarycoder',
    li='https://www.linkedin.com/in/abdulwahab-abdulyekeen-8370363a8',
)

SERVICES = [
    ('UI/UX Design', 'User flows, wireframes, high-fidelity screens, clickable prototypes and a small design system for web and mobile apps.'),
    ('Front-End Development', 'Responsive React and Next.js interfaces with Tailwind CSS, built from the design and deployed live.'),
    ('Full-Stack Web Apps', 'Python (FastAPI) back ends, REST APIs and AI features (Gemini, Groq, Scikit-learn) wired to a clean interface.'),
    ('Design to Code Handoff', 'Component-based layouts, spacing and colour tokens, documented so any developer can build without guessing.'),
]

PROJECTS = [
    dict(
        id='fuel', n='01', name='FuelFinder AI', tag='Fuel price finder for Nigeria',
        color='#16A34A', accent_soft='rgba(22,163,74,.12)',
        url='https://fuel-station-finder-omega.vercel.app',
        repo='https://github.com/bynarycoder/Fuel-Station-Finder',
        year='2026', kind='3MTT capstone project',
        role='UI/UX design and front-end development',
        stack=['Next.js', 'React', 'TypeScript', 'Leaflet + OpenStreetMap', 'REST API', 'AI assistant'],
        problem='Drivers waste time and fuel moving between stations without knowing which ones are open, what they charge, or how reliable that number is.',
        solution='A map-first app where a driver finds stations nearby, compares petrol, diesel, LPG and CNG prices, and asks an AI assistant for the cheapest option.',
        intro='I designed the flow and built the interface: map, filters, station cards, price reporting, AI assistant, dark mode and a separate mobile layout.',
        desktop='assets/f_light.jpg', mobile='assets/f_ai_m.jpg', mobile2='assets/f_list_m.jpg',
        decisions=[
            ('Trust is the real feature', 'Crowd-sourced prices go stale, so every station shows a Verified or Unverified badge, an Imported marker and a "last update" warning. A driver sees how old the data is before deciding to drive there.'),
            ('Three ways to start', 'Near me, Choose location and Search manually. Some users want one tap, some want to plan a station along a route, some have no GPS permission.'),
            ('Privacy said out loud', 'The location card states that position is only used for search and never stored, right where the permission is requested.'),
            ('Chat for the hard questions', 'The Fuel AI Assistant answers "find the cheapest petrol near me" with suggested prompts, so a first-time user never stares at an empty input.'),
            ('Mobile is not a shrunk desktop', 'A bottom tab bar (Map, Stations, AI Assistant, Report, Account) and a bottom-sheet results list, operable with one thumb.'),
        ],
        shots=[
            ('assets/f_ai.jpg', 'Fuel AI Assistant', 'Suggested prompts turn a blank chat box into a starting point.'),
            ('assets/f_detail.jpg', 'Station detail and trust cues', 'Price, verification badge, data-age warning and one primary action: Get Directions.'),
            ('assets/f_dark.jpg', 'Dark mode', 'A full dark theme for night driving, same layout and contrast ratio.'),
        ],
    ),
    dict(
        id='mammo', n='02', name='Mammo Guard', tag='AI-assisted breast cancer prediction',
        color='#0EA5E9', accent_soft='rgba(14,165,233,.12)',
        url='https://mammo-guard.vercel.app', repo='',
        year='2026', kind='3MTT NextGen Knowledge Showcase',
        role='UI/UX design and front-end development',
        stack=['React', 'Tailwind CSS', 'Recharts', 'Scikit-learn model', 'Wisconsin Diagnostic dataset'],
        problem='A prediction tool is only useful if a busy clinician can enter 30 measurements quickly and read the result without guessing what it means.',
        solution='A grouped clinical form, file upload for batch runs, a confidence-scored result with charts and a printable report, plus history and an awareness section.',
        intro='The model (Scikit-learn, trained on the Wisconsin Diagnostic dataset) reports 95.6% accuracy in the project documentation. My work was making that output readable, honest and fast to use.',
        desktop='assets/m_result.jpg', mobile='assets/m_m.jpg', mobile2='',
        decisions=[
            ('Group 30 fields, do not list them', 'Inputs are split into Mean, Standard Error and Worst value sections, each with a normal-range hint, so errors are caught while typing instead of after submit.'),
            ('Keyboard is not the only path', 'CSV and Excel upload with a downloadable template, fuzzy column matching and single-row versus multi-row handling: one record opens in the form, many run as a batch.'),
            ('Never output a bare label', 'The result screen shows confidence, a probability breakdown and a risk gauge, plus follow-up recommendations, because a decision support tool must show its uncertainty.'),
            ('Say what it is not', 'A medical disclaimer sits on the form and on every report: this supports clinical judgement, it does not diagnose.'),
            ('Work stays on the device', 'Prediction history uses browser local storage with JSON export and clear-all, so no patient record leaves the machine.'),
        ],
        shots=[
            ('assets/m_form.jpg', 'Grouped clinical form', 'Collapsible sections, range hints and one clear primary action per group.'),
            ('assets/m_result2.jpg', 'Findings and report actions', 'Prioritised follow-up steps with print, download and new-prediction shortcuts.'),
            ('assets/m_awareness.jpg', 'Awareness section', 'Symptoms, risk factors, self-examination steps and a screening checklist.'),
        ],
    ),
    dict(
        id='job', n='03', name='JobLiberty AI', tag='AI career platform for African job seekers',
        color='#4F46E5', accent_soft='rgba(79,70,229,.12)',
        url='https://jobliberty.vercel.app', repo='https://github.com/bynarycoder/JobLiberty-BE',
        year='2026', kind='3MTT NextGen Showcase 2026',
        role='UI/UX design, front-end and back-end development',
        stack=['Next.js', 'React', 'Python / FastAPI', 'Gemini AI', 'Groq AI', 'Docker'],
        problem='Most CVs are filtered before a human reads them, and applicants never learn why, or which skills they are missing for the role they actually want.',
        solution='Upload a PDF CV and get one dashboard of AI analysis: ATS score, skill gaps, job matches, interview preparation and a career roadmap.',
        intro='I designed the dashboard information architecture and built the front end against my own Python (FastAPI) back end, which calls Gemini for resume analysis.',
        desktop='assets/job0_d.jpg', mobile='assets/j_m.jpg', mobile2='',
        decisions=[
            ('Explain the pipeline up front', 'The landing page frames the product as four steps, upload to offer, so users know what happens to their CV before they hand it over.'),
            ('One dashboard, grouped sidebar', 'Workspace, Career and Growth groups keep ten destinations scannable, with a command-style search and quick actions for the three tasks people repeat.'),
            ('Numbers that answer the question', 'The dashboard leads with resume score, ATS score and matched jobs, the things a user came to check, instead of a welcome banner.'),
            ('Handle failure in the interface', 'PDF upload is capped at 5 MB, and when the analysis API is unavailable the screen says so with retry and re-upload paths, not a spinner forever.'),
            ('Comfort for long sessions', 'Light and dark themes, a language switcher and a calm indigo palette for a tool people use repeatedly while job hunting.'),
        ],
        shots=[
            ('assets/j_s0.jpg', 'Dashboard preview', 'Resume score, ATS score, matched jobs and AI insights in one glance.'),
            ('assets/j_s1.jpg', 'Feature cards', 'Six features, each with one headline number and a plain explanation.'),
            ('assets/j_s3.jpg', 'Guided journey', 'A four-step flow that sets expectations early.'),
        ],
    ),
]

CONCEPTS = [
    ('assets/01_naira_savings_app.jpg', 'Kobo', 'Savings and goals app', 'Onboarding, goal tracking and transfer confirmation flows for a personal finance app.'),
    ('assets/02_food_delivery_app.jpg', 'ChopNow', 'Food delivery app', 'Restaurant browsing, cart and live order tracking with a map, designed for one-hand use.'),
    ('assets/04_clinic_booking_app.jpg', 'CareSlot', 'Clinic booking app', 'Speciality search, doctor slots and appointment reminders for patients and clinics.'),
]

PROCESS = [
    ('Understand', 'We clarify the users, the goal and the must-have features. If a flow does not make sense, I say so before starting.'),
    ('Wireframe', 'User flow first, then low-fidelity layouts for every screen.'),
    ('Design', 'High-fidelity screens, colour, type and components, light and dark mode.'),
    ('Prototype', 'A clickable prototype you can test with real users before build.'),
    ('Build', 'Responsive React or Next.js, connected to your API, deployed live.'),
    ('Deliver', 'Organised files, handoff notes, and revisions until it is right.'),
]

# ---------------------------------------------------------------- CSS
CSS = r'''
:root{
  --bg:#F6F8FB; --surface:#FFFFFF; --surface-2:#F0F4F8; --ink:#0B1F2A; --ink-2:#48596A;
  --line:rgba(11,31,42,.10); --shadow:0 10px 30px rgba(11,31,42,.08); --shadow-lg:0 30px 70px rgba(11,31,42,.16);
  --nav-bg:rgba(246,248,251,.82); --code:#0E7C7B; --radius:18px;
}
html[data-theme="dark"]{
  --bg:#08161F; --surface:#0F232E; --surface-2:#132C38; --ink:#EAF2F6; --ink-2:#9FB4C0;
  --line:rgba(255,255,255,.12); --shadow:0 10px 30px rgba(0,0,0,.35); --shadow-lg:0 30px 70px rgba(0,0,0,.5);
  --nav-bg:rgba(8,22,31,.8); --code:#2EE6C5;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{background:var(--bg);color:var(--ink);font-family:ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  line-height:1.6;font-size:17px;transition:background .3s,color .3s}
img{display:block;max-width:100%}
a{color:inherit}
.wrap{width:min(1180px,100% - 44px);margin-inline:auto}
section{padding:96px 0}
h1{font-size:clamp(38px,6.6vw,74px);line-height:1.02;letter-spacing:-.035em;font-weight:800}
h2{font-size:clamp(28px,3.7vw,42px);line-height:1.12;letter-spacing:-.025em;font-weight:800}
h3{font-size:20px;font-weight:700;letter-spacing:-.01em}
p{color:var(--ink-2)}
.eyebrow{font-size:12.5px;font-weight:800;letter-spacing:.22em;text-transform:uppercase;color:var(--code)}
.lead{font-size:clamp(17px,1.55vw,20px);line-height:1.65}
.sec-head{max-width:760px;margin-bottom:44px}
.sec-head p{margin-top:14px}

/* nav */
header.nav{position:sticky;top:0;z-index:60;background:var(--nav-bg);backdrop-filter:blur(14px);
  border-bottom:1px solid var(--line)}
.nav-in{display:flex;align-items:center;gap:22px;height:66px}
.brand{display:flex;align-items:center;gap:11px;font-weight:800;letter-spacing:-.02em;text-decoration:none;white-space:nowrap}
.dot{width:30px;height:30px;border-radius:9px;background:linear-gradient(135deg,#0E7C7B,#2EE6C5);display:grid;place-items:center;
  color:#04231f;font-size:13px;font-weight:800;flex:0 0 auto}
nav.links{margin-left:auto;display:flex;gap:4px;overflow-x:auto;scrollbar-width:none}
nav.links::-webkit-scrollbar{display:none}
nav.links a{text-decoration:none;font-size:14.5px;font-weight:600;padding:8px 13px;border-radius:999px;color:var(--ink-2);white-space:nowrap}
nav.links a:hover{color:var(--ink);background:var(--surface-2)}
@media (max-width:720px){nav.links a.pj{display:none}nav.links a{font-size:14px;padding:8px 11px}}
.theme-btn{border:1px solid var(--line);background:var(--surface);color:var(--ink);width:36px;height:36px;border-radius:999px;
  cursor:pointer;display:grid;place-items:center;flex:0 0 auto;transition:transform .2s}
.theme-btn:hover{transform:translateY(-1px)}
.theme-btn .moon{display:none} html[data-theme="dark"] .theme-btn .sun{display:none} html[data-theme="dark"] .theme-btn .moon{display:block}
.cta{display:inline-flex;align-items:center;gap:9px;text-decoration:none;font-weight:700;font-size:15px;padding:12px 20px;border-radius:999px;
  background:var(--ink);color:var(--bg);border:1px solid var(--ink);transition:transform .2s,opacity .2s}
.cta:hover{transform:translateY(-2px)}
.cta.ghost{background:transparent;color:var(--ink);border-color:var(--line)}
.cta.ghost:hover{border-color:var(--ink)}
.nav .cta{padding:9px 16px;font-size:14px}
@media (max-width:980px){.nav .cta{display:none}.brand span.bt{display:none}nav.links{gap:0}}

/* progress bar */
#prog{position:fixed;top:0;left:0;height:2px;background:var(--code);width:0;z-index:70}

/* hero */
.hero{padding:78px 0 84px;position:relative;overflow:hidden}
.hero::after{content:"";position:absolute;inset:-40% -10% auto auto;width:620px;height:620px;border-radius:50%;
  background:radial-gradient(circle at 50% 50%,rgba(46,230,197,.16),transparent 65%);pointer-events:none}
.hero-grid{display:grid;grid-template-columns:1.02fr .98fr;gap:56px;align-items:center}
.hero h1 span{background:linear-gradient(100deg,var(--code),#12B886 60%,#4F46E5);-webkit-background-clip:text;background-clip:text;color:transparent}
.hero .lead{margin:22px 0 0;max-width:560px}
.hero-cta{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:30px}
.chip{font-size:12.5px;font-weight:700;padding:6px 12px;border-radius:999px;background:var(--surface);border:1px solid var(--line);color:var(--ink-2)}
.hero-meta{display:flex;flex-wrap:wrap;gap:8px 20px;margin-top:34px;font-size:14px;color:var(--ink-2)}
.pill-live{display:inline-flex;align-items:center;gap:8px;font-size:13px;font-weight:700;padding:7px 14px;border-radius:999px;
  background:var(--surface);border:1px solid var(--line)}
.pill-live i{width:7px;height:7px;border-radius:50%;background:#22C55E;box-shadow:0 0 0 4px rgba(34,197,94,.18)}
.hero-art{position:relative;aspect-ratio:1/1.02}
.hero-art .b1{position:absolute;left:0;top:6%;width:82%;transform:rotate(-2.2deg);z-index:2}
.hero-art .b2{position:absolute;right:0;top:36%;width:66%;transform:rotate(2.4deg);z-index:3}
.hero-art .ph1{position:absolute;right:6%;bottom:0;width:23%;z-index:4}
.hero-art:hover .b1{transform:rotate(-2.2deg) translateY(-6px)}
.hero-art .b1,.hero-art .b2,.hero-art .ph1{transition:transform .35s ease}
.hero-art:hover .b2{transform:rotate(2.4deg) translateY(6px)}
@media (max-width:1000px){
  .hero-grid{grid-template-columns:1fr;gap:44px}
  .hero-art{aspect-ratio:16/11;max-width:660px}
  .hero-art .b1{width:78%;top:0}.hero-art .b2{top:44%;width:58%}.hero-art .ph1{bottom:-4%;width:20%}
}
@media (max-width:620px){.hero-art{display:none}}

/* keep grid/flex children shrinkable */
.case-cols>*,.case-media,.case-media>*,.shots>*,.shots figure,.cards>*,.steps>*,.hero-grid>*,.phones>*,.clist>*,
.dec,.dec>div,.case-head>div,.frame,.frame img{min-width:0}
.frame img,.phone img{max-width:100%}

/* browser + phone frames */
.frame{background:var(--surface);border:1px solid var(--line);border-radius:14px;overflow:hidden;box-shadow:var(--shadow-lg)}
.frame .bar{height:34px;display:flex;align-items:center;gap:7px;padding:0 13px;background:var(--surface-2);border-bottom:1px solid var(--line)}
.frame .bar i{width:9px;height:9px;border-radius:50%;background:var(--line)}
.frame .bar i:nth-child(1){background:#FF5F57}.frame .bar i:nth-child(2){background:#FEBC2E}.frame .bar i:nth-child(3){background:#28C840}
.frame .bar span{margin-left:12px;font-size:11.5px;font-weight:600;color:var(--ink-2);background:var(--surface);
  border:1px solid var(--line);border-radius:999px;padding:3px 12px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.frame img{width:100%;height:auto;aspect-ratio:16/10;object-fit:cover;object-position:top;display:block;cursor:zoom-in}
.phone{border:9px solid var(--ink);border-radius:38px;overflow:hidden;background:var(--surface);box-shadow:var(--shadow-lg)}
.phone img{width:100%;height:auto;aspect-ratio:9/19;object-fit:cover;object-position:top;cursor:zoom-in}
a.zoom{text-decoration:none;color:inherit;display:block}

/* services */
.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
@media (max-width:1000px){.cards{grid-template-columns:repeat(2,1fr)}}
@media (max-width:560px){.cards{grid-template-columns:1fr}}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:26px;box-shadow:var(--shadow);
  transition:transform .25s,box-shadow .25s}
.card:hover{transform:translateY(-4px);box-shadow:var(--shadow-lg)}
.card .no{font-size:12px;font-weight:800;letter-spacing:.18em;color:var(--code)}
.card h3{margin:10px 0 8px}
.card p{font-size:15.5px;line-height:1.55}

/* case studies */
.case{border-top:1px solid var(--line);padding-top:76px;margin-top:20px}
.case-head{display:flex;flex-wrap:wrap;align-items:flex-end;gap:18px;justify-content:space-between}
.case-tag{display:flex;align-items:center;gap:12px;font-size:13px;font-weight:700;color:var(--ink-2);margin-bottom:12px}
.case-tag b{color:var(--acc);letter-spacing:.16em;text-transform:uppercase;font-size:12px}
.case h2{font-size:clamp(30px,4.6vw,52px)}
.case-links{display:flex;flex-wrap:wrap;gap:10px}
.case-links .cta{padding:10px 17px;font-size:14px}
.case-cols{display:grid;grid-template-columns:.86fr 1.14fr;gap:44px;margin-top:38px;align-items:start}
@media (max-width:960px){.case-cols{grid-template-columns:1fr;gap:30px}}
.block+.block{margin-top:24px}
.block h4{font-size:12px;font-weight:800;letter-spacing:.19em;text-transform:uppercase;color:var(--acc);margin-bottom:7px}
.block p{font-size:16.5px}
.role-line{font-size:15px;color:var(--ink-2);margin-top:26px;padding-top:20px;border-top:1px dashed var(--line)}
.case-media{display:grid;grid-template-columns:1fr;gap:18px}
.case-media .phones{display:grid;grid-template-columns:repeat(auto-fit,minmax(0,168px));gap:16px;justify-content:start;margin-top:2px}
@media (max-width:420px){.case-media .phones{grid-template-columns:repeat(auto-fit,minmax(0,1fr))}}
.shots{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:40px}
@media (max-width:960px){.shots{grid-template-columns:1fr}}
.shot figcaption{margin-top:12px}
.shot figcaption b{display:block;font-size:16px;font-weight:700}
.shot figcaption span{font-size:14.5px;color:var(--ink-2)}
.decisions{margin-top:44px;display:grid;grid-template-columns:repeat(2,1fr);gap:14px 30px}
@media (max-width:860px){.decisions{grid-template-columns:1fr}}
.dec{display:flex;gap:13px;padding:16px 0;border-top:1px solid var(--line)}
.dec .k{flex:0 0 auto;width:26px;height:26px;border-radius:8px;background:var(--acc-soft);color:var(--acc);
  display:grid;place-items:center;font-size:12px;font-weight:800}
.dec b{display:block;font-size:16px;margin-bottom:3px}
.dec p{font-size:15px;line-height:1.55}

/* concepts */
.concepts .cards{grid-template-columns:repeat(3,1fr)}
@media (max-width:900px){.concepts .cards{grid-template-columns:1fr}}
.concepts .card{padding:0;overflow:hidden}
.concepts .card img{aspect-ratio:16/9.4;object-fit:cover;width:100%;height:auto}
.concepts .card .pad{padding:22px 24px 26px}
.note{margin-top:26px;background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--code);
  border-radius:12px;padding:18px 22px;font-size:15px}

/* process */
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
@media (max-width:900px){.steps{grid-template-columns:1fr}}
.step{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:24px;position:relative}
.step .n{font-size:13px;font-weight:800;color:var(--code);letter-spacing:.1em}
.step h3{margin:8px 0 6px}
.step p{font-size:15.5px}

/* contact */
.contact-box{background:linear-gradient(135deg,#08161F,#0E3B43);color:#fff;border-radius:26px;padding:clamp(30px,5vw,62px);
  display:grid;grid-template-columns:1.15fr .85fr;gap:40px;align-items:center;overflow:hidden;position:relative}
@media (max-width:860px){.contact-box{grid-template-columns:1fr}}
.contact-box h2{color:#fff}
.contact-box p{color:#B6C6CE;margin-top:14px}
.contact-box .cta{background:#2EE6C5;border-color:#2EE6C5;color:#052a25}
.contact-box .cta.ghost{background:transparent;color:#fff;border-color:rgba(255,255,255,.28)}
.clist{display:grid;gap:12px}
.clist a,.clist div{display:flex;align-items:center;gap:12px;font-size:15px;min-width:0;overflow-wrap:anywhere;text-decoration:none;color:#DCE8EE;
  background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:12px;padding:13px 16px;transition:background .2s}
.clist a:hover{background:rgba(255,255,255,.12)}
.clist svg{flex:0 0 auto;opacity:.8}
.clist span{min-width:0}
@media (max-width:560px){.clist a,.clist div{font-size:13.5px;padding:12px 14px}
  .clist a span{font-size:12.5px;white-space:nowrap;overflow-wrap:normal}}
footer{padding:34px 0 46px;border-top:1px solid var(--line);font-size:14px;color:var(--ink-2)}
.foot-row{display:flex;flex-wrap:wrap;gap:12px;justify-content:space-between;align-items:center}

/* lightbox */
#lb{position:fixed;inset:0;background:rgba(6,15,20,.92);display:none;z-index:100;padding:26px;place-items:center}
#lb.on{display:grid}
#lb img{max-width:min(1500px,96vw);max-height:88vh;width:auto;height:auto;object-fit:contain;border-radius:10px;box-shadow:0 30px 80px rgba(0,0,0,.6)}
#lb .cap{color:#CBD9E0;font-size:14px;margin-top:14px;text-align:center}
#lb button{position:absolute;top:18px;right:22px;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);
  color:#fff;width:40px;height:40px;border-radius:999px;font-size:20px;cursor:pointer}
#lb .nav-ar{position:static;width:44px;height:44px;font-size:22px;top:auto;right:auto}
#lb .row{display:flex;align-items:center;gap:18px}

/* reveal */
html.js [data-reveal]{opacity:0;transform:translateY(18px);transition:opacity .6s ease,transform .6s ease}
html.js [data-reveal].in{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}html.js [data-reveal]{opacity:1;transform:none}
  .card:hover,.hero-art .b1,.hero-art .b2{transform:none!important}}
:focus-visible{outline:2px solid var(--code);outline-offset:3px;border-radius:6px}
section[id],.case[id],main[id]{scroll-margin-top:86px}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
'''

# ---------------------------------------------------------------- JS
JS = r'''
document.documentElement.classList.add('js');
// theme
(function(){
  var k='aa-theme', root=document.documentElement;
  var saved=localStorage.getItem(k);
  if(saved){root.setAttribute('data-theme',saved);}
  else if(window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches){root.setAttribute('data-theme','dark');}
  document.querySelectorAll('[data-theme-toggle]').forEach(function(b){
    b.addEventListener('click',function(){
      var n=root.getAttribute('data-theme')==='dark'?'light':'dark';
      root.setAttribute('data-theme',n);localStorage.setItem(k,n);
    });
  });
})();
// scroll progress
(function(){
  var p=document.getElementById('prog');
  function upd(){var h=document.documentElement;var m=h.scrollHeight-h.clientHeight;
    p.style.width=(m>0?(h.scrollTop/m*100):0)+'%';}
  addEventListener('scroll',upd,{passive:true});addEventListener('resize',upd);upd();
})();
// reveal on scroll
(function(){
  var els=document.querySelectorAll('[data-reveal]');
  if(!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('in')});return;}
  var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target);}});},{threshold:.12,rootMargin:'0px 0px -40px 0px'});
  els.forEach(function(e){io.observe(e)});
})();
// lightbox
(function(){
  var lb=document.getElementById('lb'), img=lb.querySelector('img'), cap=lb.querySelector('.cap');
  var items=[].slice.call(document.querySelectorAll('[data-full]')), cur=0;
  function open(i){cur=(i+items.length)%items.length;var el=items[cur];
    img.src=el.getAttribute('data-full'); img.alt=el.getAttribute('data-cap')||'';
    cap.textContent=(el.getAttribute('data-cap')||'')+'  ('+(cur+1)+' of '+items.length+')';
    lb.classList.add('on'); document.body.style.overflow='hidden';}
  function close(){lb.classList.remove('on');document.body.style.overflow='';}
  items.forEach(function(el,i){el.addEventListener('click',function(ev){ev.preventDefault();open(i);});});
  lb.addEventListener('click',function(e){if(e.target===lb||e.target.tagName==='IMG')close();});
  lb.querySelector('[data-close]').addEventListener('click',close);
  lb.querySelector('[data-prev]').addEventListener('click',function(e){e.stopPropagation();open(cur-1);});
  lb.querySelector('[data-next]').addEventListener('click',function(e){e.stopPropagation();open(cur+1);});
  addEventListener('keydown',function(e){if(!lb.classList.contains('on'))return;
    if(e.key==='Escape')close(); if(e.key==='ArrowRight')open(cur+1); if(e.key==='ArrowLeft')open(cur-1);});
  // swipe
  var x0=null; lb.addEventListener('touchstart',function(e){x0=e.touches[0].clientX;},{passive:true});
  lb.addEventListener('touchend',function(e){if(x0===null)return;var dx=e.changedTouches[0].clientX-x0;
    if(Math.abs(dx)>50)open(cur+(dx<0?1:-1)); x0=null;},{passive:true});
})();
// year
document.querySelectorAll('[data-year]').forEach(function(e){e.textContent=new Date().getFullYear();});
'''

# ---------------------------------------------------------------- builders
def frame(img, cap, bar=''):
    label = bar.replace('https://', '') or img
    return (f'<a class="zoom" href="{img}" data-full="{img}" data-cap="{cap}" aria-label="Open {cap} full size">'
            f'<figure class="frame"><div class="bar"><i></i><i></i><i></i>'
            f'<span>{label}</span></div>'
            f'<img src="{img}" alt="{cap}" loading="lazy" width="1600" height="1000"></figure></a>')


def phone(img, cap):
    return (f'<a class="zoom" href="{img}" data-full="{img}" data-cap="{cap}" aria-label="Open {cap} full size">'
            f'<div class="phone"><img src="{img}" alt="{cap}" loading="lazy" width="780" height="1688"></div></a>')


def case_study(p):
    stack = ''.join(f'<span class="chip">{s}</span>' for s in p['stack'])
    dec = ''.join(f'<div class="dec"><div class="k">{i+1:02d}</div><div><b>{t}</b><p>{d}</p></div></div>'
                  for i, (t, d) in enumerate(p['decisions']))
    shots = ''.join(f'<figure class="shot">{frame(im, cap, p["url"])}<figcaption><b>{cap}</b><span>{d}</span></figcaption></figure>'
                    for im, cap, d in p['shots'])
    mob = phone(p['mobile'], f'{p["name"]} on mobile')
    if p['mobile2']:
        mob += phone(p['mobile2'], f'{p["name"]} mobile results list')
    repo = (f'<a class="cta ghost" href="{p["repo"]}" target="_blank" rel="noopener">Source code</a>' if p['repo'] else '')
    return f'''
<article class="case" id="{p['id']}" style="--acc:{p['color']};--acc-soft:{p['accent_soft']}">
  <div class="wrap">
    <div class="case-head" data-reveal>
      <div>
        <div class="case-tag"><b>Case study {p['n']}</b> <span>{p['kind']} &nbsp;&middot;&nbsp; {p['year']}</span></div>
        <h2>{p['name']}</h2>
        <p class="lead" style="max-width:620px;margin-top:10px">{p['tag']}</p>
      </div>
      <div class="case-links">
        <a class="cta" href="{p['url']}" target="_blank" rel="noopener">Open live app
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M7 17 17 7M9 7h8v8"/></svg></a>
        {repo}
      </div>
    </div>
    <div class="case-cols">
      <div data-reveal>
        <div class="block"><h4>The problem</h4><p>{p['problem']}</p></div>
        <div class="block"><h4>The solution</h4><p>{p['solution']}</p></div>
        <div class="block"><h4>What I did</h4><p>{p['intro']}</p></div>
        <div class="block"><h4>Stack</h4><div class="chips" style="margin-top:8px">{stack}</div></div>
        <p class="role-line"><strong>Role:</strong> {p['role']}</p>
      </div>
      <div class="case-media" data-reveal>
        {frame(p['desktop'], f'{p["name"]} desktop interface', p['url'])}
        <div class="phones">{mob}</div>
      </div>
    </div>
    <div class="shots" data-reveal>{shots}</div>
    <div class="decisions" data-reveal>{dec}</div>
  </div>
</article>'''


svc_cards = ''.join(f'<div class="card" data-reveal><div class="no">{i+1:02d}</div><h3>{t}</h3><p>{d}</p></div>'
                    for i, (t, d) in enumerate(SERVICES))
cases = ''.join(case_study(p) for p in PROJECTS)
concept_cards = ''.join(f'<div class="card" data-reveal><img src="{im}" alt="{t} concept screens" loading="lazy">'
                        f'<div class="pad"><h3>{t}</h3><p style="font-weight:700;color:var(--code);font-size:14px;margin:3px 0 7px">{s}</p>'
                        f'<p style="font-size:15px">{d}</p></div></div>' for im, t, s, d in CONCEPTS)
step_cards = ''.join(f'<div class="step" data-reveal><div class="n">{i+1:02d}</div><h3>{t}</h3><p>{d}</p></div>'
                     for i, (t, d) in enumerate(PROCESS))

HTML = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{ME['name']} &mdash; Software Developer &amp; UI/UX Designer</title>
<meta name="description" content="{ME['name']} designs and builds web apps: UI/UX in Figma, front end in React and Next.js. Three live case studies: FuelFinder AI, Mammo Guard and JobLiberty AI.">
<meta name="theme-color" content="#08161F">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='9' fill='%230E7C7B'/%3E%3Ctext x='16' y='22' font-family='sans-serif' font-size='15' font-weight='700' fill='white' text-anchor='middle'%3EAA%3C/text%3E%3C/svg%3E">
<meta property="og:title" content="{ME['name']} &mdash; Software Developer &amp; UI/UX Designer">
<meta property="og:description" content="Design and code from the same person: three live products, from user flow to deployed app.">
<meta property="og:type" content="website">
<meta property="og:image" content="assets/f_light.jpg">
<style>{CSS}</style>
</head>
<body>
<div id="prog"></div>
<header class="nav">
  <div class="wrap nav-in">
    <a class="brand" href="#top"><span class="dot">AA</span> <span class="bt">{ME['name'].split()[0]} {ME['name'].split()[1]}</span></a>
    <nav class="links" aria-label="Sections">
      <a href="#services">Services</a>
      <a class="pj" href="#fuel">FuelFinder AI</a>
      <a class="pj" href="#mammo">Mammo Guard</a>
      <a class="pj" href="#job">JobLiberty AI</a>
      <a href="#concepts">Concepts</a>
      <a href="#process">Process</a>
      <a href="#contact">Contact</a>
    </nav>
    <button class="theme-btn" data-theme-toggle aria-label="Switch between light and dark theme">
      <svg class="sun" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4.2"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M19.1 4.9l-1.4 1.4M6.3 17.7l-1.4 1.4"/></svg>
      <svg class="moon" width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 14.5A8.2 8.2 0 0 1 9.5 4a8.3 8.3 0 1 0 10.5 10.5Z"/></svg>
    </button>
    <a class="cta" href="mailto:{ME['email']}">Hire me</a>
  </div>
</header>

<main id="top">
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="pill-live"><i></i> 3 products live in your browser right now</span>
      <h1 style="margin-top:20px">I design the interface,<br>then <span>I build it.</span></h1>
      <p class="lead">Software developer and UI/UX designer. Flow, wireframe, high-fidelity screens, then a
      responsive React or Next.js build that is actually deployed &mdash; so the shipped product still looks like the design.</p>
      <div class="hero-cta">
        <a class="cta" href="#fuel">See the case studies</a>
        <a class="cta ghost" href="mailto:{ME['email']}">Start a project</a>
      </div>
      <div class="chips">
        <span class="chip">React</span><span class="chip">Next.js</span><span class="chip">TypeScript</span>
        <span class="chip">Tailwind CSS</span><span class="chip">Python / FastAPI</span><span class="chip">Figma</span>
      </div>
      <div class="hero-meta"><span>{ME['city']}</span><span>&middot;</span><span>3MTT NextGen Software Development Fellow</span></div>
    </div>
    <div class="hero-art" aria-hidden="true">
      <div class="b1"><figure class="frame"><div class="bar"><i></i><i></i><i></i><span>fuel-station-finder-omega.vercel.app</span></div><img src="assets/f_light.jpg" alt="" width="1600" height="1000"></figure></div>
      <div class="b2"><figure class="frame"><div class="bar"><i></i><i></i><i></i><span>jobliberty.vercel.app</span></div><img src="assets/job0_d.jpg" alt="" width="1440" height="900"></figure></div>
      <div class="ph1"><div class="phone"><img src="assets/m_m.jpg" alt="" width="780" height="1688"></div></div>
    </div>
  </div>
</section>

<section id="services">
  <div class="wrap">
    <div class="sec-head" data-reveal><div class="eyebrow">How I can help</div>
      <h2 style="margin-top:12px">Design and build, from one person</h2>
      <p>Hire me for the screens, the code, or both. Every engagement ends with files a developer can use and
      decisions written down, not just a picture of an app.</p></div>
    <div class="cards">{svc_cards}</div>
  </div>
</section>

<section id="work" style="padding-top:24px">
  <div class="wrap">
    <div class="sec-head" data-reveal style="margin-bottom:0">
      <div class="eyebrow">Selected work</div>
      <h2 style="margin-top:12px">Three live products, end to end</h2>
      <p>Each case study below is a real, deployed app: what the problem was, the interface decisions I made and
      screenshots taken from the live site on desktop and mobile.</p>
    </div>
  </div>
  {cases}
</section>

<section id="concepts" class="concepts">
  <div class="wrap">
    <div class="sec-head" data-reveal><div class="eyebrow">More UI/UX work</div>
      <h2 style="margin-top:12px">Concept designs</h2>
      <p>Practice projects exploring mobile app patterns for Nigerian users: savings, food delivery and clinic booking.</p></div>
    <div class="cards">{concept_cards}</div>
    <p class="note"><strong>Clear labelling:</strong> the three concepts above are AI-assisted visual mockups I made to
    explore layout and flow, not client deliveries. Everything in the case studies section is a working application
    you can open and use.</p>
  </div>
</section>

<section id="process">
  <div class="wrap">
    <div class="sec-head" data-reveal><div class="eyebrow">Working together</div>
      <h2 style="margin-top:12px">A simple process, clear communication</h2>
      <p>You always know what stage we are at and what comes next.</p></div>
    <div class="steps">{step_cards}</div>
  </div>
</section>

<section id="contact">
  <div class="wrap">
    <div class="contact-box" data-reveal>
      <div>
        <h2>Let us build your product.</h2>
        <p>Tell me the users and the problem. I will come back with a flow, a fixed price and a date.</p>
        <div class="hero-cta">
          <a class="cta" href="mailto:{ME['email']}">Email me</a>
          <a class="cta ghost" href="https://www.fiverr.com" target="_blank" rel="noopener">Find me on Fiverr</a>
        </div>
      </div>
      <div class="clist">
        <a href="mailto:{ME['email']}"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2.5" y="4.5" width="19" height="15" rx="2.5"/><path d="m3 7 9 6 9-6"/></svg> <span>{ME['email']}</span></a>
        <a href="tel:{ME['phone'].replace(' ','')}"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 3h3.5l1.8 4.4-2 1.4a13 13 0 0 0 6.9 6.9l1.4-2L21 15.5V19a2 2 0 0 1-2.2 2A17 17 0 0 1 3 5.2 2 2 0 0 1 5 3Z"/></svg> <span>{ME['phone']}</span></a>
        <a href="{ME['gh']}" target="_blank" rel="noopener"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-3.2 19.5c.5.1.7-.2.7-.5v-2c-2.8.6-3.4-1.2-3.4-1.2-.4-1.2-1.1-1.5-1.1-1.5-.9-.6.1-.6.1-.6 1 .1 1.5 1 1.5 1 .9 1.5 2.4 1.1 3 .8.1-.7.4-1.1.6-1.4-2.2-.2-4.6-1.1-4.6-4.9 0-1.1.4-2 1-2.7-.1-.3-.4-1.3.1-2.7 0 0 .8-.3 2.7 1a9.4 9.4 0 0 1 5 0c1.9-1.3 2.7-1 2.7-1 .5 1.4.2 2.4.1 2.7.6.7 1 1.6 1 2.7 0 3.8-2.4 4.7-4.6 4.9.4.3.7 1 .7 2v2.9c0 .3.2.6.7.5A10 10 0 0 0 12 2Z"/></svg> <span>github.com/bynarycoder</span></a>
        <a href="{ME['li']}" target="_blank" rel="noopener"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M4.8 3.5a2.3 2.3 0 1 1 0 4.6 2.3 2.3 0 0 1 0-4.6ZM3 9.3h3.7V21H3V9.3Zm6.2 0h3.5v1.6a3.9 3.9 0 0 1 3.5-1.9c3 0 3.6 1.9 3.6 4.7V21h-3.7v-6c0-1.5-.3-2.6-1.8-2.6s-1.9 1-1.9 2.5V21H9.2V9.3Z"/></svg> <span>LinkedIn profile</span></a>
        <div><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.2 2"/></svg> <span>Replies within a day, {ME['city']}</span></div>
      </div>
    </div>
  </div>
</section>
</main>

<footer>
  <div class="wrap foot-row">
    <span>&copy; <span data-year>2026</span> {ME['name']} &nbsp;|&nbsp; Software Developer and UI/UX Designer</span>
    <a href="#top" style="text-decoration:none;font-weight:600">Back to top &uarr;</a>
  </div>
</footer>

<div id="lb" role="dialog" aria-modal="true" aria-label="Screenshot viewer">
  <button data-close aria-label="Close viewer">&times;</button>
  <div class="row">
    <button class="nav-ar" data-prev aria-label="Previous screenshot">&#8249;</button>
    <div style="text-align:center"><img src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" alt=""><div class="cap"></div></div>
    <button class="nav-ar" data-next aria-label="Next screenshot">&#8250;</button>
  </div>
</div>
<script>{JS}</script>
</body>
</html>'''

open(os.path.join(OUT, 'index.html'), 'w').write(HTML)
print('index.html written:', len(HTML), 'bytes')
