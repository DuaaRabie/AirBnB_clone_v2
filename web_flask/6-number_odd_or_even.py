#!/usr/bin/python3
""" Flask App Module """
from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)
app.config['strict_slashes'] = False


@app.route('/', strict_slashes=False)
def Hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    return f"C {escape(text.replace('_', ' '))}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    return f"Python {escape(text.replace('_', ' '))}"


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    try:
        int(n)
        return f"{n} is a number"
    except ValueError:
        return "Not a number", 404


@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    try:
        int(n)
        return render_template("5-number.html", n=n)
    except ValueError:
        return "Not a number", 404


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def odd_or_even():
    try:
        int(n)
        return render_template(
                "6-number_odd_or_even.html", n=n)
    except ValueError:
        return "Not a number", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
