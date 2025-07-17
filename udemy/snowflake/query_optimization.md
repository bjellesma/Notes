## Query Performance Analysis Tools

In the snowsight UI, you can use the query history tab to get detailed information about the steps that were performed in the query. In the following query, you can see that 99.3% of the time was spent just scanning the table so we can infer that using a limit really doesn't have any effect. We scanned 150,000,000 records on the table

```sql
SELECT C_CUSTKEY, C_NAME, C_ADDRESS, C_ACCTBAL FROM CUSTOMER 
ORDER BY C_ACCTBAL DESC
LIMIT 10000;
```

<img width="2454" height="833" alt="image" src="https://github.com/user-attachments/assets/9a6a6efa-3196-4a6f-8322-f592a59c55d2" />

Equivalently, the account admin can use the following query to see the last 365 days worth of queries

```sql
USE ROLE ACCOUNTADMIN;

-- Set context 
USE DATABASE SNOWFLAKE;
USE SCHEMA ACCOUNT_USAGE;

SELECT * FROM QUERY_HISTORY WHERE WAREHOUSE_SIZE IS NOT NULL LIMIT 100;
```

## Database order of operations

SQL queries are processed in a specific logical order, which is different from the order you write the clauses. Understanding this order is crucial for query optimization and debugging.

### 1. FROM and JOINs
- **Purpose:** Identifies source tables and combines them
- **What happens:** Cartesian products, inner/outer joins are applied
- **Result:** Creates the initial working dataset

```sql
FROM table1
JOIN table2 ON table1.id = table2.id
LEFT JOIN table3 ON table1.category = table3.category
```

### 2. WHERE
- **Purpose:** Filters rows from the result of FROM/JOINs
- **What happens:** Row-level filtering based on conditions
- **Result:** Reduces the dataset to qualifying rows only

```sql
WHERE table1.status = 'ACTIVE'
  AND table1.created_date >= '2024-01-01'
  AND table2.amount > 1000
```

### 3. GROUP BY
- **Purpose:** Groups rows that share common values
- **What happens:** Creates groups for aggregation
- **Result:** Transforms detail rows into summary groups

```sql
GROUP BY table1.category, table1.region
```

### 4. HAVING
- **Purpose:** Filters groups created by GROUP BY
- **What happens:** Group-level filtering (after aggregation)
- **Result:** Only groups meeting the criteria remain

```sql
HAVING COUNT(*) > 10
  AND SUM(table2.amount) > 50000
```

### 5. SELECT
- **Purpose:** Specifies which columns to return
- **What happens:** Column selection and expression evaluation
- **Result:** Defines the output structure

```sql
SELECT table1.category,
       table1.region,
       COUNT(*) as record_count,
       SUM(table2.amount) as total_amount,
       AVG(table2.amount) as avg_amount
```

### 6. DISTINCT
- **Purpose:** Removes duplicate rows from SELECT results
- **What happens:** Deduplication of the result set
- **Result:** Only unique combinations remain

```sql
SELECT DISTINCT category, region
FROM sales_data
```

### 7. ORDER BY
- **Purpose:** Sorts the final result set
- **What happens:** Arranges rows in specified order
- **Result:** Ordered output for presentation

```sql
ORDER BY total_amount DESC, category ASC
```

### 8. LIMIT/TOP
- **Purpose:** Restricts the number of rows returned
- **What happens:** Takes only the first N rows after ordering
- **Result:** Subset of the ordered result set

```sql
LIMIT 100
-- or in SQL Server/Snowflake
TOP 100
```

### Complete Example with Execution Order

```sql
-- This query demonstrates the logical processing order
SELECT 
    category,
    region,
    COUNT(*) as order_count,
    SUM(amount) as total_sales,
    AVG(amount) as avg_order_value
FROM sales_orders so                          -- 1. FROM
JOIN customers c ON so.customer_id = c.id     -- 1. JOIN
WHERE so.order_date >= '2024-01-01'           -- 2. WHERE
  AND c.status = 'ACTIVE'
GROUP BY category, region                     -- 3. GROUP BY
HAVING COUNT(*) > 50                          -- 4. HAVING
ORDER BY total_sales DESC                     -- 7. ORDER BY
LIMIT 20;                                     -- 8. LIMIT
```

