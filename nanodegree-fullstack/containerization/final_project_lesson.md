The final project on containerization will consist of building a docker container locally and deploying it to Kubernetes

# Docker

1. Build a simple flask api with the following endpoints
    * GET `/` returns 'Healthy'
    * POST `/auth` returns a JWT based on an email and password as JSON args that the user supplies and returns a JWT based on a secret
    * GET `\contents` returns the decrypted contents of the JWT given a valid JWT

In Addition, the app will use Gunicorn as a Web Server Gateway Interface (WSGI) server. This is because the built-in flask server is sufficient for local development, but it's not production ready. A WSGI server is better equiped to use a production load. The project will also rely on a JWT_SECRET environmental variable


