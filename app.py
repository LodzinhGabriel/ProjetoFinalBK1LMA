from flask import (Flask, render_template, request)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("inicial.html")

@app.route("/contato", methods=["GET", "POST"])
def contato():
    return render_template("contato.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")
    
@app.route("/produtos/", methods=("GET", ))
def produtos(pesquisa = None):
    return render_template("produtos.html")

@app.route("/compra/<string:produto>")
def compra(produto = None):
    return render_template("compra.html")