#!/usr/bin/env python3
# by jesse
from flask import Flask
from flask import render_template
import logging as log
import os
import sys

# these are global configs
log.basicConfig(stream=sys.stderr, level=log.INFO)
log.info("logging config loaded")
app = Flask(__name__)


@app.route("/")
def welcome():
    """
    defaults to sad patrick because I don't know what to put here yet
    """
    log.info("Reached index")
    return render_template('index.html')


@app.route("/about")
def about():
    """
    our about page and why we did this :3
    """
    log.info("Reached about")
    return render_template('about.html')
