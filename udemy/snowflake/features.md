Features make up to 30% of the exam

Snowflake is a data platform rather than just a data warehouse because of the following factor

Handles ALL data types and workloads
Multiple processing engines
Extensive ecosystem integrations
End-to-end data lifecycle management

snowflake has been built from the get go with the cloud in mind which is why we can refer to it as **cloud native**

all snowflake infra can run on cloud in aws, gcp, or azure. This is determined and chosen per account.

snowflake is described as a Software as a service (SaaS) because there is no management of hardware and it works on a subscription model.

## Shared Data Architecture

In Snowflake, there are two types of shared architectures. 

A **shared disk architecture** is a single database setup that multiple computers share.

* Simpler to setup and acts as a single source of truth.
* This does create a single point of failure and has limited scalability.

A **shared nothing architecture** means that all nodes have their own dedicated storage that no other node can directly access.

* Easier to scale by adding nodes
* Avoids single point of failure

![image](https://github.com/user-attachments/assets/bb01077c-abda-4c66-94d9-db3e8756485b)

The disadvantage of this architecture is that storage and compute are tightly coupled meaning reducing one will reduce the other.

The full multi cluster architecture

![image](https://github.com/user-attachments/assets/0c73ec28-d32d-4ad2-955c-ad0bdbda5edd)

### Storage Layer

Snowflake utilized aws s3 for it's storage layer. This allows snowflake focus on query optimization and compute

Data is loaded or inserted into micro partitions which allows snowflake to ignore partitions not needed when querying.

Snowflake stores the data in their proprietary format (a form of columnar) which allows it to ignore columns not needed in a query.

Data is not directly accessible in the underlying blob storage. Only via sql commands.

### Query Processing Layer

A compute cluster is called a **virtual warehouse**

Nodes of a virtual warehouse operate in the shared nothing architecture

Virtual Warehouses have sizes which relate to the number of nodes provisioned.

### Services Layer

a collection of highly available and scalable services that coordinate activies such as auth, infra, transaction, metadata, security, and query optimization across all snowflake accounts

## Snowflake Editions

Standard Edition:

The entry-level option with core data warehousing functionality
Includes basic security features, SQL support, and standard connectors
Time Travel up to 1 day
No advanced security features like customer-managed keys
Good for basic analytics and reporting needs

Enterprise Edition:

Builds on Standard with additional features for larger organizations
Multi-cluster warehouses for handling concurrent workloads
Time Travel extended to 90 days
Column-level security and row-level security
Database replication for disaster recovery
Annual upfront payment discounts available

Business Critical Edition:

Designed for organizations with strict security and compliance requirements
Enhanced security features including customer-managed encryption keys (CMK)
AWS/Azure PrivateLink support for private connectivity
Database failover/failback capabilities
Support for compliance standards like HIPAA, PCI DSS, SOC 2 Type II
Higher level of data protection and isolation

Virtual Private Snowflake (VPS):

The highest level of isolation and security
Completely separate Snowflake environment with dedicated virtual servers
No sharing of compute resources with other Snowflake accounts
Ultimate level of security for highly regulated industries
Significant cost premium due to dedicated infrastructure

## Snowflake Object Model

The **organization** object in snowflake is the highest level that groups accounts and is not available by default by only available when asking for access from snowflake.

Each account is hosted on a single cloud platform like aws, gcp, or azure. Each account is provisioned in a single geographic region and can't be moved easily due to regulatory restrictions.

Eact account is created as a single snowflake edition.

## Table Types

A **permanent table** is the default table type and exists until dropped. It has a time travel window of 90 days.

A **temporary table** exists for the duration of a session and might be used for holding query results. The time travel period is 1 day.

A **transient table** exists until explicity dropped. These differ from permanent tables because transient is cheaper due to a shorter time travel period of 1 day on transient and no fail safe storage. 

* An **external table** is read only and can be used to read data outside of snowflake. This is useful if we have the data stored externally which allows us to avoid costs of storing on snowflake.
  * With an external table, you'll also need to manually refresh to reflect the latest changes
 
```sql
-- Refresh external table metadata so it reflects latest changes in external cloud storage
ALTER EXTERNAL TABLE EXT_TABLE REFRESH;
```  

## View Types

A **standard view** is the default view and just stores the query so that no snowflake storage charges are incurred

A **materiaized view** is like a standard view but stores the results of a query and periodically refreshes incurring a serverless features cost.

A **secure view** can be made of a standard and materialized view and the query definitions are visible to only authorized users. Unauthorized users will be unable to use 

```sql
SELECT get_ddl('view', 'SECURE_VIEW');
```

## User Defined Function (UDF)

A User defined function can return a scalar (single number) or tabular data. Between the dollar signs, you can write code in python, java, js, or sql. The handler param is the name of the function being called here in python. The handler is only needed if there's more than one function but it's good practice to have.

```sql
-- Create a Python UDF to validate email addresses
CREATE OR REPLACE FUNCTION validate_email(email STRING)
RETURNS BOOLEAN
LANGUAGE PYTHON
RUNTIME_VERSION = '3.8'
HANDLER = 'validate_email_handler'
AS
$$
import re

def validate_email_handler(email):
    if not email:
        return False
    
    # Basic email regex pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
$$;
```

Use the SQL UDF as part of a query. 

```sql
-- Use the SQL UDF as part of a query. 
SELECT DAY_NAME_ON(100);
```

You can also call an aws lambda function from snowflake by using an external function. this applies to azure and gcp also. There is a proxy service that will call this and then return it back to snowflake

```py
CREATE OR REPLACE API INTEGRATION sentiment_api_integration
  API_PROVIDER = aws_api_gateway
  API_AWS_ROLE_ARN = 'arn:aws:iam::123456789012:role/snowflake-api-role'
  ENABLED = true
  API_ALLOWED_PREFIXES = ('https://abc123.execute-api.us-west-2.amazonaws.com/prod/');
```

## Stored Procedures

these are similar to UDFs but differ in a few ways. Notice here that we're using python to call the snowflake api. Note that the stored procedure has the execute as

```sql
CREATE OR REPLACE PROCEDURE run_daily_etl()
RETURNS STRING
LANGUAGE PYTHON
RUNTIME_VERSION = '3.8'
PACKAGES = ('snowflake-snowpark-python')
HANDLER = 'run_etl_pipeline'
EXECUTE AS OWNER
AS
$$
def run_etl_pipeline(session):
    try:
        # Step 1: Clean staging data
        session.sql("""
            DELETE FROM staging_orders 
            WHERE order_date < DATEADD(day, -30, CURRENT_DATE())
        """).collect()
        
        # Step 2: Transform and load new data
        session.sql("""
            INSERT INTO fact_orders 
            SELECT 
                order_id,
                customer_id,
                order_date,
                total_amount,
                CURRENT_TIMESTAMP() as processed_date
            FROM staging_orders 
            WHERE processed_date IS NULL
        """).collect()
        
        # Step 3: Update staging table
        session.sql("""
            UPDATE staging_orders 
            SET processed_date = CURRENT_TIMESTAMP()
            WHERE processed_date IS NULL
        """).collect()
        
        # Step 4: Log success
        session.sql("""
            INSERT INTO etl_log (process_name, status, run_date)
            VALUES ('daily_etl', 'SUCCESS', CURRENT_TIMESTAMP())
        """).collect()
        
        return "ETL pipeline completed successfully"
        
    except Exception as e:
        # Log the error
        session.sql(f"""
            INSERT INTO etl_log (process_name, status, error_message, run_date)
            VALUES ('daily_etl', 'FAILED', '{str(e)}', CURRENT_TIMESTAMP())
        """).collect()
        
        return f"ETL pipeline failed: {str(e)}"
$$;
```

You'll want to use the call keyword to call a stored procedure

```sql
CALL data_quality_check('ORDERS');
```

## UDF vs Stored Procedure Comparison

| Aspect | User Defined Functions (UDFs) | Stored Procedures |
|--------|-------------------------------|-------------------|
| **Primary Purpose** | Return calculated values or result sets | Execute multi-step business logic and operations |
| **Return Type** | Single value (scalar) or table | Various types (STRING, VARIANT, ARRAY, etc.) |
| **SQL Statement Usage** | Can only execute SELECT statements | Can execute any SQL statements (INSERT, UPDATE, DELETE, DDL) |
| **Transaction Control** | Cannot control transactions | Can manage transactions (COMMIT, ROLLBACK) |
| **Usage in Queries** | Can be used in SELECT, WHERE, GROUP BY clauses | Must be called independently with CALL statement |
| **Side Effects** | Cannot modify data or database objects | Can modify data, create objects, perform administrative tasks |
| **Performance** | Generally faster for simple calculations | Higher overhead due to session management |
| **Supported Languages** | SQL, JavaScript, Python, Java, Scala | SQL, JavaScript, Python, Java, Scala |
| **Package Support** | Limited to function scope | Full access to external packages and libraries |
| **Error Handling** | Basic error handling | Comprehensive try-catch error handling |
| **Session Access** | No direct session access | Full session object access in Python |
| **Snowpark Integration** | Limited Snowpark capabilities | Full Snowpark DataFrame and SQL execution |
| **Parameterization** | Input parameters only | Input/output parameters and return values |
| **Complexity** | Best for simple, focused calculations | Ideal for complex, multi-step workflows |

### Similarities

- **Multi-language support**: Both support SQL, JavaScript, Python, Java, and Scala
- **Reusability**: Both can be saved and reused across multiple queries and sessions
- **Security**: Both inherit the caller's privileges and security context
- **Version control**: Both can be versioned and managed through database schema
- **Runtime versions**: Both support multiple runtime versions for supported languages
- **External packages**: Both can utilize external libraries (Python, Java, etc.)
- **Documentation**: Both support inline comments and documentation
- **Performance optimization**: Both are compiled and optimized by Snowflake

### Key Decision Factors

**Choose UDFs when:**
- Need to perform calculations within SQL queries
- Want to reuse complex logic in SELECT statements
- Require simple data transformations or validations
- Need to return single values or result sets for queries

**Choose Stored Procedures when:**
- Need to execute multiple SQL statements in sequence
- Require data modification operations (INSERT, UPDATE, DELETE)
- Want to implement complex business workflows
- Need comprehensive error handling and transaction control
- Require logging, auditing, or administrative tasks

## Sequences

Though snowflake doesn't enforce primary keys and can't guarentee uniqueness, there's still the concept of sequences that we can use

```sql
-- Create a sequence
CREATE SEQUENCE customer_id_seq START = 1 INCREMENT = 1;

-- Use it to generate unique customer IDs
INSERT INTO customers (customer_id, name, email)
VALUES (customer_id_seq.NEXTVAL, 'John Doe', 'john@email.com');
```

## Tasks

A task is an object used to schedule the execution of a sql statement. In the following example, we use a task to run a stored procedure every monday at 6am. Notice that we need to specify a warehouse

```sql
-- Create a task that runs data quality checks
CREATE OR REPLACE TASK weekly_data_quality_check
  WAREHOUSE = 'ANALYTICS_WH'
  SCHEDULE = 'USING CRON 0 6 * * 1 UTC'  -- Every Monday at 6 AM
AS
  CALL data_quality_monitoring_procedure('SALES_DB', 'PUBLIC');
```

We can also suspend and resume a task

```sql
-- Suspend a task
ALTER TASK daily_staging_cleanup SUSPEND;

-- Resume a task
ALTER TASK daily_staging_cleanup RESUME;
```

Please note the following

Tasks are created in SUSPENDED state by default
You need EXECUTE TASK privilege to create tasks
Tasks can be chained together with dependencies
Task execution history is available for monitoring and troubleshooting

## Streams

A stream is an object created to view and track dml changes to a source table

A stream captures and tracks change data (not just metadata) from DML operations on a table, showing what specific data changed along with metadata about those changes. Imagine having a notebook to track all changes that occur to an object.

Also keep in mind that when you read from a stream, you start to consume it. This means that the stream appears empty when you view it again.

![image](https://github.com/user-attachments/assets/cb6fc3d7-b1c3-4d77-9e60-c76db3a7c036)

```sql
-- 1. Create a table
CREATE TABLE customers (
    id INTEGER,
    name STRING,
    email STRING
);

-- 2. Create a stream to watch the table
CREATE STREAM customer_stream ON TABLE customers;

-- 3. Add some data
INSERT INTO customers VALUES 
(1, 'John', 'john@email.com'),
(2, 'Jane', 'jane@email.com');

-- 4. Make changes
UPDATE customers SET email = 'john.doe@email.com' WHERE id = 1;
DELETE FROM customers WHERE id = 2;
INSERT INTO customers VALUES (3, 'Bob', 'bob@email.com');

-- 5. Check what the stream captured
SELECT 
    id, 
    name, 
    email,
    METADATA$ACTION,
    METADATA$ISUPDATE
FROM customer_stream;

-- 6. Process the changes (this consumes the stream)
INSERT INTO customer_audit 
SELECT id, name, METADATA$ACTION, CURRENT_TIMESTAMP()
FROM customer_stream;

-- 7. Stream is now empty until new changes happen
SELECT * FROM customer_stream; -- Returns nothing
```

## Billing

You can pay on demand for what you use or you can pay upfront. 

Virtual Warehouses are charged on a credit hour basis depending on the warehouse size. If you used a small warehouse for 2.5 hours, you'd be charged 2.5 credits. Keep in mind also that snowflake has a minimum of 60 seconds. So if you were to spin up and use a virtual warehouse for 35 seconds, you'd still be charged for 1 minute. However, every second after is charged per second.

Cloud services are billed at 4.4 credits per hour. These are queries that do not require a warehouse compute resource to run. For example, when you create a table, you don't actually need to spin up a warehouse. However, cloud services are usually included as free until it exceed 10% of your daily compute consumption. Because of this, most customers don't actually pay for cloud services because they stay under this threshold.

Each serverless feature typically consists of both compute services and cloud servers so they have their own credit rate per compute hour.

Data storage is calculated monthly based on the average number of on disk bytes per day for tables and stages. This differs from virtual warehouses as you're not using credits but are instead charged a dollar value. These values are charged based on a flat dollar value rate per terabye bases on the cloud provider and region.

Data transfer will also use a dollar value and applies when transferring data from one location or cloud provider to another.

## Snowsql

This is the command line version of snowflake that we can use. This can be useful for running a file through a script. Alternatively, the UI is refered to as Snowsight.

## Drivers

Snowflake has wide integrations with BI tools like powerBI to data security and governance tools like datadog to ML tools like data robot to data modeling tools like sqldbm.

## Snowflake Scripting

Snowflake provides a way to introduce scripting logic by using snowflake scripting.

Snowflake scripting is used as an alternative to using something like snowpark which is more python integrated

```sql
-- Snowflake Scripting for bulk data processing
DECLARE
    table_list ARRAY := ['customers', 'orders', 'products'];
    current_table STRING;
    row_count INTEGER;
    total_processed INTEGER := 0;
    result_summary STRING := '';
BEGIN
    -- Loop through each table
    FOR i IN 0 TO ARRAY_SIZE(table_list) - 1 DO
        current_table := table_list[i];
        
        BEGIN
            -- Dynamic SQL to get row count
            EXECUTE IMMEDIATE 'SELECT COUNT(*) FROM ' || current_table 
            INTO row_count;
            
            -- Archive old data (example: older than 1 year)
            EXECUTE IMMEDIATE 
                'DELETE FROM ' || current_table || 
                ' WHERE created_date < DATEADD(year, -1, CURRENT_DATE())';
            
            total_processed := total_processed + row_count;
            result_summary := result_summary || current_table || ': ' || row_count || ' rows; ';
            
        EXCEPTION
            WHEN OTHER THEN
                -- Log the error and continue with next table
                INSERT INTO error_log (error_date, table_name, error_message)
                VALUES (CURRENT_TIMESTAMP(), current_table, SQLERRM);
                
                result_summary := result_summary || current_table || ': ERROR; ';
        END;
    END FOR;
    
    -- Final summary
    INSERT INTO processing_log (process_date, tables_processed, total_rows, summary)
    VALUES (CURRENT_TIMESTAMP(), ARRAY_SIZE(table_list), total_processed, result_summary);
    
    RETURN 'Processed ' || total_processed || ' total rows across ' || ARRAY_SIZE(table_list) || ' tables';
END;
```

## Snowpark

Snowpark is an api for snowflake built on top of higher level languages like java, scala, and python. Snowpark dataframes are lazily evaluated allowing them to be sped up. 

Lazy evaluation means that Snowpark DataFrames don't actually execute operations immediately when you write the code - instead, they build up a query plan and only execute when you explicitly request results.

