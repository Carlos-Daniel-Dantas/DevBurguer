from flask import Flask, render_template, request, redirect, session, jsonify
from model.produto import capturando_produtos, capturando_destaques, capturando_produto
from model.carrinho import  recuperar_carrinho
from model.usuarios import Usuarios

app = Flask(__name__)

app.secret_key = "banana_loca"

@app.route("/")
def pagina_principal():

    produtos = capturando_produtos()
    destaques = capturando_destaques()

    return render_template("index.html", produtos = produtos, destaques = destaques)

@app.route("/pagina2/<codigo>")
def pagina_pagina2(codigo):

    rcp = capturando_produto(codigo)

    return render_template("pagina2.html", rcp = rcp)

# //======================= LOGIN E CADASTRO FUNÇÕES =========================

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    try:
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        nome = request.form.get ("nome")

        novo_usuario = Usuarios(usuario, senha, nome)
        if Usuarios.cadastrar(novo_usuario):
            return redirect('/')
    except Exception as erro:
        return False

@app.route("/cadastro", methods=["GET"])
def entrar_cadastro():

    return render_template("/login.html")

@app.route("/login/usuario", methods=["POST"])
def pagina_login():
    try:
        usuario = request.form.get("nome")
        senha = request.form.get("senha")

        resultado = Usuarios.logar(usuario, senha)

        session["usuario_logado"] = resultado
        return redirect("/")
    except Exception as erro:
        print(erro)
        return False

# //===========================================================================

@app.route("/api/get/carrinho", methods=["GET"] )
def api_get_carrinho():
    if "usuario_logado" in session:
        usuario = session["usuario_logado"]["usuario"]
        carrinho = recuperar_carrinho(usuario)
        return jsonify(carrinho), 200
    else:
        return jsonify({"message":"Usuário não logado"}), 401




if __name__=="__main__":
    app.run(debug=True)