`infer_schema` is a command used to get the schema of a snowflake object.

Table Stages aren't appropriate to load data into multiple tables.

UDFs can be created using python, java, sql, and javascripts.

Snowflake uses a hierachical key model which is rooted in a hardware key.

Tri-secret secure makes use of a composite key made up of a customer managed key and a Snowflake managed key.

Materialized views can be created on top of external tables to improve their query performance.

A Virtual warehouse is a named abstraction for one or more compute nodes.

Snowflake can store the following semi structured data formats:
* json
* orc
* avro
* parquet
* xml

The maximum DATA_RETENTION_TIME_IN_DAYS  is 0 or 1 for temporary and transient tables regardless of the edition of Snowflake.

To create a share object, you need to specify object privileges and the account identifier

Clustering improves performance of queries that frequently filter or sort on the clustered keys so it optimizes where and join statements.

A snowflake user stage is referenced with @~ while a snowflake table stage is referenced with @%

custom roles are recommended to be assigned to sysadmin. This is recommended for administrative capacity over the objects that you own 

account usage views typically have a retention period of 1 year.

Table data is partitioned and stored in the order it was loaded. This means that if we don't specify a clustering key, Snowflake will just use the natural ordering.

An external function makes use of an API integration object to store secure information.

The default value for DATA_RETENTION_TIME_IN_DAYS is 1 for all editions of Snowflake.

User authentication is handled by the services layer in the multi cluster shared data architecture.

The two scaling policies that can be defined when creating a multi cluster warehouse are standard and economy.

To retrieve metadata on clustering, you would use system$clustering_information

The recommended compressed file size when loading data into snowflake is 100-250mb.

To reuse the results cache, the query must match exactly and the role executing the query must have the necessary access privileges for all the tables used in the cached query. This means that the user can be different and just the role has to be the same.

If periodic rekeying is enabled, then when the retired encryption key for a table is older than one year, Snowflake automatically creates a new encryption key and re-encrypts all data previously protected by the retired key using the new key. The new key is used to decrypt the table data going forward.

When CONTINUE is used with ON_ERROR when using COPY INTO <table>, the file is loaded anyway if errors are found (Snowflake attempts partial loading) and not skipped
