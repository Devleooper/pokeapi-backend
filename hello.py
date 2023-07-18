from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Pokeapi!</p>"

@app.route("/test")
def hello_2():
    return "<p> this is a test of a custom path 2 </p>" 