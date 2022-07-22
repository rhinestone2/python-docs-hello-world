from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/67bc5gA3df32G
def takeover():
           return "Subdomain Takeover by @rhinestonecowboy"
