<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero.svg">
  <img src="assets/hero.svg" width="100%" alt="Vamsi Ramakrishnan — I build the machinery around models">
</picture>

<br>

<a href="https://www.linkedin.com/in/vamsiramakrishnan/"><img src="https://img.shields.io/badge/LinkedIn-vamsiramakrishnan-0A66C2?style=flat-square&logo=linkedin&logoColor=white"></a>
<a href="https://twitter.com/mrvemzi"><img src="https://img.shields.io/badge/X-@mrvemzi-111111?style=flat-square&logo=x&logoColor=white"></a>
<a href="https://mrvemzi.notion.site"><img src="https://img.shields.io/badge/Essays-mrvemzi.notion.site-111111?style=flat-square&logo=notion&logoColor=white"></a>

**Forward Deployed Engineering · JAPAC · Google Cloud** · Melbourne, Australia

</div>

I build compilers, runtimes, control planes, synthetic-data systems, evaluation infrastructure, and developer tools around AI models.

<table>
<tr>
<td><b>NOW</b></td><td><a href="https://github.com/vamsiramakrishnan/straitjacket">straitjacket</a> — bounded context and exact evidence retrieval for coding agents</td>
</tr>
<tr>
<td><b>RECENT</b></td><td><a href="https://github.com/vamsiramakrishnan/anvil">Anvil</a> — API and legacy estates compiled into agent-facing capabilities</td>
</tr>
<tr>
<td><b>BUILDING</b></td><td><a href="https://github.com/vamsiramakrishnan/synthetic-foundry">Worldloom</a> — coherent synthetic enterprises with generated evaluation truth</td>
</tr>
</table>

## Activity

<div align="center">
<img src="https://github-readme-activity-graph.vercel.app/graph?username=vamsiramakrishnan&bg_color=00000000&color=8b949e&line=3fb950&point=58a6ff&area=true&area_color=238636&hide_border=true&custom_title=Rolling%20engineering%20activity" width="100%" alt="GitHub activity graph">
</div>

## Start here

