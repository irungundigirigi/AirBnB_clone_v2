#!/usr/bin/python3
"""
Flask web application with two routes
"""
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
