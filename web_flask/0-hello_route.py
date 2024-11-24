#!/usr/bin/python3
""" Flask App Module """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False) 
def Hello():
    return "Hello HBNB!"
