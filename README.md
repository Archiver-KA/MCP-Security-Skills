# MCP Security Skills — Secure MCP Server Development and Auditing

An open-source, security-first **Agent Skill for Model Context Protocol (MCP) server security**: design, threat-model, harden, review, and test stdio and Streamable HTTP MCP servers.

**Status:** Community draft (v0.1.0). Documentation and agent workflow, **not** an MCP server, security scanner, certification, or substitute for a project-specific security review.

## Project and community

- **Project website:** [Sinera](https://sinera.io/)
- **Project X account:** [@sinera_labs](https://x.com/sinera_labs)
- **Personal X account:** [@archivist336](https://x.com/archivist336)

The project and personal social accounts serve different purposes. These profiles are provided by the repository maintainer; they do not constitute an independent security endorsement.


- **License:** MIT
- **Skill:** `mcp-server-security`
- **Protocols:** Version-aware guidance for MCP `2026-07-28` and earlier handshake-era revisions
- **Audience:** Coding agents and engineers implementing local (stdio) or remote (Streamable HTTP) MCP servers
- **Principle:** Deny by default; verify identity and authorization for every effectful call; do not infer permissions from conversation or tool metadata.

## Security coverage

- MCP server authentication and resource-level authorization (OAuth, audience, scopes).
- Prompt injection, tool poisoning, and confused-deputy threats.
- SSRF, filesystem traversal, command injection, and network egress restrictions.
- Least privilege, tenant isolation, secrets, and supply-chain controls.
- Idempotency, state-transition safety, negative testing, and release gates.

The [skill entry point](skills/mcp-server-security/SKILL.md) and its versioned [security references](skills/mcp-server-security/references/SOURCES.md) provide an auditable, fail-closed implementation workflow. These are agent instructions, not an executable MCP server.

## Install

**Recommended (skills CLI):** Requires Git and Node.js 22.20+ for the current CLI.

```bash
# Install into the current project; choose an agent when prompted.
npx skills add Archiver-KA/MCP-Security-Skills --skill mcp-server-security

# Install globally (prompts for compatible agents).
npx skills add Archiver-KA/MCP-Security-Skills --skill mcp-server-security -g

# Example: non-interactive install for Claude Code.
npx skills add Archiver-KA/MCP-Security-Skills --skill mcp-server-security -a claude-code -y

# Verify and later check for updates.
npx skills list
npx skills check
```

**Manual installation:** Clone and copy `skills/mcp-server-security/` into an Agent Skills-compatible directory. Complete macOS/Linux, Windows PowerShell, update, uninstall, and private-repository instructions are in [INSTALL.md](INSTALL.md).

> Review this repository and any install tools before running commands. Installing a skill gives an agent instructions, not permissions. The repository must be public for unauthenticated community installations; until then GitHub authentication is required.

## Use it

After installation, ask your coding agent:

> Use the mcp-server-security skill to threat-model and audit my MCP server. First inventory protocol version, SDK/runtime, transport, principal/tenant model, tool permissions, data boundaries, and state owner. If any security contract field is unknown, report BLOCKED and do not implement dependent changes.

For an implementation request, supply the relevant repository, approved tool list and schemas, transport, MCP/SDK versions, identity provider, upstream permissions, deployment boundary, and tests. The skill does **not** choose these on your behalf.

## Contents

```text
.
├── README.md
├── INSTALL.md
├── LICENSE
├── SECURITY.md
├── CONTRIBUTING.md
├── .github/workflows/validate.yml
├── scripts/validate_skill.py
├── tests/test_validate_skill.py
└── skills/
    └── mcp-server-security/
        ├── SKILL.md
        ├── assets/CONTRACT.example.yaml
        └── references/
            ├── PROTOCOL.md
            ├── THREATS.md
            ├── CONTROLS.md
            ├── TESTS.md
            └── SOURCES.md
```

The short skill is the entry point. Its references are loaded only for relevant tasks.

## Security model

1. **Contract gate:** Identify exact protocol/SDK versions, tool effects, principal, tenant, upstream resources, and state owner. Unknown required information -> `BLOCKED`.
2. **Trust boundaries:** Treat caller input, LLM output, tool descriptions, fetched content, and upstream responses as untrusted.
3. **Protocol correctness:** Follow the specified MCP revision, rather than mixing handshake-era and stateless-era rules.
4. **Authorization:** Authenticate and authorize the specific principal/tenant/resource/tool/operation before any effect. Never treat a session ID, tool annotation, or user-supplied tenant as authorization.
5. **I/O confinement:** Restrict filesystem, subprocess, outbound network, and secrets to explicitly approved scopes.
6. **Effect semantics:** Use the authoritative state owner, bounded external interactions, and explicit idempotency/reconciliation for writes.
7. **Evidence:** Require real negative tests for auth bypass, cross-tenant access, SSRF, path traversal, replay, failures, and leakage. A checklist alone is not evidence.

Rules tagged **[SPEC MUST]** are version-scoped claims requiring a citation to the pinned MCP specification. **[POLICY MUST]** are stricter requirements of this skill, not necessarily protocol requirements. **[SHOULD]** are recommendations subject to documented rationale.

## Validate this repository

```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```

These checks validate packaging and documentation references only. They do **not** test an actual MCP server or its deployment.

## References

- [MCP 2026-07-28 specification](https://modelcontextprotocol.io/specification/2026-07-28)
- [MCP Authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [MCP security considerations](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations)
- [Agent Skills specification](https://agentskills.io/specification)
- [OWASP MCP Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html)
- [skills CLI](https://github.com/vercel-labs/skills)

See [SOURCES.md](skills/mcp-server-security/references/SOURCES.md) for the versioned source list and update policy.

## Discoverability and social preview

For GitHub About description, topic tags, CLI verification, and the official social-preview upload procedure, see [DISCOVERY.md](docs/DISCOVERY.md). GitHub repository About fields and the preview image require repository Settings access; files in this repository do not set those properties automatically.

## Contributing and security reports

Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing changes. Report vulnerabilities through [SECURITY.md](SECURITY.md), not a public issue containing exploit details or secrets.

Copyright (c) 2026 Archiver-KA. Released under the [MIT License](LICENSE).
