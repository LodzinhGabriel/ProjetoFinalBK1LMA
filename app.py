from flask import (Flask, render_template, request)

app = Flask(__name__)

class CRUD:
    caminho = "produtos.json"
    def __init__(self, modo) -> None:
        self.modo = modo

    def set_nome(self, nome):
        set.nome = nome

    def conexão(self, dados=None):
        with open(self.caminho, self.modo, encoding='utf8') as file:
            if self.modo == "+w":
                file.write(dados)
            elif self.modo == "+r":
                return file.read()

@app.route("/")
def index():
    return render_template("inicial.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/contato/email", methods=["GET", "POST"])
def contatoemail():
    return render_template("contatoemail.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")
    
@app.route("/produtos/", methods=("GET", ))
def produtos(pesquisa = None):
    return render_template("produtos.html")

@app.route("/compra/<string:produto>")
def compra(produto = None):
    return render_template("compra.html")
    
@app.route("/erro404")
def erro():
    return render_template("pagina404.html")

@app.route("/carrinho")
def carrinho():
    return render_template("carrinho.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/novaconta")
def novaconta():
    return render_template("novaconta.html")