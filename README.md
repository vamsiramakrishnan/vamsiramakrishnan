<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero.svg">
  <img src="assets/hero.svg" width="100%" alt="Vamsi Ramakrishnan — I build the machinery around models">
</picture>

<br>

<a href="https://www.linkedin.com/in/vamsiramakrishnan/"><img src="https://img.shields.io/badge/LinkedIn-vamsiramakrishnan-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
<a href="https://twitter.com/mrvemzi"><img src="https://img.shields.io/badge/X-@mrvemzi-111111?style=flat-square&logo=x&logoColor=white" alt="X"></a>
<a href="https://mrvemzi.notion.site"><img src="https://img.shields.io/badge/Essays-mrvemzi.notion.site-111111?style=flat-square&logo=notion&logoColor=white" alt="Essays"></a>

**Forward Deployed Engineering · JAPAC · Google Cloud** · Melbourne, Australia

</div>

---

I work on the layer between **a model that can do something** and **a system you can trust to keep doing it**.

That usually means compilers, agent runtimes, control planes, durable execution, context containment, synthetic worlds, evaluation infrastructure and developer tooling. Before probabilistic systems, I spent years around safety-critical automotive software. The habit survived: put stochasticity where it buys something; make the rest inspectable.

> **The model can improvise. The system should know what happened.**

## Things were compiled.

<div align="center">

<img src="https://github-readme-activity-graph.vercel.app/graph?username=vamsiramakrishnan&bg_color=00000000&color=8b949e&line=3fb950&point=58a6ff&area=true&area_color=238636&hide_border=true&custom_title=Rolling%20engineering%20activity" width="100%" alt="Vamsi Ramakrishnan GitHub activity graph">

<sub>The profile repo also contains a self-hosted GitHub GraphQL calendar generator under <code>scripts/generate_activity.py</code>; the goal is to remove this external renderer once Actions is enabled for the profile repository.</sub>

</div>

---

## The body of work

```text
INTENT
  │
  ├── contracts / specs ───────► Anvil ─────────────► CLI · MCP · skills · hooks
  │                                │
  │                                └───────────────► legacy API estates
  │
  ├── agent design ─────────────► GE Agent Factory ─► code · evals · passports
  │
  ├── runtime semantics ────────► gemini-rs ────────► voice · state · governed flows
  │                         └───► Tape ─────────────► journal · replay · effects
  │
  ├── fleet / policy ───────────► AIPlex / Scion ───► identity · isolation · routing
  │
  ├── context pressure ─────────► straitjacket ─────► bounded digests · exact retrieval
  │
  ├── synthetic reality ────────► Worldloom ────────► facts · artifacts · eval truth
  │
  └── human surfaces ───────────► Pixelpitch / ge-msft
                                  PPTX · Office · reversible actuation
```

The projects are separate because the boundaries matter. The design argument is one system.

## Selected systems

<table>
<tr>
<td width="50%" valign="top">

### [Anvil](https://github.com/vamsiramakrishnan/anvil)
**API estate → agent-safe capability compiler**

One canonical model emits aligned **CLI, MCP, skills, hooks, mocks, evals and deployment contracts** from OpenAPI, SOAP/WSDL, gRPC, GraphQL, OData, Discovery and Postman.

Legacy mode inventories Java/.NET/messaging estates without executing them. Unknown stays unknown until evidence or a human closes it.

`TypeScript · compilers · MCP · legacy modernization`

</td>
<td width="50%" valign="top">

### [Worldloom](https://github.com/vamsiramakrishnan/synthetic-foundry)
**Synthetic enterprises with a memory of truth**

Builds company state first—people, systems, services, events, permissions, timelines—then projects the same ledger into **XLSX, DOCX, PPTX, PDF, Markdown, Jira, Confluence and ServiceNow**.

Evaluation truth and evidence originate from the same world. Large corpora are deterministic, dispersed, sharded and resumable.

