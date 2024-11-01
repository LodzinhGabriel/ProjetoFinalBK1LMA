from flask import (Flask, render_template, request)

app = Flask(__name__)

app.route("/")
def index():
    return "<h1>Página inicial<h1>"

app.route("/contato", methods=("POST", ))
def contato():
    return "<h1>Contato<h1>"

app.route("/sobre")
def sobre():
    return "<h1>Sobre<h1>"
    
app.route("/produtos/", methods=("GET", ))
def produtos(pesquisa = None):
    return "<h1>Produtos<h1>"

app.route("/compra/<string:produto>")
def compra(produto = None):
    return "<h1>Produtos<h1>"