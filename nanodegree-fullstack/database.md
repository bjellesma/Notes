**DBAPI** - method of interacting with a webserver framework such as python, nodejs, ruby on rails, etc.

**DBMS** - software that allows you to interact with a database (access or modify data) such as PostgreSQL

Databases have a concept called **Concurrency Control** that allows multiple database actions to occur at once.

Examples of popular**relational** databases are **PostgreSQL**, **SQL Server**, and **SQLite**

**Nonrelation (NOSQL)** database are a larger family of databases that use different schemas such as **MongoDB** which use documents and **neo4j** which uses a series of graphs to store data.

In **relational databases**, all data is stored in tables and comes with a set of rules (**constraint**) for enforcing **data integrity**

If you have more than 1 column identifying the uniqueness of a table, the set of primary key columns is known as a **composite key**.

**Foreign keys** will map the primary key from one table to another table.

Every relational database system (Postgres, SQL Server, MySQL, etc.) has its own *flavor* (**dialect**) of SQL that it implements because none of them are 100% compliant with the SQL standard.

**Inner Joins** - returns rows of data only if they exist between all joined tables

**Outer Joins** - return every row that exists in the left and right joined table while rendering NULL values on rows who foreign key does not match a record in the other table. LEFT and RIGHT JOINS will return null for the other table.

## Commands to know

| Manipulating | Querying | Structuring | Joins | Grouping | Aggregate |
|---|---|---|---|---|---|
| Insert | Select | Create Table | (Inner) Join | Group By | Sum |
| Update |   | Alter Table | Left Join |    | Count |
| Delete |   | Drop Table | Right Join |    |    |
|   |   | Add Column |   |   |   |
|   |   | Drop Column |   |   |   |

## SQL Practice

### Manipulating data

**Schema (PostgreSQL v9.6)**
```sql
    create table drivers (
      id serial primary key,
      first_name varchar,
      last_name varchar
    );
    
    create table vehicles (
      id serial primary key,
      make varchar,
      model varchar,
      driver_id integer references drivers(id)
    );
    
    INSERT INTO drivers (first_name, last_name) VALUES ('Bill', 'Jellesma'),('Bob', 'Smith'),('John', 'Smith');
    INSERT INTO vehicles (make, model, driver_id) VALUES ('Chevy', 'Malibu', 1),('Ford', 'Station Wagon',2),('Chevy','Silverado',3);
    
    --Update name of first driver
    UPDATE drivers SET first_name = 'William' WHERE id = 1;
    
    --Delete all vehicles from driver id 2
    DELETE from vehicles where driver_id = 2;
    
    --Driver id 1 gets a new vehicle
    INSERT INTO vehicles (make, model, driver_id) VALUES ('Chevy', 'Camero', 1)
    
```
---

**Query #1**

    SELECT * from drivers ORDER by id desc;

| id  | first_name | last_name |
| --- | ---------- | --------- |
| 3   | John       | Smith     |
| 2   | Bob        | Smith     |
| 1   | William    | Jellesma  |

---
**Query #2**

    SELECT * from vehicles order by id desc LIMIT 3 ;

| id  | make  | model     | driver_id |
| --- | ----- | --------- | --------- |
| 4   | Chevy | Camero    | 1         |
| 3   | Chevy | Silverado | 3         |
| 1   | Chevy | Malibu    | 1         |

---

## Structuring Data

**Schema (PostgreSQL v9.6)**
```sql
    create table drivers (
      id serial primary key,
      first_name varchar,
      last_name varchar
    );
    
    create table vehicles (
      id serial primary key,
      make varchar,
      model varchar,
      driver_id integer references drivers(id)
    );
    
    INSERT INTO drivers (first_name, last_name) VALUES ('Bill', 'Jellesma'),('Bob', 'Smith'),('John', 'Smith');
        INSERT INTO vehicles (make, model, driver_id) VALUES ('Chevy', 'Malibu', 1),('Ford', 'Station Wagon',2),('Chevy','Silverado',3);
    
    -- Add vehicle color column
    ALTER TABLE vehicles
    ADD COLUMN color varchar;
    
    --Update vehicles to add colors
    UPDATE vehicles SET color = 'blue' WHERE id = 1;
    UPDATE vehicles SET color = 'green' WHERE id = 2;
    UPDATE vehicles SET color = 'black' WHERE id = 3;
    
    --add email and address to drivers table
    ALTER TABLE drivers
    ADD COLUMN email varchar,
    ADD COLUMN address varchar;
```
---

**Query #1**

    SELECT * from drivers ORDER by id desc;

| id  | first_name | last_name | email | address |
| --- | ---------- | --------- | ----- | ------- |
| 3   | John       | Smith     |       |         |
| 2   | Bob        | Smith     |       |         |
| 1   | Bill       | Jellesma  |       |         |

---
**Query #2**

    SELECT * from vehicles order by id desc LIMIT 3 ;

| id  | make  | model         | driver_id | color |
| --- | ----- | ------------- | --------- | ----- |
| 3   | Chevy | Silverado     | 3         | black |
| 2   | Ford  | Station Wagon | 2         | green |
| 1   | Chevy | Malibu        | 1         | blue  |

---

## Joins and Group Bys

