# Installation and usage

This project distributes **agent instructions**. It does not install an MCP server, start a service, request tokens, or modify your existing server.

## Prerequisites

- A coding agent that supports the [Agent Skills format](https://agentskills.io/specification).
- For CLI installation: Git and Node.js 22.20+ (current `skills` CLI requirement).
- For manual installation: Git and the ability to copy files.
- A working GitHub credential **only while the source repository is private**.

Do not run unknown install scripts as an administrator. Read the files you install before granting your agent tool access.

## Option A: skills CLI (recommended)

Run inside the project that should use the skill:

```bash
npx skills add Archiver-KA/MCP-Security-Skills --skill mcp-server-security
```

Or install globally (for agents that support global skills):

```bash
npx skills add Archiver-KA/MCP-Security-Skills --skill mcp-server-security -g
```

Choose the agent in the CLI prompt. For Claude Code specifically:

```bash
npx skills add Archiver-KA/MCP-Security-Skills --skill mcp-server-security -a claude-code -y
```

For reproducible installs, use a reviewed release tag or exact commit instead of a moving branch:

```bash
# Replace vX.Y.Z with a published release tag; do not use this placeholder unchanged.
npx skills add Archiver-KA/MCP-Security-Skills@vX.Y.Z --skill mcp-server-security
```

Current CLI commands:

```bash
npx skills list
npx skills check
npx skills update mcp-server-security
npx skills remove mcp-server-security
```

CLI flags and installation paths can change. Confirm against the [official CLI documentation](https://github.com/vercel-labs/skills/blob/main/docs/commands.md).

## Option B: manual installation (macOS/Linux)

From the **target project's directory**:

```bash
git clone --depth 1 https://github.com/Archiver-KA/MCP-Security-Skills.git ./MCP-Security-Skills
mkdir -p .agents/skills

# Refuse to overwrite an existing skill.
if [ -e .agents/skills/mcp-server-security ]; then
  echo "Already installed; inspect and update deliberately." >&2
else
  cp -R ./MCP-Security-Skills/skills/mcp-server-security .agents/skills/
fi

test -f .agents/skills/mcp-server-security/SKILL.md
```

Do not run the clone command where a directory called `MCP-Security-Skills` already exists. Choose another destination in that case.

For an agent that only scans a different skills directory (for example `.claude/skills`), change the destination only after checking that agent's documentation. Keep the complete skill folder, including `references/` and `assets/`.

## Option C: manual installation (Windows PowerShell)

From the target project directory:

```powershell
git clone --depth 1 https://github.com/Archiver-KA/MCP-Security-Skills.git .\MCP-Security-Skills
New-Item -ItemType Directory -Force .\.agents\skills | Out-Null

if (Test-Path .\.agents\skills\mcp-server-security) {
    throw "Already installed. Inspect the existing directory before updating."
}

Copy-Item .\MCP-Security-Skills\skills\mcp-server-security .\.agents\skills\ -Recurse
if (-not (Test-Path .\.agents\skills\mcp-server-security\SKILL.md)) {
    throw "Installation failed: SKILL.md not found."
}
```

## Update / uninstall for manual copies

Manual installation does not automatically receive upstream changes. Compare the new release against your current copy; back up local edits and explicitly approve replacements. To uninstall, delete **only** the dedicated `mcp-server-security` directory after verifying the path is correct. Do not delete the parent skills directory.

## Using a private repository

Until this repository is public, authenticate with GitHub through your existing Git credentials or GitHub CLI. Do not embed personal access tokens in commands, configuration files, screenshots, or commit history.

## Trigger examples

- "Audit this MCP server against the mcp-server-security skill; produce failing tests and evidence."
- "Plan a secure stdio MCP tool set. Stop at the contract gate if permissions are missing."
- "Review OAuth audience validation, tenant separation, and outbound network controls for our Streamable HTTP MCP server."
- "Generate a negative-test matrix without modifying the server."

## Before implementing an MCP server

Copy [CONTRACT.example.yaml](skills/mcp-server-security/assets/CONTRACT.example.yaml) into your project as a planning document. Fill in every required field using approved project evidence. **Do not treat placeholder values as permissions.**

The agent must report `BLOCKED` for missing required policy details and `NOT_RUN` for tests not actually executed.
