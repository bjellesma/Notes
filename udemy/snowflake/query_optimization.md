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
