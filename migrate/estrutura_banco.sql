CREATE DATABASE IF NOT EXISTS dev_burguer;
use dev_burguer;

CREATE TABLE if not exists produtos  (
	codigo INT AUTO_INCREMENT PRIMARY KEY,
    produto VARCHAR(200),
    descricao VARCHAR(200),
    preco FLOAT,
    destaque VARCHAR(20),
    foto VARCHAR(255),
    disponibilidade VARCHAR(20)
);
    
CREATE TABLE IF NOT EXISTS carrinho (
	cod_carrinho INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(20),
    data datetime default current_timestamp,
    finalizado bool,
    constraint fk_carrinho_usuario FOREIGN KEY (usuario) REFERENCES usuarios(usuario)
);
    
CREATE TABLE IF NOT EXISTS itens_carrinho (
	cod_itens_carrinho INT AUTO_INCREMENT PRIMARY KEY,
    cod_carrinho int,
    cod_produto int,
    quantidade int default 1,
    constraint fk_carrinho_carrinhos foreign key (cod_carrinho) references carrinho(cod_carrinho),
    constraint fk_itens_carrinho_itens foreign key (cod_produto) references produtos (codigo)
);

CREATE TABLE IF NOT EXISTS usuarios (
    nome VARCHAR(100) DEFAULT "ANONIMO",
    usuario VARCHAR(100) NOT NULL PRIMARY KEY,
    senha VARCHAR(255) NOT NULL
);