| Problem | Repository |
| --- | --- |
| Agents need to use APIs or legacy middleware with explicit policy | **[Anvil](https://github.com/vamsiramakrishnan/anvil)** |
| A coding agent is carrying too much tool output in context | **[straitjacket](https://github.com/vamsiramakrishnan/straitjacket)** |
| An acting agent must resume after crashes or partial effects | **[Tape](https://github.com/vamsiramakrishnan/durable-agents)** |
| You need synthetic enterprise corpora with generated ground truth | **[Worldloom](https://github.com/vamsiramakrishnan/synthetic-foundry)** |
| You need a Gemini voice/runtime layer in Rust | **[gemini-rs](https://github.com/vamsiramakrishnan/gemini-rs)** |
| You need to turn agent requirements into code, evals, and admission evidence | **[GE Agent Factory](https://github.com/vamsiramakrishnan/ge-agent-factory)** |

## Core systems

<a href="https://github.com/vamsiramakrishnan/anvil"><img src="assets/projects/anvil.svg" width="100%" alt="Anvil mechanism"></a>

<a href="https://github.com/vamsiramakrishnan/straitjacket"><img src="assets/projects/straitjacket.svg" width="100%" alt="Straitjacket mechanism"></a>

<a href="https://github.com/vamsiramakrishnan/durable-agents"><img src="assets/projects/durable-agents.svg" width="100%" alt="Tape mechanism"></a>

<details>
<summary><strong>Worldloom · gemini-rs · GE Agent Factory</strong></summary>
<br>
<a href="https://github.com/vamsiramakrishnan/synthetic-foundry"><img src="assets/projects/synthetic-foundry.svg" width="100%" alt="Worldloom mechanism"></a>
<br><br>
<a href="https://github.com/vamsiramakrishnan/gemini-rs"><img src="assets/projects/gemini-rs.svg" width="100%" alt="gemini-rs mechanism"></a>
<br><br>
<a href="https://github.com/vamsiramakrishnan/ge-agent-factory"><img src="assets/projects/ge-agent-factory.svg" width="100%" alt="GE Agent Factory mechanism"></a>
</details>

## How the projects relate

```text
INTENT
  │
  ├── contracts / specs ───────► Anvil ─────────────► CLI · MCP · skills · hooks
  │                                └───────────────► legacy API estates
  ├── agent design ─────────────► GE Agent Factory ─► code · evals · passports
  ├── runtime semantics ────────► gemini-rs ────────► voice · state · governed flows
  │                         └───► Tape ─────────────► journal · replay · effects
  ├── fleet / policy ───────────► AIPlex / Scion ───► identity · isolation · routing
  ├── context pressure ─────────► straitjacket ─────► bounded digests · exact retrieval
  ├── synthetic reality ────────► Worldloom ────────► facts · artifacts · eval truth
  └── human surfaces ───────────► Pixelpitch / ge-msft
```

<details>
<summary><strong>Other systems</strong></summary>
<br>

| System | Focus |
| --- | --- |
| **[AIPlex](https://github.com/vamsiramakrishnan/aiplex)** | Policy across agent-to-tool, agent-to-agent, and agent-to-model traffic |
| **[adk-fluent](https://github.com/vamsiramakrishnan/adk-fluent)** | Python and TypeScript fluent builders that return native ADK objects |
| **[Scion](https://github.com/vamsiramakrishnan/scion)** | Isolated container and worktree execution for collaborating agent harnesses |
| **[Pixelpitch](https://github.com/vamsiramakrishnan/pixelpitch)** | Agent-authored HTML converted to editable PPTX under visual-fidelity checks |
| **[ge-msft](https://github.com/vamsiramakrishnan/ge-msft)** | Gemini Enterprise inside Microsoft 365 with provenance-bearing actions |
| **[antigravity-a2a-a2ui](https://github.com/vamsiramakrishnan/antigravity-a2a-a2ui)** | Identity-derived per-user managed-agent workspaces and credential brokering |

</details>

## Essays and code

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/lineage.svg">
  <img src="assets/lineage.svg" width="100%" alt="Idea lineage from essays to software systems">
</picture>

| Thesis | Related systems |
| --- | --- |
| **Agents are at Docker. We think we need k8s. We actually need CNCF.** | `AIPlex · Scion · GE Agent Factory` |
| **Winter is Coming** | `Anvil · Tape · gemini-rs · AIPlex` |
| **The Asymptote of Good Enough** | `straitjacket · adk-fluent · Worldloom` |
| **Tacit Code, Real Friction** | `Anvil · ge-msft · eval infrastructure` |

<div align="center"><b><a href="https://mrvemzi.notion.site">Read the essays</a></b></div>

## Generated profile assets

```text
portfolio.yaml
      │
      ├── README-facing project diagrams
      ├── social / Open Graph card
      ├── standalone landing page
      ├── generated portfolio index
      └── activity surface
```

`portfolio.yaml` is the source model. [`scripts/generate_portfolio.py`](scripts/generate_portfolio.py) generates the projections. [`profile-assets.yml`](.github/workflows/profile-assets.yml) regenerates them when the model changes.

The social card is [`assets/og-card.svg`](assets/og-card.svg). The site projection lives under [`site/`](site/).

## Engineering preferences

```text
01  SPEC > PROMPT                 durable intent should outlive a model call
02  IR > HAND-WIRING             compile multiple surfaces from one source model
03  REFUSE > GUESS               surface uncertainty instead of inventing state
04  RESUME > RETRY               acting agents need a record of prior effects
05  ADDRESSES > SUMMARIES        omitted bytes need a deterministic path home
06  EVIDENCE > VIBES             performance claims need receipts
07  PURE COMPOSES; EFFECTS GATE  side effects stay explicit and reviewable
08  LOCAL FIRST                  cloud cost and mutation should be opt-in
09  BORING CONTROL PLANE         spend model calls where they change the result
10  DEVEX IS ARCHITECTURE        setup, errors, introspection, and docs affect system use
```

## Earlier work

Older repositories cover lane detection, behavioral cloning, traffic-sign recognition, Kubernetes, CI/CD, landing zones, and operational plumbing. The stack changed over time; the recurring problem stayed similar: make uncertain behavior observable, constrained, and testable.

<div align="center">
<sub>Python for reach · Rust for runtimes · Go for control planes · TypeScript for compilers and product surfaces</sub>
<br><br>
<a href="https://github.com/vamsiramakrishnan?tab=repositories"><b>browse the code</b></a> · <a href="https://mrvemzi.notion.site"><b>read the essays</b></a>
</div>
