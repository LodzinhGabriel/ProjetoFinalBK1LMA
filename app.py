from flask import (Flask, render_template, request)

app = Flask(__name__)

app.route("/")
def index():
    return "<h1>Página inicial<h1>"