# GitHub discovery and social preview (maintainer checklist)

The Agent Skills package is committed in this repository. The repository's **About** fields, topics, visibility, and social preview are GitHub-hosted settings; changing Markdown files alone does not update them.

## GitHub About metadata

**Recommended repository description** (keep this as a single plain-text line):

```text
Security-first Agent Skill for MCP servers: OAuth, prompt injection, SSRF, least privilege, tenant isolation, threat modeling and testing.
```

**Topics** (12 relevant discoverability keywords):

```text
mcp
model-context-protocol
mcp-security
agent-skills
ai-security
security-audit
threat-modeling
prompt-injection
oauth
least-privilege
claude-code
codex
```

## Approved website and social profiles

- Project website / GitHub homepage: **https://sinera.io/**
- Project X: **https://x.com/sinera_labs**
- Personal X: **https://x.com/archivist336**

Only the project website belongs in the GitHub About **Website** field. GitHub About has no dedicated fields for both X accounts; distinguish them in the [README](../README.md).

GitHub About properties are hosted settings; editing repository files does not change them. To apply these, use **About** (gear icon) or an authenticated GitHub CLI.

Alternatively, from a machine with an authenticated `gh` CLI and explicit maintainer approval:

```bash
gh repo edit Archiver-KA/MCP-Security-Skills \
  --description "Security-first Agent Skill for MCP servers: OAuth, prompt injection, SSRF, least privilege, tenant isolation, threat modeling and testing." \
  --homepage "https://sinera.io/"

# CAUTION: The PUT below REPLACES all existing topics. Review the current set first.
gh api repos/Archiver-KA/MCP-Security-Skills/topics --jq '.names'
gh api --method PUT repos/Archiver-KA/MCP-Security-Skills/topics \
  -f 'names[]=mcp' \
  -f 'names[]=model-context-protocol' \
  -f 'names[]=mcp-security' \
  -f 'names[]=agent-skills' \
  -f 'names[]=ai-security' \
  -f 'names[]=security-audit' \
  -f 'names[]=threat-modeling' \
  -f 'names[]=prompt-injection' \
  -f 'names[]=oauth' \
  -f 'names[]=least-privilege' \
  -f 'names[]=claude-code' \
  -f 'names[]=codex'
```

Never paste a token into the README, a shell command, or CI logs.

## Publishing safely

Before switching to Public, inspect the full Git commit history (including author email metadata), Actions logs and artifacts, and any release or branch not represented by a current-file scan. The previously completed basic pattern scan found no matches in 17 current tracked text files, but does not certify that the repo contains no secrets.

A repository administrator can change visibility in GitHub **Settings -> General -> Danger Zone -> Change repository visibility -> Public**. With an authenticated GitHub CLI, use:

```bash
gh repo view Archiver-KA/MCP-Security-Skills --json visibility,description,homepageUrl,repositoryTopics
gh repo edit Archiver-KA/MCP-Security-Skills --visibility public --accept-visibility-change-consequences
gh repo view Archiver-KA/MCP-Security-Skills --json visibility --jq '.visibility'
```

Publishing exposes code, commit metadata and Actions history; it can affect rulesets and stars. See the [GitHub visibility documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility).

## Social preview

Image created for the project: `mcp-security-social-preview.png` (1280 × 640 px, PNG, < 1 MB). GitHub requires an image upload in the web UI and does not provide a public REST/GraphQL upload endpoint.

1. Ensure the image was reviewed and the repository is **public**. GitHub says public repositories can upload a new preview; private repositories may require a previously uploaded image, and preview sharing requires a public repository.
2. Visit `https://github.com/Archiver-KA/MCP-Security-Skills/settings`.
3. Choose **General -> Social preview -> Edit -> Upload an image**.
4. Upload the approved `mcp-security-social-preview.png`.
5. Verify the card renders when the **public** repository URL is shared.

GitHub guide: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview

## Install verification

The repository's GitHub Actions workflow tests **local, checked-out source installation** via a pinned `skills` CLI and Node.js 22.20.0. This works without public repository access. It does **not** prove GitHub shorthand installation.

Once the repo is public, the workflow conditionally tests the public shorthand. The public, unauthenticated installation command is:

```bash
npx skills add Archiver-KA/MCP-Security-Skills --skill mcp-server-security
```

For local inspection before publishing:

```bash
npx skills add . --skill mcp-server-security --list
```

For a noninteractive check in a disposable directory:

```bash
npx --yes skills@1.8.1 add /path/to/MCP-Security-Skills --skill mcp-server-security -a claude-code -y --copy
```

Requires Node.js 22.20 or later. CLI reference: https://github.com/vercel-labs/skills/blob/main/docs/commands.md

## Release checklist

- [ ] Confirm visibility is intentionally changed from private to public by the maintainer.
- [ ] Apply repository Description and Topics in GitHub About.
- [ ] Upload the social preview via GitHub Settings.
- [ ] Confirm the public installation workflow passes.
- [ ] Inspect the repository from a signed-out browser.
- [ ] Only then announce public installation in community directories.

**No claim of MCP server security is implied** by a passing skill packaging/install test.
