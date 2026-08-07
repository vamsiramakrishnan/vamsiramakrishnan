#!/usr/bin/env python3
"""Generate a self-hosted contribution calendar SVG for the profile README."""
from __future__ import annotations

import json
import os
import pathlib
import urllib.request

LOGIN = os.environ.get("GITHUB_ACTOR", "vamsiramakrishnan")
TOKEN = os.environ["GITHUB_TOKEN"]
OUT = pathlib.Path("assets/activity.svg")

QUERY = r'''
query($login:String!) {
  user(login:$login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays { date contributionCount contributionLevel weekday }
        }
      }
    }
  }
}
'''

req = urllib.request.Request(
    "https://api.github.com/graphql",
    data=json.dumps({"query": QUERY, "variables": {"login": LOGIN}}).encode(),
    headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
)
with urllib.request.urlopen(req) as response:
    payload = json.load(response)
cal = payload["data"]["user"]["contributionsCollection"]["contributionCalendar"]
weeks = cal["weeks"]
total = cal["totalContributions"]

CELL, GAP = 13, 4
LEFT, TOP = 56, 88
WIDTH = LEFT + len(weeks) * (CELL + GAP) + 36
HEIGHT = 242
colors = {
    "NONE": "var(--c0)", "FIRST_QUARTILE": "var(--c1)",
    "SECOND_QUARTILE": "var(--c2)", "THIRD_QUARTILE": "var(--c3)",
    "FOURTH_QUARTILE": "var(--c4)",
}
rects = []
for x, week in enumerate(weeks):
    for day in week["contributionDays"]:
        y = day["weekday"]
        rects.append(
            f'<rect x="{LEFT+x*(CELL+GAP)}" y="{TOP+y*(CELL+GAP)}" width="{CELL}" height="{CELL}" rx="3" fill="{colors[day["contributionLevel"]]}"/>'
        )

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">
<title id="title">Things were compiled — contribution calendar</title><desc id="desc">{total} GitHub contributions over the last year for {LOGIN}.</desc>
<style>
:root{{--bg:#0d1117;--fg:#f0f6fc;--muted:#8b949e;--border:#30363d;--c0:#161b22;--c1:#0e4429;--c2:#006d32;--c3:#26a641;--c4:#39d353}}@media(prefers-color-scheme:light){{:root{{--bg:#fff;--fg:#1f2328;--muted:#57606a;--border:#d0d7de;--c0:#ebedf0;--c1:#9be9a8;--c2:#40c463;--c3:#30a14e;--c4:#216e39}}}}
text{{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}}.h{{font-size:22px;font-weight:700;fill:var(--fg)}}.m{{font-size:13px;fill:var(--muted)}}
</style><rect width="100%" height="100%" rx="16" fill="var(--bg)" stroke="var(--border)"/><text class="h" x="28" y="38">THINGS WERE COMPILED.</text><text class="m" x="28" y="62">{total:,} contributions · rolling 12 months · generated from GitHub GraphQL</text>
<text class="m" x="28" y="102">M</text><text class="m" x="28" y="136">W</text><text class="m" x="28" y="170">F</text>{''.join(rects)}
<text class="m" x="28" y="220">less</text><rect x="64" y="208" width="11" height="11" rx="2" fill="var(--c0)"/><rect x="81" y="208" width="11" height="11" rx="2" fill="var(--c1)"/><rect x="98" y="208" width="11" height="11" rx="2" fill="var(--c2)"/><rect x="115" y="208" width="11" height="11" rx="2" fill="var(--c3)"/><rect x="132" y="208" width="11" height="11" rx="2" fill="var(--c4)"/><text class="m" x="151" y="220">more</text></svg>'''
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(svg)
print(f"wrote {OUT} ({total} contributions)")
