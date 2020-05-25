# Intro

SQLAlchemy is an **Object Relational Mapping (ORM) Library** and the most popular Python SQL Toolkit while psycopg2 is a **DBAPI** library. This ORM maps tables and columns to classes and objects to give it a more familiar feel to object oriented programming. For example, in SQL you would use the following to create a table

```sql
CREATE TABLE todos(
    id INTEGER PRIMARY KEY,
    description VARCHAR NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT false
)
```

With SQLAlchemy, you would instead use the following Python code:

```py
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
```

Another example, instead of the SQL

```sql
select * from todos
```

We would use

```py
Todo.query.all()
```

While we can just use a DBAPI to communicate with a database, this solution doesn't scale as complexity grows. Using an ORM offers us layers of abstraction for performance and scalability reasons. While psycopg2 will send our SQL statements directly to the database, SQLAlchemy will generate the sql statements. SQLAlchemy does depend on psycopg2 or other database drivers to connect to a database under the hood.

## Layers of abstraction

![Layers of Abstraction](images/abstraction_layers.png)

SQLAlchemy is able to use 3 layers of abstraction when communicating with a database.
* Able to write high level code on the ORM layer
* Able to use database operations to run customized SQL code on the expressions layer
* Able to write raw SQL statements if needed on the engine level of abstraction.

### Dialect

