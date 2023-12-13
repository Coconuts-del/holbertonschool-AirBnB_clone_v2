#!/usr/bin/python3
"""Start a flask web app"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    """Return string when route queried"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Return string when route queried"""
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """return text reformatted"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """return text depending optional variable """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:nbr>')
def number(nbr):
    """return nbr is a number only if nbr is integer"""
    return str(nbr) + " is a number"


@app.route('/number_template/<int:n>')
def number_template(n):
    """retrieve HTML page only if n is integer"""
    path = '5-number.html'
    return render_template(path, n=n)


@app.route('/number_odd_or_even/<int:n>')
def number__odd_or_even(n):
    """retrieve HTML page only if n is integer
       and display if it is odd or even
    """
    path = '6-number_odd_or_even.html'
    return render_template(path, n=n)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
