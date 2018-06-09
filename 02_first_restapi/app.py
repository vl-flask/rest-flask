from flask import Flask
print(__name__)
# Create an app using this `Flask` class
app = Flask(__name__)

# Tell the app what requests it's gonna understand
@app.route('/')
def home():
    return "Hello World!"

app.run(port=5000)
