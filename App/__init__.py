import os
import flask
import requests
import json

from flask import render_template
from flask_bootstrap import Bootstrap
from App.translationService import executeStreaming

app = flask.Flask(__name__)

@app.route('/')
def index():
    # executeStreaming()
    return render_template('index.html')

Bootstrap(app)
