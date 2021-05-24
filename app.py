from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/request/<url>")
def fetch(url):
    response = requests.get(url, timeout=30)
    return "{}: {}".format(url, response.elapsed.total_seconds())
