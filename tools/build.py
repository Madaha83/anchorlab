"""Generator for anchorlab.science.

Run:  python tools/build.py
Writes plain, hand-editable HTML into site/. Content lives in this file (pages)
and tools/pubdata.py (publications, shared with matthewdhanson.com).
Rules: ANCHOR is spelled out as EXPANSION below (working name; may change); no URI logos; no student names,
photos, or partner names without written permission.
"""
from pathlib import Path
import html, json, re, sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pubdata import ARTICLES, CHAPTERS, REPORTS, REVIEW, TALKS, POSTERS, pub_li, group  # noqa: E402

SITE = Path(__file__).resolve().parents[1] / "site"
URL = "https://anchorlab.science"
EMAIL = "matthew.hanson@uri.edu"
PERSONAL = "https://matthewdhanson.com"
YEAR = 2026
UPDATED = "October 2026"
PLAUSIBLE = "https://plausible.io/js/pa-GkYF17wRYqotwuI0Cg_Py.js"   # setup line lives in site.js (CSP-safe)
EXPANSION = "Awareness, Needs, and Competencies for Human and Organizational Resources"

# Anchor mark, modeled on the plain anchor of Rhode Island's flag and seal: ring,
# stock with ball ends (accent color), shank, curved arms with flukes, crown point.
MARK = ('<svg viewBox="0 0 32 32" aria-hidden="true" focusable="false">'
        '<g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">'
        '<circle cx="16" cy="4.4" r="2.2" stroke-width="1.9"/>'
        '<path d="M16 6.6 V27.4" stroke-width="2.6"/>'
        '<path d="M6.4 20.6 C7.6 25.9 11.4 27.9 16 27.9 C20.6 27.9 24.4 25.9 25.6 20.6" stroke-width="2.3"/></g>'
        '<g fill="currentColor"><path d="M14.6 27.6 L16 30.6 L17.4 27.6 Z"/>'
        '<path d="M6 16.4 L9.6 21.6 Q7.4 21.2 6.5 22.9 Q5.4 21.4 3.1 21.9 Z"/>'
        '<path d="M26 16.4 L22.4 21.6 Q24.6 21.2 25.5 22.9 Q26.6 21.4 28.9 21.9 Z"/></g>'
        '<g class="mk-datum"><path d="M9.4 10.4 H22.6" stroke-width="2.2" stroke-linecap="round"/>'
        '<circle cx="8.4" cy="10.4" r="1.55" stroke="none"/><circle cx="23.6" cy="10.4" r="1.55" stroke="none"/></g></svg>')

NAV = [("/research.html", "Research", "research"), ("/people.html", "People", "people"),
       ("/publications.html", "Publications", "publications"), ("/join.html", "Get involved", "join"),
       ("/partners.html", "Partners", "partners")]


def head(title, desc, path, extra=""):
    canonical = URL + ("/" if path == "" else "/" + path)
    noindex = "noindex" in extra
    plausible = f'\n<script async src="{PLAUSIBLE}"></script>' if PLAUSIBLE else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{html.escape(desc)}">
{"" if noindex else f'<link rel="canonical" href="{canonical}">'}
<meta property="og:type" content="website">
<meta property="og:site_name" content="ANCHOR Lab">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
{"" if noindex else f'<meta property="og:url" content="{canonical}">'}
<meta property="og:image" content="{URL}/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="ANCHOR Lab, University of Rhode Island College of Business">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#F3F5F4" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0A1520" media="(prefers-color-scheme: dark)">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400;0,500;0,600;1,400&family=Newsreader:ital,opsz,wght@0,6..72,400..600;1,6..72,400&display=swap">
<link rel="stylesheet" href="/style.css">
<script src="/site.js"></script>{plausible}{extra}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
"""


def header(active):
    items = []
    for href, label, key in NAV:
        cur = ' aria-current="page"' if key == active else ""
        items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    items.append('<li><a class="nav-cta" href="/join.html#apply">Apply</a></li>')
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="wordmark" href="/index.html"{' aria-current="page"' if active == "home" else ""}>{MARK}<span>ANCHOR <i>Lab</i></span></a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav class="site-nav" id="site-nav" aria-label="Primary">
      <ul>
        {chr(10).join('        ' + i for i in items).strip()}
      </ul>
    </nav>
  </div>
</header>
"""


ANALYTICS_NOTE = ('      <p class="disclaimer">This site uses privacy-friendly, cookie-free analytics; no personal data is collected.</p>\n' if PLAUSIBLE else "")