Since each database system has its own flavor of SQL that we refer to as a **dialect**, we can say that SQLAlchemy is able to abstract these dialects so that we can use multiple backends. For example, according to the documentation [here](https://docs.sqlalchemy.org/en/13/dialects/mssql.html), SQLAlchemy is able to communicate with MSSQL using the pyodbc DBAPI.

### Connection Pool

SQLAlchemy uses a **connection pool** to handle connections to the database, abstracting away the management of connections. Using a connection pool has the following advantages:

* Handles reusing of existing connections rather than opening and closing new connections.
* Avoid opening and closing connections for every data change
* Handles dropped connections due to network interruption
* Pools calls to the database rather than performing many smaller calls to the database improving the performance

### Engine layer

The **engine** is the lowest layer of abstraction that SQLAlchemy will use to communicate with the database. The following code will allow us to communicate with raw sql, just as if we were using a *DBAPI*:

```py
from sqlalchemy import create_engine

engine = create_engine('postgres://..')
conn = engine.connect()
# the execute method on engine will allow us to use raw sql statements
result = conn.execute('SELECT * FROM ...')

result.close()
```

The Engine in SQLAlchemy refers to both itself, the Dialect and the Connection Pool, which all work together to interface with our database so a connection pool is automatically created when we create a SQLAlchemy engine.

![SQLAlchemy Engine](images/sqlalchemy_engine.png)

The dialect is determine when the engine if first created:

```py
from sqlalchemy import create_engine
engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')
```

**In summary, we use an engine to interact with our database, much like how we would interact with a DBAPI**

### SQL Expressions Layer

The following is example code for the **SQL Expressions** abstraction layer

```py
todos = Table('todos',...)

insert_stmt = todos.insert().values(
    description = 'Clean my room'
    completed = False
)
```

Using SQL Expressions, you don't need to know how to build raw strings

### ORM layer

Lets you compose SQL Expressions by building Python classes of objects which map to tables in the database.

SQLAlchemy is split into two libraries:

* SQLAlchemy Core
* SQLAlchemy ORM (Object Relational Mapping library). SQLALchemy ORM is offered as an optional library, so you don't have to use the ORM in order to use the rest of SQLAlchemy.
    * The ORM uses the Core library inside
    * The ORM lets you map from the database schema to the application's Python objects
    * The ORM persists objects into corresponding database tables

In an ORM, we have the following mappings:

* Tables map to classes
* Table records map to class objects
* Table columns map to class attributes

For example, the following SQLAlchemy class

```py
class Tweet:
    def __init__(self, content):
        self.content = content
```

Maps to

```SQL
CREATE TABLE tweets (
    id INTEGER PRIMARY KEY
    content VARCHAR(140) NOT NULL
);
```

And

```py
tweet = Tweet('hey')
```

Maps to

```SQL
INSERT INTO tweets (content) VALUES ('hey')

## Pros of using sqlalchemy over raw sql

* Since everything that you do will be in python, you won't need to context switch as much
* You won't need to think about the database system that you're using so you can switch database systems
    * For example, you can use SQLite for development and deploy to Postgres for production
    * In the above code, **VARCHAR** is a type unique to only some database systems like MSSQL and Postgres so the raw SQL code couldn't be transferred to other systems. With an ORM like SQLAlchemy, you would avoid needing to rewrite code.
* SQLAlchemy offers **automatic** caching of common queries reducing the amount of raw sql sent to the database
```
## Connecting to your database

You'll need to use a connection string

![SQLAlchemy Connection String](images/sqlalchemy_connection_string.png)

In a flask app, you might use it like this:

```py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# sets the name of the app to the name of the module
app = Flask(__name__)
# config variables in flask are set to the app.config dictionary
app.config['SQLALCHEMY_DATABASE_URI'] = CONNECT_STRING

# Link database
db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'Hello world!'

# continuously runs the server
if __name__ == '__main__':
    app.run()
```

Where `CONNECT_STRING` is the connection string

Optionally, you can specify the driver

![SQLAlchemy Connection String](images/sqlalchemy_connection_string_option.png)

`db` is an instance of our database and gives us access to:

* db.Model - Ability to create and manipulate models
* db.session - Ability to create and manipulate transactions

Now that we've connected to the database, we'll create a database model by using a class:

```py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# sets the name of the app to the name of the module
app = Flask(__name__)
# config variables in flask are set to the app.config dictionary
app.config['SQLALCHEMY_DATABASE_URI'] = CONNECT_STRING

# db is an instance of our database
db = SQLAlchemy(app)

class Person(db.Model):
    # an init method is not needed because SQLAlchemy creates it automatically
    __tablename__ = "persons"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

# db.create_all will only use the classes to define models to the database if they don't exist
# This is good so that we're not creating tables all the time
db.create_all()

@app.route('/')
def index():
    return 'Hello world!'

# continuously runs the server
if __name__ == '__main__':
    app.run()
```

When defining database columns, we use this scheme:
`db.Column` takes `<datatype>`, `<primary_key?>`, `<constraint?>`, `<default?>`

## Queries using ORM

When we create a record, we can view it with:

```py
@app.route('/')
def index():
    query = Person.query.filter(Person.name == 'me')
    person = Person.first().name
    return 'Hello ' + person.name + '!'
```

## Transactions using ORM

we can create a new person object

```py
person = Person(name='Billy')
```

Queue the insert statement into the transaction

```py
db.session.add(person)
```

And commit the transaction when we're ready

```py
db.session.commit()
```

## SQLAlchemy Data Types and constraints

SQLAlchemy has its own data types rather than using the standard `VARCHAR`, etc.

![SQLAlchemy Data Types](images/sqlalchemy_data_types.png)

```py
class Person(db.Model):
    # an init method is not needed because SQLAlchemy creates it automatically
    __tablename__ = "persons"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(50), nullable=False, unique=True)
    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}>'
``` 

Notice in the above code that we've added a new field, title, with a uniqueness constraint. The database will now throw an error is this constraint is not met. These errors are to enforce **data integrity**.

Notice also that you're able to create custom constraints called **check constraints**. The following is a check constraint to ensure that the price contains only positive values.

```py
class Product(db.Model):
  ...
  price = db.Column(db.Float, db.CheckConstraint('price>0'))
```

## Debug App in interactive mode

You can enter an interactive session with python with the following command

```bash
python
```

In the interactive session, you can import the module you're building (assuming the filename is app.py)

```bash
import app
from app import Person
```

You can now use object Person

```py
Person.query.all()
```

by default, you'll receive output like

```py
<Person 1>
```

but by adding a method to override the default `__repr__()` method

```py
def __repr__(self):
    return f'<Person ID: {self.id}, name: {self.name}>'
```

We now receive output more suited to debugging

```bash
<Person ID: 2, name: dustin>
```