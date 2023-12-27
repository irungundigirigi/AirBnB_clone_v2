#!/usr/bin/python3
"""
Flask web application with two routes
"""
from flask import Flask, render_template
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
    string = s.replace("_", " ")
    return "C {}".format(string)

@app.route('/python', strict_slashes=False)
@app.route('/python/<string:s>')
def python(s="is cool"):
    """ /python/<text>: display "Python" followed by value of text - default text: "is cool" """
    string = s.replace("_", " ")
    return "Python {}".format(string)

@app.route('/number/<n>')
def number(n):
    """ /number/<n>: display "n is a number" only if n is an integer """
    try:
        n = int(n)
        return "{} is a number".format(n)
    except:
        abort(404)

@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', num=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
