❄️ SnowPro Core — Top 10 Gotchas

1. COPY INTO vs. Snowpipe

COPY INTO = efficient bulk load (batch).

Snowpipe = continuous loading (near real-time).
⚠️ They’ll phrase it as “efficient” → answer = COPY INTO.

2. Time Travel vs. Fail-safe

Time Travel (Enterprise default = 1 day, up to 90 days) → user-managed recovery.

Fail-safe (always 7 days) → Snowflake-managed, you must contact support.
⚠️ Users cannot query Fail-safe directly.

3. Result Caching

Stored 24 hours.

Tied to same user + same role + same warehouse.

Invalidated if underlying data changes.
⚠️ Not shared across all users.

4. Zero-Copy Cloning

Clones are writable, not read-only.

Storage cost only for changes (new micro-partitions).
⚠️ Exam will try to trick you by saying “doubles storage immediately.”

5. Warehouses

Do not store data.

Can be resized while running, with no downtime.

Auto-suspend saves cost, auto-resume wakes them.

Multi-cluster = only needed for concurrency, not query speed.
⚠️ Bigger warehouse = more parallelism, not less cost.

6. Storage Billing

Snowflake automatically compresses storage.

Billed per compressed TB per month, or by actual bytes if < 1 TB.
⚠️ Don’t confuse uncompressed size with billed size.

7. Data Sharing

Secure Data Sharing = no copy, live read-only access.

Consumers can CTAS or clone to persist a local copy.

Works cross-region and cross-cloud.
⚠️ Not limited to same cloud or region.

8. Semi-structured Data

Stored in VARIANT (can hold JSON, Avro, Parquet, ORC).

For performance → extract fields into relational columns or use materialized views.
⚠️ Clustering on nested fields usually doesn’t help.

9. Roles & Security

SYSADMIN → create databases, schemas, tables.

SECURITYADMIN → manage users, roles, grants.

ACCOUNTADMIN → full access, but not for daily work.
⚠️ Never grant privileges directly to users. Always through roles.

10. Architecture

Compute = stateless virtual warehouses.

Storage = centralized, micro-partitioned, compressed, immutable.

Cloud Services = metadata, security, optimizer, authentication.
⚠️ Key phrase: “independent compute & storage layers, connected by cloud services.”
