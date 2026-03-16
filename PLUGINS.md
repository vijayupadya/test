# Test Agent Plugins

Example agent plugins for testing the VS Code Copilot Chat "Install Plugin from Source" feature.

## Plugins

| Plugin | Description | Features Tested |
|--------|-------------|-----------------|
| `hello-world` | Simple plugin with default structure | Commands, skills, agents in default dirs |
| `custom-paths` | Uses custom component directories | Manifest `commands`/`skills`/`agents` path overrides |
| `mcp-and-hooks` | MCP servers and hooks | `.mcp.json`, `hooks/hooks.json` |
| `multi-plugin` | Two sub-plugins in one repo | `marketplace.json` with multiple plugins, quick pick selection |

## Usage

### Install the whole repo as a marketplace
Use `vijayupadya/test` with the "Install Plugin from Source" command.

### Install a specific sub-repo plugin
Use `vijayupadya/test` — when multiple plugins are found, pick the one you want from the quick pick.

### Install the multi-plugin repo
Navigate to `plugins/multi-plugin` or use the repo root — the `marketplace.json` at the root lists three plugins to choose from.
