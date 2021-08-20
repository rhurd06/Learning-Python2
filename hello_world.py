from flask import Flask
app = Flask(__name__)

# to get it to run:
# FLASK_APP= hello_world.py (filename) flask run

# to set a new environment (for debugging & automatic reload)
# FLASK_APP= hello_world.py FLASK_ENV=development


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/french")
def bonjour_world():
    return "Bonjour, World!"


@app.route("/name/<name>")
def hello_name(name):
    return f"Hello, {name}"
