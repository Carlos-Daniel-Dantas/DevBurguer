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

    CREATE TABLE IF NOT EXISTS usuarios (
    nome VARCHAR(100) DEFAULT "ANONIMO",
    usuario VARCHAR(100) NOT NULL PRIMARY KEY,
    senha VARCHAR(255) NOT NULL
);

