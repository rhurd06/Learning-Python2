from flask import Flask, render_template
app = Flask(__name__)

# to get it to run:
# FLASK_APP= hello_world.py (filename) flask run

# to set a new environment (for debugging & automatic reload)
# FLASK_APP=hello_world.py FLASK_ENV=development flask run


@app.route("/")
def hello_world():
    # return "Hello World!"
    name = "Robyn"
    return render_template("index.html", name=name)


@app.route("/french")
def bonjour_world():
    return "Bonjour, World!"


@app.route("/name/<name>")
def hello_name(name):
    return f"Hello, {name}"
