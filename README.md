<div align="center">

<pre>
┌──────────────────────────────────────────────────────────────────────────────┐
│ VAMSI RAMAKRISHNAN                                                          │
│ forward deployed engineering · agent runtimes · compilers · systems         │
│                                                                              │
│ deterministic where possible. probabilistic where necessary.                │
└──────────────────────────────────────────────────────────────────────────────┘
</pre>

### I build the machinery around models.

**Forward Deployed Engineering · JAPAC · Google Cloud**  
Melbourne, Australia

<a href="https://www.linkedin.com/in/vamsiramakrishnan/"><img src="https://img.shields.io/badge/LinkedIn-vamsiramakrishnan-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
<a href="https://twitter.com/mrvemzi"><img src="https://img.shields.io/badge/X-@mrvemzi-111111?style=for-the-badge&logo=x&logoColor=white" alt="X"></a>
<a href="https://mrvemzi.notion.site"><img src="https://img.shields.io/badge/notes-mrvemzi.notion.site-111111?style=for-the-badge&logo=notion&logoColor=white" alt="Notes"></a>

</div>

---

My day job is taking AI into production with large enterprises across JAPAC. This GitHub account is where I work through the systems questions underneath that job: **how agents should execute, recover, authenticate, retrieve context, expose tools, generate artifacts, and prove what they did.**

Before probabilistic systems, I spent years around safety-critical automotive software — ABS, ADAS, embedded control and ISO 26262. That leaves a useful bias: **make the model creative at the edges; make the machinery around it boring, inspectable and deterministic.**

I tend to build the missing layer rather than another wrapper around a model.

```text
                                      ┌─────────────────────────────┐
                                      │        HUMAN INTENT         │
                                      └──────────────┬──────────────┘
                                                     │
                         ┌───────────────────────────▼──────────────────────────┐
                         │ specs · contracts · skills · capability manifests    │
                         └──────────────┬───────────────────────────┬───────────┘
                                        │                           │
                 ┌──────────────────────▼────────────┐   ┌─────────▼──────────────┐
                 │ compile deterministic surfaces   │   │ generate coherent worlds│
                 │ CLI · MCP · APIs · hooks · evals │   │ data · docs · eval truth│
                 └──────────────────────┬────────────┘   └─────────┬──────────────┘
                                        │                           │
                       ┌────────────────▼───────────────────────────▼──────────────┐
                       │                  AGENT RUNTIME                            │
                       │ state · policy · context · tools · orchestration · voice │
                       └────────────────┬───────────────────────────┬──────────────┘
                                        │                           │
                            ┌───────────▼──────────┐      ┌────────▼───────────┐
                            │ durable side effects │      │ isolated executors │
                            │ journal · replay     │      │ containers · worktrees│
                            └───────────┬──────────┘      └────────┬───────────┘
                                        │                           │
                       ┌────────────────▼───────────────────────────▼──────────────┐
                       │             REAL SYSTEMS + HUMAN SURFACES                  │
                       └────────────────────────────────────────────────────────────┘
```

## Selected systems

<table>
<tr>
<td width="50%" valign="top">

### ⚒️ [Anvil](https://github.com/vamsiramakrishnan/anvil)
**API estate → agent-safe capability compiler**

Compiles OpenAPI, WSDL/SOAP, gRPC, GraphQL, OData, Discovery and Postman contracts into one canonical intermediate representation, then emits aligned **CLI, MCP, skills, hooks, mocks, evals and deployment contracts**.

It also inventories legacy Java/.NET/messaging estates without executing them, preserving provenance and uncertainty instead of hallucinating a business API.

`TypeScript · compilers · MCP · legacy modernization · safety`

</td>
<td width="50%" valign="top">

### 🧵 [Worldloom](https://github.com/vamsiramakrishnan/synthetic-foundry)
**A deterministic compiler for synthetic enterprises**

Builds the company before it builds the documents: people, org structure, systems, services, events, facts, permissions and timelines first; then projects the same state into **XLSX, DOCX, PPTX, PDF, Markdown, Jira, Confluence and ServiceNow**.

Evaluation ground truth comes from the same fact ledger as the evidence. Seeded replay is byte-stable and large corpora are sharded and resumable.

