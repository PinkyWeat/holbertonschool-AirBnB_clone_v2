#!/usr/bin/python3
"""Python Module"""
from models import storage
from flask import Flask, render_template


app = Flask(__name__)
# create Flask obj referencing self
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear_down(exit):
    #  removes current SQLAlchemy Session
    storage.close()


@app.route('/states')
def states_list():
    # lists states
    states = storage.all("State")
    return render_template('8-cities_by_states.html', states=states, id=None)


@app.route('/states/<id>')
def state_id(id):
    states = storage.all("State")
    for state in states.values():
        if state.id == id:
            return render_template('9-states.html', states=state, id=state.id)
    return render_template('9-states.html', state=None)


# check that's the route + run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
