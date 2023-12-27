#!/usr/bin/python3
"""
Flask web application with two routes
"""
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """ return 'Hello HBNB!' at route / """
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    """ return "HBNB" at route /hbnb """
    return "HBNB"

@app.route('/c/<string:s>')
def c(s):
    """ display "C" followed by value of text variable, replaces "_" with underscore """
    str = s.replace("_", " ")
    return "C {}".format(str)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
