#!/usr/bin/python3
""" Flask App Module """
from flask import Flask
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
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    if isinstance(n, int):
        return f"{n}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
