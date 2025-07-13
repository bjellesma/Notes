A virtual warehouse is a named abstraction for a massively parallet processing compute cluster and are required for DQL operations (Select), DML operations (update), and Data Loading operations (copy into)

Virtual Warehouse configuration can be changed on the fly

Virtual Warehouses contain local SSD storage used to store raw data retrieved from the storage layer

suspend warehouse - `alter warehouse my_wh suspend`. This will suspend the warehouse after current queries are finished executing

you can auto suspend a warehouse - `create warehouse my_med_wh auto_suspend=300;`. This is useful for controlling costs as it says that a warehouse can shut down after so many second.

By default, a warehouse will auto resume. We can control this by manually setting auto resume `create warehouse MY_MED_WH AUTO_RESUME=FALSE`. This may be useful if we want to not have a warehouse auto turn on.

## Billing

| Warehouse Size | Credits per Hour | Credits per Second |
|----------------|------------------|-------------------|
| **X-Small**    | 1                | 0.000278          |
| **Small**      | 2                | 0.000556          |
| **Medium**     | 4                | 0.001111          |
| **Large**      | 8                | 0.002222          |
| **X-Large**    | 16               | 0.004444          |
| **2X-Large**   | 32               | 0.008889          |
| **3X-Large**   | 64               | 0.017778          |
| **4X-Large**   | 128              | 0.035556          |
| **5X-Large**   | 256              | 0.071111          |
| **6X-Large**   | 512              | 0.142222          |

The cost of the credits will be different based on the region

| Snowflake Edition | US Regions (AWS/Azure/GCP) | Non-US Regions | Notes |
|-------------------|---------------------------|----------------|-------|
| **Standard**      | ~$2.00 - $2.50           | ~$2.50 - $3.00 | Entry-level features |
| **Enterprise**    | ~$3.00 - $3.50           | ~$3.50 - $4.00 | Multi-cluster warehouses, advanced features |
| **Business Critical** | ~$4.00 - $4.50        | ~$4.50 - $5.00 | Enhanced security, compliance features |
| **Virtual Private Snowflake** | Contact Snowflake | Contact Snowflake | Dedicated infrastructure |

If a XS Virtual Warehouse is active for 1 hour on the Standard Edition of Snowflake deployed in AWS Europe region, it will consum 1 snowflake credit and cost ~$2.50 - $3.00

### Key Billing Notes

- **Minimum charge:** 60 seconds (even if you use it for 10 seconds, you're charged for 1 minute)
- **After 60 seconds:** Billing is per-second
- **Pattern:** Each size up doubles the credit consumption and compute power

### Examples

- Start X-Small warehouse for 30 seconds → Charged 1 credit (60-second minimum)
- Start X-Small warehouse for 90 seconds → Charged for 90 seconds = 0.025 credits

## resource monitors

these are objects that can be set up to track the credit consumption on a warehouse.

when limits are reached, an action can be triggered such as notify user or suspend warehouse.

```sql
-- Weekly Resource Monitor for Development Environment
CREATE RESOURCE MONITOR dev_weekly_monitor
WITH
  CREDIT_QUOTA = 100
  FREQUENCY = WEEKLY
  START_TIMESTAMP = IMMEDIATELY
TRIGGERS
  ON 75 PERCENT DO NOTIFY
  ON 80 PERCENT DO SUSPEND
  ON 100 PERCENT DO SUSPEND_IMMEDIATE;
```

In the above query, the frequency is the time when the quota will be reset. Suspend will suspend after the currently running queries are finished whereas suspend immediately will not wait for that. Notify will notify all account admins with notifications enabled.

We'd then set the warehouse with

```sql
ALTER WAREHOUSE "COMPUTE_WH" SET RESOURCE_MONITOR = "dev_weekly_monitor";
```

On the UI, you can use the usage tab to track credit consumption or the following query 

```sql
-- Total credits used grouped by warehouse
SELECT WAREHOUSE_NAME,
       SUM(CREDITS_USED) AS TOTAL_CREDITS_USED
FROM WAREHOUSE_METERING_HISTORY
WHERE START_TIME >= DATE_TRUNC(MONTH, CURRENT_DATE)
GROUP BY 1
ORDER BY 2 DESC;
```

### Multi cluster warehouses

We can scale a virtual warehouse by scaling up or scaling out. scaling up refers to bumping up the size of the warehouse whereas scaling out refers to add more clusters to the warehouse so that it can handle more. So if you have a long individual query, it'd be better to increase the size of the warehouse. If you have many concurrent sessions, it'd be better to increase the number of clusters.

A virtual warehouse can only be scaled up manually where it can be scaled out by setting an auto scaling property.

Resizing a running warehouse does not impact running queries. the additional compute resources are used for queued and new queries.

### Query Acceleration Service

Query Acceleration Service is a serverless feature in Snowflake that automatically accelerates eligible queries by adding additional compute resources when beneficial. It works independently of your virtual warehouse size.

#### How QAS Works

Automatic detection - Snowflake automatically identifies queries that could benefit from acceleration
Serverless compute - Adds extra processing power without resizing your warehouse
Transparent operation - No query changes required - works automatically
Per-query basis - Each query is evaluated individually for acceleration eligibility

QAS works best for:

Large table scans
Simple aggregations (SUM, COUNT, AVG, MIN, MAX)
Basic filtering and GROUP BY operations
Straightforward analytical workloads

QAS doesn't help with:

Complex window functions
Recursive queries
UDFs and stored procedures
Advanced string/text processing
Machine learning functions
Highly complex analytical operations

```sql
-- Enable QAS on a warehouse (Enterprise edition and above)
ALTER WAREHOUSE my_warehouse SET QUERY_ACCELERATION_MAX_SCALE_FACTOR = 8;

-- Disable QAS
ALTER WAREHOUSE my_warehouse SET QUERY_ACCELERATION_MAX_SCALE_FACTOR = 0;
```

You can check if a query would benefit from query acceleration before activating it

```sql
-- Check if a query can benefit from QAS before running it
SELECT SYSTEM$ESTIMATE_QUERY_ACCELERATION('
    SELECT region, COUNT(*), SUM(sales_amount)
    FROM large_sales_table 
    WHERE order_date >= ''2023-01-01''
    GROUP BY region
');

-- Example JSON response:
{
  "estimatedQueryAcceleration": {
    "eligible": true,
    "estimatedSpeedupFactor": 2.5,
    "estimatedAdditionalCredits": 1.2,
    "upperLimitScaleFactor": 8
  }
}
```