`Python · synthetic data · artifacts · evals · replay`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [gemini-rs](https://github.com/vamsiramakrishnan/gemini-rs)
**Rust runtime for Gemini Multimodal Live**

Wire protocol → agent runtime → fluent DX. Full-duplex audio, typed state, tools, phases, extraction, background work and governed conversation DAGs.

The shared state spine lets deterministic recognizers and model-driven resolution coexist without turning control flow into prompt folklore.

`Rust · realtime voice · WebSockets · governed agents`

</td>
<td width="50%" valign="top">

### [Tape / Durable Agents](https://github.com/vamsiramakrishnan/durable-agents)
**Resume remembers the story**

An append-only journal records model decisions and effect intent/results. Restart means **replay decisions, skip confirmed effects, stop on ambiguity, reconcile reality, compensate when needed**.

Rust server + language-neutral gRPC + Python/TypeScript/Go/Java SDKs.

`Rust · WAL · durable execution · replay · gRPC`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [straitjacket](https://github.com/vamsiramakrishnan/straitjacket)
**Lossless context containment for coding agents**

Noisy tool output goes into an immutable local store. The transcript receives a bounded deterministic digest with exact retrieval addresses.

Not summarization: **bounded visibility without destroying evidence**.

`Python + Rust · coding harnesses · prompt-cache locality`

</td>
<td width="50%" valign="top">

### [GE Agent Factory](https://github.com/vamsiramakrishnan/ge-agent-factory)
**Intent → contract → proof → admission**

Interviews and BRDs become an Enterprise Agent Contract, which drives ADK code, tools, evals, synthetic source systems and proof. Evidence is sealed into an **Agent Passport** before handoff.

The same machinery is exercised across hundreds of horizontal and vertical agent specifications.

`TypeScript · ADK · evals · provenance · policy gates`

</td>
</tr>
</table>

<details>
<summary><strong>More systems — control planes, DX, multi-agent execution and human surfaces</strong></summary>
<br>

<table>
<tr><td width="25%"><b><a href="https://github.com/vamsiramakrishnan/aiplex">AIPlex</a></b></td><td>One Envoy-based policy plane across agent↔tool, agent↔agent and agent↔model interactions. Go control plane, Rust authz, OPA/Rego, mTLS and runtime consent.</td></tr>
<tr><td><b><a href="https://github.com/vamsiramakrishnan/adk-fluent">adk-fluent</a></b></td><td>Python + TypeScript fluent builders generated from a shared manifest, producing native ADK objects while compressing topology ceremony.</td></tr>
<tr><td><b><a href="https://github.com/vamsiramakrishnan/scion">Scion</a></b></td><td>Containerized deep-agent execution with isolated credentials and git worktrees across local machines and Kubernetes.</td></tr>
<tr><td><b><a href="https://github.com/vamsiramakrishnan/pixelpitch">Pixelpitch</a></b></td><td>Agent-authored HTML → designer-grade editable PPTX; maximizes native PowerPoint area under SSIM/OCR fidelity constraints.</td></tr>
<tr><td><b><a href="https://github.com/vamsiramakrishnan/ge-msft">ge-msft</a></b></td><td>Gemini Enterprise inside Microsoft 365 with client-direct identity federation, typed command algebra, reversible writes and durable provenance.</td></tr>
<tr><td><b><a href="https://github.com/vamsiramakrishnan/antigravity-a2a-a2ui">antigravity-a2a-a2ui</a></b></td><td>Identity-derived per-user Antigravity workspaces over Managed Agents, with credential brokering and sandbox hardening.</td></tr>
</table>

</details>

---

## The essays are upstream of the code

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/lineage.svg">
  <img src="assets/lineage.svg" width="100%" alt="Idea lineage from essays to software systems">
</picture>

<table>
<tr>
<td width="50%" valign="top">

### Agents are at Docker. We think we need k8s. We actually need CNCF.

The primitive attracts attention; the coordination layer absorbs the operational complexity and often captures the durable value. Agents are generating exactly that next coordination problem.

→ `AIPlex · Scion · GE Agent Factory`

</td>
<td width="50%" valign="top">

### Winter is Coming

Protocols, frameworks and infrastructure are individually useful but production requires a translation layer between them: identity, networking, policies, retries, audit and durable state.

→ `Anvil · Tape · gemini-rs · AIPlex`

</td>
</tr>
<tr>
<td valign="top">

### The Asymptote of Good Enough

Quality, price and latency are not scalar leaderboards. Optimization matters only while marginal improvement still changes user behavior or system outcomes.

→ `straitjacket · adk-fluent · runtime economics`

</td>
<td valign="top">

### Tacit Code, Real Friction

As code generation gets cheaper, the scarce part moves: tacit constraints, integration, verification, institutional knowledge and production consequences become more important.

→ `Anvil · ge-msft · eval infrastructure`

</td>
</tr>
</table>

<div align="center">

**[Read the essays →](https://mrvemzi.notion.site)**

</div>

<details>
<summary><strong>Writing shelf</strong></summary>
<br>

| Piece | Question underneath it |
|---|---|
| **Agents are at Docker. We think we need k8s. We actually need CNCF.** | Where does value move after the primitive becomes abundant? |
| **The Winter is Coming: The Infrastructure Reality of Production-Ready Agents** | What survives the transition from demo to distributed system? |
| **The Asymptote of Good Enough** | When does another unit of quality stop changing behavior? |
| **Tacit Code, Real Friction** | What becomes scarce when code itself becomes cheap? |
| **AI Leaderboards Are No Longer Useful. It's Time to Switch to Pareto Curves.** | Why collapse multi-dimensional systems into one rank? |
| **On AI-UX and Data Feedback Loops as Moats** | When does product interaction become proprietary learning? |
| **An ode to all AI Prisoners** | What do agent economics look like once inference is only one line item? |

</details>

---

## Operating principles

```text
01  SPEC > PROMPT                 durable intent should outlive a model call
02  IR > HAND-WIRING             compile multiple surfaces from one source of truth
03  REFUSE > GUESS               uncertainty is information
04  RESUME > RETRY               acting agents need memory of reality
05  ADDRESSES > SUMMARIES        omitted bytes need a deterministic path home
06  EVIDENCE > VIBES             performance claims need receipts
07  PURE COMPOSES; EFFECTS GATE  side effects stay explicit and reviewable
08  LOCAL FIRST                  cloud cost and mutation should be opt-in
09  BORING CONTROL PLANE         spend stochasticity only where it buys leverage
10  DEVEX IS ARCHITECTURE        setup, errors, introspection and docs are system design
```

## Archaeology

The newer agent work sits on older layers: autonomous-driving projects around lane geometry, behavioral cloning and traffic-sign recognition; then Kubernetes, CI/CD, landing zones and operational plumbing. The technologies changed. The recurring interest did not: **how do you turn uncertain behavior into an engineered system with explicit boundaries?**

<div align="center">

<sub>Python for reach · Rust for runtimes · Go for control planes · TypeScript for compilers and product surfaces</sub>

<br><br>

<a href="https://github.com/vamsiramakrishnan?tab=repositories"><b>browse the code</b></a> · <a href="https://mrvemzi.notion.site"><b>read the thinking</b></a>

</div>
