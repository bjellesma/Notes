Rather than sending along a username/password combo with every request, it is more common nowadays to use an authentication token. This is done to reduce the sensative information sent in a request.
![Token Based Authentication](../images/token_based_authentication.png)

However, we usually implement a third party auth service to do this.
![Third Party Autentication](../images/third_party_authentication.png)

There are two status codes associated with authentication/authorization:

* 401 Unauthorized - The client must pass authentication before access to this resource is granted. The server cannot validate the identity of the requested party.

* 403 Forbidden - The client does not have permission to access the resource. Unlike 401, the server knows who is making the request, but that requesting party has no authorization to access the resource.

# Different Ways on Signing in

## Single Sign On

SSO is where we are trusting a third party to provide credentials on our behalf. The following is a diagram showing the relationship of this:

![SSO Diagram](../images/SSO_Diagram.png)

These can be implemented like the following screen

![SSO Example](../images/sso_example.png)

## Multi Factor Authentication

MFA assumes that you have a secondary way to authenticate. The most common way that this is done is through a text message like so:

![MFA](../images/mfa.png)

In looking at a diagram of how it can be implemented, the server is tasked with sending a code to a seperate device which the user will then enter on the frontend

![MFA diagram](../images/mfa_diagram.png)

MFA can also be implement with what's called a **decaying temporal algorithm**. In this approach, the other device will generate a code based on a timestamp and send it to the server. Only the device and server know the code at any given time and the code is only good for a certain amount of time before a new code is generated. This is most commonly implemented in a google authenticator app.

![MFA Temporal](../images/mfa_temporal.png)

## Passwordless

Taking multifactor authentication a step further, you can use a **passwordless** design to remove the complexity (and often users make bad password choices). Like MFA, a code is still sent to an external device that you'll use to authenticate with the service.

![Passwordless](../images/passwordless_diagram.png)

As you can see, besides users choosing bad passwords, developers can also implement a password comparison incorrectly so we are removing the password step and just sending an authorization code to a device. The following example shows Google sending a code to your device to unlock it.

![Passwordless Example](../images/passwordless_example.png)

These links might also be referred to as **magic links**

## Biometrics

**Biometrics** are, in theory, the best form of authentication as you won't be able to copy someone's body part. However, these can be poorly designed on IOS as the tech is still fairly new and can be faked with as little as a photocopy.

## Summary

Ultimately, the method of authentication chosen for an application depends on the level of risk associated with the application. The more complexity that an app introduces, the better the change of poor implementation/design. This is a fact to keep in mind when choosing an authentication system.

# Deletegation of auth

As systems grow and scale, it becomes very difficult to maintain current codebases, this is referred to as **technical debt**. A solution to this is **microservices** where different parts of your system are delegated to different architectures. For example, in the following diagram, we use four microservices to delegate the responsibility of our application. The important thing to keep in mind is that these services have minimal interaction.

![Microservices](../images/microservices.png)

Notice that we're making authentication into its own self contained service as oposed to the following architecture which has auth services listed in each microservice.

![Microservices](../images/microservices_incorrect.png)

**Delegation of authorization** makes the following diagram more likely. Notice that the change is that our frontend serivce will now login to the third party auth service which issues a token that we can use on behalf of the user. The API server will also talk to the auth service to make sure that the JWT is authentic and hasn't been tampered with. This takes complexity out of the hands of developers to reduce risk.

![Auth Delegation](../images/auth_delegation.png)

While deletation of authorization can reduce security risks, keep in mind that the auth is only as strong as the vendor. If you're not using a common vendor such as Amazon Web Services, Google Firebase, or Okta, you may need to ask for their security practices to ensure the security of your users' credentials. Authorization is also not the only vector of attack and the rest of your system will need to be properly architected as well.

For practice, we're using an Auth0 service so that users are redirected to auth0's servers to login. We need to be sure to specify allowed callback URLs as well as an application login URI and application logout URI. We will also set the JWT expiration time. Ideally, this should be a small amount of time because we can silently refresh the token on page loads.

For my application of image service, for example, my test auth url is `https://dev-cpb64ukj.us.auth0.com/authorize?audience=image&response_type=token&client_id=CLIENT_ID&redirect_uri=https://127.0.0.1:8080/login-results` where CLIENT_ID can be found on the homepage of your app. This is the result of this call:

![Auth0 URL](../images/auth0_url.png)

Signing up or logging to this will give back a url with an access token as a query param. We can use this token in `jwt.io` to decode and read the information.

The auth0 dashboard also makes it easy to bring in other providers such as facebook and setup sms.

# JSON Web Tokens

## Intro

JWTs are stateless meaning that the API server sends the code to the auth service once and that's the only communication they have.

![JWT stateless](../images/jwt_stateless.png)

JWTs are also scalable so, as the demand on the api servers grows, the jwt can be sent to any api server and be assured of the identity.

![JWT scalable](../images/jwt_scalable.png)

JWTs are perfect for a microservices architecture because, no matter where the JWT is sent to, we can be confident in the identity.

