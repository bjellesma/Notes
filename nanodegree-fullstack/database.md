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

## SQL Practice

### Manipulating data

**Schema (PostgreSQL v9.6)**

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

[View on DB Fiddle](https://www.db-fiddle.com/)
