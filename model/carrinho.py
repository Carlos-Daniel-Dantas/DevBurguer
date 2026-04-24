from database.conexao import conectar

def recuperar_carrinho( usuario:str )-> list:

    conexao, cursor = conectar()

    cursor.execute("""
                    select carrinhos.cod_carrinho,
                        usuarios.usuario,
                        carrinhos.data,
                        carrinhos.finalizado,
                        produtos.produto,
                        itens_carrinho.quantidade,
                        produtos.preco,
                        produtos.foto
                    From carrinhos
                    inner join itens_carrinho on carrinhos.cod_carrinho = itens_carrinho.cod_carrinho
                    inner join  produtos on produto.codigo = itens_carrinho.cod_produto
                   """)

    produto = cursor.fetchall()

    conexao.close()

    return produto