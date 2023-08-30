#In this code I aim to attempt to convert my Assessment V3 console-based webapp into a Flask webapp

from flask import Flask

EventManager = Flask(__name__)




# Open the app in the browser when this file is executed
if __name__ == '__main__':
    webbrowser.open_new('http://127.0.0.1:5000/')  # Open the URL in the default browser
    EventManager.run()