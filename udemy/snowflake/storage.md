# Micro Partitions

When you load data into snowflake, snowflake automatically divides the rows into different micro partitions that are stored as blobs on the cloud storage being used. Snowflake will globally track metadata in the services layer on the micro partitions such as the min and max value for each column stored in each partition. This allows snowflake to take advantage of **micro partition pruning** where snowflake will be able to ignore reading micro partitions that wont be required in the query plan.

These micro partitions are 50-100mb blobs of uncompressed data

<img width="1400" height="788" alt="image" src="https://github.com/user-attachments/assets/4fc6d1cd-262d-41b8-8ac0-db01d4f2c17d" />

## Time Travel

We can use undrop 

```sql
UNDROP TABLE DEMO_TABLE_TT;
```

We can also use this offset function to get the data as it was 5 minutes ago

```sql
SELECT * FROM DEMO_TABLE_TT
AT(OFFSET => -60*5);
```

You can also use the before keyword along with a query id to get table data as it was before a certain query. Note that the before keyword will not include the query itself so if the query was an insert, you would get the results of the query before the insert

```sql
SELECT * FROM DEMO_TABLE_TT
BEFORE(STATEMENT => '<insert_statement_id>');
```

This also enables us to use cloning to create a new table as it was in the past

```sql
-- Create clone from point in past with Time Travel 
CREATE OR REPLACE TABLE DEMO_TABLE_CLONE_TIME_TRAVEL CLONE DEMO_TABLE
AT(OFFSET => -60*2);
```

The default time rention on snowflake objects is 1 day but you can configure with

```sql
alter database my_db
set data_retention_time_in_days=90
```

On standard edition, you can only set retention to 1 but with enterprise and higher, you can set retention up to 90

Beyond time travel there is **fail safe** a non configurable period of 7 days in which historical data can be recovered by contaction support.

<img width="804" height="357" alt="image" src="https://github.com/user-attachments/assets/067ce51b-7d92-42a7-9cd9-d00a83adfce5" />


# Cloning

In addition to cloning tables, you can also clone databases and schemas which may contain views despite the fact that you can't clone a view.

```sql
CREATE TABLE DEMO_TABLE_CLONE CLONE DEMO_TABLE;
```

You can clone

* databases
* schemas
* tables
* streams
* stages
* file formats
* sequences
* tasks
* pipes (reference external stages only)

Cloning is a metadata only operation, copying the properties, structure, and configuration of its source.
Therefore,
Cloning does not contribute to storage costs until data is modified or new data is added to the clone.

This is because adding new data to a clone will create new micro partitions.

It's important to note that a cloned object does not retain the privileges of the source without the use of `copy grants`

```sql
-- Clone database and copy all access privileges
CREATE DATABASE sales_dev 
CLONE sales_prod 
COPY GRANTS;
```

# Replication

Replication is a feature in Snowflake which enables replicating databases between Snowflake accounts within an organization. Replication differs from cloning in the data is physically moved.

```sql
alter database db_1
enable replication to accounts org1.account2;
```

The use case for replication is more for disaster recovery.

# Billing

Data storage cost is calculated monthly based on the average number of on disk bytes for all data stored each day in a snowflake account.

# Secure Data Sharing

Secure Data Sharing allows an account to provide read-only access to selected database objects to other snowflake accounts without transferring data. A **data provider** is the person that shares the data whereas the **data consumer** is the one that reads the data. A data consumer would be able to read the data but not modify or add any new records.

Sharing is enabled with an account level **share** object. Is is created by a data provider. An account can share the following database objects:

* Tables
* External tables
* secure views
* secure materialized views
* secure UDFs

Sharing is available on all editions of Snowflake except for VPS editions

Here are the commands that a data provider would use to create a share

```sql
-- Create a new share as data provider
CREATE SHARE customer_analytics_share
COMMENT = 'Customer analytics data for business partners';

-- Grant usage on database to the share
GRANT USAGE ON DATABASE customer_analytics TO SHARE customer_analytics_share;

-- Grant usage on schema to the share
GRANT USAGE ON SCHEMA customer_analytics.public TO SHARE customer_analytics_share;

-- Add consumer accounts to the share
ALTER SHARE customer_analytics_share 
ADD ACCOUNTS = ('CONSUMER_ACCOUNT_1', 'CONSUMER_ACCOUNT_2');
```

And the following are the commands that the consumer would use

```sql
-- Check all shares you've created as provider
SHOW SHARES;

-- View what's shared in a specific share
DESCRIBE SHARE customer_analytics_share;

-- Check which accounts have access
SHOW GRANTS TO SHARE customer_analytics_share;

-- Monitor share usage (if available in your account)
SELECT * FROM TABLE(INFORMATION_SCHEMA.SHARE_USAGE_HISTORY())
WHERE share_name = 'customer_analytics_share';
```

As you can see, the consumer can now use the share like regular data. To create a database from a share however a user must have a role with the IMPORT SHARE privilege

Only that object is shared at that point in time. Future objects will need to be explicitly shared.

Only one database can be added per share.

Access to a share can be revoked at any time if the object is dropped on the provider's end.

A share can only be granted to accounts in the same region and cloud provider as the data provider account. If you want to share with a different region or provider, you will need to use replication.

If you want to share data with a non-snowflake user, the provider can setup a **reader account**. This means that any costs that the reader uses will be incurred on the provider account.

```sql
-- Create a reader account
CREATE MANAGED ACCOUNT SNOWFLAKE_TUTORIAL_READER_ACCOUNT 
admin_name='admin', 
admin_password='Passw0rd11111111111111111111111111111111111111', 
type=reader;
```

# Data Marketplace

On the snowsight ui, snowflake uses the sharing technology to enable the public sharing of data. You can search for anything on the marketplace to bring up a wizrd to allow you to import

<img width="642" height="856" alt="image" src="https://github.com/user-attachments/assets/f2e418d6-f92a-40b9-9f43-f9715bac5338" />

Once ready, the UI will give us sample commands that we can use

```sql
// Show me all flights to Paris from the USA 
select *
from public.OAG_schedule
where DEPCTRY='US'
and ARRCITY='PAR'

;

// Show all American Airlines Flights 
select *
from public.OAG_schedule
where CARRIER='AA';

// What is the capacity of flights arriving into Melbourne? 
SELECT SUM(TOTAL_SEATS) FROM public.OAG_schedule
WHERE ARRAPT='MEL'
AND OPERATING!='N'
AND STOPS =0;

```

There are also some marketplace items where you'll need to request the data as the provider will attempt to personalize the data. This could come at a cost

<img width="483" height="712" alt="image" src="https://github.com/user-attachments/assets/d6524157-4651-4894-b12b-eb50108082bf" />

You can setup a private marketplace called a **data exchange**. This could be useful if you want other departments within your company to be able to request data but now have it be public.
