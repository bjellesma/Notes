To start a connection to the external api, we need to connect to our local instance using `xmlrpc`. With our server already running, we can create a new python file to query the server

```py
import xmlrpc.client

server = "http://localhost:8069"
common = xmlrpc.client.ServerProxy(f'{server}/xmlrpc/2/common')
```

You can also use `.env` files to obscure sensative information

```py
import xmlrpc.client
import dotenv
import os

# env vars
dotenv.load_dotenv()
server = os.getenv('SERVER')
port = os.getenv('PORT')

common = xmlrpc.client.ServerProxy(f'http://{server}:{port}/xmlrpc/2/common')

print(f'version: {common.version()}')
```

We can now do something like get the version information

```py
print(f'version: {common.version()}')
```

You can find the api reference information here [https://www.odoo.com/documentation/14.0/developer/webservices/odoo.html](https://www.odoo.com/documentation/14.0/developer/webservices/odoo.html)

# Authenticating

Now that we have a common connection, we can authenticate to get a uid to make object calls.

```py
# env vars
dotenv.load_dotenv()
server = os.getenv('SERVER')
port = os.getenv('PORT')
database = os.getenv('DATABASE')
user = os.getenv('USER')
# TODO in odoo 14, you should be able to setup developer keys
password=os.getenv('PASSWORD')

common = xmlrpc.client.ServerProxy(f'http://{server}:{port}/xmlrpc/2/common')
# Get the user id of our logged in user
# necessary for object calls in the script
uid = common.authenticate(database, user, password, {})
```

# Object calls

In addition to getting a uid to perform our object calls with, we'll make another `xmlrpc` call to `/objects`

```py
odoo_api = xmlrpc.client.ServerProxy(f'http://{server}:{port}/xmlrpc/2/object')
```

Now, let's use an example to count the number of objects that appear in `product.template`

```py
# count items in model
product_count = odoo_api.execute_kw(database,uid, password, 'product.template', 'search_count', [[]])
print(f'count: {product_count}')
```

The final empty parameter is a required filter that you can use to filter the results. You saw above that the filter parameter was left as an empty nested listed to show that no filter is applied.

```py
# count items in model
filter = [[['calories', '<', '100']]]
product_count = odoo_api.execute_kw(database,uid, password, 'product.template', 'search_count', filter)
print(f'count: {product_count}')
```

## Insert records

Inserting records requires knowledge of the database that you're trying to insert into. Once you know this, you can create a record as a nested dictionary and use the api's `execute_kw` method with the `create` keyword

```py
record = [{
    'name': meal_name,
    'calories': calories,
    'categ_id': categ_id
}]
inserted_record = odoo_api.execute_kw(database,uid, password, "product.template", 'create', record)
print(f'inserted record: {inserted_record}')
```

With this logic, we can use an if statement to search if this record is already in the database.

```py
product_id = odoo_api.execute_kw(database,uid,password,'product.template','search',filter)
        if not product_id:
            record = [{
                'name': meal_name,
                'calories': calories,
                'categ_id': categ_id
            }]
            inserted_record = odoo_api.execute_kw(database,uid, password, "product.template", 'create', record)
            print(f'inserted record: {inserted_record}')
        # if the product already exists, we want to update the record
        else:
            ...
```

## Update Records

In the else clause, we'll update the proper record

```py
if not product_id:
    record = [{
        'name': meal_name,
        'calories': calories
    }]
    inserted_record = odoo_api.execute_kw(database,uid, password, "product.template", 'create', record)
    print(f'inserted record: {inserted_record}')
# if the product already exists, we want to update the record
else:
    record = {
        'name': meal_name,
        'calories': calories
    }
    odoo_api.execute_kw(database,uid, password, "product.template", 'write', [product_id, record])
    updated_record = odoo_api.execute_kw(database,uid, password, "product.template", 'name_get', [product_id])
    print(f'updated record: {updated_record}')
```

Notice that we need to search for the record after we update it