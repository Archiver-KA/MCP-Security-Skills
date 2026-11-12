# Source registry and normative-claim policy

Verified starting points on **2026-11-12**. Standards and SDKs evolve; the project-pinned revision and version-specific implementation documentation take precedence.

## Normative MCP sources

- [2026-07-28 specification](https://modelcontextprotocol.io/specification/2026-07-28)
- [Transport overview](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports)
- [Streamable HTTP transport](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)
- [Authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [Authorization security considerations](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations)
- [2025-11-25 specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP 2026 release announcement (explanatory; not normative)](https://blog.modelcontextprotocol.io/posts/2026-07-28/)

## Agent and security references

- [Agent Skills specification](https://agentskills.io/specification)
- [MCP security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices)
- [OWASP MCP Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html)
- [NIST SP 800-190, Application Container Security Guide](https://csrc.nist.gov/pubs/sp/800/190/final)
- [OAuth protected resource metadata, RFC 9728](https://www.rfc-editor.org/rfc/rfc9728)
- [OAuth resource indicators, RFC 8707](https://www.rfc-editor.org/rfc/rfc8707)
- [OAuth security best current practice, RFC 9700](https://www.rfc-editor.org/rfc/rfc9700)
- [skills CLI usage and supported agents](https://github.com/vercel-labs/skills)

## Evidence rule

For every **[SPEC MUST]** in an implementation, capture the **exact versioned clause** in the selected protocol specification. Do not cite a blog, issue, draft, or this skill as the normative authority. A security hardening measure may instead be a **[POLICY MUST]** with its own rationale.

For every SDK-specific code or configuration example, verify against the **exact installed SDK version** and its documentation/source. Do not assume automatic modern/legacy fallback, authentication enforcement, or client compatibility. If facts are missing, return `BLOCKED`.
