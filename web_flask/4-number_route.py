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


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def py(text="is cool"):
    return "Python " + str(text).replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def is_num(n):
    return "{} is a number".format(n)


# check that's the route + run the app
if __name__ == '__main__':
    app.run(port=5000)
