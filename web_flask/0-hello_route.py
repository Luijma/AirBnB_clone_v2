#!/usr/bin/python3
"""
Starts flask application
"""


from flask import Flask

app = FLask(__name__)


@app.route('/', strict_slashes=False)
def hellow_world():
    return 'Hello HBNB!'

if __name__ == '__main__'):
    app.run(host='0.0.0.0')
