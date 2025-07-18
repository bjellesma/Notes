Data loading and unloading comprises 10-15% of the exam.

## Loading Data

* Insert - the easiest way to load data is to just use the insert statement with or without overwriting lik so

```sql
-- Insert multiple rows via VALUES syntax
INSERT INTO FILMS VALUES 
('9x3wnr0zit', 'Citizen Kane', DATE('1942-01-24')),
('2wyaojnzfq', 'Old Boy', DATE('2004-10-15')), 
('0s0smukk2p', 'Ratatouille', DATE('2007-06-29'));

INSERT OVERWRITE INTO FILMS_2000 SELECT * FROM FILMS;
```

* Snowsight Load Table - This is an option is the snowflake UI

<img width="780" height="742" alt="image" src="https://github.com/user-attachments/assets/2a0b968c-d0c0-4743-93b3-3dbff1dc6920" />

## Stages

### User Stage

```sql
-- Each user has a personal stage
-- Format: @~
PUT file://my_file.csv @~;  -- Upload to your user stage
LIST @~;                     -- See your personal files
```

### Table Stage

Snowflake has a stage setup for every table

```sql
-- Every table automatically has an internal stage
-- Format: @%table_name
PUT file://my_data.csv @%customers;  -- Upload to customers table stage
LIST @%customers;                     -- See files in table stage
```

### Named Internal Stage

```sql
-- Create a reusable internal stage
CREATE STAGE my_internal_stage;

-- Upload files
PUT file://sales_data.csv @my_internal_stage;

-- Load from stage
COPY INTO sales FROM @my_internal_stage/sales_data.csv;
```

### Named External Stage

A named external stage can be used to point to other cloud storage like S3, Azure, or Google

```sql
CREATE STAGE my_s3_stage
  URL = 's3://my-bucket/data-files/'
  CREDENTIALS = (AWS_KEY_ID = 'your-key' AWS_SECRET_KEY = 'your-secret');

-- Or with IAM role (better security)
CREATE STAGE my_s3_stage_secure
  URL = 's3://my-bucket/data-files/'
  STORAGE_INTEGRATION = my_s3_integration;
```

Notice for the above that we need to specify credentials for the storage integration. A storage integration is a reusable and securable snowflake object which can be applied across stages and is recommended to avoid have to explicity set sensitive information for each stage definition.

```sql
-- Storage integrations for secure access
CREATE STORAGE INTEGRATION s3_integration
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = S3
  ENABLED = TRUE
  STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::123456789012:role/snowflake-role'
  STORAGE_ALLOWED_LOCATIONS = ('s3://my-bucket/data/');
```

In addition to use the list command above, you can also use select just like with a table

```sql
-- create file format
CREATE FILE FORMAT CSV_FILE_FORMAT
  TYPE=CSV
  SKIP_HEADER=1;

-- Check file metadata
SELECT metadata$filename, metadata$file_row_number, *
FROM @my_stage/data.csv
(FILE_FORMAT => CSV_FILE_FORMAT);
```

The put command will also be different in linux vs windows. Not that the PUT command must be executed on the command line and can't be used in snowsight.

```bash
-- From Documents folder (Mac)
PUT file:///Users/john/Documents/data/monthly_sales.csv @sales_stage;

-- Upload single file from Windows
PUT file://C:\Users\username\data\customers.csv @my_stage;
```

Snowflake will keep track of the files uploaded on stages and will skip duplicates.

# Bulk Loading with copy into

COPY INTO is Snowflake's primary command for loading data from files into tables. It reads data from staged files (internal or external stages) and inserts it into Snowflake tables with built-in error handling, validation, and transformation capabilities.

## Basic Syntax

```sql
COPY INTO <table_name>
FROM <stage_location>
[FILES = ('file1.csv', 'file2.csv')]
[PATTERN = 'regex_pattern']
[FILE_FORMAT = (TYPE = 'CSV' | <named_file_format>)]
[VALIDATION_MODE = RETURN_ERRORS | RETURN_ALL_ERRORS | RETURN_<n>_ROWS]
[ON_ERROR = CONTINUE | SKIP_FILE | ABORT_STATEMENT]
[SIZE_LIMIT = <num>]
[PURGE = TRUE | FALSE]
[FORCE = TRUE | FALSE];
```

