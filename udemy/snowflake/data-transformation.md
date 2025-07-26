# Supported Function Types

## Scalar Functions

These are data generation functions like `Date()` or  `UUID_STRING()` that return one value.

## Aggregate Functions

operate on values across rows to perform mathematical calculations like `SUM()` or `MAX()`

## Window Functions

a subset of aggregate functions allowing us to aggregate one on a subset of rows this is done using the `over` syntax with the aggregate. 

```sql
select account_id, max(amount) over (partition by account_id) from account
```

will give us the max for each account id

## Table Functions

return a set of rows for each input row. The returned set can contain zero, one, or mor rows. Each row can contain one or more columns.

```sql
select randstr(5, RANDOM()), RANDOM() FROM TABLE(GENERATOR(ROWCOUNT => 3)):
```

The above query creates a table of 3 rows whereas the first col is random string of 5 chars and the second column is random data

<img width="1828" height="415" alt="image" src="https://github.com/user-attachments/assets/e38b087f-47b5-42b0-a48c-360d93d83e6e" />

## System Functions

This is a built in function that uses the $ syntax

```sql
select system$pipe_status('my_pipe`);
```

```sql
select system$explain_plan_json('SELECT * FROM FILMS_DB.FILMS_SCHEMA.FILMS')
```

<img width="1864" height="438" alt="image" src="https://github.com/user-attachments/assets/575e5925-95e1-4646-b463-5f0759e76afc" />

# Estimation Functions

These are a special type of aggregate function

## Cardinality Estimation

Estimate the number of distinct values.

Though count(distinct) can get an exact value, Snowflake has implemented an algorithm called **HyperLogLog** which returns an approximation but is a lot more memory efficient. The margin of error of using this approximation is 1.6%.

```sql
SELECT APPROX_COUNT_DISTINCT(L_ORDERKEY) FROM LINEITEM
```

When comparing this to 

```sql
SELECT COUNT(DISTINCT L_ORDERKEY) FROM LINEITEM
```

The Accuracy goes does slightly but the time to execute this on a 16gb table is also reduced by 4x.

## Similarity Estimation

Estimate similarity of two or more sets

Jacard Similarity Coefficient is usually how similarities have historically been calculated but this is computationally expensive. Snowflake has implemented a two step process using `minhas` and `approximate_similarity` that avoids computing intersections and unions.

First, Snowflake generates MinHash signatures for each record to create compact representations

```sql
-- Create MinHash signatures for customer records
SELECT 
    customer_id,
    MINHASH(100, name, address, phone) as signature
FROM customers;
```

This creates a 100-element MinHash signature for each customer based on their name, address, and phone fields. The MinHash function converts the text data into a fixed-size numeric signature that preserves similarity relationships.

Then, Snowflake uses these signatures to estimate similarity between records:

```sql
-- Find similar customer records using MinHash signatures
WITH customer_signatures AS (
    SELECT 
        customer_id,
        MINHASH(100, name, address, phone) as signature
    FROM customers
),
similarity_pairs AS (
    SELECT 
        a.customer_id as customer_a,
        b.customer_id as customer_b,
        APPROXIMATE_SIMILARITY(a.signature, b.signature) as similarity_score
    FROM customer_signatures a
    JOIN customer_signatures b ON a.customer_id < b.customer_id
)
SELECT *
FROM similarity_pairs
WHERE similarity_score > 0.8;
```

The APPROXIMATE_SIMILARITY function compares the MinHash signatures to estimate Jaccard similarity between the original records. A score of 0.8 means approximately 80% similarity.
This two-step approach allows Snowflake to efficiently process large datasets for similarity matching without having to perform expensive pairwise comparisons of the original text data. The MinHash signatures are much smaller and faster to compare while maintaining good approximation accuracy.

## Frequency Estimation

Estimate frequency in a set

```sql
-- Approximate frequency estimation
SELECT 
    product_category,
    APPROX_COUNT_DISTINCT(customer_id) as approx_unique_customers,
    COUNT(*) as total_transactions
FROM sales_transactions
WHERE transaction_date >= '2024-01-01'
GROUP BY product_category
ORDER BY total_transactions DESC;
```

Traditional GROUP BY:

Accuracy: 100% exact results
Performance: Slower on large datasets, requires full data scan and sorting
Memory: High memory usage for large cardinality groups
Scalability: Can become prohibitively expensive on billions of rows

Frequency Estimation:

Accuracy: ~2-3% error rate (configurable)
Performance: Much faster, especially on large datasets
Memory: Fixed, small memory footprint regardless of data size
Scalability: Scales to massive datasets efficiently

Example Results Comparison:
Traditional GROUP BY:
Electronics    | 1,234,567 | 45,231
Clothing       | 987,654   | 38,492
Home & Garden  | 654,321   | 29,103

Frequency Estimation:
Electronics    | 1,234,567 | 45,187  (~0.1% difference)
Clothing       | 987,654   | 38,531  (~0.1% difference)  
Home & Garden  | 654,321   | 29,156  (~0.2% difference)
The frequency estimation provides nearly identical results with significantly better performance on large datasets, making it ideal for real-time analytics and exploratory data analysis where approximate results are acceptable.

## Percentile Estimation

Estimate percentile of values in a set

Snowflake have implemented the t-Digest algorithm as an efficient way of estimating

```sql
-- Calculate approximate percentiles for order values
SELECT 
    product_category,
    APPROX_PERCENTILE(order_amount, 0.25) as approx_25th_percentile,
    APPROX_PERCENTILE(order_amount, 0.50) as approx_median,
    APPROX_PERCENTILE(order_amount, 0.75) as approx_75th_percentile,
    APPROX_PERCENTILE(order_amount, 0.90) as approx_90th_percentile,
    APPROX_PERCENTILE(order_amount, 0.95) as approx_95th_percentile,
    COUNT(*) as total_orders
