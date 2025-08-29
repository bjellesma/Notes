Snowflake uses a hybrid architecture of shared disk and shared nothing. Shared disk because all compute nodes can access the same centralized storage layer. Shared nothing because each virtual warehouse operates independently with its own compute resources.

## Snowpipe

The key benefit of using snowpipe is that it has automatic scaling.

Snowpipe has built-in duplicate detection to prevent loading the same file multiple times:

How it works:

Snowpipe tracks file metadata (name, size, timestamp, checksum)
If the exact same file is uploaded again, Snowpipe skips it
Only loads files that are new or modified

Snowpipe doesn't support transformations during loading
Snowpipe is designed for simple, fast ingestion of data "as-is"
Transformations with Snowpipe happen after loading (ELT pattern)

## Data Loading

Which file format option would you use to handle CSV files that contain commas within quoted fields?
A) FIELD_OPTIONALLY_ENCLOSED_BY = '"'
B) ESCAPE_UNENCLOSED_FIELD = '\'
C) FIELD_DELIMITER = ','
D) SKIP_HEADER = 1

A) FIELD_OPTIONALLY_ENCLOSED_BY = '"' ✅ Correct answer

Tells Snowflake that fields may be enclosed in quotes
Handles commas inside quoted fields properly
Snowflake won't treat commas inside quotes as delimiters

B) ESCAPE_UNENCLOSED_FIELD = '\'

Used when fields have escape characters like John\,Doe
For backslash-escaped delimiters, not quoted fields

C) FIELD_DELIMITER = ','

Just sets the delimiter (default is already comma)
Doesn't solve the "comma inside fields" problem

D) SKIP_HEADER = 1

Skips first row if it contains column names
Unrelated to comma handling

## Data Sharing

Cross-cloud sharing is supported! Consumer can be on different cloud platforms (AWS consumer can access Azure provider's data). Consumer pays for:

✅ Compute credits when querying shared data
❌ NO storage costs for shared data
❌ NO data transfer costs in most cases

Data remains in provider's region, consumer pays cross-region data transfer costs

Consumers CAN create their own views on shared data:
```sql
-- Consumer can create views on shared data
CREATE VIEW my_analysis AS 
SELECT region, SUM(sales) 
FROM shared_database.shared_table 
GROUP BY region;
```

## Data Masking

Only one masking policy can be applied to a column at a time. But masking policies are applied before row acess policies. This is because masking policies are more security focused so that even if the row policies have an edge case, the data is still securly masked.

## Secure Views

Secure views are about definition privacy, not row-level security.

Hide business logic - competitors can't see your algorithms
Protect data sources - users don't know which tables are queried
Security through obscurity - harder to reverse-engineer data model

## Time Travel

Historical data versions are maintained in storage
Longer retention = more historical versions = higher storage costs
Proportional relationship - 90 days costs more than 7 days

## Flatten object

There is no flatten_json attribute when using file_format but you must use the flatter() function

## Role Changes

A user's role doesn't change until they begin a new session. For this you would want to use `ALTER USER john SET DISABLED = TRUE;` to disable their account immediately.

