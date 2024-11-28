from flask import (Flask, render_template, request)
import json

app = Flask(__name__)

class CRUD:
    def __init__(self, modo, caminho) -> None:
        self.modo = modo
        self.caminho = caminho

    def set_nome(self, nome):
        set.nome = nome

    def conexao(self, dados=None):
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

@app.route("/contato-email", methods=["GET", "POST"])
def email(nome = None, email = None, cidade = None, telefone = None, assunto = None, mensagem = None, concluido=None):

    if 'nome' and 'email' and 'cidade' and 'telefone' and 'assunto' and 'mensagem' in request.form:
        nome = request.form.get('nome')
        email = request.form.get('email')
        cidade = request.form.get('cidade')
        telefone = request.form.get('telefone')
        assunto = request.form.get('assunto')
        mensagem = request.form.get('mensagem')



        texto = {
            "nome": nome,
            "email": email,
            "cidade": cidade,
            "telefone": telefone,
            "assunto": assunto,
            "mensagem": mensagem
        }

        conversao = json.bumps(texto)

        crud = CRUD('+w', f'./relatorios/email/{email}.json')
        crud.conexao(conversao)

        concluido = True

        return render_template("contatoemail.html", concluido=concluido)
    else:
        return render_template("contatoemail.html")
    

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")
    
@app.route("/produtos/", methods=("GET", ))
def produtos(pesquisa = None):
    dados = None
    crud = CRUD('+r', './static/assets/json/produtos.json')
    dados = crud.conexao(dados)
    dados = json.loads(dados)

    print(dados)

    return render_template("produtos.html", produtos=dados)

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

@app.errorhandler(404)
def coisa(coisa):
    return render_template("pagina404.html")