## File Format Types Explained

If the file_format option is not specified, snowflake will attempt to import as string.

### TYPE Parameter
The TYPE parameter tells Snowflake how to parse your data files:

**CSV (Comma-Separated Values):**
- Most common format for structured data
- Text files with delimited columns
- Supports custom delimiters, headers, null values

**JSON (JavaScript Object Notation):**
- Semi-structured data format
- Key-value pairs, nested objects, arrays
- Flexible schema, good for varying data structures

**PARQUET:**
- Columnar binary format
- Highly compressed and optimized for analytics
- Preserves data types and schema information

**AVRO:**
- Binary format with embedded schema
- Good for streaming data and schema evolution
- Compact and fast to process

**ORC (Optimized Row Columnar):**
- Columnar format optimized for Hive workloads
- Good compression and predicate pushdown

**XML:**
- Markup language for structured documents
- Hierarchical data representation
- Less common for bulk data loading

### Example File Format Specifications
```sql
-- CSV with custom settings
FILE_FORMAT = (
  TYPE = 'CSV' 
  FIELD_DELIMITER = '|'          -- Use pipe instead of comma
  RECORD_DELIMITER = '\n'        -- Line ending character
  SKIP_HEADER = 1                -- Skip first row (headers)
  NULL_IF = ('NULL', '', 'N/A')  -- Treat these as NULL values
  ESCAPE_UNENCLOSED_FIELD = NONE -- How to handle special chars
)

-- JSON with parsing options
FILE_FORMAT = (
  TYPE = 'JSON'
  STRIP_OUTER_ARRAY = TRUE       -- Remove outer array brackets
  STRIP_NULL_VALUES = FALSE      -- Keep null values in JSON
)

-- Parquet (minimal options needed)
FILE_FORMAT = (TYPE = 'PARQUET')  -- Parquet is self-describing
```

## Validation Mode Explained

Validation mode lets you **test and preview** data before actually loading it into your table. Think of it as a "dry run" that shows you what would happen.

### VALIDATION_MODE Options

**RETURN_ERRORS:**
- Shows you any parsing errors without loading data
- Useful for checking if your file format is correct
- Returns error messages for problematic rows

**RETURN_ALL_ERRORS:**
- Shows ALL errors in the file, not just the first few
- Good for comprehensive data quality assessment
- Can be slow on large files with many errors

**RETURN_<n>_ROWS (e.g., RETURN_10_ROWS):**
- Returns the first N rows as they would be loaded
- Perfect for previewing data structure and transformations
- Lets you verify column mapping before full load

### Validation Examples
```sql
-- Check for any data parsing errors
COPY INTO customers
FROM @my_stage/customers.csv
FILE_FORMAT = my_csv_format
VALIDATION_MODE = 'RETURN_ERRORS';
-- Result: Shows any rows that can't be parsed

-- Preview first 5 rows to verify data looks correct
COPY INTO customers  
FROM @my_stage/customers.csv
FILE_FORMAT = my_csv_format
VALIDATION_MODE = 'RETURN_5_ROWS';
-- Result: Shows exactly how first 5 rows will appear in table

-- Get comprehensive error report
COPY INTO customers
FROM @my_stage/customers.csv  
FILE_FORMAT = my_csv_format
VALIDATION_MODE = 'RETURN_ALL_ERRORS';
-- Result: Shows every single error in the file
```

## Simple Examples

### Basic COPY with CSV
```sql
-- Load from internal stage
COPY INTO customers
FROM @my_stage/customers.csv
FILE_FORMAT = (TYPE = 'CSV' SKIP_HEADER = 1);

-- Load from external stage (S3)
COPY INTO orders
FROM @s3_stage/orders.csv
FILE_FORMAT = (TYPE = 'CSV' FIELD_DELIMITER = ',' SKIP_HEADER = 1);
```

### Using Named File Format
```sql
-- Create reusable file format
CREATE FILE FORMAT my_csv_format
  TYPE = 'CSV'
  FIELD_DELIMITER = ','
  RECORD_DELIMITER = '\n'
  SKIP_HEADER = 1
  NULL_IF = ('NULL', 'null', '');

-- Use named file format
COPY INTO products
FROM @my_stage/products.csv
FILE_FORMAT = my_csv_format;
```

## Loading Multiple Files