**Logical execution steps:**
1. **FROM/JOIN:** Combine sales_orders and customers tables
2. **WHERE:** Filter to 2024 orders from active customers
3. **GROUP BY:** Group by category and region
4. **HAVING:** Keep only groups with >50 orders
5. **SELECT:** Calculate count, sum, and average for each group
6. **ORDER BY:** Sort by total_sales descending
7. **LIMIT:** Return only top 20 results

### Performance Optimization
- **Filter early:** WHERE conditions reduce data before expensive operations
- **Efficient JOINs:** Join conditions and indexes matter for FROM/JOIN performance
- **GROUP BY optimization:** Proper indexing on GROUP BY columns improves performance
- **HAVING vs WHERE:** Use WHERE when possible (filters before grouping)

### Common Mistakes
- **Using column aliases in WHERE:** Aliases aren't available until SELECT is processed
  ```sql
  -- ❌ This fails
  SELECT amount * 0.1 as tax,
         amount + tax as total  -- ERROR: tax not yet available
  FROM orders
  WHERE total > 1000;           -- ERROR: total not yet available
  
  -- ✅ This works
  SELECT amount * 0.1 as tax,
         amount + (amount * 0.1) as total
  FROM orders
  WHERE (amount + (amount * 0.1)) > 1000;
  ```

- **Referencing non-grouped columns:** All SELECT columns must be in GROUP BY or be aggregate functions
  ```sql
  -- ❌ This fails
  SELECT customer_id, order_date, COUNT(*)
  FROM orders
  GROUP BY customer_id;  -- order_date must be in GROUP BY or aggregated
  
  -- ✅ This works
  SELECT customer_id, MAX(order_date), COUNT(*)
  FROM orders
  GROUP BY customer_id;
  ```


if you see "Spilling to Disk" in snowsight, this indicates that the volume of data spilled to virtual warehouse local disk. You should combat this by ensuring that you're doing a where clause to filter results.

Spilling to Disk indicates that query operations exceeded available warehouse memory and had to use slower disk storage. While WHERE clauses can reduce spilling by filtering data early, you should also consider increasing warehouse size, optimizing JOINs, reducing GROUP BY cardinality, and improving query structure.

**Cardinality** is an indication of how unique a value is. Customer ID is an example of a value with a very high cardinality as it is unique whereas gender is an example of low cardinality because it's expected that there'll be a very high repition of results. Why this matters is because when you're doing a group by, you want to use high cardinality because that'll create less groups and therefore use less memory. On the other hand when doing an operation like indexing or clustering, it's a good idea to use something with low cardinality as there's less chance of data skew.

## Cache

### Services Layer

**Metadata Cache** - information about the data and not the data inself is stored in the metadata to speed up query planning. An example would be the table structure.

```sql
-- When you run this query
SELECT * FROM customers WHERE customer_id = 12345;

-- Snowflake uses metadata cache to:
-- ✅ Know which micro-partitions contain customer_id = 12345
-- ✅ Skip irrelevant micro-partitions (partition pruning)
-- ✅ Optimize query execution plan
```

It'll take into account partition pruning to find the relevant partitions

```sql
-- Query: Find orders from January 2024
SELECT * FROM orders WHERE order_date >= '2024-01-01' AND order_date < '2024-02-01';

-- Metadata cache contains min/max dates for each micro-partition:
-- Partition 1: min_date='2023-12-15', max_date='2023-12-31' → SKIP
-- Partition 2: min_date='2024-01-01', max_date='2024-01-15' → SCAN  
-- Partition 3: min_date='2024-01-16', max_date='2024-01-31' → SCAN
-- Partition 4: min_date='2024-02-01', max_date='2024-02-15' → SKIP
```

Another example would be a query like below which relies only on the metadata cache since this is the table structure.

```sql
-- first suspend our warehouse
ALTER WAREHOUSE COMPUTE_WH SUSPEND;
ALTER WAREHOUSE SET AUTO_RESUME=FALSE;

--the following query returns instantly and doesnt need to wake up our warehouse
SELECT COUNT(*) FROM CUSTOMER;
```

