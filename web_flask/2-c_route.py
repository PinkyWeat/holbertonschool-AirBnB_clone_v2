#!/usr/bin/python3
"""Python Package 1"""
from flask import Flask


app = Flask(__name__)
# create Flask obj referencing self


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text=None):
    return "C " + str(text).replace("_", " ")


# check that's the route + run the app
if __name__ == '__main__':
    app.run(port=5000)
