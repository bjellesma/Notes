The CRUD models maps to the following:

|| SQL Statement | SQLAlchemy Code
|---|---|---|
| Create | Insert | `db.session.add(user)` |
| Read | Select |  `User.query.all()` |
| Update | Update | `user.foo = 'new value'` |
| Delete | Delete | `db.session.delete(user)` |

# MVC (Model View Controller)

## Model
Manage data and business logic of application. For example, I usually refactor my database representations under a `models` folder. 

Changes to the database schema would fall under the category of editing the models of our application

In SQLAlchemy, `Todo.query.all()` would be seen as code that accomplishes this because it references data from a database.

## View

Handles display and representation logic. This would commonly be what a user sees. In flask applications, these can commonly be as the templates.

In SQLAlchemy, `<h1>My Todo App</h1>` would be seen as code that accomplishes this because it is HTML

## Controller

Allows models and views to communicate with one another. This can be referred to as **control logic**. In flask applications, these are the routes. Our route is telling us what to display to the user as well as what data from the model to interact with.

In SQLAlchemy, `render_template('index.html', data=data)` would be seen as code that accomplishes this because it tells the app what to display to the user as well as what data from the model to use.

## Summary

![MVC Diagram](images/mvc_diagram.png)

The MVC design paradigm is a useful method for thinking about how to architect our application as well as locate which part of the application the bug is affecting.

For example, if we wanted to add to our application to allow for user input, we might use the following logic

![MVC User Input](images/mvc_user_input.png)

# Getting user data in Flask

Sending data as a request to a server is typically done by creating a form in html

```html
<form action="action_page.php" method="post">
  <div class="imgcontainer">
    <img src="img_avatar2.png" alt="Avatar" class="avatar">
  </div>

  <div class="container">
    <label for="uname"><b>Username</b></label>
    <input type="text" placeholder="Enter Username" name="uname" required>

    <label for="psw"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="psw" required>

    <button type="submit">Login</button>
    <label>
      <input type="checkbox" checked="checked" name="remember"> Remember me
    </label>
  </div>

  <div class="container" style="background-color:#f1f1f1">
    <button type="button" class="cancelbtn">Cancel</button>
    <span class="psw">Forgot <a href="#">password?</a></span>
  </div>
</form>
```

The `action` attribute describes where the data is to be sent while the `method` attibute describes how the data is to be sent. We reference the data on our server by using the `name` attribute on `input` elements.

HTML forms are only able to send GET and POST requests by themselves. We'll need to use AJAX to use other HTTP verbs.

## Synchronous HTTP Requests

**Synchronous** requests are where the user sends data to a server and waits for a response to refresh the page. In these requests, the server will dictate how the data is to be handled. These are generally noticed in practice when there is a page refresh that occurs as a result of the request.

There are three commonly used ways of getting user data in a flask app.

* request.args
    * This is sending the data as **query parameters** so that the url looks like this: `/foo?field=value&field2=value2`
    * The data is attached as a dictionary to `request.args` and we retreive the data as `request.args.get(field)`
    * The upside is that this is a quick and easy way to get user input to a server
    * The downside is that this is not the most secure way if you are sending usernames and passwords
    * Another downside is that if you have a lot of data, this is not very efficient.
* `request.form`
    * accomplished by sending **POST data** from an application
    * The data comes in to our server as a dictionary on `request.form` and we retrieve it in Flask with code similar to `request.form.get('username')`
* Setting the data type of the request to `application/json`
    * This is a more modern technique of getting user data
    * The data from the request is attached to `request.data`. We must use the json library and retrieve the data of a request as 
    ```py
    import json
    data = json.loads(request.data)
    ```

## Asynchronous HTTP Requests

**Asynchronous** Requests are where the users send data and when a response is received, the data is given to the client to update the web page. This all happens without any refresh of the page occurring. These requests require the client to dictate how to use the data. This is a more popular approach when designing apps that require real time data.

Implementation of Asynchronous requests are usually done through a javascript library such as **axios** or **jquery**. There are different different ways that these requests are handled under the hood.

### XMLHttpRequest (XHR)

This is an older implementation but is still used with jquery. The following is a snippet of code to use this without a library

```js
// Create XHR object
var xhttp = new XMLHttpRequest();
// Retrieve data from DOM
description = document.getElementById("description").value;
// Open a connection with the data
xhttp.open("GET", "/todos/create?description=" + description);
// Send the data
xhttp.send();
```

After making the request, you would use code similar to the following to process the results of the request

```js
xhttp.onreadystatechange = function() { 
    // readyState = 4 just indicated that the server was ready
    if (this.readyState === 4 && this.status === 200) { 
      // on successful response
      console.log(xhttp.responseText);
    }
};
```

### Fetch Object

This is a more modern (ES2015) way to implement AJAX request. The following is an example of a fetch request:
```js
fetch('/my/request', {
  method: 'POST',
  body: JSON.stringify({
    'description': 'some description here'
  }),
  headers: {
    'Content-Type': 'application/json'
  }
});
```

Notice that we're adding header `'Content-Type': 'application/json'`. This tells the server that we can accept json and will parse it server side. In Flask, this parsing can be accomplished server side like so:

```py
    import json
    data = json.loads(request.data)
```
Fetch is supported natively in javascript

# Database Sessions

If a commit to the database fails, we will want to rollback the session to avoid any potential implicit commits done by the database on closing the connection. Remember that it is good practice to close the connection at the end of every session used in a controller so that we may return the connection back to the connection pool.

For example, when creating an object in our TODO list database, we may want error handling similar to the following code:

```py
try:
    new_task = Todo(description=task_description)
    db.session.add(new_task)
    db.session.commit()
except:
    db.session.rollback()
    print(sys.exc_info)
finally:
    db.session.close()
```