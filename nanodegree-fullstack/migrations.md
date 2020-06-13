# Database Schemas

**Data migrations** are how we manage modifications over time.

A **schema migration** is a file that tracks changes to our **database schema** (the structure of our database). This causes us to think of **migration** as a git version control system with each commit being a **schema migration**. We'll upgrade our database schema by **applying migrations** and we'll roll back our database schema by reverting migrations.

There are libraries available for our frameworks that will allow us to perform database migrations. For example, Flask has a library called **Flask-Migrate** which is capable of managing migrations for SQLAlchemy-based databases.

**Important Note**: When first looking at a migration library, it doesn't seem very useful. Database migration libraries mearly look at your current database compared to what you want to do (drop column, add column, change keys, etc.) and figures out how to drop all of your models in order to incorporate the changes. The reason that this doesn't seem useful at first is because, when you have an application that you're starting, you have no data so it's trivial to just add/drop columns as needed. However, when you have data in your database such as usernames and passwords, you don't want to have to recreate these models because you'll lose a lot of data. I know that I've personally run into this issue where I want to add a new attribute for the database but I already have some user records. My solution was actually to create scripts using plain python that would copy the data to the database.

[Pretty Printed has a good video on this](https://www.youtube.com/watch?v=BAOfjPuVby0). His video shows a simple example of dropping and adding a column but it gives a good demo of the use of Flask-Migrate when your database has a lot of data. **NOTE** Flask-Script is no longer supported but the same CLI can be accomplished by using `flask db init` instead of `python script.py db init`. See the example section below.

# Example

Flask-Migrate includes **Flask-Script**, which is needed to run migrations from the command line. Use the following script (call it `script.py` as an example. Flask-Migrate also uses **alembic** under the hood to run the migrations. In Flask-Migrate, **migrations** are referred to as files in your local repository that capture changes to your database schema.

```py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
# init the migration on the app
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

if __name__ == '__main__':
    app.run()
```

**Special Note**: If you have models scattered across serveral apps, you'll need to import the models on your `app.py` initializing script after all other objects have been created like the following.

```py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate #used for database migrations

from secure import (
    CONNECT_STRING, DEBUG
)


app = Flask(__name__)
app.config['DEBUG'] = DEBUG
app.config['SQLALCHEMY_DATABASE_URI'] = CONNECT_STRING
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# Instantiate migrate instance
migrate = Migrate(app, db)

from models.todo import Todo
```

Now use the following command in the terminal. Notice that this will create a migrations folder in your root directory. All database migration scripts will be stored in this folder. Optionally, you'll be asked to edit configurations in an ini file that is placed in that folder.

```bash
flask db init
```

Now run the following command to create a migration script. This command will analze your current sqlalchemy database and compare it with the models that are in your app code and create a migration script.

```bash
flask db migrate
```

You can now use the following command to go to the new version of the database that you want

```bash
flask db upgrade
```

You can also use the following command to roll back the database to its previous version

```bash
flask db downgrade
```

After running a `db upgrade` or `db-downgrade`, a new table will be created called `alembic version` in whatever database that we're creating. Going back to our analogy of git versioning, this can be thought of as the `.git` folder in that it's always in the repo but it just used to store version information and rarely, if ever needs to be touched.

# Migrate with library vs migrate without library

## Without library

Once we create our models, we would use the following line of code in our python app.

```py
db.create_all()
```

When we want to modify our models that we have, we would simply rewrite the model classes

```py
class Todo(db.Model):
    completed = db.Column(...)
```

But since we already have a database with the previous models, we will need to drop our existing database in order to update the model. From the command line, we call the following:

```bash
dropdb todoapp && createdb todoapp
```

and now we will recreate the tables on the database by using

```py
db.create_all()
```

As you can see, doing this process when our database is bare isn't a problem since there is no data to worry about. If we had data in our todoapp already, this would become a problem because we would lose all of our data. Secondly, if all we want to do is add a column to a table, we would still be dropping and recreating an entire database. Again, this isn't a problem with a tiny database but when our database begins to get large, this will become an intensive task.

## With Library

With a library, we'll not be using `db.createall()` anymore. 

* Using a library will detect the changes of the current version to the new version and generate a script with only accomplishing those changes, such as adding a column to database. This is big because we remove the overhead of performance with needing to recreate the entire database.
* Since the library doesn't drop any tables, but just modifies them, we'll be able to keep any existing data in our database.
* Because the scripts are able to isolate units of change, we'll be able to rollback the database if needed.

# Special Notes/tips

I ran a `flask db migrate` and then when running `flask db upgrade`, I received an error because I see one of the columns as `nullable=False` while forgetting a default value. When I rewrote the model to include the changed code and attempted to run `flask db migrate` again, I received the following message

```bash
ERROR [root] Error: Target database is not up to date.
```

I also couldn't run `flask db downgrade` to undo the migrate. I ended up deleted the script autogenerated in the `versions` folder and then reran `flask db migrate`.

## Adding default values to a prepopulated database

I attempted to add a default constraint to a table already containing data, alembic wasn't able to add this so I had to add/modify the following code to my migration script

```py
def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('completed', sa.Boolean(), nullable=True))
    op.execute("UPDATE todo SET completed = false")
    op.alter_column('todo', 'completed', nullable=False)
```

Notice that I 

1. allowed nulls for my completed column
2. added an update command to set completed to my desired null value
3. alter the completed column to disallow nulls

# Final Notes

It's a good idea to setup flask-migrate at the begining of our setup even though it is a little extra work. The advantage here is that we will more easily be able to keep our database in a valid state.