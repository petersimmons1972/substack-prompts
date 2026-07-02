Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text

Inventory one named shared host's temporary infrastructure. For each resource class — Docker volumes, Docker images, build artifacts, temp directories, log directories, cache directories — output a table with these exact columns: class | total_bytes | bytes_older_30d | pct_older_30d | bytes_no_ttl | top_offender_path | top_offender_bytes. Then add two lines: "Age timestamp source: <which timestamp was used>" and "TTL annotation source: <where TTL was looked for>". Output only the table and the two lines.

FIXTURE:
Host: build-shared-01
Docker volumes: 42 volumes total, 180GB. 31 volumes have no labels; 11 have ttl labels. Of the 11, 8 are >30 days old. Of the 31 without TTL, 29 are >30 days old. Largest volume: vol-ab12 at 24GB. Estimated reclaimable from unlabeled + expired: 38GB.
Docker images: 23 images, 60GB. 19 older than 30 days. 20 lack a retention label. Largest: pytorch-test:2025-11 at 18GB.
Build artifacts (/var/builds): 12GB total. All older than 30 days. No TTL policy defined. Largest subdir: /var/builds/run-4481 at 2.1GB.
Temp directories (/tmp/agent-*): 8GB. Owned by agent sessions, no expiry. All created >7 days ago. Largest: /tmp/agent-run-2203 at 1.4GB.
Logs (/var/log/agents): 15GB. Rotated by date. No size cap. Oldest: 90 days. Largest segment: 2025-09-15.log.gz at 3.2GB.
Cache (/home/agent/.cache): 6GB. Mix of pip/npm/docker layer cache. No TTL. Largest: pip/torch at 2.8GB.
````
