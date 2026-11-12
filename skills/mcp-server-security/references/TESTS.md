# MCP server security test and release gates

This is a plan for a **project-specific executable test suite**. These tests cannot pass merely by executing this documentation repository's CI.

| ID | Test input / adversarial condition | Required assertion |
| --- | --- | --- |
| AUTH-01 | Missing, invalid, expired, revoked (if supported), wrong-issuer or wrong-audience token | Denied; zero effects |
| AUTH-02 | Authenticated identity lacking tool/resource permission | Denied; zero effects |
| TENANT-01 | Client alters tenant/resource identifier | No cross-tenant read/write |
| RPC-01 | Direct calls without discovery, out of order or concurrent | Same authorization as sequential flow |
| RPC-02 | Unsupported revision; conflicting HTTP routing metadata/body | Reject as required by pinned revision |
| HTTP-01 | Untrusted Host/forwarded header or disallowed Origin | Reject before dispatch |
| HTTP-02 | Oversized payload, slow stream, concurrency flood | Bounded CPU/memory/connections |
| INPUT-01 | Unknown fields, invalid types, oversized strings, deep nesting | Schema rejection; zero effects |
| FILE-01 | Traversal, encoded paths, symlink switches/races | Never leaves authorized root |
| NET-01 | Private/metadata IP, DNS rebinding, redirect to disallowed host | No forbidden socket connection |
| INJECT-01 | Tool result contains forged system/agent instructions | No unauthorized tool, credential or policy changes |
| SUPPLY-01 | Tool name/schema/permissions or runtime dependency changes | Review gate detects and blocks unapproved expansion |
| EFFECT-01 | Concurrent duplicate/replay/retry | At most approved effects, matching idempotency contract |
| EFFECT-02 | Timeout, partial success, unexpected upstream reply | No fabricated success; durable reconciliation state |
| SECRET-01 | Error/log/tool-result includes sensitive payload candidate | No secret/token leakage |
| TRANSPORT-01 | Stdio stdout pollution; HTTP cancellation/stream termination | Transport correctness; effects remain consistent |

## Evidence

Record for each applicable test:

```text
TEST_ID:
TARGET_REVISION:
SDK_AND_RUNTIME:
TEST_COMMAND:
ENVIRONMENT:
ACTUAL_RESULT:
ASSERTION_ON_SIDE_EFFECTS:
EVIDENCE_PATH_OR_CI_RUN:
STATUS: PASS | FAIL | NOT_RUN
```

Use fake upstream APIs and disposable filesystem/network namespaces for negative testing. Do not scan or attack public infrastructure.

## Release decision

Release is **BLOCKED** if:

- a relevant [SPEC MUST] or [POLICY MUST] is violated;
- identity, authorization, tenant isolation, egress boundaries, or the state owner are unverified;
- a write tool has no approved duplicate-effect / partial-failure policy;
- high-impact supply-chain findings are unresolved without accepted mitigation;
- mandatory tests are FAIL/NOT_RUN or evidence is unavailable;
- tool or permission expansion lacks explicit approval.

Documentation CI only validates that a skill package is structured correctly; it does not satisfy any test case above. Do not suppress checks or fabricate evidence.
