#!/usr/bin/python3
"""
Starts flask application
"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    ''' prints text variable '''
    result = text.replace('_', ' ')
    return "C {}".format(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