FOOTER = f"""<footer class="site-footer" id="contact">
  <div class="wrap">
    <div>
      <p class="affil">ANCHOR: {EXPANSION}.</p>
      <p class="affil">The ANCHOR Lab is led by Matthew D. Hanson, Ph.D., Assistant Professor of Human Resource Management, College of Business, University of Rhode Island, Kingston, RI.</p>
      <p>Contact: <a href="mailto:{EMAIL}">{EMAIL}</a> &middot; <a href="{PERSONAL}">matthewdhanson.com</a></p>
      <p class="disclaimer">anchorlab.science is a faculty research-lab website maintained by Dr. Matthew D. Hanson. It is not an official University of Rhode Island website, and views expressed here do not necessarily reflect those of the University of Rhode Island.</p>
{ANALYTICS_NOTE}    </div>
    <ul>
      <li><a href="/research.html">Research</a></li>
      <li><a href="/people.html">People</a></li>
      <li><a href="/join.html">Get involved</a></li>
      <li><a href="/partners.html">Partners</a></li>
    </ul>
    <p>&copy; {YEAR} ANCHOR Lab &middot; Updated {UPDATED}</p>
  </div>
</footer>
</body>
</html>
"""


def write(name, content):
    (SITE / name).write_text(content, encoding="utf-8", newline="\n")
    print("wrote", name, len(content))


# ───────────────────────── Content ─────────────────────────
AREAS = [
    ("assessment", "Fair and accurate assessment",
     "How do we know a test measures something real, and treats people fairly?",
     "Organizations make hiring, development, and promotion decisions based on assessments, so those tools need to work. We build and evaluate them: defining what good performance looks like, writing items that capture it, and testing whether scores are reliable, valid, and fair across groups. This work grows out of Dr. Hanson's experience building assessments for military organizations, and the lab now asks the same questions in public-sector and business settings.",
     ["Do leader assessment scores predict later performance equally well for different groups?",
      "How do design and recruitment choices affect data quality and whose experiences are represented?"]),
    ("leadership", "Leadership competencies and AI-assisted feedback",
     "What does good leadership look like in a given role, and can AI help people develop it?",
     "“Good leadership” looks different from one role to the next. Defining role-specific competencies first is what makes later selection and feedback defensible. We study how competency models are built and validated, and how assessment feedback can serve as a development tool, not only a gate. A newer thread asks whether large language models, paired with validated assessments, can give personalized feedback to many more people without lowering the standards that make it trustworthy.",
     ["Can conversational AI administer an assessment and give feedback that is accurate and useful?",
      "Can AI help translate competency models into practical guidance, such as resume advice for service members moving into civilian careers?"]),
    ("needs", "Motivation, needs, and recovery",
     "Can a good life outside work make up for needs that go unmet at work?",
     "Self-determination theory holds that people need autonomy, competence, and relatedness. We study how meeting those needs, at work and away from it, shapes motivation, burnout, recovery, and well-being. Dr. Hanson's dissertation found that need satisfaction outside work predicted better recovery overall, but it did not make up for the specific needs that work left unmet. The lab is now testing that question day by day in a daily diary study, and extending it to work design, management practices, and recovery in demanding jobs.",
     ["Which features of work design best support autonomy, competence, and connection?",
      "How do need satisfaction and motivation relate to burnout in high-demand occupations?"]),
    ("learning", "Training and workplace learning",
     "What keeps attention on the task when learning happens on a screen and nobody is watching?",
     "A growing share of workplace learning is self-paced and online, where distraction is the default. We study how attention, mindfulness, and self-regulation shape what people take away from training, and what helps people adapt under pressure. Earlier work showed that off-task attention is especially costly in self-directed learning. The lab builds on a published model of “mindful training” and tests its limits: when, and for whom, these approaches improve learning.",
     ["Does mindfulness help training because of the practice itself, or because of the label?",
      "How can informal, on-the-job learning be supported and measured?"]),
]

