CREATE DATABASE IF NOT EXISTS dev_burguer;
USE dev_burguer;

CREATE TABLE IF NOT EXISTS produtos (
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    produto VARCHAR(200),
    descricao VARCHAR(200),
    preco DECIMAL(10, 2), 
    destaque VARCHAR(20),
    foto VARCHAR(255),
    disponibilidade VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS usuarios (
    usuario VARCHAR(100) NOT NULL PRIMARY KEY,
    nome VARCHAR(100) DEFAULT "ANONIMO",
    senha VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS carrinhos (
    cod_carrinho INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(100),
    data DATETIME DEFAULT CURRENT_TIMESTAMP,
    finalizado BOOL,
    CONSTRAINT fk_carrinho_usuario FOREIGN KEY (usuario) REFERENCES usuarios(usuario)
);

CREATE TABLE IF NOT EXISTS itens_carrinho (
    cod_itens_carrinho INT AUTO_INCREMENT PRIMARY KEY,
    cod_carrinho INT,
    cod_produto INT,
    quantidade INT DEFAULT 1,
    CONSTRAINT fk_carrinho_carrinhos FOREIGN KEY (cod_carrinho) REFERENCES carrinhos(cod_carrinho),
    CONSTRAINT fk_itens_carrinho_produtos FOREIGN KEY (cod_produto) REFERENCES produtos(codigo)
);