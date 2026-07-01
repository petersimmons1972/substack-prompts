Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
Add a reachability gate to the deploy checklist below. For every new outbound host:port this integration introduces, output one row: **host_port | runtime_segment | dns_evidence | tcp_tls_evidence | egress_policy_link | verdict**.
- `runtime_segment`: the specific namespace, subnet, or execution environment the agent or service runs from — not "the cluster" or "prod."
- `dns_evidence`: the command or tool output that proves the name resolves from the runtime segment — not from your laptop. Format: `<command> → <result>`. If not yet verified: "NOT VERIFIED."
- `tcp_tls_evidence`: the command or tool output that proves a TCP/TLS connection succeeds from the runtime segment. Format: `<command> → <result>`. If not yet verified: "NOT VERIFIED."
- `egress_policy_link`: the NetworkPolicy, firewall rule, allowlist entry, or equivalent that explicitly permits this outbound connection — with a link or filename. If it does not exist: "NOT FILED."
- `verdict`: DONE (all three evidence fields are verified and egress is filed) or BLOCKED (any NOT VERIFIED or NOT FILED — do not mark the integration done).

Output the table and nothing else. Any row with verdict BLOCKED means the integration is not done.

**No evidence, no done.**

INTEGRATION: *(describe your integration: what service or agent, what runtime segment it runs from, and every new outbound host:port it calls)*
````
