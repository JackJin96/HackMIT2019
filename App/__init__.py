import os
import flask
import requests
import json

from flask import render_template, redirect, url_for, request
from flask_socketio import SocketIO, send, emit
from flask_bootstrap import Bootstrap
from App.translationService import executeStreaming

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'hackmit2019'
socketio = SocketIO(app)

@app.route('/')
def index():
    # executeStreaming()
    print('34556')
    return render_template('index.html')

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received my event: ' + str(json))
    # socketio.emit('my data', 'connection succeeded')
    executeStreaming(socketio)

# @app.route('/', methods=['POST'])
# def startStreaming():
    # executeStreaming(socketio)
    # socketio.emit('my data', 'some data')
    # return redirect(url_for('index'))
    # return "Nothing"

Bootstrap(app)

if __name__ == '__main__':
    socketio.run(app)