PROJECTS = [
    ("Practice, label, or placebo? Mindfulness in training", "learning", "review", "Under review",
     "A 2×2 experiment in an air traffic control simulation that separates the effects of actual mindfulness practice from simply calling an activity “mindfulness.”", None),
    ("Need satisfaction at work and away from it", "needs", "dev", "In progress",
     "A two-study project on whether meeting psychological needs outside work can make up for needs unmet at work. Study 1, a time-lagged survey, is being revised. Study 2, a daily diary study built with lab students, is in preparation for ethics review.", None),
    ("AI-assisted assessment and feedback", "leadership", "dev", "In development",
     "Building on a proof-of-concept platform, this project will test whether large language models paired with validated assessments can give accurate, personalized developmental feedback at scale.", None),
    ("Validity and fairness in leader assessment", "assessment", "dev", "In development",
     "A planned line of studies on whether leadership assessments predict outcomes equally well across groups, and how to make results clearer for the people who use them.", None),
    ("Did more competition close the strength gap?", "assessment", "done", "Completed",
     "An analysis of 2.7 million powerlifting results asking how much of women’s gains reflect a bigger talent pool and how much reflect real improvement.", PERSONAL + "/strength"),
    ("Do women’s records catch up?", "learning", "done", "Completed",
     "World-record histories in 28 events, modeled as catch-up curves to show how fast the performance gap closed and where it levels off.", PERSONAL + "/records"),
]
AREA_NAME = {k: n for k, n, *_ in AREAS}


def project_card(p):
    title, area, cls, label, text, link = p
    t = f'<a href="{link}">{title}</a>' if link else title
    go = f'<a class="go" href="{link}">Read the analysis &rarr;</a>' if link else ""
    return f"""      <article class="project">
        <span class="status {cls}">{label}</span>
        <h3>{t}</h3>
        <p>{text}</p>
        <p class="meta">{AREA_NAME[area]}</p>
        {go}
      </article>"""


# ───────────────────────── Home ─────────────────────────
jsonld = '\n<script type="application/ld+json">\n' + json.dumps({
    "@context": "https://schema.org", "@type": "ResearchOrganization", "name": "ANCHOR Lab", "alternateName": f"{EXPANSION} (ANCHOR) Lab", "url": URL + "/",
    "description": "A research lab at the University of Rhode Island College of Business studying how people are assessed, developed, and supported at work.",
    "parentOrganization": {"@type": "CollegeOrUniversity", "name": "University of Rhode Island"},
    "founder": {"@type": "Person", "name": "Matthew D. Hanson", "url": PERSONAL + "/"},
    "email": EMAIL}, indent=1) + "\n</script>"

home = head("ANCHOR Lab · University of Rhode Island",
            "The ANCHOR Lab at URI studies how people are assessed, developed, and supported at work, with students as full members of the research team.",
            "", jsonld) + header("home") + f"""
<main id="main">
<section class="lab-hero">
  <div class="wrap hero-grid">
    <div>
    <span class="datum" aria-hidden="true"></span>
    <p class="eyebrow">University of Rhode Island &middot; College of Business</p>
    <p class="expansion"><abbr title="{EXPANSION}">ANCHOR</abbr>: {EXPANSION}</p>
    <h1>Better ways to measure, develop, and support people at work.</h1>
    <p class="lede">The ANCHOR Lab studies fair and accurate assessment, leadership, motivation and recovery, and workplace learning. We do careful science on practical questions, with students as full members of the team.</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="/join.html#apply">Apply to the lab</a>
      <a class="btn btn-secondary" href="/partners.html">Partner with us</a>
    </div>
    </div>
    <div class="hero-mark">{MARK}</div>
  </div>
</section>

<section class="section" aria-labelledby="areas-h">
  <div class="wrap">
    <p class="eyebrow">Research</p>
    <h2 id="areas-h">What we study</h2>
    <div class="areas">
""" + "\n".join(f"""      <article class="area">
        <span class="num">0{i + 1}</span>
        <h3>{name}</h3>
        <p class="q">{q}</p>
        <a class="more" href="/research.html#{key}">Projects &rarr;</a>
      </article>""" for i, (key, name, q, *_rest) in enumerate(AREAS)) + f"""
    </div>
  </div>
</section>

<section class="section" aria-labelledby="students-h">
  <div class="wrap section-grid">
    <div class="section-label">
      <p class="eyebrow">For students</p>
      <h2 id="students-h">What students do here</h2>
      <p>Our founding cohort joined in Fall 2026. Applications are open for future cohorts.</p>
    </div>
    <div>
      <p class="prose">Lab members work on real research, from designing a study to presenting what it found. College of Business students can join for 1 to 3 credits a semester through MGT 491 (fall) or MGT 492 (spring) Directed Study, and students from any major can join as volunteers. You don&rsquo;t need prior research experience. <strong>New to research? That&rsquo;s who this is for.</strong></p>
      <ul class="skills">
        <li><strong>Design studies</strong><span>Build surveys and experiments on leadership, motivation, and training.</span></li>
        <li><strong>Work with data</strong><span>Collect, clean, and analyze data in R or SPSS.</span></li>
        <li><strong>Share findings</strong><span>Help prepare posters, presentations, and papers.</span></li>
      </ul>
      <div class="btn-row"><a class="btn btn-primary" href="/join.html#apply">Apply to the lab</a> <a class="btn btn-secondary" href="/join.html">How it works</a></div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="proj-h">
  <div class="wrap">
    <p class="eyebrow">Projects</p>
    <h2 id="proj-h">Current and recent work</h2>
    <div class="project-grid">
{chr(10).join(project_card(p) for p in PROJECTS[:4])}
    </div>
    <p><a class="more" href="/research.html">All research &rarr;</a></p>
  </div>
</section>

<section class="section" aria-labelledby="cta-h">
  <div class="wrap">
    <h2 id="cta-h" class="visually-hidden">Get involved</h2>
    <div class="split-cta">
      <div>
        <p class="eyebrow">Students</p>
        <h3>Apply for a future cohort</h3>
        <p>Our founding cohort is in place. Undergraduate and graduate students from any major can apply now for a future cohort; it takes about five minutes.</p>
        <a class="btn btn-primary" href="/join.html#apply">Apply to the lab</a>
      </div>
      <div class="partner">
        <p class="eyebrow">Organizations</p>
        <h3>Let&rsquo;s study what works</h3>
        <p>We work with Rhode Island employers and public agencies on questions about selection, development, and well-being.</p>
        <a class="btn btn-secondary" href="/partners.html">Partner with us</a>
      </div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="dir-h">
  <div class="wrap">
    <p class="eyebrow" aria-hidden="true">Lab director</p>
    <h2 id="dir-h" class="visually-hidden">Lab director</h2>
    <article class="person">
      <img src="/hanson-480.jpg" width="480" height="600" alt="Matthew D. Hanson" loading="lazy" decoding="async">
      <div>
        <h3>Matthew D. Hanson, Ph.D.</h3>
        <p class="role">Lab Director</p>
        <p>Assistant Professor of Human Resource Management, College of Business, University of Rhode Island. He studies how organizations assess, develop, and support people.</p>
        <p><a href="/people.html">More about the team &rarr;</a> &middot; <a href="{PERSONAL}">Personal website</a></p>
      </div>
    </article>
  </div>
</section>
</main>
""" + FOOTER
write("index.html", home)