### Pattern Matching
```sql
-- Load all CSV files matching pattern
COPY INTO sales
FROM @my_stage
PATTERN = '.*sales_2024.*\.csv'
FILE_FORMAT = my_csv_format;

-- Load files with specific date pattern
COPY INTO daily_logs
FROM @log_stage
PATTERN = '.*log_2024_01_[0-9]{2}\.txt'
FILE_FORMAT = (TYPE = 'CSV');
```

### Specific File List
```sql
-- Load specific files only
COPY INTO transactions
FROM @my_stage
FILES = ('jan_transactions.csv', 'feb_transactions.csv', 'mar_transactions.csv')
FILE_FORMAT = my_csv_format;
```

## Advanced File Formats

### JSON Data
```sql
-- Load JSON files
COPY INTO user_events
FROM @json_stage/events.json
FILE_FORMAT = (TYPE = 'JSON');

-- Load JSON with specific parsing
COPY INTO user_profiles
FROM @json_stage/profiles.json
FILE_FORMAT = (TYPE = 'JSON' STRIP_OUTER_ARRAY = TRUE);
```

### Parquet Files
```sql
-- Load Parquet files
COPY INTO analytics_data
FROM @parquet_stage/data.parquet
FILE_FORMAT = (TYPE = 'PARQUET');
```

### Compressed Files
```sql
-- Load GZIP compressed CSV
COPY INTO large_dataset
FROM @my_stage/data.csv.gz
FILE_FORMAT = (TYPE = 'CSV' COMPRESSION = 'GZIP' SKIP_HEADER = 1);

-- Auto-detect compression
COPY INTO customers
FROM @my_stage/customers.csv.gz
FILE_FORMAT = (TYPE = 'CSV' COMPRESSION = 'AUTO' SKIP_HEADER = 1);
```

## Error Handling Explained

Error handling determines what happens when COPY INTO encounters problematic data (missing columns, wrong data types, parsing errors, etc.).

### ON_ERROR Options

**CONTINUE (default):**
- Skips bad rows and continues loading good rows
- Most common choice for production loads
- Bad rows are logged but don't stop the process

**SKIP_FILE:**
- If ANY error occurs in a file, skip the entire file
- Good for files that must be completely clean
- Ensures all-or-nothing loading per file

**ABORT_STATEMENT:**
- Stops the entire COPY operation on first error
- Good for critical data that must be perfect
- Most conservative approach

### Error Handling Examples
```sql
-- Production approach: load good data, skip bad rows
COPY INTO orders
FROM @my_stage/orders.csv
FILE_FORMAT = my_csv_format
ON_ERROR = 'CONTINUE';
-- Result: Loads 9,800 good rows, skips 200 bad rows

-- Quality-first approach: file must be perfect or skip entirely  
COPY INTO financial_data
FROM @my_stage/transactions.csv
FILE_FORMAT = my_csv_format
ON_ERROR = 'SKIP_FILE';
-- Result: Either loads entire file or none of it

-- Mission-critical approach: any error stops everything
COPY INTO regulatory_data
FROM @my_stage/compliance.csv
FILE_FORMAT = my_csv_format
ON_ERROR = 'ABORT_STATEMENT';
-- Result: First bad row stops the entire operation
```

## Other Key Parameters Explained

### SIZE_LIMIT
- Limits how much data to load (in bytes)
- Useful for testing with large files
- Stops loading after reaching the byte limit

```sql
-- Load only first 1MB for testing
COPY INTO test_table
FROM @my_stage/huge_file.csv
FILE_FORMAT = my_csv_format
SIZE_LIMIT = 1048576;  -- 1MB in bytes
```

### PURGE
- Controls whether files are deleted from stage after successful load
- TRUE = delete files after loading (saves storage costs)
- FALSE = keep files in stage (default, safer for troubleshooting)

```sql
-- Delete files after successful load (save storage costs)
COPY INTO daily_logs
FROM @log_stage/today.csv
FILE_FORMAT = my_csv_format
PURGE = TRUE;
```

### FORCE
- Controls whether to reload files that were already processed
- TRUE = reload even if file was previously loaded
- FALSE = skip files that were already loaded (default, prevents duplicates)

```sql
-- Force reload of file (even if loaded before)
COPY INTO customers
FROM @my_stage/customers.csv
FILE_FORMAT = my_csv_format
FORCE = TRUE;  -- Will create duplicates if run multiple times
```

