#!/usr/bin/python3
"""Starts a web application"""
from os import environ\
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/maze/', strict_slashes=False)
def maze():
    """do we really need the python part to make the maze run?"""
    return render_template('maze.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
