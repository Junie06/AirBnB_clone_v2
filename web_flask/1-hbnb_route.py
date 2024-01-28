#!/usr/bin/python3
'''starts a Flask web application'''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''directs to the home page'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''directs to the home page'''
    return 'HBNB'


if __name__ = "__main__":
    app.run(host="0.0.0.0", port=5000)
