from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/request/<url>")
def fetch(url):
    response = requests.get("https://{}".format(url), timeout=5)

    return "{}: {}".format("https://{}".format(url), response.elapsed.total_seconds())


@app.route("/request/<url>/<path>")
def fetch_path(url, path):

    response = requests.get("https://{}/{}".format(url, path), timeout=5)

    return "{}: {}".format("https://{}/{}".format(url, path), response.elapsed.total_seconds())
