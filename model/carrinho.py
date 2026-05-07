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

def inserir_item(usuario,  cod_produto, quantidade=1):

    conexao, cursor = conectar()

    cursor.execute("""SELECT cod_carrinho FROM carrinhos
                   where usuario = %s
                   AND finalizado = 0
                   limit 1;
                   
                   """, [usuario])

    resultado_carrinho = cursor.fetchone()

    if resultado_carrinho:
        cod_carrinho = resultado_carrinho["cod_carrinho"]
    else:
        cursor.execute("""
                        insert into carrinhos (usuario)
                        values (%s)

                        """, [usuario])
    
    codigo_carrinho = cursor.lastrowid

    cursor.execute("""
                    insert into itens_carrinho
                        (cod_carrinho, cod_produto, quantidade)
                    values
                        (%s, %s, %s)
                    """,
                    [cod_carrinho, cod_produto, quantidade])

    conexao.close()

    return resultado_carrinho