## Error Handling

### Error Handling Options
```sql
-- Continue loading despite errors (default)
COPY INTO orders
FROM @my_stage/orders.csv
FILE_FORMAT = my_csv_format
ON_ERROR = 'CONTINUE';

-- Skip entire file if any errors
COPY INTO clean_data
FROM @my_stage/data.csv
FILE_FORMAT = my_csv_format
ON_ERROR = 'SKIP_FILE';

-- Abort entire operation on first error
COPY INTO critical_data
FROM @my_stage/critical.csv
FILE_FORMAT = my_csv_format
ON_ERROR = 'ABORT_STATEMENT';
```

### Validation and Testing
```sql
-- Validate data without loading (return first 10 errors)
COPY INTO customers
FROM @my_stage/customers.csv
FILE_FORMAT = my_csv_format
VALIDATION_MODE = 'RETURN_10_ROWS';

-- See all errors without loading
COPY INTO orders
FROM @my_stage/orders.csv
FILE_FORMAT = my_csv_format
VALIDATION_MODE = 'RETURN_ALL_ERRORS';

-- Return sample rows for preview
COPY INTO products
FROM @my_stage/products.csv
FILE_FORMAT = my_csv_format
VALIDATION_MODE = 'RETURN_5_ROWS';
```

## Performance Options

### Size Limits
```sql
-- Limit data loaded (useful for testing)
COPY INTO test_table
FROM @my_stage/large_file.csv
FILE_FORMAT = my_csv_format
SIZE_LIMIT = 1000000;  -- Load max 1MB
```

### Force Reload
```sql
-- Force reload of previously loaded files
COPY INTO customers
FROM @my_stage/customers.csv
FILE_FORMAT = my_csv_format
FORCE = TRUE;  -- Reload even if file was already processed
```

### Purge Files After Load
```sql
-- Delete files from stage after successful load
COPY INTO orders
FROM @my_stage/orders.csv
FILE_FORMAT = my_csv_format
PURGE = TRUE;  -- Remove file from stage after loading
```

## Column Mapping and Transformation

### Basic Column Mapping
```sql
-- Map file columns to table columns
COPY INTO customers (customer_id, first_name, last_name, email)
FROM (
  SELECT $1, $2, $3, $4
  FROM @my_stage/customers.csv
)
FILE_FORMAT = (TYPE = 'CSV' SKIP_HEADER = 1);
```

### Data Transformation During Load
```sql
-- Transform data while loading
COPY INTO customers
FROM (
  SELECT 
    $1::INTEGER as customer_id,
    UPPER($2) as first_name,
    UPPER($3) as last_name,
    LOWER($4) as email,
    $5::DATE as signup_date,
    CURRENT_TIMESTAMP() as loaded_at
  FROM @my_stage/customers.csv
)
FILE_FORMAT = (TYPE = 'CSV' SKIP_HEADER = 1);
```

### Conditional Loading
```sql
-- Load only rows meeting criteria
COPY INTO valid_orders
FROM (
  SELECT $1, $2, $3, $4
  FROM @my_stage/orders.csv
  WHERE $3::NUMBER > 0  -- Only positive amounts
    AND $4::DATE >= '2024-01-01'  -- Only recent orders
)
FILE_FORMAT = (TYPE = 'CSV' SKIP_HEADER = 1);
```

## Working with Semi-Structured Data

### JSON Column Extraction
```sql
-- Load JSON and extract specific fields
COPY INTO user_events (user_id, event_type, event_time, properties)
FROM (
  SELECT 
    $1:user_id::STRING,
    $1:event_type::STRING,
    $1:timestamp::TIMESTAMP,
    $1:properties::VARIANT
  FROM @json_stage/events.json
)
FILE_FORMAT = (TYPE = 'JSON');
```

### Nested JSON Handling
```sql
-- Extract nested JSON fields
COPY INTO user_profiles
FROM (
  SELECT 
    $1:id::INTEGER as user_id,
    $1:profile.name::STRING as full_name,
    $1:profile.address.city::STRING as city,
    $1:profile.address.country::STRING as country,
    $1:preferences::VARIANT as preferences
  FROM @json_stage/profiles.json
)
FILE_FORMAT = (TYPE = 'JSON');
```

