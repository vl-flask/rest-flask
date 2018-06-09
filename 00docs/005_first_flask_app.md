# First Flask App

Flask apps are built around requests and responses.  

## Minimum Flask App
Create a file for your app.
```
touch app.py
```
Create a minimum Flask app.
```python
from flask import Flask
# Create an app using this `Flask` class
app = Flask(__name__)
# Specify the endpoint and the view.
@app.route('/')
def home():
    return "Hello World!"
# Specify the port
app.run(port=5000)
```
Access `localhost:5000`.

## Web Server and Requests / Responses
What is a web server. Hardware/software designed to accept the incoming web requests.  
Example of a request (http://www.google.com). Include the VERB (GET), the PATH (/), and the PROTOCOL (HTTP/1.1). There are already attempts to use HTTP v 1.2.
```
GET / HTTP/1.1
Host: www.google.com
```
And then, there's a response.
* An error if the path (/) not found.
* An error if HTTP not supported
* An error if the server is unavailable
* Some HTML code (normal behavior)
* Some text info
* May give you nothing back.
Another ex [Twitter login](https://twitter.com/login):
```
GET /login HTTP/1.1
Host: https://twitter.com
```
What else:
* Going to a page - GET request
* Other things - POST, DELETE, PUT, OPTIONS, HEAD, and more.

## HTTP Verbs
* GET - Retrieve page (GET /item/1)
* POST - Receive data and use it. (POST /item)
* PUT - Make sure something is there (PUT /item)
* DELETE - Remove something (DELETE /item/1)
