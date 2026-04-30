from database.conexao import conectar

def recuperar_carrinho( usuario:str )-> list:

    conexao, cursor = conectar()

    cursor.execute("""
                    select carrinhos.cod_carrinho,
                        carrinhos.usuario,
                        carrinhos.data,
                        carrinhos.finalizado,
                        produtos.produto,
                        itens_carrinho.quantidade,
                        produtos.preco,
                        produtos.foto
                    From carrinhos
                    inner join itens_carrinho on carrinhos.cod_carrinho = itens_carrinho.cod_carrinho
                    inner join  produtos on produtos.codigo = itens_carrinho.cod_produto
                   WHERE carrinhos.usuario = %s;
                   """, [usuario])

    produto = cursor.fetchall()

    conexao.close()

    return produto