## Monitoring and Troubleshooting

### Check Load History
```sql
-- View recent COPY operations
SELECT *
FROM TABLE(INFORMATION_SCHEMA.COPY_HISTORY(
  TABLE_NAME => 'CUSTOMERS',
  START_TIME => DATEADD(hours, -24, CURRENT_TIMESTAMP())
));

-- Check for errors in recent loads
SELECT *
FROM TABLE(INFORMATION_SCHEMA.COPY_HISTORY())
WHERE status = 'LOAD_FAILED'
ORDER BY last_load_time DESC;
```

### File Metadata Query
```sql
-- Preview file contents before loading
SELECT metadata$filename, metadata$file_row_number, *
FROM @my_stage/customers.csv
(FILE_FORMAT => my_csv_format)
LIMIT 10;
```

### Check Stage Contents
```sql
-- List files in stage
LIST @my_stage;

-- Check file details
SELECT "name", "size", "md5", "last_modified"
FROM TABLE(RESULT_SCAN(LAST_QUERY_ID()));
```

## Common Patterns and Best Practices

### Incremental Loading Pattern
```sql
-- Load only new files (using pattern with dates)
COPY INTO daily_sales
FROM @sales_stage
PATTERN = '.*sales_' || TO_CHAR(CURRENT_DATE(), 'YYYY_MM_DD') || '.*\.csv'
FILE_FORMAT = my_csv_format
ON_ERROR = 'CONTINUE';
```

### Bulk Loading with Error Handling
```sql
-- Production bulk load with comprehensive error handling
COPY INTO production_table
FROM @production_stage
PATTERN = '.*\.csv'
FILE_FORMAT = production_csv_format
ON_ERROR = 'CONTINUE'
SIZE_LIMIT = 10000000000  -- 10GB limit
PURGE = FALSE  -- Keep files for troubleshooting
FORCE = FALSE;  -- Don't reload processed files
```

### Multi-Format Loading
```sql
-- Load different file types to same table
-- CSV files
COPY INTO raw_data
FROM @my_stage
PATTERN = '.*\.csv'
FILE_FORMAT = (TYPE = 'CSV' SKIP_HEADER = 1);

-- JSON files  
COPY INTO raw_data
FROM @my_stage
PATTERN = '.*\.json'
FILE_FORMAT = (TYPE = 'JSON');
```

## Error Recovery

### Retry Failed Loads
```sql
-- Find failed files
SELECT file_name, error_description
FROM TABLE(INFORMATION_SCHEMA.COPY_HISTORY())
WHERE status = 'LOAD_FAILED';

-- Retry specific file with adjusted parameters
COPY INTO customers
FROM @my_stage/problematic_file.csv
FILE_FORMAT = (TYPE = 'CSV' SKIP_HEADER = 1 ERROR_ON_COLUMN_COUNT_MISMATCH = FALSE)
ON_ERROR = 'CONTINUE'
FORCE = TRUE;
```

### Data Quality Validation
```sql
-- Validate before full load
COPY INTO customers
FROM @my_stage/customers.csv
FILE_FORMAT = my_csv_format
VALIDATION_MODE = 'RETURN_ALL_ERRORS';

-- If validation passes, proceed with actual load
COPY INTO customers
FROM @my_stage/customers.csv
FILE_FORMAT = my_csv_format
ON_ERROR = 'ABORT_STATEMENT';
```

## Key Points to Remember

- **COPY INTO is idempotent** - same files won't be loaded twice (unless FORCE = TRUE)
- **Use VALIDATION_MODE** for testing before production loads
- **Pattern matching** supports regex for flexible file selection
- **File formats** can be inline or named for reusability
- **Error handling** provides flexible options for data quality management
- **Transformations** can be applied during load for data cleaning
- **Metadata queries** help preview and validate data before loading
- **Monitoring** through COPY_HISTORY helps track load operations

# Snowpipe

Snowpipe allows you to automate a data ingestion pipeline to continuously upload files.

Snowpipe load history is stored in the metadata of the pipe for 14 days to prevent reloading the same files in a table. 

Snowpipe is a serverless feature using snowflake managed compute resources to load data files and not a user managed virtual warehouse. However, a user specified warehouse will be required to execute copy into statements

Snowpipes can be paused.
