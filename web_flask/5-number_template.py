#!/usr/bin/python3
"""Python Package 1"""
from flask import Flask, render_template


app = Flask(__name__)
# create Flask obj referencing self
app.url_map.strict_slashes = False


@app.route('/')
def index():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def c(text=None):
    return "C " + str(text).replace("_", " ")


@app.route('/python/<text>')
@app.route('/python')
def py(text="is cool"):
    return "Python " + str(text).replace("_", " ")


@app.route('/number/<int:n>')
def is_num(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template_route(n):
    return render_template("5-number.html", variable=n)


# check that's the route + run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