# ───────────────────────── Research ─────────────────────────
def area_section(i, a):
    key, name, q, body, questions = a
    projs = [p for p in PROJECTS if p[1] == key]
    plist = ("\n    <div class=\"project-grid\">\n" + "\n".join(project_card(p) for p in projs) + "\n    </div>") if projs else ""
    qs = "".join(f"<li>{x}</li>" for x in questions)
    return f"""<section class="section" id="{key}" aria-labelledby="{key}-h">
  <div class="wrap section-grid">
    <div class="section-label">
      <p class="eyebrow">0{i + 1}</p>
      <h2 id="{key}-h">{name}</h2>
    </div>
    <div>
      <p class="prose q-lead"><em>{q}</em></p>
      <p class="prose">{body}</p>
      <div class="key-work"><h3>Current questions</h3><ul>{qs}</ul></div>{plist}
    </div>
  </div>
</section>"""


research = head("Research · ANCHOR Lab", "Research on fair assessment, leadership competencies, AI-assisted feedback, psychological needs, recovery, and workplace learning.",
                "research") + header("research") + f"""
<main id="main">
<section class="page-intro">
  <div class="wrap">
    <p class="eyebrow">Research</p>
    <h1>Careful science on practical questions about people at work.</h1>
    <p class="lede">We run experiments and surveys, build and test assessments, and analyze data. Every study with people is approved by URI&rsquo;s research ethics board (the IRB) before it begins.</p>
  </div>
</section>
{chr(10).join(area_section(i, a) for i, a in enumerate(AREAS))}
</main>
""" + FOOTER
write("research.html", research)

