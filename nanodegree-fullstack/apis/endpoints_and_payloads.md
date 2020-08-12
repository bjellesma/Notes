* Endpoints should be intuitive so that fellow developers have a sense of what the endpoint does. 
    * This is why making sure that you use the correct HTTP method. 
    * I expect that performing a GET request on /api/item/1 will get all information of an item with id 1.
* Use nouns in the endpoint locations rather than verbs
    * example.com/send is a **bad example** because it's non intuitive as to what the endpoint does
    * example.com/tasks is a **good example** because it tells the user that we're working with task objects
* Collections as a resource should be plural
    * example.com/user/task is unclear because we're not sure the user
    * example.com/users/1/tasks is a better example because we know that we're getting task objects
* Endpoints should be no longer than collection/item/collection
    * example.com/users/1/tasks/8/notes is a little lengthy and makes the endpoint difficult to parse
    * assuming 8 is an id for the task in the above exampple, we can just do example.com/tasks/8/notes
        * user id is unnecessary because we already know that task id 8 belongs to user id 1

The following is an example scheme that we might use. This is a very intuitive scheme.

| Resource | Get | Post | Patch | Delete | Notes |
|---|---|---|---|---|---|
|/tasks | get all tasks | create a new task | partially update all tasks | delete all tasks | This endpoint might only allow get and post so that we don't perform inadvertant damage |
| /tasks/1 | get task with id 1 | error because task 1 already exists, if it didn't, we would use /tasks | partial update of task 1 | delete task 1 |
| /tasks/1/notes | get all notes for task 1 | create new notes for task 1 | partial updates of all notes for task 1 | delete all notes of task 1 | again, we may only allow get and post |

## Cross Origin Resource Sharing

The **Same-Origin Policy** says that an application on one webpage cannot access the data on the other webpage unless they are from the same origin. This is a security measure. Let's say that you have spotify on one page which has a couple ads and you have your banking information open on another page, without the same-origin policy, rogue javascript from one of the ads could manipulate our banking information. In summary, CORS is a security mechanism that blocks requests from rogue javascript.

CORS will be triggered from the following

* Different Domains
    * Spotify and your bank
* Different Subdomains
    * example.com and api.example.com will still trigger this policy
* Different Ports
    * example.com and example.com:1234
* Different Protocols
    * http://example.com and https://example.com

CORS will send out an OPTIONS request beforehand on some requests that will get the permission of the browser. Notice that you're still able to get the webpage, that's because this is a simple GET request that doesn't require this policy.

In order for the server to allow access from a trigger of CORS, the server will use one of the following headers:

* Access-Control-Allow-Origin
    * This is a whitelist to allow access for certain websites. For any domain, you will set this to *
* Access-Control-Allow-Credentials
    * If you're using cookies for authentication, you can use this header to tell CORS to check for a cookie
* Access-Control-Allow-Method
    * This is a list of HTTP headers that a server will allow
* Access-Control-Allow-Headers
    * List of request headers that the server will allow. This is particularly useful if you're using custom headers

The following will set up a basic website using flask-cors:

```py
# Import Dependencies
from flask import Flask
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__)
#   CORS(app)
# Notice in this next line that we're passing resources as an optional param saying that every URI with /api/* will be able to come from any origin
    CORS(app, resources={r"*/api/*": {"origins": "*"}})

    # CORS Headers 
    # app.after_request will add headers to the response
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response
    
    @app.route('/messages')
    # cross_origin is a decorator that we'll put on any route where we want to use CORS
    @cross_origin()
    def get_messages():
        return 'GETTING MESSAGES'
```

**TIP**: To send form data via curl, you'd use something like

```bash
curl -X patch -F 'rating=4' http://127.0.0.1:5000/api/books/7
```

Also here is how to send json as the body via curl:

```bash
curl -X post -H "Content-Type: application/json" -d '{"title": "af", "author": "adfasfs", "rating": 5}' http://127.0.0.1:5000/api/books
```

## Error Hanling

Create an error handler as follows:

```py
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False, 
        "error": 404,
        "message": "Not found"
        }), 404
```