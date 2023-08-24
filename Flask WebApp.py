#In this code I aim to attempt to convert my Assessment V3 console-based webapp into a Flask webapp

from flask import Flask

EventManager = Flask(__name__)

@EventManager.route('/')
def hello():
    return 'Hello World!'
