This section makes up 20-25% of the exam

## Access Control

**Role based access control** entail that a certain role will grant priveledges of statements to a user.

**Discretionary access control** gives a role ownership over an object and that role can grant another role statement priveledges to that object.

![image](https://github.com/user-attachments/assets/b2e67f22-1415-467d-972a-557b2146fa7e)

Object Hierarchy

![image](https://github.com/user-attachments/assets/8ce29e4e-0382-4293-926d-604f57da6f04)

## Roles

ORGADMIN

Can create acccount in an organization
Can view usage information across an org

ACCOUNTADMIN

Highest level - "super admin" role
Can manage the entire account, including other roles and users
Can view and manage all objects in the account
Can view view and manage billing
Only role that can create other ACCOUNTADMIN users
Best practice: Use sparingly, don't use for daily operations
By default, the only role that can access the snowflake database.

SYSADMIN

System administration for databases and warehouses
Can create databases, schemas, warehouses, and other objects
Cannot manage users or roles (that's SECURITYADMIN)
Inherits: All privileges granted to custom roles
Most common role for database administrators
It is recommended to assign users to this role

SECURITYADMIN

Manages users and roles (security-focused admin)
Can create, modify, and grant/revoke roles
Can manage users and their assignments
Cannot manage account-level settings (that's ACCOUNTADMIN)
Inherits: All privileges that can be granted to custom roles

USERADMIN

Limited user management capabilities
Can create users but with limited privileges
Cannot create roles or manage high-level security
Inherits: Nothing special - more restrictive than SECURITYADMIN



Default Database Role
PUBLIC

Every user automatically gets this role
Lowest privilege level by default
Used to grant minimal access that everyone should have
Often used for shared, non-sensitive objects

Here's a handy query to see the roles that you have

```sql
-- Set context 
USE ROLE ACCOUNTADMIN;

SHOW ROLES;
SELECT "name", "comment" FROM TABLE(result_scan(last_query_id()));
```

## Privileges

A security privalige defines a level of access to an object

There are 4 categories of privaledges

Global Privileges
Definition: Account-wide privileges that apply across the entire Snowflake account, not tied to specific databases or schemas.
Examples:

CREATE ACCOUNT - Create new accounts (for organizations)
CREATE USER - Create users in the account
CREATE ROLE - Create new roles
CREATE WAREHOUSE - Create virtual warehouses
CREATE DATABASE - Create databases
CREATE INTEGRATION - Create integrations (API, notification, etc.)
EXECUTE MANAGED TASK - Execute tasks
MANAGE GRANTS - Manage privilege grants
MONITOR USAGE - View account usage information

Usage example:
```sql
GRANT CREATE WAREHOUSE TO ROLE data_admin;
GRANT CREATE USER TO ROLE user_manager;
```
Account Privileges
Definition: Privileges that control account-level operations and settings, typically reserved for account administrators.
Examples:

MANAGE GRANTS - Grant/revoke privileges across the account
MONITOR USAGE - View account-level usage and billing
MONITOR EXECUTION - View query history across the account
CREATE DATA EXCHANGE LISTING - Create data marketplace listings
IMPORT SHARE - Import shared data from other accounts
CREATE SHARE - Create outbound data shares

Usage example:
```sql
GRANT MONITOR USAGE TO ROLE billing_admin;
GRANT MANAGE GRANTS TO ROLE security_admin;
```
Schema Privileges
Definition: Privileges that control access to schemas and operations within schemas (but not on the individual objects inside them).
Examples:

USAGE - Access the schema (required to see objects in it)
CREATE TABLE - Create tables in the schema
CREATE VIEW - Create views in the schema
CREATE FUNCTION - Create UDFs in the schema
CREATE PROCEDURE - Create stored procedures in the schema
CREATE SEQUENCE - Create sequences in the schema
CREATE STREAM - Create streams in the schema
CREATE TASK - Create tasks in the schema

Usage example:
```sql
GRANT USAGE ON SCHEMA sales TO ROLE analyst;
GRANT CREATE TABLE ON SCHEMA sales TO ROLE data_engineer;
GRANT ALL PRIVILEGES ON SCHEMA sales TO ROLE schema_admin;
```
Schema Object Privileges
Definition: Privileges that control access to specific objects within schemas (tables, views, functions, etc.).
Examples:
Table/View privileges:

SELECT - Query the table/view
INSERT - Insert data into table
UPDATE - Update data in table
DELETE - Delete data from table
TRUNCATE - Truncate the table
REFERENCES - Create foreign key references

Function/Procedure privileges:

USAGE - Execute the function/procedure

Other object privileges:

USAGE - Use sequences, file formats, stages
READ - Read files from stages
WRITE - Write files to stages

Usage example:
```sql
-- Table privileges
GRANT SELECT ON TABLE customers TO ROLE analyst;
GRANT INSERT, UPDATE ON TABLE orders TO ROLE data_loader;
```

You can use the following query to see the priveledges associated with your role

```sql
SHOW GRANTS TO ROLE SECURITYADMIN;
```

## Future Grants

Rather than having to grant the select priveledge to analyst for every new table that you make, you can use the future command.

Without future grants:

```sql
-- Every time someone creates a new table, you have to do this:
CREATE TABLE new_customers (...);
GRANT SELECT ON TABLE new_customers TO ROLE analyst;  -- Ugh, again!

CREATE TABLE new_orders (...);  
GRANT SELECT ON TABLE new_orders TO ROLE analyst;     -- Ugh, again!
```

With future grants

```sql
-- Say this ONCE:
GRANT SELECT ON FUTURE TABLES IN SCHEMA sales TO ROLE analyst;

-- Now ANY new table automatically gives SELECT permission to analyst!
CREATE TABLE new_customers (...);  -- analyst can SELECT automatically! ✨
CREATE TABLE new_orders (...);     -- analyst can SELECT automatically! ✨
```

## Auth

Snowflake strongly recommends all users with accountadmin be reqquired to use MFA.

For a user who has lost their MFA device, it is possible to disable mfa

```sql
-- Only option - disable indefinitely
ALTER USER john_doe SET DISABLE_MFA = TRUE;
```

Snowflake does support federated auth too so that we can use something like Okta

Snowflake also supports oauth so that snowflake doesn't manage login credentials

Snowflake also supports SCIM so that we can use Microsoft ADFS as an IDP

## Network Policies

Snowflake can allow you to set network policies so that we can allow and block certain IPs

```sql
-- Create a network policy with allowed IP ranges
CREATE NETWORK POLICY corporate_access_policy
  ALLOWED_IP_LIST = ('192.168.1.0/24', '10.0.0.0/8', '203.0.113.0/24')
  BLOCKED_IP_LIST = ('192.168.1.99')
  COMMENT = 'Allow corporate network access only';

-- Apply network policy to the entire account
ALTER ACCOUNT SET NETWORK_POLICY = corporate_access_policy;

-- Apply network policy to individual user
ALTER USER john_doe SET NETWORK_POLICY = corporate_access_policy;
```

Only the securityadmin and accountadmin roles can apply policies unless you grant another role the ATTACH POLICY priveledge.

## Data encryption

all tables and stages are loaded with AES-256 encryption applied. in fact, all data at rest is encrypted. snowflake uses tls2.0 for data in transit.

by default when using an internal stage with the PUT command, the data is encrypted. However when loading data into an external stage, because the data comes from elsewhere, encryption isn't guarenteed until it is loaded into snowflake.

Snowflake manages all of these keys in a hierarchical key model. Looking at this model, we can see that each database and table is encrypted with a seperate key.

![image](https://github.com/user-attachments/assets/1e535f2d-f3ec-455d-bdf2-22ec171183f5)

Snowflake automatically makes use of key rotations. You can also set re-keying to make a new key and re-encrypt periodically, however this is an enterprise feature and does incur cost.

## Column level security

Snowflake can allow you to create a masking policy so that lower level users can't see everything. In the following example, users not in hr_admin or compliance_officer are unable to see the full ssn of a user.

```sql
CREATE MASKING POLICY ssn_mask AS (val STRING) RETURNS STRING ->
  CASE 
    WHEN CURRENT_ROLE() IN ('HR_ADMIN', 'COMPLIANCE_OFFICER') THEN val
    ELSE 'XXX-XX-XXXX'
  END;

-- Apply SSN masking
ALTER TABLE employees 
MODIFY COLUMN ssn SET MASKING POLICY ssn_mask;
```

## Row level security

Similarly, you can set row level security

```sql
CREATE ROW ACCESS POLICY user_data_policy AS (data_owner STRING) RETURNS BOOLEAN ->
  CASE 
    WHEN CURRENT_ROLE() IN ('ADMIN', 'SUPERVISOR') THEN TRUE
    WHEN CURRENT_USER() = data_owner THEN TRUE  -- Users can see their own data
    ELSE FALSE
  END;

-- Apply user policy to personal data table
ALTER TABLE user_profiles 
ADD ROW ACCESS POLICY user_data_policy ON (username);
```

Row acccess policies are evaluated before data masking policies meaning that the row policies act on unmasked data.

The Information Schema is a special read-only schema that Snowflake automatically creates in every database. It provides metadata about all the objects and structures within that database.

Account usage views can be used to view current and dropped objects.

## Object Tagging

An object tag is a schema level object that allows you to assign specific metadata to other database objects.

![image](https://github.com/user-attachments/assets/45a03123-8f60-4088-835c-bc9fa82ae9dc)

```sql
-- Create tags first
CREATE TAG cost_center;
CREATE TAG data_classification VALUES ('public', 'internal', 'confidential', 'restricted');
CREATE TAG environment VALUES ('dev', 'test', 'prod');

-- Apply tags to a table
ALTER TABLE customers SET TAG (
  cost_center = 'marketing',
  data_classification = 'confidential',
  environment = 'prod'
);
```

Key Benefits of Object Tagging

Cost allocation - Track spending by department/project
Data governance - Classify and manage data by sensitivity
Compliance - Track regulatory requirements (GDPR, SOX, etc.)
Resource management - Organize objects by team/project
Automation - Use tags to trigger automated policies
Search and discovery - Find objects by business context

Tagging can allow us to automatically apply masking policies
