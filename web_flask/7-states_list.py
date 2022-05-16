#!/usr/bin/python3
''' Starts flask app '''


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.rout('/states_list', strict_slashes=False)
def states_list():
    ''' returns states in DB '''
    all_states = storage.all(State).values()
    return render_template('7-states_list.html', states=all_states)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
