<div align="center">

# Vamsi Ramakrishnan

**Forward Deployed Engineering · JAPAC lead · Google Cloud**

Melbourne, Australia

[![LinkedIn](https://img.shields.io/badge/LinkedIn-vamsiramakrishnan-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vamsiramakrishnan/)
[![X](https://img.shields.io/badge/X-@mrvemzi-000000?style=flat&logo=x&logoColor=white)](https://twitter.com/mrvemzi)
[![Notion](https://img.shields.io/badge/Notes-mrvemzi.notion.site-999999?style=flat&logo=notion&logoColor=white)](https://mrvemzi.notion.site)

</div>

I lead Google Cloud's Forward Deployed Engineering organization across JAPAC. My teams put AI into production with enterprises across the region — banks, telcos, universities — across Gemini Enterprise, Vertex AI, and agents.

This account is the other half of that job. I ship something every day — not as a discipline, but because building a thing is how I understand it. A problem isn't formalized until it compiles. My daily collaborators: Antigravity, Claude, Codex, DeepSeek.

Before all this: seven years of safety-critical automotive systems — ABS, ADAS, ISO 26262. It left me a permanent instinct for deterministic systems in a probabilistic field. Everything below is that instinct, applied to agents.

<br/>

## Compilers, not copilots

Agent tooling should be deterministic wherever it can be, and probabilistic only where it must be. Specs are the durable asset; code is a side effect.

<table>
<tr>
<td width="50%">

**[anvil](https://github.com/vamsiramakrishnan/anvil)** · TypeScript

Compiles API specifications — OpenAPI, SOAP/WSDL, gRPC, GraphQL — into type-safe, agent-ready tools. A compiler, not a per-run agent task. Built for environments where "the agent figured it out" is not an acceptable audit answer.

</td>
<td width="50%">

**[gemini-rs](https://github.com/vamsiramakrishnan/gemini-rs)** · Rust

Full SDK for the Gemini Multimodal Live API. Wire protocol, agent runtime, and fluent DX in three layered crates. Real-time voice agents with Rust's guarantees underneath.

</td>
</tr>
<tr>
<td width="50%">

**[adk-fluent](https://github.com/vamsiramakrishnan/adk-fluent)** · Python

A fluent builder API over Google's Agent Development Kit. The ADK, with the ceremony removed.

</td>
<td width="50%">

**[aiplex](https://github.com/vamsiramakrishnan/aiplex)** · Go

Tool, agent, and model registry & gateway. Keycloak, GKE, cloud service mesh, mTLS, SPIFFE. The control plane enterprises ask for after their first hundred agents.

</td>
</tr>
</table>

<br/>

## Durability

Agents that act on the world need the recovery semantics of databases, not chatbots.

<p>
<a href="https://github.com/vamsiramakrishnan/tape"><img src="https://github-stats-extended.vercel.app/api/pin/?username=vamsiramakrishnan&repo=tape&theme=transparent&hide_border=true" alt="tape"/></a>
<a href="https://github.com/vamsiramakrishnan/durable-agents"><img src="https://github-stats-extended.vercel.app/api/pin/?username=vamsiramakrishnan&repo=durable-agents&theme=transparent&hide_border=true" alt="agents-that-act"/></a>
</p>

**Tape** is a durable execution substrate for ADK agents — append-only journaling underneath the agent loop, so a crashed agent resumes instead of re-deciding. **Agents That Act** is the treatise that argues why.

<br/>

## Activity

<p>
<img src="https://github-stats-extended.vercel.app/api?username=vamsiramakrishnan&show_icons=true&include_all_commits=true&rank_icon=github&theme=transparent&hide_border=true&disable_animations=true&custom_title=Shipping" height="165" alt="stats"/>
<img src="https://github-stats-extended.vercel.app/api/top-langs/?username=vamsiramakrishnan&layout=compact&langs_count=6&theme=transparent&hide_border=true" height="165" alt="languages"/>
</p>

Python for reach. Rust for correctness. Go for infrastructure. TypeScript for tools.

<br/>

## Writing

Essays on agent infrastructure, inference economics, and evaluation — on [Substack and LinkedIn](https://www.linkedin.com/in/vamsiramakrishnan/), with longer notes at [mrvemzi.notion.site](https://mrvemzi.notion.site).

*The Plumbing Paradox* · *Winter is Coming* · *The Asymptote of Good Enough*
