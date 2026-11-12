# MCP threat model worksheet

Model the chain: untrusted content -> host/LLM -> MCP client -> transport/gateway -> MCP handler -> privileged API / durable state.

For every boundary, record:

```text
Asset:
Attacker-controlled entry:
Principal / tenant:
Trust boundary:
Authorized operation:
Authoritative state owner:
Possible unwanted effect:
Preventive control:
Detection / audit:
Negative test:
Residual risk / reviewer:
```

## Priority scenarios

| Threat | Boundary failure | Required check |
| --- | --- | --- |
| Prompt or tool-output injection | External text promoted to agent instruction | Tool output cannot grant permissions or execute commands |
| Tool metadata poisoning / rug pull | Changed tool name, description, schema or annotations | Reviewed tool contract diff; no implicit approval |
| Confused deputy / BOLA | Server uses broad credentials for unprivileged caller | Authenticated principal, tenant and resource permission verified on each call |
| Token passthrough | Inbound token used at unrelated downstream API | Validate MCP audience; distinct downstream credential/audience |
| SSRF | Caller-controlled URL reaches private network or metadata endpoint | Explicit host/scheme/port policy, DNS/connect-time and redirect checks |
| Path traversal / symlink race | File access escapes approved root | OS-enforced scoped paths and safe handle-based operations |
| Command / SQL injection | String interpolation into privileged interpreter | Fixed commands/typed APIs and bound parameters |
| Replay / race / retry | Duplicate or inconsistent external writes | Durable idempotency, concurrency control and reconciliation |
| Partial failure | Timeout becomes false success, or state is lost | Explicit pending/unknown states; owner-based reconciliation |
| Secret exposure | Credentials leak through logs/errors/tool output | Redaction by allowlist; non-public audit sinks |
| Denial of service | Unbounded bodies, streams, CPU, external calls | Quotas and hard resource limits |
| Dependency compromise | Malicious SDK/image/startup script changes privileges | Pinning, integrity checks, review and CI gates |

For each scenario, ask: **What changes if the attacker calls the tool directly, out of order, concurrently, or repeatedly?** Never assume earlier discovery or a UI confirmation proves current authorization.

Do not run adversarial tests against third-party networks or production users without a designated authorized test environment. Prefer fixtures, stubs and isolated services.
