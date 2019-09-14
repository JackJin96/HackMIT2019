import os
import flask
import requests
import json

from flask import render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from App.translationService import executeStreaming

app = flask.Flask(__name__)

@app.route('/')
def index():
    # executeStreaming()
    return render_template('index.html')

@app.route('/', methods=['POST'])
def startStreaming():
    executeStreaming()
    return redirect(url_for('/'))

Bootstrap(app)
