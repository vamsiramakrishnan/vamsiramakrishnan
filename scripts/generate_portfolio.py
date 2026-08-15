#!/usr/bin/env python3
from __future__ import annotations

from html import escape
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = yaml.safe_load((ROOT / "portfolio.yaml").read_text())
ASSETS = ROOT / "assets"
PROJECTS = ASSETS / "projects"
SITE = ROOT / "site"
GEN = ROOT / "generated"
for p in (ASSETS, PROJECTS, SITE, GEN): p.mkdir(parents=True, exist_ok=True)

CSS = """
:root{--bg:#0d1117;--panel:#161b22;--fg:#f0f6fc;--muted:#8b949e;--border:#30363d;--green:#3fb950;--blue:#58a6ff;--purple:#bc8cff}
@media(prefers-color-scheme:light){:root{--bg:#fff;--panel:#f6f8fa;--fg:#1f2328;--muted:#57606a;--border:#d0d7de;--green:#1a7f37;--blue:#0969da;--purple:#8250df}}
text{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}.fg{fill:var(--fg)}.muted{fill:var(--muted)}.green{fill:var(--green)}.blue{fill:var(--blue)}.box{fill:var(--panel);stroke:var(--border)}
"""

def project_svg(p: dict) -> str:
    steps = p["pipeline"]
    xs = [38, 250, 462, 674]
    nodes = []
    edges = []
    for i, step in enumerate(steps):
        nodes.append(f'<rect class="box" x="{xs[i]}" y="104" width="176" height="72" rx="12"/><text class="fg" x="{xs[i]+88}" y="134" text-anchor="middle" font-size="15" font-weight="700">{escape(step)}</text>')
        if i < len(steps)-1:
            edges.append(f'<path d="M{xs[i]+176} 140 H{xs[i+1]-14}" stroke="var(--green)" stroke-width="2"/><path d="M{xs[i+1]-20} 134 l8 6 -8 6" fill="none" stroke="var(--green)" stroke-width="2"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="888" height="232" viewBox="0 0 888 232" role="img"><style>{CSS}</style><rect width="888" height="232" rx="16" fill="var(--bg)" stroke="var(--border)"/><text class="green" x="38" y="40" font-size="14">{escape(p['id']).upper()}</text><text class="fg" x="38" y="70" font-size="23" font-weight="700">{escape(p['tagline'])}</text>{''.join(edges)}{''.join(nodes)}<text class="muted" x="38" y="210" font-size="13">{escape(p['evidence'])}</text></svg>'''

for p in DATA["projects"]:
    (PROJECTS / f"{p['id']}.svg").write_text(project_svg(p))

identity = DATA["identity"]
labels = " · ".join(["COMPILERS", "RUNTIMES", "CONTROL PLANES", "DURABILITY", "EVALS"])
og = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630"><style>{CSS}</style><rect width="1200" height="630" fill="var(--bg)"/><rect class="box" x="42" y="42" width="1116" height="546" rx="22"/><text class="green" x="82" y="108" font-size="18">SYSTEMS.LOG / GITHUB</text><text class="fg" x="82" y="190" font-size="58" font-weight="800">{escape(identity['name'])}</text><text class="blue" x="82" y="250" font-size="27">{escape(identity['headline'])}</text><line x1="82" y1="300" x2="1118" y2="300" stroke="var(--border)"/><text class="fg" x="82" y="362" font-size="22">{labels}</text><text class="muted" x="82" y="422" font-size="20">{escape(identity['thesis'])}</text><text class="green" x="82" y="526" font-size="20">github.com/vamsiramakrishnan</text><text class="muted" x="1118" y="526" text-anchor="end" font-size="16">spec → system → evidence → repeat</text></svg>'''
(ASSETS / "og-card.svg").write_text(og)

rows = []
for p in DATA["projects"]:
    rows.append(f'''<article><a href="{p['repo']}"><img src="../assets/projects/{p['id']}.svg" alt="{escape(p['name'])} architecture"></a><p>{escape(p['audience'])}</p></article>''')
now = "".join(f'<span><b>{escape(x["label"])}</b> / {escape(x["project"])} — {escape(x["text"])}</span>' for x in DATA["now"])
site = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(identity['name'])} — Systems around models</title><meta name="description" content="{escape(identity['headline'])}"><meta property="og:title" content="{escape(identity['name'])} — {escape(identity['headline'])}"><meta property="og:description" content="Compilers, runtimes, control planes, durability, synthetic worlds and evaluation infrastructure."><meta property="og:image" content="https://raw.githubusercontent.com/vamsiramakrishnan/vamsiramakrishnan/main/assets/og-card.svg"><meta property="og:type" content="website"><style>body{{max-width:1120px;margin:auto;padding:48px 24px;background:#0d1117;color:#f0f6fc;font:16px system-ui}}h1{{font-size:54px;margin-bottom:8px}}h2{{margin-top:64px}}a{{color:#58a6ff}}.now{{display:flex;gap:16px;flex-wrap:wrap}}.now span,article{{border:1px solid #30363d;border-radius:14px;padding:16px;background:#161b22}}.grid{{display:grid;grid-template-columns:1fr 1fr;gap:18px}}article img{{width:100%}}@media(max-width:800px){{.grid{{grid-template-columns:1fr}}h1{{font-size:38px}}}}</style></head><body><p>~/vamsi / systems.log</p><h1>{escape(identity['name'])}</h1><p><strong>{escape(identity['headline'])}</strong></p><p>{escape(identity['thesis'])}</p><div class="now">{now}</div><h2>Start here</h2><div class="grid">{''.join(rows)}</div><h2>Writing → systems</h2><img src="../assets/lineage.svg" style="width:100%" alt="Idea lineage"><p><a href="{identity['github']}">GitHub</a> · <a href="{identity['essays']}">Essays</a> · <a href="{identity['linkedin']}">LinkedIn</a></p></body></html>'''
(SITE / "index.html").write_text(site)

md = ["# Generated portfolio index", "", "Source: `portfolio.yaml`", "", "## Start here", ""]
for p in DATA["projects"]:
    md += [f"### [{p['name']}]({p['repo']})", p["audience"], "", f"**Mechanism:** `{p['mechanism']}`", "", f"**Evidence:** {p['evidence']}", ""]
(GEN / "portfolio.md").write_text("\n".join(md))
print(f"generated {len(DATA['projects'])} project cards, OG card, site and index")
