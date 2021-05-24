from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/request/<url>")
def fetch(url):
    return "{}".format(url)
