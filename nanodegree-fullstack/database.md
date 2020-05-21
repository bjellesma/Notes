**DBAPI** - method of interacting with a webserver framework such as python, nodejs, ruby on rails, etc.

**DBMS** - software that allows you to interact with a database (access or modify data) such as PostgreSQL

Databases have a concept called **Concurrency Control** that allows multiple database actions to occur at once.

Examples of popular**relational** databases are **PostgreSQL**, **SQL Server**, and **SQLite**

**Nonrelation (NOSQL)** database are a larger family of databases that use different schemas such as **MongoDB** which use documents and **neo4j** which uses a series of graphs to store data.

In **relational databases**, all data is stored in tables and comes with a set of rules (**constraint**) for enforcing **data integrity**

If you have more than 1 column identifying the uniqueness of a table, the set of primary key columns is known as a **composite key**.

**Foreign keys** will map the primary key from one table to another table.

Every relational database system (Postgres, SQL Server, MySQL, etc.) has its own *flavor* (**dialect**) of SQL that it implements because none of them are 100% compliant with the SQL standard.

## Commands to know

| Manipulating | Querying | Structuring | Joins | Grouping | Aggregate |
|---|---|---|---|---|---|
| Insert | Select | Create Table | (Inner) Join | Group By | Sum |
| Update |   | Alter Table | Left Join |    | Count |
| Delete |   | Drop Table | Right Join |    |    |
|   |   | Add Column |   |   |   |
|   |   | Drop Column |   |   |   |
