"""Publication data and list helpers, copied from matthewdhanson.com (tools/build.py).
Keep in sync when publications change."""
import re

# ───────────────────────── Publications data (from April 2026 CV) ─────────────────────────
ME = re.compile(r"Hanson, M\.(?: D\.)?")

ARTICLES = [
    dict(year=2025, authors="Randall, J. G., Zajac, S. A., & Hanson, M. D.", title="Mindful training: Integrating mindfulness into workplace learning",
         venue="Human Resource Development Review", details="Advance online publication", doi="10.1177/15344843251395914"),
    dict(year=2022, authors="Randall, J. G., Hanson, M. D., & Nassrelgrgawi, A. S.", title="Staying focused when nobody is watching: Self-regulatory strategies to reduce mind wandering during self-directed learning",
         venue="Applied Psychology: An International Review", details="71(4), 1428&ndash;1464", doi="10.1111/apps.12366"),
    dict(year=2020, authors="Ulatowska, J., Olszewska, J., & Hanson, M. D.", title="Does test type influence false recognition in the DRM paradigm? Comparison of the yes/no recognition test and two-alternative forced-choice test",
         venue="American Journal of Psychology", details="133(1), 49&ndash;62", doi="10.5406/amerjpsyc.133.1.0049"),
    dict(year=2020, authors="Steinert, S. W., Hanson, M. D., Weiss, N., Berg, J. V., Hong, P. Y., & Lancaster, R.", title="A critical analysis of student nurses&rsquo; knowledge and use of the American Psychological Association&rsquo;s Publication Manual",
         venue="TNNMC Journal of Nursing Education and Administration", details="8(1), 31&ndash;39"),
    dict(year=2019, authors="Lee, S. Y., Hanson, M. D., & Cheung, H. K.", title="Incorporating bystander intervention into sexual harassment training",
         venue="Industrial and Organizational Psychology", details="12(1), 52&ndash;57", doi="10.1017/iop.2019.8"),
    dict(year=2018, authors="Hong, P. Y., Hanson, M. D., Lishner, D. A., Kelso, S. L., & Steinert, S. W.", title="A field experiment examining mindfulness on eating enjoyment and behavior in children",
         venue="Mindfulness", details="9(6), 1748&ndash;1756", doi="10.1007/s12671-018-0916-1"),
    dict(year=2018, authors="Atherton, R. P., Chrobak, Q. M., Rauscher, F. H., Karst, A. T., Hanson, M. D., Steinert, S. W., & Bowe, K. L.", title="Shared processing of language and music: Evidence from a cross-modal interference paradigm",
         venue="Experimental Psychology", details="65(1), 40&ndash;48", doi="10.1027/1618-3169/a000388"),
    dict(year=2016, authors="Ulatowska, J., Olszewska, J., & Hanson, M. D.", title="Do format differences in the presentation of information affect susceptibility to memory distortions? The three-stage misinformation procedure reconsidered",
         venue="American Journal of Psychology", details="129(4), 407&ndash;417", doi="10.5406/amerjpsyc.129.4.0407"),
]
CHAPTERS = [
    dict(year=2020, authors="Hanson, M. D., Randall, J. G., Danna, G. C., & Le, H. Q.", title="Enhancing workplace learning through mindfulness",
         venue="The Routledge Companion to Mindfulness at Work", pre="In S. K. Dhiman (Ed.), ", details="Routledge"),
]
REPORTS = [
    dict(year=2023, authors="Bizarro, A., Dilweg, D., Hernandez, D., Hanson, M. D., & Louie, J.", title="Development of a leadership competency model for submarine command triads",
         venue="Defense Technical Information Center", details="Publication No. AD1217151", url="https://apps.dtic.mil/sti/citations/AD1217151"),
    dict(year=2022, authors="Bizarro, A., Hernandez, D., Hanson, M. D., Peltier, C., & Handy, J.", title="Development of the Submarine Environment Fit (SUBFIT) Assessment: Psychometric review and comparison of enlisted and officer trainees",
         venue="Defense Technical Information Center", details="Publication No. AD1183611", url="https://apps.dtic.mil/sti/citations/AD1183611"),
]
REVIEW = [
    dict(authors="Hanson, M. D., Randall, J. G., & Banfi, J. T.", title="Practice, label, or placebo? An experimental test of mindfulness effects in organizational training"),
    dict(authors="Hanson, M. D., Randall, J. G., & Banfi, J. T.", title="Basic psychological need satisfaction across life domains: Implications for work recovery and well-being"),
    dict(authors="Hanson, M. D., & Hong, P. Y.", title="Brief focused-attention and open-monitoring mindfulness meditation: A randomized controlled experiment on mindfulness, anxiety, affect, and attention"),
    dict(authors="Hong, P. Y., Hanson, M. D., Lishner, D. A., Kelso, S., & Steinert, S.", title="A randomized field experiment examining the effect of mindfulness on children&rsquo;s, parents&rsquo;, and teachers&rsquo; ratings of children&rsquo;s mood and behavior"),
]
TALKS = [
    dict(year=2024, authors="Clark, D., Hernandez, D., Dilweg, D., Hanson, M. D., & Bizarro, A.", title="Associations between submarine officer personality and operational outcomes", venue="Military Health System Research Symposium", details="Kissimmee, FL"),
    dict(year=2024, authors="Hernandez, D. B., Dilweg, D. R., & Hanson, M. D.", title="Building a competency model for Submarine Force leadership", venue="Office of Naval Research Manpower, Personnel, Training, and Education Program Review", details="Annapolis, MD"),
    dict(year=2024, authors="Hernandez, D., Dilweg, D., Hanson, M. D., & Clark, D. A.", title="SUBFOR research progress and results", venue="Office of Naval Research Manpower, Personnel, Training, and Education Annual Workshop", details="San Diego, CA"),
    dict(year=2023, authors="Hanson, M. D., Louie, J. F., Bizarro, A., Dilweg, D., Hernandez, D., & Clark, D. A.", title="Building a competency model for Submarine Force leadership", venue="Office of Naval Research Manpower, Personnel, Training, and Education Program Review", details="Arlington, VA"),
    dict(year=2021, authors="Hanson, M. D., Baranik, L. E., Smith, R. W., & Fan, L.", title="Development of the refugee job search stressor scale", venue="Academy of Management Annual Meeting", details="Symposium, virtual"),
    dict(year=2021, authors="Hanson, M. D., & Randall, J. G.", title="Training on purpose: Mindfulness in a training environment", venue="Society for Industrial and Organizational Psychology Annual Conference", details="Symposium co-chair and presenter"),
    dict(year=2021, authors="Baranik, L. E., Hanson, M. D., Mian, M., & Yeo, A.", title="Refugee Roundtable survey: Supporting economic stability", venue="Capital Region Refugee Roundtable", details="Albany, NY"),
    dict(year=2020, authors="Randall, J., Hanson, M. D., Neuburger, A., & Shaju, S.", title="Training evaluation efforts to help professionalize direct support professionals", venue="Society for Industrial and Organizational Psychology Annual Conference", details="Symposium"),
]
POSTERS = [
    dict(year=2024, authors="Handy, J., Clark, D. A., Hernandez, D. B., Hanson, M. D., Marshall, J., & Harris, E.", title="Non-clinical personality indices and stress coping behaviors predict attrition from the Navy nuclear training pipeline", venue="Military Health System Research Symposium", details="Kissimmee, FL"),
    dict(year=2022, authors="Handy, J., Bizarro, A., Clark, D. A., Hanson, M. D., Hernandez, D., & Smallidge, T.", title="Warrior toughness improves outcomes for enlisted sailors at Naval Nuclear Power Training Command", venue="Military Health System Research Symposium", details="Kissimmee, FL"),
    dict(year=2019, authors="Hanson, M. D., Randall, J. G., & Nassrelgrgawi, A. S.", title="Self-regulation interventions in a self-directed learning environment", venue="Society for Industrial and Organizational Psychology Annual Conference", details="National Harbor, MD"),
    dict(year=2019, authors="Randall, J. G., Hanson, M. D., Arredondo, M. L., & Jandrew, M.", title="Predicting self-regulation failures in training", venue="Society for Industrial and Organizational Psychology Annual Conference", details="National Harbor, MD"),
    dict(year=2017, authors="Zimmerman, C., Hong, P. Y., Lishner, D. A., Ebert, A., Hanson, M. D., Steinert, S., & Kelso, S.", title="Mindfulness, academic performance, and mood", venue="Society for Personality and Social Psychology Annual Convention", details="San Antonio, TX"),
    dict(year=2017, authors="Hong, P. Y., Zimmerman, C. N., Lishner, D. A., & Hanson, M. D.", title="Mindfulness and eating enjoyment and behavior in preschool children", venue="Society for Personality and Social Psychology Annual Convention", details="San Antonio, TX"),
    dict(year=2016, authors="Ebert, A., Hanson, M. D., Rapp, E., Wenzel, T., Bagley, A., & Hong, P. Y.", title="The effect of perceived child intelligence on public perception of hyper-parenting: A replication study", venue="Association for Psychological Science Annual Convention", details="Chicago, IL"),
    dict(year=2016, authors="Hanson, M. D., Ebert, A., Voskuil, T., Barbieri, A., Schlueter, A., Steinert, S. W., Kelso, S., Zimmerman, C., Hong, P. Y., & Lishner, D. A.", title="Anxiety, attention, and mindfulness following focused attention and open-monitoring mindfulness meditation", venue="International Conference on Mindfulness", details="Rome, Italy"),
    dict(year=2015, authors="Steinert, S., Hanson, M. D., Kelso, S., Lishner, D. A., Hong, P. Y., & Vitacco, M. J.", title="A replication of psychopathic callous affect as a predictor of empathic concern and positive affect toward those in need", venue="Association for Behavioral and Cognitive Therapies Annual Convention", details="Chicago, IL"),
    dict(year=2015, authors="Ebert, A., Kelso, S., Steinert, S., Hanson, M. D., Hong, P. Y., & Lishner, D. A.", title="An examination of the role of source credibility on invalidating messages on affect", venue="Association for Behavioral and Cognitive Therapies Annual Convention", details="Chicago, IL"),
    dict(year=2015, authors="Hanson, M. D., Steinert, S., Kelso, S., Ebert, A., Lishner, D. A., Hong, P. Y., & Vitacco, M. J.", title="Psychopathy and ability emotional intelligence: A re-analysis of Lishner, Swim, Hong, &amp; Vitacco (2011)", venue="American Psychological Association Annual Convention", details="Toronto, Canada"),
    dict(year=2015, authors="Miller, T., Pionk, T., Kelso, S., Steinert, S., Hanson, M. D., Lishner, D. A., Hong, P. Y., & Vitacco, M. J.", title="Psychopathic callous affect as a predictor of empathic concern and happiness toward those in need", venue="Midwestern Psychological Association Annual Meeting", details="Chicago, IL"),
]


