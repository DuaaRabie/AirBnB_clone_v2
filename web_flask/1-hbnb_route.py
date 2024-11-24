#!/usr/bin/python3
""" Flask App Module """
from flask import Flask


app = Flask(__name__)
app.config['strict_slashes'] = False


@app.route('/', strict_slashes=False)
def Hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
