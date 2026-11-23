# AgentRouter for Hermes

Compare where competitors appear for one Google query with what people said about them on Reddit this week. The plugin adds one Hermes skill, `agentrouter:competitor-brief`. It uses AgentRouter's hosted MCP connection.

## Install from this package

From the extracted package root, run the following for your active Hermes profile. Set `HERMES_HOME` to that profile's directory if you use a custom profile. The copy command stops if the plugin directory already exists.

```sh
profile_dir="${HERMES_HOME:-$HOME/.hermes}"
mkdir -p "$profile_dir/plugins"
mkdir "$profile_dir/plugins/agentrouter" &&
  cp -R plugin.yaml __init__.py skills "$profile_dir/plugins/agentrouter/" &&
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

The plugin registers a local Markdown skill. Hermes manages OAuth credentials and sends research queries to AgentRouter. Paid requests go to the selected provider and can spend the signed-in user's balance. The skill asks for a budget. The `untrusted` MCP setting enables Hermes approval for write-capable calls in interactive approval mode. Keep approvals enabled when using the plugin. The plugin adds no telemetry, shell tools or scheduled jobs.

[AgentRouter MCP and account setup](https://docs.agentrouter.to/integrations/mcp?utm_source=hermes&utm_medium=plugin) · [Examples with receipts](https://docs.agentrouter.to/examples)