`Python · synthetic data · artifact generation · evals · replay`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🦀 [gemini-rs](https://github.com/vamsiramakrishnan/gemini-rs)
**Full Rust SDK + runtime for Gemini Multimodal Live**

Three layers: wire protocol, runtime and fluent DX. Handles full-duplex audio, tool dispatch, typed state, VAD/barge-in, phases, extraction, background work and governed conversation DAGs.

The interesting bit is the shared state spine: deterministic recognizers, model-assisted extraction and orchestration all converge on one reactive runtime model.

`Rust · realtime voice · WebSockets · agent runtime · typed state`

</td>
<td width="50%" valign="top">

### 📼 [Tape / Durable Agents](https://github.com/vamsiramakrishnan/durable-agents)
**Durable execution beneath the agent loop**

An append-only journal records model decisions and external effect intent/results. On restart the runtime **replays decisions, skips confirmed effects, stops on ambiguity, reconciles reality and compensates when needed**.

Rust server, language-agnostic gRPC protocol, and SDKs for Python, TypeScript, Go and Java. Integrates with ADK through extension points rather than forking the framework.

`Rust · WAL · exactly-once-effective execution · replay · gRPC`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🪢 [straitjacket](https://github.com/vamsiramakrishnan/straitjacket)
**Context containment for coding agents**

Large tool outputs are captured into an immutable local artifact store and replaced in the transcript with small deterministic digests carrying exact retrieval addresses.

The goal is not summarization. It is **lossless addressability with bounded transcript cost**, preserving prompt-cache stability while keeping every omitted byte retrievable.

`Python + Rust · coding harnesses · context engineering · cache locality`

</td>
<td width="50%" valign="top">

### 🧬 [GE Agent Factory](https://github.com/vamsiramakrishnan/ge-agent-factory)
**Intent → contract → agent → evidence → admission**

Turns interviews/BRDs into a canonical enterprise-agent contract, then generates ADK code, tools, evals, synthetic systems and proof artifacts. Evidence is sealed into an **Agent Passport** before handoff to agents-cli / Agent Engine / Gemini Enterprise.

The catalog currently exercises the same machinery across hundreds of horizontal and vertical agent specifications.

`TypeScript · ADK · evals · provenance · policy gates`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🌐 [AIPlex](https://github.com/vamsiramakrishnan/aiplex)
**One control plane for agent ↔ tool, agent ↔ agent and agent ↔ model**

Envoy-based gateway with MCP, A2A and LLM planes; OAuth/OIDC, mTLS, policy and audit under one architecture. Effective permission is the intersection of **agent ceiling × user ceiling × runtime consent**.

Go control plane, Rust authorization service, React console, GKE/Service Mesh deployment.

`Go · Rust · Envoy · OPA/Rego · SPIFFE · GKE`

</td>
<td width="50%" valign="top">

### 🎛️ [adk-fluent](https://github.com/vamsiramakrishnan/adk-fluent)
**A lower-ceremony API over Google ADK**

Python + TypeScript builders generated from a shared manifest, producing native ADK objects while compressing common agent topology into composable expressions.

Includes pipelines, fan-out, loops, skills, guards, reactive agents, A2A/A2UI surfaces, typed stubs and parity checks across both language implementations.

`Python · TypeScript · DSLs · code generation · developer experience`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🖥️ [Scion](https://github.com/vamsiramakrishnan/scion)
**Containerized multi-agent execution**

Runs Claude Code, Gemini CLI, Codex and other deep-agent harnesses concurrently with isolated containers, credentials and git worktrees, locally or across Kubernetes.

The model gets a small coordination CLI rather than a prescriptive orchestration framework; agents decide how to collaborate while the substrate supplies isolation and telemetry.

`Go · containers · Kubernetes · worktrees · multi-agent systems`

</td>
<td width="50%" valign="top">

### 🎞️ [pixelpitch](https://github.com/vamsiramakrishnan/pixelpitch)
**Agent-authored HTML → editable PPTX**

A designer-grade slide system with live preview, multiple code-agent backends and an HTML→PowerPoint compiler. The converter maximizes **native editable PowerPoint area** subject to visual-fidelity floors, selectively rasterizing only effects PowerPoint cannot represent.

Includes corpus harvesting, SSIM/OCR oracles, reusable design systems and dozens of presentation/media skills.

`Python · TypeScript · Playwright · PPTX · visual evaluation`

</td>
</tr>
</table>

## Other experiments I keep close

<table>
<tr>
<td><b><a href="https://github.com/vamsiramakrishnan/ge-msft">ge-msft</a></b></td>
<td>Gemini Enterprise inside Word, Excel, PowerPoint, OneNote, Outlook and Teams; client-direct Entra→Google federation, typed command algebra, reversible writes and durable provenance.</td>
</tr>
<tr>
<td><b><a href="https://github.com/vamsiramakrishnan/antigravity-a2a-a2ui">antigravity-a2a-a2ui</a></b></td>
<td>Per-user Antigravity workspaces over Managed Agents, with identity-derived tenancy, credential brokering, skill revisions and sandbox hardening.</td>
</tr>
<tr>
<td><b><a href="https://github.com/vamsiramakrishnan/AdvancedLaneLines">AdvancedLaneLines</a></b> · <b><a href="https://github.com/vamsiramakrishnan/BehavioralCloning">BehavioralCloning</a></b> · <b><a href="https://github.com/vamsiramakrishnan/TrafficSignRecognition">TrafficSignRecognition</a></b></td>
<td>Older autonomous-driving work: lane geometry, behavioral cloning and traffic-sign recognition — useful fossils from the deterministic-controls → ML transition.</td>
</tr>
<tr>
<td><b><a href="https://github.com/vamsiramakrishnan/kubernetes-ci-cd">kubernetes-ci-cd</a></b> · <b><a href="https://github.com/vamsiramakrishnan/landing-zone">landing-zone</a></b> · <b><a href="https://github.com/vamsiramakrishnan/splunk-export-logs">splunk-export-logs</a></b></td>
<td>Earlier cloud/platform work around Kubernetes, landing zones, CI/CD and operational data plumbing.</td>
</tr>
</table>

## The recurring design rules

```text
01  SPEC > PROMPT                  durable intent should outlive a model call
02  IR > HAND-WIRING              compile multiple surfaces from one source of truth
03  REFUSE > GUESS                uncertainty is data; preserve it
04  RESUME > RETRY                acting agents need memory of reality
05  ADDRESSES > SUMMARIES         if bytes disappear, keep a deterministic path back
06  EVIDENCE > VIBES               performance claims need receipts
07  PURE COMPOSES; EFFECTS GATE    keep side effects explicit and reviewable
08  LOCAL FIRST                    make expensive/cloud execution opt-in when possible
09  BORING CONTROL PLANE           put stochasticity where it buys something
10  DEVEX IS ARCHITECTURE          setup, errors, introspection and docs are system design
```

## Languages I reach for

<div align="center">

<img src="https://img.shields.io/badge/Python-reach%20%2B%20experimentation-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Rust-runtimes%20%2B%20correctness-000000?style=flat-square&logo=rust&logoColor=white" alt="Rust">
<img src="https://img.shields.io/badge/Go-control%20planes%20%2B%20infra-00ADD8?style=flat-square&logo=go&logoColor=white" alt="Go">
<img src="https://img.shields.io/badge/TypeScript-compilers%20%2B%20product%20surfaces-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript">

<br><br>

<img src="https://github-readme-stats.vercel.app/api?username=vamsiramakrishnan&show_icons=true&hide_border=true&rank_icon=github&theme=transparent&include_all_commits=true&custom_title=Ship%20log" height="165" alt="GitHub stats">
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=vamsiramakrishnan&layout=compact&hide_border=true&theme=transparent&langs_count=8" height="165" alt="Top languages">

</div>

## Writing

I write about the infrastructure around AI systems: agent runtimes, evaluation, inference economics, developer tooling, context engineering and the gap between a demo and a system that survives contact with an enterprise.

**The Plumbing Paradox** · **Winter is Coming** · **The Asymptote of Good Enough**

Longer notes: [mrvemzi.notion.site](https://mrvemzi.notion.site) · posts: [LinkedIn](https://www.linkedin.com/in/vamsiramakrishnan/)

---

<div align="center">

<sub>
The repo names change. The question usually does not:<br>
<b>what deterministic machinery has to exist around a probabilistic model before the result becomes an engineering system?</b>
</sub>

</div>