# ───────────────────────── People ─────────────────────────
people = head("People · ANCHOR Lab", "Meet the ANCHOR Lab team at URI's College of Business, led by Matthew D. Hanson, Ph.D., and learn how students can join.",
              "people") + header("people") + f"""
<main id="main">
<section class="page-intro">
  <div class="wrap">
    <p class="eyebrow">People</p>
    <h1>The team</h1>
    <p class="lede">Our founding cohort of student researchers joined in Fall 2026.</p>
  </div>
</section>
<section class="section pt-1">
  <div class="wrap">
    <article class="person">
      <img src="/hanson-480.jpg" width="480" height="600" alt="Matthew D. Hanson" loading="lazy" decoding="async">
      <div>
        <h2>Matthew D. Hanson, Ph.D.</h2>
        <p class="role">Lab Director</p>
        <p>Matthew Hanson is the Fred &rsquo;78 and Sue Newton Assistant Professor of Human Resource Management in URI&rsquo;s College of Business, where he directs the ANCHOR Lab and co-directs the College of Business Behavioral Lab. He studies how organizations assess, develop, and support people, with a focus on leadership assessment, training, and motivation and recovery.</p>
        <p>Before joining URI in 2026, he was a research psychologist with the U.S. Army, where he led the development and validation of leadership assessments. Earlier, with Leidos at the Naval Submarine Medical Research Laboratory, he studied assessment, burnout, and training success among submariners. He earned his Ph.D. in industrial-organizational psychology from the University at Albany, SUNY.</p>
        <p><a href="{PERSONAL}">Personal website</a> &middot; <a href="{PERSONAL}/cv">CV</a> &middot; <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
    </article>
    <div class="cohort">
      <h2>Join a future cohort</h2>
      <p>Our founding cohort is in place, and we&rsquo;ll add student researchers in later cohorts. Undergraduate and graduate students from any major are welcome to apply now, and no prior research experience is needed.</p>
      <a class="btn btn-primary" href="/join.html#apply">Apply to the lab</a>
    </div>
  </div>
</section>
</main>
""" + FOOTER
write("people.html", people)

# ───────────────────────── Publications ─────────────────────────
pubs = head("Publications · ANCHOR Lab", "Peer-reviewed articles, technical reports, manuscripts under review, and presentations from the ANCHOR Lab at URI.",
            "publications") + header("publications") + f"""
<main id="main">
<section class="page-intro">
  <div class="wrap">
    <p class="eyebrow">Publications &amp; outputs</p>
    <h1>Research &amp; writing</h1>
    <p class="lede">Our work appears in peer-reviewed journals, technical reports, and conference presentations, and some of it as public data analyses. The list includes published work, manuscripts under review, and talks.</p>
  </div>
</section>
<section class="section pt-1">
  <div class="wrap">
{group("g-articles", "article", "Peer-reviewed articles", ARTICLES)}
{group("g-chapters", "chapter", "Book chapters", CHAPTERS)}
{group("g-reports", "report", "Technical reports", REPORTS)}
{group("g-review", "review", "Manuscripts under review", REVIEW)}
{group("g-talks", "talk", "Conference presentations", TALKS, collapse=True)}
{group("g-posters", "talk", "Conference posters", POSTERS, collapse=True)}
  </div>
</section>
</main>
""" + FOOTER
write("publications.html", pubs)


# ───────────────────────── Join ─────────────────────────
def options(name, items, kind="checkbox", required=False):
    req = " required" if required and kind == "radio" else ""
    return "\n".join(
        f'          <label class="opt"><input type="{kind}" name="{name}" value="{html.escape(v)}"{req}> <span>{t}</span></label>'
        for v, t in items)


def faq(q, a):
    return f"      <details><summary>{q}</summary><p>{a}</p></details>"


