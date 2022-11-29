#!/usr/bin/python3
"""Python Package 1"""
from flask import Flask

app=Flask(__name__)  # create Flask obj referencing self

@app.route('/', strict_slashes=False)  #
def index():
    return "Hello HBNB!"

if __name__ == '__main__':  #  check that's the route + run the app
    app.run(port=5000)
