# Security control implementation guide

These are skill policy controls, not blanket claims about all MCP revisions.

## Identity and authorization

- Verify issuer, audience/resource, signature or introspection, expiry/not-before, subject and scope when using OAuth-protected HTTP.
- Derive tenant and effective resource permissions from trusted identity/policy services, not LLM arguments or client headers.
- Bind each effectful handler to an explicit permission and resource selector; deny absent/ambiguous decisions before I/O.
- Treat proxy assertions as trusted **only** across a documented authenticated proxy boundary.
- Treat approvals as scoped, attributable and time-limited where applicable. Tool annotations such as read-only hints are not approvals.

## Inputs, filesystem and network

- Validate object shape, types, enums, sizes, nesting, and unknown fields against the approved schema.
- Resolve files relative to a permitted root and use platform filesystem primitives resistant to symlink/TOCTOU races; a string-prefix test alone is insufficient.
- Prefer fixed upstream API clients. For URL inputs, authorize scheme/hostname/port, resolve/address at connection time, validate all redirects and block forbidden/internal/metadata networks unless explicitly allowed for that workload.
- Avoid raw command execution; use approved fixed binaries with separate, validated argument arrays. Use parameterized SQL or typed SDK calls.
- Enforce independent output schema and sensitivity controls; sanitize error and audit data.

## Secrets and isolation

- Inject secrets from an approved runtime secret source. Do not check them into Git, interpolate them into logs, or return them in tool responses.
- Restrict workload identity, filesystem mounts, host OS permissions, subprocess capabilities and network egress.
- For multi-tenant servers, test tenant separation at data, credentials, cache, queue, rate-limit and logs boundaries.
- Treat all external responses as tainted; prevent tool result text from changing authorization or policy.

## Effects -> interactions and recovery

For an approved non-idempotent write, define the authoritative state owner and an idempotency key scoped to principal/tenant/operation. Where the architecture supports it, atomically record a durable intent or outbox entry **before** the external call. Reconcile completion from the authoritative external system. A timeout yields pending/unknown until reconciled, never invented success.

This pattern requires a project-approved state model and storage mechanism. **Do not introduce a database, retry worker, message bus or new API without approval.** When those requirements are absent and cannot be met, block the write tool.

## Supply chain and deployment

- Pin exact SDK/runtime/dependencies and commit relevant lockfiles; verify provenance and vulnerability advisories against the pinned versions.
- Review tool names, descriptions, schemas and annotations as privileged interfaces; changing them requires a security review.
- Apply least-privilege CI permissions and restrict fork PR secret exposure. Never run untrusted pull request code with deployment credentials.
- Set explicit resource budgets, timeouts, audit retention and incident response owners.
- Before deployment, verify TLS, proxy trust, origin/host policy, secret rotation path, backups/recovery and rollback.

## Exceptions

An exception must identify its owner, approved duration, affected invariant, concrete compensating control, and negative tests. Exceptions cannot waive normative requirements of the selected protocol while still claiming conformance. Unknown or unapproved exceptions remain `BLOCKED`.
