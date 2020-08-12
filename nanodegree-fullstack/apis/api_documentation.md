## API Documentation Best Practices

* Intro
    * What is the purpose of the api
* Getting Started
    * Base url
    * Auth headers or api keys that need to be included
* Error
    * What the expected error messages
        * What is a deeper dive into those expected error messages
    * What art the expected error codes
* Resources
    * Endpoints organized by collection
        * For example, we list Customers as a resource and then within that customer resource we may have endpoints such as the following:
            * GET `/api/customers`
            * GET `/api/customers/<customer_id>`
            * POST `/api/customers`
            * PATCH `/api/customers/<customer_id>`
            * POST `/api/customers/<customer_id>/notes`
            * Even though notes will belong to customers primarily, if we're attempting to edit/get/delete certain notes, we should list notes as a resource because notes should have a unique id
                * GET `/api/notes/<note_id>`
                * PATCH `/api/notes/<note_id>`
                * DELETE `/api/notes/<note_id>`
                * Yes, you may use `customer_id` and `note_number` to be a composite key, but I would consider this bad practice. It's a lot less confusing to have `note_id` as a primary key
    * Each of these endpoints should have a sample request (what our api expects to receive and parse) along with expected format
    ```json
    {
        'customer_id': int
    }
    ```
    ```json
    {
        'customer_id': 1
    }
    ```
        * **BONUS**: Include how to format this response in CUrl
            * `curl -X GET http://localhost/api/customer/1
    * Each of these endpoints should also have a sample response along with expected format
    ```json
    {
        'customer_name': string
    }
    ```
    ```json
    {
        'customer_name': 'Jimbob'
    }
    ```
    * Each endpoint should include the expected http status codes as well

## Project Documentation Best Practices

API documentation is great for describing how to technically use the project. For for someone looking to contribute or even for yourself after taking a break from the project, it will also be useful to some overall project documentation. The following are some of the best practices for a readme.

* Intro
    * Project Title
    * Description of Project
    * Motivation and need for project
        * Even if it's a project just for practice and fun, put that in there
    * Screenshots
* Getting Started
    * Any dependencies needed
    * How to install the project
        * There may be separate instructions for the frontend vs. the backend
* Contributing
    * How to install a local environment of the project
    * How to deploy your project locally
    * How to run tests
    * How to submit pull requests (if applicable)
    * link to the api reference docs
* Code style guide
    * For example, if you're using python, you may be following a certain PEP
    * Camel casing vs. snake casing
* Credits
    * Yourself
    * contributors
    * library authors
* Acknowledgement
    * Any specific people that helped test or submit issues or gave the motivation for the project

The key with a readme is that you want to be able to give the docs to another developer and, without needing to speak with the developer, enable them to be able to work on the project