**Schema (PostgreSQL v9.6)**
```sql
    create table drivers (
          id serial primary key,
          first_name varchar,
          last_name varchar
        );
        
        create table vehicles (
          id serial primary key,
          make varchar,
          model varchar,
          driver_id integer references drivers(id)
        );
        
    INSERT INTO drivers (first_name, last_name) VALUES ('Bill', 'Jellesma'),('Sarah', 'Smith'),('John', 'Smith');
    INSERT INTO vehicles (make, model, driver_id) VALUES ('Chevy', 'Malibu', 1),('Ford', 'Station Wagon',2),('Chevy','Silverado',3),('Chevy','Camero',1),('Tesla','Model S', 2),('Ford', 'Explorer',3);
```
---

**Query #1**

    SELECT drivers.first_name, drivers.last_name, vehicles.make, vehicles.model 
    FROM vehicles
    INNER JOIN drivers
    ON drivers.id = vehicles.driver_id
    where drivers.id = 3;

| first_name | last_name | make  | model     |
| ---------- | --------- | ----- | --------- |
| John       | Smith     | Chevy | Silverado |
| John       | Smith     | Ford  | Explorer  |

---
**Query #2**

    SELECT drivers.first_name, drivers.last_name, vehicles.make, vehicles.model 
    FROM vehicles
    INNER JOIN drivers
    ON drivers.id = vehicles.driver_id
    where drivers.first_name = 'Sarah';

| first_name | last_name | make  | model         |
| ---------- | --------- | ----- | ------------- |
| Sarah      | Smith     | Ford  | Station Wagon |
| Sarah      | Smith     | Tesla | Model S       |

---
**Query #3**

    SELECT drivers.first_name, drivers.last_name, COUNT(vehicles.driver_id) 
    FROM vehicles
    INNER JOIN drivers
    ON drivers.id = vehicles.driver_id
    GROUP BY drivers.first_name, drivers.last_name;

| first_name | last_name | count |
| ---------- | --------- | ----- |
| Sarah      | Smith     | 2     |
| Bill       | Jellesma  | 2     |
| John       | Smith     | 2     |

---
**Query #4**

    SELECT vehicles.make, COUNT(drivers.id)
    FROM vehicles
    INNER JOIN drivers
    ON drivers.id = vehicles.driver_id
    WHERE vehicles.make = 'Chevy'
    GROUP BY vehicles.make;

| make  | count |
| ----- | ----- |
| Chevy | 3     |

---

### Query to remind user of vehicle registration

**Schema (PostgreSQL v9.6)**
```sql
    create table drivers (
          id serial primary key,
          first_name varchar,
          last_name varchar
        );
        
        create table vehicles (
          id serial primary key,
          make varchar,
          model varchar,
          driver_id integer references drivers(id)
        );
        
    INSERT INTO drivers (first_name, last_name) VALUES ('Bill', 'Jellesma'),('Sarah', 'Smith'),('John', 'Smith');
    INSERT INTO vehicles (make, model, driver_id) VALUES ('Chevy', 'Malibu', 1),('Ford', 'Station Wagon',2),('Chevy','Silverado',3),('Chevy','Camero',1),('Tesla','Model S', 2),('Ford', 'Explorer',3);
    
    --Update vehicles table to show date of registration information
    ALTER TABLE vehicles
    ADD COLUMN registration_date TIMESTAMPTZ;
    UPDATE vehicles SET registration_date = '2019-06-12 00:00' WHERE id=1;
    UPDATE vehicles SET registration_date = '2020-02-01 00:00' WHERE id=2;
    UPDATE vehicles SET registration_date = '2020-05-01 00:00' WHERE id=3;
    UPDATE vehicles SET registration_date = '2019-12-22 00:00' WHERE id=4;
    UPDATE vehicles SET registration_date = '2020-01-04 00:00' WHERE id=5;
    UPDATE vehicles SET registration_date = '2020-03-22 00:00' WHERE id=6;
```
---

**Query #1**
```sql
    SELECT 
    FORMAT('%1$s %2$s', drivers.first_name, drivers.last_name) full_name,
    FORMAT('%1$s %2$s', vehicles.make, vehicles.model) vehicle,
    to_char(registration_date, 'Month DD, YYYY') date_of_registration,
    to_char(registration_date+interval '12 month', 'Month DD, YYYY') registration_due
    FROM vehicles
    INNER JOIN drivers
    ON drivers.id = vehicles.driver_id
    WHERE registration_date < NOW() - interval '11 month';
```
| full_name     | vehicle      | date_of_registration | registration_due   |
| ------------- | ------------ | -------------------- | ------------------ |
| Bill Jellesma | Chevy Malibu | June      12, 2019   | June      12, 2020 |

---

Keep in mind the execution plan on queries to identify bottlenecks. Check out the execution plan for the last query. If using SQL Fiddle, you can get the execution plan after you've written the query.

```
Hash Join (cost=29.12..58.81 rows=250 width=128)
Hash Cond: (vehicles.driver_id = drivers.id)
-> Seq Scan on vehicles (cost=0.00..23.12 rows=250 width=76)
Filter: (registration_date < (now() - '11 mons'::interval))
-> Hash (cost=18.50..18.50 rows=850 width=68)
-> Seq Scan on drivers (cost=0.00..18.50 rows=850 width=68)
```
