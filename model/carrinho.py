from database.conexao import conectar

def recuperar_carrinho( usuario:str )-> list:

    conexao, cursor = conectar()

    cursor.execute("""
                    select * from itens_carrinho;
                   """)

    produto = cursor.fetchall()

    conexao.close()

    return produto