join = head("Get involved · ANCHOR Lab", "URI students from any major can join the ANCHOR Lab as volunteers, and College of Business students can earn MGT 491/492 directed-study credit. No experience needed.",
            "join") + header("join") + f"""
<main id="main">
<section class="page-intro">
  <div class="wrap essay-head">
    <p class="eyebrow">Get involved &middot; Applications open for future cohorts</p>
    <h1>Join the lab</h1>
    <p class="lede">Lab members work on real research, from designing a study to presenting what it found. Credit is available through MGT 491 (fall) or MGT 492 (spring) Directed Study for College of Business students, 1 to 3 credits a semester. Students from any major can join as volunteers. No prior research experience is needed.</p>
    <div class="btn-row"><a class="btn btn-primary" href="#apply">Apply now</a></div>
  </div>
</section>

<div class="wrap essay">
  <section class="essay-section" aria-labelledby="do-h">
    <h2 id="do-h">What you&rsquo;ll do</h2>
    <ul>
      <li>Help design surveys, experiments, and assessments on leadership, motivation, burnout, and training</li>
      <li>Collect and manage data, including studies run in the College of Business Behavioral Lab</li>
      <li>Analyze data in R or SPSS and help write up results</li>
      <li>Meet regularly with Dr. Hanson and other lab members</li>
    </ul>
  </section>

  <section class="essay-section" aria-labelledby="sem-h">
    <h2 id="sem-h">A typical first semester</h2>
    <ol class="roadmap">
      <li><span class="wk">Weeks 1&ndash;3</span><span>Lab onboarding and CITI research-ethics training, completed before you work on any study or data</span></li>
      <li><span class="wk">Weeks 4&ndash;8</span><span>Read up on a project&rsquo;s topic and help build a survey or study materials</span></li>
      <li><span class="wk">Weeks 9&ndash;12</span><span>Help collect or clean data and learn to analyze it</span></li>
      <li><span class="wk">Weeks 13&ndash;15</span><span>Present what you worked on at a lab meeting</span></li>
    </ol>
    <p class="muted">Every project is different; this is the general shape.</p>
  </section>

  <section class="essay-section" aria-labelledby="gain-h">
    <h2 id="gain-h">What you&rsquo;ll gain</h2>
    <ul>
      <li><strong>Skills</strong> in research design, survey and assessment development, data management, statistics, and clear scientific writing</li>
      <li><strong>Course credit</strong>, if you choose and you are a College of Business student: 1 to 3 credits a semester through MGT 491 (fall) or MGT 492 (spring) Directed Study, up to 6 credits in total</li>
      <li><strong>Experience presenting</strong> research, with opportunities to contribute to posters and presentations. Members who make a substantial contribution are credited as co-authors.</li>
      <li><strong>A mentor</strong> who knows your work well. Members who contribute for two or more semesters can ask for a detailed letter of recommendation.</li>
    </ul>
  </section>

  <section class="essay-section faq" aria-labelledby="faq-h">
    <h2 id="faq-h">Questions</h2>
{faq("Do I need research experience?", "No. Curiosity, reliability, and attention to detail matter most. We&rsquo;ll teach you the rest.")}
{faq("How does course credit work?", "For College of Business students, lab work counts as a directed study with Dr. Hanson: MGT 491 in the fall and MGT 492 in the spring. You can take 1 to 3 credits a semester, up to 6 credits in total. If you choose credit, we&rsquo;ll walk you through the short directed-study form together before the add/drop deadline. Students from any major can volunteer, which involves the same work without the course.")}
{faq("Is there training before I start?", "Yes. One of the first things every member does is CITI training in research ethics and human-subjects protection. It is completed before anyone works on a study or with data.")}
{faq("Can I do this if I work or have a busy schedule?", "Yes. Most tasks can be done on your own time, and lab meetings are scheduled around members&rsquo; availability. Tell us your constraints on the form; they won&rsquo;t count against you.")}
{faq("Can graduate students join?", "Yes. Master&rsquo;s, MBA, and doctoral students interested in research collaboration are welcome to apply.")}
{faq("How much time does it take?", "Plan on at least 3 to 5 hours a week during the semester. Some members commit more for a larger role on a project.")}
{faq("How are students selected?", "Dr. Hanson reads every application and replies by email. We look for curiosity and reliability, not grades or experience, and we&rsquo;ll match you to a project based on your interests.")}
  </section>

  <section class="essay-section" id="apply" aria-labelledby="apply-h">
    <h2 id="apply-h">Apply</h2>
    <p class="muted">Our founding cohort joined in Fall 2026, so new applications are for future cohorts. The form takes about five minutes, and Dr. Hanson will be in touch as the next cohort takes shape.</p>

    <form class="lab-form" name="lab-application" method="POST" action="/join-thanks.html"
          data-netlify="true" netlify-honeypot="company">
      <input type="hidden" name="form-name" value="lab-application">
      <p class="hp" aria-hidden="true"><label>Leave this empty: <input name="company" tabindex="-1" autocomplete="off"></label></p>

      <div class="field-row">
        <div class="field">
          <label for="f-name">Full name <span class="req">required</span></label>
          <input id="f-name" name="name" type="text" autocomplete="name" required maxlength="120">
        </div>
        <div class="field">
          <label for="f-goes">Name you go by</label>
          <input id="f-goes" name="preferred_name" type="text" maxlength="60" autocomplete="nickname">
        </div>
      </div>

      <div class="field-row">
        <div class="field">
          <label for="f-email">URI email <span class="req">required</span></label>
          <input id="f-email" name="email" type="email" autocomplete="email" required
                 pattern="[^@\\s]+@([Mm][Yy]\\.)?[Uu][Rr][Ii]\\.[Ee][Dd][Uu]" title="Please use your @uri.edu or @my.uri.edu address" placeholder="name@uri.edu" aria-describedby="f-email-hint">
          <p class="hint" id="f-email-hint">Use your @uri.edu or @my.uri.edu address. Not a URI student? Email <a href="mailto:{EMAIL}">{EMAIL}</a> instead.</p>
        </div>
        <div class="field">
          <label for="f-pron">Pronouns</label>
          <input id="f-pron" name="pronouns" type="text" maxlength="40" placeholder="Optional">
        </div>
      </div>

      <div class="field-row">
        <div class="field">
          <label for="f-level">Program level <span class="req">required</span></label>
          <select id="f-level" name="level" required>
            <option value="">Choose one</option>
            <option>Undergraduate</option>
            <option>Master&rsquo;s or MBA</option>
            <option>Doctoral</option>
            <option>Other</option>
          </select>
        </div>
        <div class="field">
          <label for="f-major">Major or program <span class="req">required</span></label>
          <input id="f-major" name="major" type="text" required maxlength="120" placeholder="e.g., Management, Psychology">
        </div>
      </div>

      <div class="field-row">
        <div class="field">
          <label for="f-grad">Expected graduation</label>
          <input id="f-grad" name="graduation" type="text" maxlength="40" placeholder="e.g., May 2028">
        </div>
        <div class="field">
          <label for="f-start">When would you like to start? <span class="req">required</span></label>
          <select id="f-start" name="start" required>
            <option value="">Choose one</option>
            <option>Spring 2027</option>
            <option>Fall 2027</option>
            <option>Spring 2028 or later</option>
            <option>Whenever there&rsquo;s an opening</option>
          </select>
        </div>
      </div>

      <fieldset class="field">
        <legend>Which topics interest you? <span class="hint">Choose any</span></legend>
        <div class="opts">
{options("interests", [("Assessment and measurement", "Assessment &amp; measurement"), ("Leadership", "Leadership"), ("Motivation and well-being", "Motivation &amp; well-being"), ("Training and learning", "Training &amp; learning"), ("AI and data science", "AI &amp; data science"), ("Not sure yet", "Not sure yet")])}
        </div>
      </fieldset>

      <div class="field-row">
        <fieldset class="field">
          <legend>How would you like to participate? <span class="req">required</span></legend>
          <div class="opts">
{options("participation", [("For credit (MGT 491/492)", "For credit (MGT 491 fall / MGT 492 spring, 1&ndash;3 credits; College of Business students)"), ("Volunteer", "Volunteer"), ("Either", "Either")], kind="radio", required=True)}
          </div>
        </fieldset>
        <div class="field">
          <label for="f-hours">Hours per week you can commit <span class="req">required</span></label>
          <select id="f-hours" name="hours" required>
            <option value="">Choose one</option>
            <option>3&ndash;5</option>
            <option>6&ndash;9</option>
            <option>10 or more</option>
            <option>Not sure yet</option>
          </select>
        </div>
      </div>

      <div class="field">
        <label for="f-why">Why are you interested in the lab? <span class="req">required</span></label>
        <textarea id="f-why" name="why" rows="5" required maxlength="1500" aria-describedby="f-why-hint"></textarea>
        <p class="hint" id="f-why-hint">A few sentences is plenty: what draws you to this research and what you hope to get out of it.</p>
      </div>

      <div class="field">
        <label for="f-exp">Relevant courses, skills, or experience</label>
        <textarea id="f-exp" name="experience" rows="3" maxlength="1000" placeholder="e.g., statistics or research methods courses, Excel, R or SPSS, survey design, writing"></textarea>
      </div>

      <div class="field-row">
        <div class="field">
          <label for="f-heard">How did you hear about the lab?</label>
          <select id="f-heard" name="heard">
            <option value="">Choose one (optional)</option>
            <option>A class</option>
            <option>A friend or classmate</option>
            <option>An advisor or professor</option>
            <option>The website</option>
            <option>Social media</option>
            <option>Other</option>
          </select>
        </div>
        <div class="field">
          <label for="f-avail">When are you usually available?</label>
          <input id="f-avail" name="availability" type="text" maxlength="200" placeholder="Optional, e.g., Tue/Thu afternoons">
        </div>
      </div>

      <div class="field">
        <label for="f-access">Scheduling limits, accommodations, or anything else we should know</label>
        <input id="f-access" name="access_needs" type="text" maxlength="300" placeholder="Optional">
      </div>

      <label class="opt consent"><input type="checkbox" name="consent" value="yes" required>
        <span>I understand my responses will be used only to consider my application to the ANCHOR Lab.</span></label>

      <button class="btn btn-primary" type="submit">Submit application</button>
      <p class="privacy">Your application goes to Dr. Matthew Hanson through this website&rsquo;s host (Netlify) and is used only to consider you for a position in the lab. It is not shared outside the lab and is not part of your academic record. Applications are removed from the host after each review cycle, and applications not selected are deleted within 60 days after the term starts. To withdraw or delete your application, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    </form>
  </section>
</div>
</main>
""" + FOOTER
write("join.html", join)