FROM sales_transactions
WHERE transaction_date >= '2024-01-01'
GROUP BY product_category;
```
Key Benefits of APPROX_PERCENTILE:
Performance:

Much faster on large datasets (millions/billions of rows)
Uses fixed memory regardless of data size
Can process streaming data efficiently

Accuracy:

Typically within 1-2% of exact values
Uses t-digest algorithm for high accuracy
Better accuracy at extreme percentiles (p95, p99) compared to some other approximation methods

Scalability:

Maintains consistent performance as data grows
Ideal for real-time dashboards and monitoring
Can handle high-cardinality grouping without performance degradation

The approximate percentile is particularly valuable for SLA monitoring, performance analysis, and any scenario where you need quick insights into data distribution without waiting for exact calculations.

# Table Sampling

Sampling is used to get a random subset of data. This is useful for statistical applications whereas Limit can be used to give the top or bottom results.

```sql
-- Sample exactly 1000 rows from the table
SELECT *
FROM sales_transactions SAMPLE ROW (1000 ROWS);

-- Sample 1000 rows from each partition/group
SELECT *
FROM sales_transactions SAMPLE ROW (1000 ROWS)
WHERE product_category = 'Electronics';
```

## Unstructured File Functions

The BUILD_SCOPED_FILE_URL function generates a scoped Snowflake-hosted URL to a staged file using the stage name and relative file path as inputs.

```sql
-- Generate scoped URL for a specific file
SELECT BUILD_SCOPED_FILE_URL(@my_stage, 'reports/sales_report.pdf');
```

The BUILD_SCOPED_FILE_URL function is particularly useful for secure, temporary file sharing, API integrations, and creating controlled access to staged files without granting direct stage privileges to users.

Keep in mind that this url is only available for the length of the query cache results.

The BUILD_STAGE_FILE_URL function generates a Snowflake file URL to a staged file that is permanent using the stage name and relative file path as inputs.

```sql
-- Generate file URL for a specific document
SELECT BUILD_STAGE_FILE_URL(@my_stage, 'reports/quarterly_report.pdf');
```

The GET_PRESIGNED_URL function generates a pre-signed URL to a file on a stage using the stage name and relative file path as inputs, with configurable expiration time.

```sql
-- Generate pre-signed URL that expires in 1 hour (3600 seconds)
SELECT GET_PRESIGNED_URL(@my_stage, 'reports/sales_report.pdf', 3600);
```

You would primarily use GET_PRESIGNED_URL when you want to set an expiration time

# Directory Tables

Directory tables are special metadata tables that automatically track files stored in internal or external stages. They provide a SQL-queryable interface to examine file metadata without having to list stage contents manually. They're an optional feature of stages that you must explicity enable

```sql
-- Create internal stage with directory table enabled
CREATE STAGE my_internal_stage
  ENCRYPTION = (TYPE = 'SNOWFLAKE_SSE')
  DIRECTORY = (ENABLE = TRUE);
```

You can also add a directory table to an existing stage

```sql
-- Add directory table to existing stage
ALTER STAGE existing_stage 
SET DIRECTORY = (ENABLE = TRUE);

-- Remove directory table from stage
ALTER STAGE existing_stage 
SET DIRECTORY = (ENABLE = FALSE);
```

Enable Directory Tables When:

You need to query file metadata with SQL
You want to join file information with other tables
You're building automated file processing pipelines
You need to monitor file changes over time
You want to use streams on file metadata

Skip Directory Tables When:

You're just using the stage for simple data loading
You don't need to query file metadata
You want to minimize storage costs (directory tables use some storage)
You're working with temporary or short-lived files

Directory table need to be refreshed and consume credits to do this. You can enable this automatically

```sql
-- External stage with auto-refresh enabled
CREATE STAGE my_auto_stage
  URL = 's3://my-bucket/data/'
  CREDENTIALS = (AWS_KEY_ID = 'key' AWS_SECRET_KEY = 'secret')
  DIRECTORY = (
    ENABLE = TRUE
    AUTO_REFRESH = TRUE
    NOTIFICATION_INTEGRATION = 'my_s3_notification_integration'
  );
```

# File Support REST API

This allows us to download from a stage using `/api/files`

You can download from URLs you create with BBUILD_SCOPED_URL and BUILD_STAGE_FILE_URL but not GET_PRESIGNED_URL

