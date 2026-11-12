# Protocol and transport compatibility

Read this file when choosing or auditing a protocol/transport implementation. **Verify the selected revision and exact SDK version before translating requirements into code.**

## Two protocol eras

| Property | Handshake era (through 2025-11-25) | Modern era (2026-07-28) |
| --- | --- | --- |
| Lifecycle | `initialize` / `notifications/initialized` | Stateless requests; no initialize handshake |
| Capability information | Negotiated during handshake | Per-request `_meta` |
| Discovery | Initialize result | `server/discover` available (not a prerequisite to every operation) |
| Session | Optional HTTP session concepts | No MCP protocol-level sessions or `Mcp-Session-Id` |
| HTTP messages | Streamable HTTP revision-specific handling | One HTTP POST per message, response JSON or request-scoped SSE |
| HTTP routing metadata | Revision-specific | `MCP-Protocol-Version`, `Mcp-Method`, and `Mcp-Name` when required by the current transport rules |
| Request authority | Never derive from session or caller claims alone | Never derive from metadata or headers alone |

The JSON-RPC body is the source of truth for protocol metadata. Where headers mirror body information, enforce the revision's mismatch rules. `server/discover` is optional for modern clients to call; it is not an authorization gate.

[Official transport overview](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports) and [Streamable HTTP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http).

## stdio controls

- Standard output carries **only** protocol messages; send sanitized diagnostics to stderr.
- Fix the process command and arguments. Do not splice tool arguments into shell commands.
- Give the subprocess only the environment variables, filesystem access and network access the use case requires.
- Local processes inherit local OS privileges unless explicitly restricted. Treat client configuration and installed packages as a supply-chain boundary.

## Streamable HTTP controls

- Require TLS in remote production deployments; use trusted reverse-proxy headers only from configured proxies.
- Validate `Origin` where present, enforce allowed hosts, and avoid unauthenticated state-changing tools unless specifically approved.
- Bound request body/header size, concurrency, stream duration, resource use and idle timeouts.
- Keep allowlisted hosts/destinations and admission decisions independent from LLM or tool-text instructions.
- Implement correct version-specific cancellation and rejection behavior; do not mix session-era and modern-era transports.

## Authorization responsibilities

MCP authorization is **optional** as a protocol feature. When implementing protected HTTP MCP resources, follow the pinned revision's OAuth/resource server requirements.

- The MCP server validates that access tokens were issued for **that MCP resource**; reject wrong audience/resource, signature, issuer, lifetime, scope and tenant per applicable policy.
- MCP clients, not MCP servers, initiate client-side PKCE and resource-indicator requests. Do not misattribute client requirements to the server.
- Authorize the actual tool operation on the actual resource, independently of token authentication.
- Never forward inbound MCP bearer tokens as credentials for another resource server.
- Other authentication models must be specifically approved and must not be advertised as MCP OAuth compliance without evidence.
- For stdio, credentials commonly come from the launch environment; HTTP OAuth flows are not automatically applicable.

[Official authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization), [security considerations](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations).

## SDK support is separate from specification support

Never assume that a current SDK supports every MCP 2026-07-28 feature, or that the project is using its modern server APIs. Record the exact library package, version, transport class/entry point, compatibility mode, and evidence from installed code and official SDK documentation.

If current SDK docs disagree with examples here, identify the mismatch and block unsupported implementation choices.
