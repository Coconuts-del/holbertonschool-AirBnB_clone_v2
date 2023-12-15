#!/usr/bin/python3
"""Start a web app"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states')
def states():
    """Display a HTML page of state"""
    path = '9-states.html'
    states = storage.all(State).values()
    return render_template(path, states=states)


@app.route('/states/<id>')
def states_list(id=None):
    """Render template with id states"""
    path = '9-states.html'
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template(path, state=state, id=True)
    return render_template(path, not_found=True)


@app.teardown_appcontext
def app_teardown(arg=None):
    """Clean-up session"""
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