![JWT microservices](../images/jwt_microservices.png)

As long as the secret or public key to encode the JWT is sufficiently complex, the encoded version of the jwt will be difficult to change or manipulate data.

## Data of a JWT

A JWT follows the scheme of `header.payload.signature`. When the JWT is encoded, it may look closer to this:

```js
adfsafdsadfddsafdsfdsfda.adfdsafdsafsafddsdsfsdafsfds.adfasfdsafdsdsfsdffs
```

Notice that the dot seperators are still present to follow the scheme `header.payload.signature`

![JWT Payload](../images/jwt_payload.png)

It's important to not that the payload of JWT is not secret and can easily be decoded on [jwt.io](jwt.io). This is because the JWT payload uses **base64 encoding** which is two way meaning it it can encoded and decoded on the fly. Therefore, we should not use JWT payloads as a place to store sensitive information. Typically, we use the JWT payload to store information such as who made the request.

![JWT Header](../images/jwt_header.png)

The JWT header is also base 64 encoded and typically just contains information about the algorithm used to encode the JWT signature.

![JWT signature](../images/jwt_signature.png)

The signature is done using a one way algorithm because this is something that we're using to encode a secret. We'll take the base 64 versions of our header and payload, and combine it with our secret to create the signature. The server will also perform this hashing when it receives the base64 header and payload as well as the secret which it also has access to. If the hashing on the server matches the signature of the JWT that was sent, then we can trust the information.

Keep in mind that anyone can still read the header and payload parts of the JWT as they're only base64 encoded.

The following is a simple implementation of jwt in python:

```py
import jwt
# init data
payload = {'park':'madison square'}
algo = 'HS256' #HMAC-SHA 256
secret = 'learning'
# encode
encoded_jwt = jwt.encode(payload, secret, algorithm=algo)
print(encoded_jwt)
# b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXJrIjoibWFkaXNvbiBzcXVhcmUifQ.ctfBq05cMuRy_INzkTFeiKVLxb9RH9y4ZwD2HKFrN6g'

# decode
decoded_jwt = jwt.decode(encoded_jwt, secret, verify=True)
print(decoded_jwt)
{'park': 'madison square'}
```

If we really wanted, notice that we can use simple base64encoding to get the payload of the jwt

```py
import base64
# We need to do a little extra work and know how JWTs work but we can decode it without the secret
# more reason to not encode sensative information in here
decoded_base64 = base64.b64decode(str(encoded_jwt).split(".")[1]+"==") 
print(decoded_base64)
# b'{"park":"madison square"}'
```

# LocalStorage

![LocalStorage](../images/localstorage.png)

LocalStorage is utilized by the browser to remember certain things that the website chooses for us to remember.

* LocalStorage is **domain specific** meaning that there is now way for google.com to access any localstorage for udacity.com and vise versa.
* LocalStorage is **persistent** and remains in memory until the user clears the browser or the storage expires.
* LocalStorage is accessible through javascript for applications
* LocalStorage only stores string content, not images or other media and it is only meant for smaller strings

We can easily set the localstorage in javascript with something like

```js
localstorage.setItem("token", jwt)
```

Similarly, we will use the following to retreive the jwt:

```js
jwt = localstorage.getitem("token")
```

## LocalStorage Security

We can also use `localStorage` in the dev tools of a browser to see everything that site has stored on your browser. This inherently isn't an issue because it's all your information, HOWEVER, if the site is vulnerable to **cross-site scripting** (XSS) attacks (users can inject rendered html to the website), this could mean that the jwts for the user could be comprimised. This is something to keep in mind if choosing to store JWTs in localstorage.

### Unsanitized Input

An example of malicious HTML that an attacker might inject in an XSS attack is the following:

![Unsanitized Input](../images/unsanitized_input.png)

As you can see, the people asking the question likely don't intend for this type of response. But we could define something like this and then use an ajax call to send this information to a server. Now, whenever anyone lands on this page, they'll unwittingly give away copies of their access tokens which attackers can now use or sell.

How we mitigate this is we escape or transform any html entities

![Sanitized Input](../images/sanitized_input.png)

### Hosted JavaScript

Sometimes, when using CDNs, a hosted script could be comprimised such as

```html
<script src="http://trendstartup.com/library.js">
```

The only way to know about this kind of attack is to properly vet the vendor of the code before using it.

### Bad packages

It's pretty easy to unknowingly install a compromised package from pip or npm. This remediation for this is to ensure that the developers of the packages are trusted and use security best practices.

### Best Practices

1. Never store truly sensative information such as passwords or social security numbers in JWTs.

Fortunately, if you discover an issue, you can simply change the public key on the server side so that the JWT can no longer authenticate.

2. Make sure the JWTs have a short period until expiration.

It's not difficult to refresh a JWT from our app so expiration shouldn't be a big issue. By having a short expiration time, the attacker will only have a limited amount of time even if they do compromise the JWT.

3. Instead of using localstorage, you can store the data in a cookie with the HTTP Only flag turned on.

By turning this flag on, the data of the cookie is inaccessible to all javascript including our own javascript.