We can also see in the query profile that this is a metadata based result

<img width="279" height="96" alt="image" src="https://github.com/user-attachments/assets/6efdea60-9cc9-49ab-9cb3-1646d8d74853" />

However, if we try to use the following query to select actual data, it will fail

```sql
-- this will fail because this query will require us to have actual data and need a warehouse
SELECT * FROM CUSTOMER;
```

<img width="1169" height="215" alt="image" src="https://github.com/user-attachments/assets/2c423ef5-a43f-4668-a99c-d41cc12fd482" />

**results cache** - this caches results for up to 31 days so that if a query is run with the exact same syntax, same role, and the underlying table data has not changed, the results can be instantly used

Another note is that if you use a sql function that must be evaluated at runtime like `CURRENT_TIMESTAMP()`, this'll never get cached

If results cache is used, you'll see something like the following in the query profile

<img width="288" height="120" alt="image" src="https://github.com/user-attachments/assets/f22561c8-0b5e-4add-81d5-5e39a67dfd78" />

If you want to force the cache to bust, you can also set the following as account admin

```sql
USE ROLE ACCOUNTADMIN;

ALTER ACCOUNT SET USE_CACHED_RESULT = FALSE;
```

### Warehouse Layer

Similar query results are stored on a warehouse's SSD so that similar query can access the same data without having to go back to the slower blob storage

```sql
-- First time running this query
SELECT customer_id, SUM(order_amount)
FROM large_orders_table
WHERE order_date >= '2024-01-01'
GROUP BY customer_id;

-- Data gets pulled from cloud storage (S3/Blob/GCS) 
-- AND cached locally on warehouse SSDs
```

```sql
-- Running similar query later (same warehouse)
SELECT customer_id, COUNT(*)
FROM large_orders_table  
WHERE order_date >= '2024-01-01'
GROUP BY customer_id;

-- Data served from local SSD cache = MUCH faster!
```

If results are being cached on the local disk, you'll see in the query profile that remote storage is not accessed at all anymore

## Materialed View

This is an enterpise feature.

Unlike a regular view which runs the query each time someone accesses it, a materialized view stores the query results and can refresh either manually or automatically when underlying data changes. Materialized views can be suspended (to stop refreshes and save costs) and resumed (to allow refreshes again) similar to virtual warehouses.

```sql
-- Auto-refresh (when base tables change)
CREATE MATERIALIZED VIEW sales_summary 
AUTO_REFRESH = TRUE  -- Refreshes when underlying data changes
AS SELECT region, SUM(amount) FROM sales GROUP BY region;

-- Manual refresh
ALTER MATERIALIZED VIEW sales_summary REFRESH;

-- Check refresh status
SHOW MATERIALIZED VIEWS;
```

Materialized views cannot use the following:

❌ Window functions (ROW_NUMBER, RANK, LAG, LEAD, etc.)
❌ HAVING clauses
❌ LIMIT/TOP clauses
❌ ORDER BY clauses
❌ Subqueries in SELECT clause
❌ UNION/INTERSECT/EXCEPT
❌ User-defined functions (UDFs)
❌ Non-deterministic functions (CURRENT_TIMESTAMP, RANDOM, etc.)

## Clustering

**Overlap Depth** is a metric used to measure how many partitions will need to be scanned to find a value based on how you've setup the micro partitioning. For example, if the metadata says that we have to search at most 3 partitions out of a possible 5 to find a value, the overlap depth is 3.

<img width="372" height="209" alt="image" src="https://github.com/user-attachments/assets/c24d8df2-2bbf-4058-b4c6-7738af630693" />

Clustering should be reserved for large tables (>10gb) because many micro partitions will be used and proper clustering can improve performance 80-90%.


Clustering should generally be used for columns with high cardinality where you would frequently filter.

```sql
-- For queries filtering by multiple columns
ALTER TABLE sales CLUSTER BY (region, order_date);

-- Optimizes these queries:
SELECT * FROM sales WHERE region = 'US' AND order_date >= '2024-01-01';
SELECT * FROM sales WHERE region = 'EU' AND order_date = '2024-01-15';
```

