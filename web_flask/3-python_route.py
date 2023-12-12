#!/usr/bin/python3
"""Start a flask web app"""

from flask import Flask
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


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
