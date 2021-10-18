#!/usr/bin/env python3
# by jesse
from flask import Flask
from flask import render_template
from flask import request
import groceries_db
import logging as log
import os
import sys

# these are global configs
log.basicConfig(stream=sys.stderr, level=log.INFO)
log.info("logging config loaded")
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def grocery_submit():
    if request.method == 'POST':
        # get grocery from post
        grocery = request.form.get('inputGrocery')
        log.info(f"received grocery name: {grocery}")
        # add new grocery to db
        add_new_grocery = groceries_db.add_new_grocery(grocery)

    # run this regardless of post success
    all_groceries = groceries_db.get_all_groceries()
    log.info("received grocery collection response: {0}".format(all_groceries))
    return render_template('index.html', groceries=all_groceries)


@app.route("/about")
def about():
    """
    our about page and why we did this :3
    """
    log.info("Reached about")
    return render_template('about.html')
