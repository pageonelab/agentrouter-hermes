# AgentRouter for Hermes

The plugin registers four research skills in Hermes. Connect your AgentRouter account to look up current evidence and prices.

Preview two tools available to the competitor brief, including their inputs and pricing: [Google organic search results](https://www.agentrouter.to/tools/dataforseo.serp_google_organic?utm_source=hermes&utm_medium=plugin) and [Reddit post search](https://www.agentrouter.to/tools/anyapi.reddit.search?utm_source=hermes&utm_medium=plugin).

## Bundled skills

Ask in your own words or name a skill. The host uses its description to select the instructions.

| Skill | Try asking |
| --- | --- |
| [competitor-brief](skills/competitor-brief/SKILL.md) | Which alternatives do buyers mention on Reddit, and what made them switch? |
| [job-shortlist](skills/job-shortlist/SKILL.md) | Find three Toronto sales roles I can apply for today. Link the employer forms. |
| [growth-teardown](skills/growth-teardown/SKILL.md) | How does this product turn free users into referrals? Show where that happens. |
| [ugc-teardown](skills/ugc-teardown/SKILL.md) | Use my clip notes to write a 12-second Reel for this product, with two opening lines. |

In Hermes the names are qualified, for example `agentrouter:job-shortlist`. Enabling the plugin makes the skills available in that profile.

## Install

To install the published source directly, use `hermes plugins install PageOneLab/agentrouter-hermes --enable`. For an existing install from that repository, add `--force` to refresh it. For catalog-managed installations, `hermes plugins update agentrouter` installs the version currently approved in the [Hermes catalog](https://hermes-agent.nousresearch.com/marketplace/agentrouter).

### Manual installation

From the extracted package root, run the following for your active Hermes profile. Set `HERMES_HOME` to that profile's directory if you use a custom profile. The copy command stops if the plugin directory already exists.

```sh
profile_dir="${HERMES_HOME:-$HOME/.hermes}"
mkdir -p "$profile_dir/plugins"
mkdir "$profile_dir/plugins/agentrouter" &&
  cp -R plugin.yaml __init__.py skills.json skills "$profile_dir/plugins/agentrouter/" &&
  hermes plugins enable agentrouter
```

Merge this entry into the profile's `config.yaml` under its existing `mcp_servers` key.

```yaml
mcp_servers:
  agentrouter:
    url: https://mcp.agentrouter.to/
    auth: oauth
    oauth:
      scope: "read invoke"
    trust: untrusted
    tools:
      include: [find_tools, describe_tool, invoke_tool, get_run]
```

Run `hermes mcp login agentrouter`, finish sign-in in your browser, and start a new Hermes session. Ask “Use the AgentRouter competitor brief to compare vercel.com and netlify.com for ‘frontend hosting’ in US English. Quote the cost first.” After approval, the report includes linked evidence, missing data and receipt totals.

## Data and billing

The plugin registers four local Markdown skills. Hermes manages OAuth credentials and sends research queries to AgentRouter. Paid requests go to the selected provider and can spend the signed-in user's balance. Users can request a free quote or set a spending limit. Approved calls without a per-call ceiling use actual-usage billing under configured account budgets. The `untrusted` MCP setting enables Hermes approval for write-capable calls in interactive approval mode. Keep approvals enabled when using the plugin. The plugin adds no telemetry, shell tools or scheduled jobs.

[AgentRouter MCP and account setup](https://docs.agentrouter.to/integrations/mcp?utm_source=hermes&utm_medium=plugin) · [Examples with receipts](https://docs.agentrouter.to/examples)
