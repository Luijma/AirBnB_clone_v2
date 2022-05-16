#!/usr/bin/python3
"""
Starts flask application
"""


from flask import Flask
from flask import render_template

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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    ''' prints text var '''
    result = text.replace('_', ' ')
    return "Python {}".format(result)


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    ''' prints pyton and text '''
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    ''' returns page '''
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    ''' returns page '''
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
