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


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    '''directs to the home page'''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text="is cool"):
    '''display Python followed by the value'''
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    '''display n followed by the value'''
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    '''display a HTML page only if n is an integer'''
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n=None):
    """display a HTML page only if n is an integer
    """
    if isinstance(n, int):
        if n % 2:
            result = "odd"
        else:
            result = "even"
        return render_template("6-number_odd_or_even.html", n=n, result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
