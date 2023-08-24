import webbrowser
from flask import Flask, request

# Create a Flask app instance
app = Flask(__name__)

greeted_name = ""


@app.route('/')
def index():
    return """
    <h1>Flask App</h1>
    <p>Enter your name and an additional input:</p>
    <form method="post" action="/greet">
        <input type="text" name="name" placeholder="Enter your name" /><br>
        <input type="submit" value="Submit" />
    </form>
    """


@app.route('/greet', methods=['POST'])
def greet():
    global greeted_name
    name = request.form.get('name')

    if name:
        greeted_name = name
        return f"Hello, {name}! Enter an additional input:<br><form method='post' action='/show_additional_input'><input type='text' name='extra_input'><input type='submit' value='Submit'></form><br><a href='/'>Go back to start</a>"
    else:
        return "Hello, World! <br><a href='/'>Go back to start</a>"


@app.route('/show_additional_input', methods=['POST'])
def show_additional_input():
    extra_input = request.form.get('extra_input')

    if extra_input:
        with open("input_data.txt", "a") as file:
            file.write(f"Greeted: {greeted_name}, Additional Input: {extra_input}\n")
        return f"You entered: {extra_input}<br><a href='/'>Go back to start</a>"
    else:
        return "No additional input provided.<br><a href='/'>Go back to start</a>"


# Open the app in the browser when this file is executed
if __name__ == '__main__':
    webbrowser.open_new('http://127.0.0.1:5000/')  # Open the URL in the default browser
    app.run()
