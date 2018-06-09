# REST Principles

* GET returns HTML or other data.
* Other things too.

REST API:
* A way of thinking how a web server responds to your requests
* It doesn't respond w/ just data
* It responds w/ resources
An example:
* Same endpoint(/item/chair)
* Different verbs (GET, POST (more data), PUT (more data), DELETE)
* Endpoint+verb = resource
 * GET + (/item/chair)
 * POST + (/item/chair)
 * ...

REST is stateless:
* One request can't depend on any other request.
* The server only know about the current request and not any previous requests. Ex:
 * `POST /item/chair` creates an item
 * The server doesn't know about it anymore.
 * `GET /item/chair` goes to the db and checks whether the item is there.
* Another ex:
 * A user logs in to a web app.
 * The web server doesn't know the user is logged in (it's stateless)
 * The web app must send enough data to identify the user _in every reuqest_, or else the server won't associate the request w/ the user.
