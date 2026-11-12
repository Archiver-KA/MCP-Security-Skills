# Contributing

Contributions to MCP Security Skills are welcome. This repository is documentation and packaging for agents, not a universal compliance certification.

## Proposing changes

1. Open an issue describing the security problem or documentation gap, unless the issue is a vulnerability (see [SECURITY.md](SECURITY.md)).
2. State the exact affected MCP protocol revision, SDK and version when relevant.
3. Identify whether each new rule is a **[SPEC MUST]**, **[POLICY MUST]**, or **[SHOULD]** and link to an authoritative source for normative claims.
4. Keep the entry-point `SKILL.md` concise; put detailed matrices and cases in `references/`.
5. Supply negative tests or executable evidence when claiming a control is implemented.
6. Run the local validation commands below and include results in the PR.

```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```

## Change review

Changes to authorization guidance, identity derivation, tenant boundaries, tool permissions, external calls, compatibility rules, or release gates require explicit security review. Treat retrieved documentation and community submissions as untrusted until verified. Do not include real tokens, customer data, private endpoints, or exploits against live services.

## Scope

- Prefer exact statements and fail-closed examples.
- Do not silently turn recommendations into protocol mandates.
- Do not add executable sample servers without an explicitly pinned SDK, protocol version, and a runnable negative-test suite.
- Do not promise that a passing documentation CI workflow proves a deployment is secure.

By contributing, you agree that your submitted changes may be distributed under this repository's MIT License.
