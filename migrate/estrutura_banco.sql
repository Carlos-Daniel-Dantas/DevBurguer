CREATE DATABASE IF NOT EXISTS dev_burguer;
use dev_burguer;

CREATE TABLE produtos (
	codigo INT AUTO_INCREMENT PRIMARY KEY,
    produto VARCHAR(200),
    descricao VARCHAR(200),
    preco FLOAT,
    destaque VARCHAR(20),
    foto VARCHAR(255),
    disponibilidade VARCHAR(20)
    );

    insert into produtos(produto, descricao, preco, destaque, foto, disponibilidade)
    values("Godo Burguer", "Um lanche especial espera por voce com uma carne divina", 24.00, 1, "https://assets.grok.com/users/6c51eb9c-5b1a-4715-b68c-9f325c88541d/generated/82bc4c98-4a2d-4e4f-b243-0fcce9c83917/image.jpg", 1);

    CREATE TABLE IF NOT EXISTS usuarios (
    nome VARCHAR(100) DEFAULT "ANONIMO",
    usuario VARCHAR(100) NOT NULL PRIMARY KEY,
    senha VARCHAR(255) NOT NULL
);

