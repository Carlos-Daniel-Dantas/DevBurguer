 async function mostrarcarrinho() {
    const reesposta = await fetch("/api/get/carrinho")

    if (!reesposta.ok) {
        alert("ERRO AO CARREGAR CARRINHO!")
    }
    else {
        const dados = await reesposta.json()

        const carrinho = document.querySelector("#carrinho")

        carrinho.innerHTML = "";
        let total = 0

        for (let dado of dados) {

            

            total += dado.preco

            let linha = `   <img src= "${dado.foto}" alt="Classic Dev" class="card__image"/>
                            <div>
                                <div class="card__body">
                                    <h3 class="card__title">${dado.produto}</h3>
                                    <p class="card__description"> ${dado.descricao} </p>
                                <div class="card__footer">
                                    <span class="card__price">R${dado.preco}}</span>
                                    <button class="button button--small"><a href="/detalhes_produto/${ dado.codigo }">Comprar</a></button>
                                </div>
                            </div>`

            carrinho.innerHTML += linha
        }
        document.querySelector(".cart-item__price").textContent = "R$" + total
    }
}

mostrarcarrinho()

async function inserirItemCariinho(cod_produto, quantidade=1) {
    const resposta = await fetch("/api/post/item_carrinho",
                                    {
                                        method:"POST",
                                        headers:{
                                                    "Content-Type": "application/json"
                                                },
                                        body: JSON.stringify(

                                                                {
                                                                "cod_produto" :cod_produto,
                                                                "quantidade" : quantidade
                                                                }
                                                            )
                                    }

                                 )

    if (resposta.ok)
    {
        alert("Erro ao inserir Item")
    }

    mostrarcarrinho()

}