The following query can show clustering information

```sql
USE ROLE SYSADMIN;
USE DATABASE SNOWFLAKE_SAMPLE_DATA;
USE SCHEMA TPCDS_SF100TCL;
SELECT SYSTEM$CLUSTERING_INFORMATION('CATALOG_SALES', '(CS_LIST_PRICE)');
```

This'll give you a json like 

```json
{
  "cluster_by_keys" : "LINEAR(CS_LIST_PRICE)",
  "total_partition_count" : 587268,
  "total_constant_partition_count" : 0,
  "average_overlaps" : 587267.0,
  "average_depth" : 587268.0,
  "partition_depth_histogram" : {
    "00000" : 0,
    "00001" : 0,
    "00002" : 0,
    "00003" : 0,
    "00004" : 0,
    "00005" : 0,
    "00006" : 0,
    "00007" : 0,
    "00008" : 0,
    "00009" : 0,
    "00010" : 0,
    "00011" : 0,
    "00012" : 0,
    "00013" : 0,
    "00014" : 0,
    "00015" : 0,
    "00016" : 0,
    "1048576" : 587268
  },
  "clustering_errors" : [ ]
}
```

The above is a badly clustered key

Here's a well partitioned table

```sql
SELECT SYSTEM$CLUSTERING_INFORMATION('CATALOG_SALES');
```

```json
{
  "cluster_by_keys" : "LINEAR(  cs_sold_date_sk, cs_item_sk  )",
  "total_partition_count" : 587268,
  "total_constant_partition_count" : 11,
  "average_overlaps" : 3.5188,
  "average_depth" : 2.7695,
  "partition_depth_histogram" : {
    "00000" : 0,
    "00001" : 8,
    "00002" : 135337,
    "00003" : 451923,
    "00004" : 0,
    "00005" : 0,
    "00006" : 0,
    "00007" : 0,
    "00008" : 0,
    "00009" : 0,
    "00010" : 0,
    "00011" : 0,
    "00012" : 0,
    "00013" : 0,
    "00014" : 0,
    "00015" : 0,
    "00016" : 0
  },
  "clustering_errors" : [ ]
}
```

As you can see, the values are more spread out. 

When doing a tablescan operation for a well partitioned table, you'll see that the partitions scanned is very low

<img width="303" height="268" alt="image" src="https://github.com/user-attachments/assets/c28fab0c-3681-4a30-a3a4-5a685a59a2d9" />

This type of clustering does require an up front compute cost. The following query can be used to monitor costs.

```sql
-- Set context
USE ROLE ACCOUNTADMIN;
USE DATABASE SNOWFLAKE;
USE SCHEMA ACCOUNT_USAGE;

-- Monitoring Automatic Clustering serverless feature costs 
SELECT 
  START_TIME, 
  END_TIME, 
  CREDITS_USED, 
  NUM_BYTES_RECLUSTERED,
  TABLE_NAME, 
  SCHEMA_NAME,
  DATABASE_NAME
FROM AUTOMATIC_CLUSTERING_HISTORY;
```

## Search Optimization Service (SOS)

These are useful for low cardinality searches but cost 2x the serverless compute cost.

```sql
-- These queries get much faster with SOS
SELECT * FROM customers WHERE customer_id = 12345;
SELECT * FROM orders WHERE order_number = 'ORD-2024-001';
SELECT * FROM products WHERE sku = 'LAPTOP-DELL-XPS13';
```

Perfect use cases:

✅ Large tables (millions+ rows) with point lookups
✅ Customer service searching by email, phone, ID
✅ Log analysis searching for error messages
✅ Product catalogs searching by SKU, name, description
✅ User lookup systems finding specific users quickly
✅ JSON/semi-structured data searches

Poor use cases:

❌ Small tables (< 1M rows) - overhead not worth it
❌ Range queries (WHERE date BETWEEN) - clustering is better
❌ Aggregation queries (SUM, COUNT, GROUP BY)
❌ Full table scans for analytics

Clustering = organizing your library by subject, SOS = having a computerized card catalog to find any specific book instantly.
