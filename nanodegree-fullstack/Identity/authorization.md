After verifying who the user is, we also want to make sure that they are **authorized** or have the proper permission. Permissions might be defined in the following two table system where a role (id) on the users table will be a foreign key to a roles table. The roles table would typically contain permissions in a key value pair seperated by a colon.

![Permissions Table](./images/permissions_table.png)

If using a JWT, a permissions object may be included within the payload of a JWT. For example, the payload of the JWT `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiSm9obiBEb2UiLCJyb2xlIjoicGhvdG9ncmFwaGVyIiwicGVybWlzc2lvbnMiOlsicG9zdDppbWFnZSIsImVkaXQ6aW1hZ2UiLCJnZXQ6aW1hZ2UiXX0.JxxxdRl8_FIAr76njWQwB2UC48irjWvmBHcLVp81qdk` (use [jwt.io](https://jwt.io) to decode)is 

```js
{
  "name": "John Doe",
  "role": "photographer",
  "permissions": [
    "post:image",
    "edit:image",
    "get:image"
  ]
}
```

Watch [https://www.youtube.com/watch?time_continue=161&v=Rj4AAMjynj0&feature=emb_logo](https://www.youtube.com/watch?time_continue=161&v=Rj4AAMjynj0&feature=emb_logo) for a detail example of how to add permissions to your JWT. Decoding the access token that you get from logging in will give the permissions in the payload.

Now that we've setup role based permissions, we can refactor the `requires_auth` decorator to include an additional function to check permissions:

```py
def requires_auth(permission=''):
    def requires_auth_decor(f):
        @wraps(f)
        def wrapper(*args,**kwargs):
            payload = get_auth_header()
            # Check that the user has the proper permissions
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)
        return wrapper
    return requires_auth_decor
```

Notice that we're making a new call to a check_permissions fuction which we'll define as below:

```py
def check_permissions(permission, payload):
    #if no permissions are included in our payload, abort as a 400
    if 'permissions' not in payload:
        abort(400)

    # if the permission that we require is not in the payload, we'll abort with a 403
    if permission not in payload['permissions']:
        abort(403)

    return True

```

This function will use the payload of the jwt to see if the permission exists in the payload of that jwt. We'll now call the requires auth decorator as the following

```py
@requires_auth('delete:images')
```

Here, we're saying only users that have the delete:images permission will be allowed to access this route. If they don't have this permission, they'll receive a 403 error.

# Frontend JWTs

It's important to validate JWTs on the backend as this is the most secure method. Rather than thinking of validating JWTs on the frontend as added security, think of it as a way to improve the UX. We know that a user can simply turn off javascript but by using JWTs on the frontend to validate roles, we can take away buttons and add buttons. By using the boilerplate javascript provided by auth0, we can insert the javascript into a dev tools console:

![ParseJWT](./images/parse_jwt_frontend.png)