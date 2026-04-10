from flask import Flask, render_template
from model.produto import capturando_produtos, capturando_destaques, capturando_produto

app = Flask(__name__)

@app.route("/")
def pagina_principal():

    produtos = capturando_produtos()
    destaques = capturando_destaques()

    return render_template("index.html", produtos = produtos, destaques = destaques)




@app.route("/pagina2/<codigo>")
def pagina_pagina2(codigo):

    recuperar_produto = capturando_produto(codigo)

    return render_template("pagina2.html", recuperar_produtoproduto = recuperar_produto)


if __name__=="__main__":
    app.run(debug=True)