def auth(a):
    a = a.replace("&", "&amp;").replace("&amp;amp;", "&amp;")
    return ME.sub(lambda m: f"<strong>{m.group(0)}</strong>", a, count=1)


def pub_li(p, status=None):
    link = None
    if p.get("doi"):
        link = "https://doi.org/" + p["doi"]
    elif p.get("url"):
        link = p["url"]
    title = f'<a href="{link}">{p["title"]}</a>' if link else p["title"]
    year = p.get("year", "")
    venue = ""
    if p.get("venue"):
        venue = f'{p.get("pre", "")}<cite>{p["venue"]}</cite>'
        if p.get("details"):
            venue += f', {p["details"]}'
    pill = f' <span class="pill">{status}</span>' if status else ""
    links = ""
    if p.get("doi"):
        links = f'<p class="links"><a href="{link}">DOI</a></p>'
    elif p.get("url"):
        links = f'<p class="links"><a href="{link}">Read on DTIC</a></p>'
    return f"""  <li class="pub">
    <span class="year"{"" if year else ' aria-hidden="true"'}>{year if year else "&mdash;"}</span>
    <div>
      <p class="title">{title}{pill}</p>
      <p class="authors">{auth(p["authors"])}</p>
      {f'<p class="venue">{venue}</p>' if venue else ''}
      {links}
    </div>
  </li>"""


def group(gid, gtype, label, items, status=None, collapse=False):
    lis = "\n".join(pub_li(p, status) for p in items)
    ul = f'<ol class="pub-list">\n{lis}\n</ol>'
    if collapse:
        ul = f'<details class="more-pubs"><summary>Show all {len(items)}</summary>\n{ul}\n</details>'
    return f"""<section class="pub-group" data-type="{gtype}" aria-labelledby="{gid}">
  <h2 id="{gid}">{label} <span class="count">{len(items)}<span class="visually-hidden"> items</span></span></h2>
  {ul}
</section>"""


