# Vamsi Ramakrishnan

I build the software around AI models: tools that expose useful capabilities,
keep execution inspectable, and make results testable.

[LinkedIn](https://www.linkedin.com/in/vamsiramakrishnan/) ·
[Essays](https://mrvemzi.notion.site) · [X](https://twitter.com/mrvemzi)

## Three places to start

### Straitjacket: keep tool output out of the agent's way

A long test log should not consume the context needed to fix the failure.
Straitjacket captures tool output, returns a bounded result, and gives the agent
addresses for retrieving the omitted evidence. Its edit workflow connects
observed source, anchored changes, verification, and continuation evidence.

**First proof:** run one noisy command with `ctx run`, then retrieve the lines
behind the result. Compare with native tools on your own task; the published
benchmarks include cases where the extra layer loses.

[Repository and quickstart](https://github.com/vamsiramakrishnan/straitjacket) ·
[Evidence](https://github.com/vamsiramakrishnan/straitjacket/blob/main/BENCHMARKS.md) ·
[Docs](https://vamsiramakrishnan.github.io/straitjacket/)

### Anvil: turn an API contract into tools with shared policy

A CLI and an MCP server should not disagree about whether a refund needs
confirmation. Anvil compiles an API description and a reviewed manifest into
interfaces that carry the same policy, plus mocks and evidence for checking it.

**First proof:** compile the payments fixture, inspect the refund policy,
observe a refusal, then produce a dry-run request plan with its requirements
satisfied. No upstream payment service is needed for that workflow.

[Repository and quickstart](https://github.com/vamsiramakrishnan/anvil) ·
[Supported inputs](https://github.com/vamsiramakrishnan/anvil/blob/main/docs/SOURCE_FORMATS.md) ·
[Docs](https://vamsiramakrishnan.github.io/anvil/)

### Worldloom: build a synthetic enterprise with answers you can check

Plausible documents are not enough for an evaluation. Worldloom builds related
facts, artifacts, and evaluation truth from a synthetic world, then renders
files such as spreadsheets, documents, slides, and PDFs. The repository is
named **synthetic-foundry**; the product and CLI are **Worldloom** and `worldloom`.

**First proof:** build a seeded incident corpus, render it, validate its
coherence, and run the retrieval baselines. Coherent source data and successful
retrieval are separate results, both available for inspection.

[Repository and quickstart](https://github.com/vamsiramakrishnan/synthetic-foundry) ·
[Guides](https://github.com/vamsiramakrishnan/synthetic-foundry/blob/main/docs/README.md) ·
[Docs](https://vamsiramakrishnan.github.io/worldloom/)

These products address different parts of an agent workflow. They can be
assessed independently; this is not a claim of a packaged integration between them.

## Find the system for your problem

| You need to… | Start with | Evaluate first |
|---|---|---|
| Recover an acting agent after interruption | [Tape](https://github.com/vamsiramakrishnan/durable-agents) | Journal, replay, and effect recovery |
| Build a Rust text or live-voice agent | [gemini-rs](https://github.com/vamsiramakrishnan/gemini-rs) | One text request or voice session |
| Write native ADK agents with less setup code | [adk-fluent](https://github.com/vamsiramakrishnan/adk-fluent) | A builder and the native object it returns |
| Turn agent requirements into reviewable implementation evidence | [GE Agent Factory](https://github.com/vamsiramakrishnan/ge-agent-factory) | A local proof pack |
| Apply policy to agent, tool, and model traffic | [AIPlex](https://github.com/vamsiramakrishnan/aiplex) | The traffic plane you need |
| Convert authored HTML into PowerPoint | [Pixelpitch](https://github.com/vamsiramakrishnan/pixelpitch) | Export fidelity and element editability |
| Use Gemini Enterprise inside Microsoft 365 | [ge-msft](https://github.com/vamsiramakrishnan/ge-msft) | The supported host and document operation |
| Explore an agent authoring interface | [Ember](https://github.com/vamsiramakrishnan/gemini-enterprise-ember) | One playbook through the frontend prototype |

## Explore the wider portfolio

The [repository directory](PORTFOLIO.md) separates original projects from forks
and links older experiments without presenting every repository as a supported
product. Each project's README is the starting point for its setup and limits.

Earlier work includes autonomous-driving experiments, cloud operations,
Kubernetes, and application integrations. The recurring interest is making
uncertain behavior observable and testable.

## Activity

<div align="center">
<img src="https://github-readme-activity-graph.vercel.app/graph?username=vamsiramakrishnan&bg_color=00000000&color=8b949e&line=3fb950&point=58a6ff&area=true&area_color=238636&hide_border=true&custom_title=Rolling%20engineering%20activity" width="100%" alt="GitHub activity graph">
</div>

## How I judge the work

Useful output before architecture tours. Reviewable policy before unattended
effects. Reproducible evidence before performance claims. A small first run
that makes the next decision clear.

[Read the essays](https://mrvemzi.notion.site) ·
[Browse all repositories](https://github.com/vamsiramakrishnan?tab=repositories)
