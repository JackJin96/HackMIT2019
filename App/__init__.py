import os
import flask
import requests
import json

from flask import render_template
from flask_bootstrap import Bootstrap

app = flask.Flask(__name__)

Bootstrap(app)

@app.route('/')
def index():
  return render_template('index.html')