thanks = head("Application received · ANCHOR Lab", "Thanks for applying to the ANCHOR Lab.", "join-thanks",
              '\n<meta name="robots" content="noindex">') + header("join") + f"""
<main id="main">
<section class="page-intro">
  <div class="wrap essay-head">
    <p class="eyebrow">ANCHOR Lab</p>
    <h1>Thanks for applying!</h1>
    <p class="lede">Your application was received. Our founding cohort is in place, so Dr. Hanson will email you as the next cohort takes shape.</p>
  </div>
</section>
<div class="wrap essay">
  <section class="essay-section" aria-labelledby="next-h">
    <h2 id="next-h">What happens next</h2>
    <ol>
      <li>A short conversation to talk about your interests and current projects.</li>
      <li>If you&rsquo;re joining for credit, a directed-study form (MGT 491 in fall, MGT 492 in spring), signed before the add/drop deadline.</li>
      <li>Onboarding, starting with CITI research-ethics training, completed before you work on any study or data.</li>
    </ol>
    <p>Questions in the meantime? Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    <div class="btn-row"><a class="btn btn-secondary" href="/research.html">Explore our research</a></div>
  </section>
</div>
</main>
""" + FOOTER
write("join-thanks.html", thanks)

# ───────────────────────── Partners ─────────────────────────
partners = head("Partners · ANCHOR Lab", "Partner with the ANCHOR Lab at URI on evidence-based research into selection, development, and employee well-being.",
                "partners") + header("partners") + f"""
<main id="main">
<section class="page-intro">
  <div class="wrap essay-head">
    <p class="eyebrow">Partners</p>
    <h1>Better answers about your people, built on evidence.</h1>
    <p class="lede">We partner with organizations that want to know how well they select, develop, and support their people, including Rhode Island employers, public agencies, and healthcare and defense organizations.</p>
    <div class="btn-row"><a class="btn btn-primary" href="mailto:{EMAIL}?subject=Research%20partnership%20inquiry">Start a conversation</a></div>
  </div>
</section>
<div class="wrap essay">
  <section class="essay-section" aria-labelledby="how-h">
    <h2 id="how-h">How a partnership works</h2>
    <p>Most partnerships start with a question you already have: a selection process you&rsquo;re unsure of, a training program to evaluate, or burnout and turnover to understand.</p>
    <ol class="steps">
      <li><strong>Talk it through.</strong> We turn your question into a research question and agree on what success looks like.</li>
      <li><strong>Design the study.</strong> From a short survey to a field experiment, built to fit your setting and reviewed for ethics.</li>
      <li><strong>Share what we learn.</strong> A plain-language report, a briefing for your leadership team, and clear recommendations.</li>
    </ol>
  </section>
  <section class="essay-section" aria-labelledby="get-h">
    <h2 id="get-h">What you get</h2>
    <ul>
      <li>Evidence on whether your assessments, training, or practices are doing what you need</li>
      <li>A clear report of findings and recommendations, written for decision-makers</li>
      <li>A briefing for your leadership team</li>
    </ul>
    <p>Students work on partner projects under Dr. Hanson&rsquo;s supervision.</p>
  </section>
  <section class="essay-section" aria-labelledby="ethics-h">
    <h2 id="ethics-h">Ethics and confidentiality</h2>
    <p class="note-box">Research involving people is reviewed by URI&rsquo;s Institutional Review Board before it begins. Participation is voluntary, individual responses stay confidential, and data sharing is set out in a written agreement. Partners receive results in aggregate, and no partner is named publicly without written permission.</p>
  </section>
  <section class="essay-section" aria-labelledby="talk-h">
    <h2 id="talk-h">Start a conversation</h2>
    <p>Have a question about your people you&rsquo;d like answered with evidence? Email Dr. Hanson at <a href="mailto:{EMAIL}?subject=Research%20partnership%20inquiry">{EMAIL}</a>.</p>
  </section>
</div>
</main>
""" + FOOTER
write("partners.html", partners)

notfound = head("Page not found · ANCHOR Lab", "That page doesn't exist.", "404", '\n<meta name="robots" content="noindex">') + header("") + """
<main id="main">
<section class="page-intro">
  <div class="wrap essay-head">
    <p class="eyebrow">404</p>
    <h1>That page isn&rsquo;t here.</h1>
    <p class="lede">Try the <a href="/index.html">home page</a>, our <a href="/research.html">research</a>, or <a href="/join.html">how to join</a>.</p>
  </div>
</section>
</main>
""" + FOOTER
write("404.html", notfound)
