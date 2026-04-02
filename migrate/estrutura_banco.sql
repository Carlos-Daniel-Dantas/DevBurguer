CREATE DATABASE IF NOT EXISTS dev_burguer;
use dev_burguer;

CREATE TABLE produtos (
	codigo INT AUTO_INCREMENT PRIMARY KEY,
    produto VARCHAR(200),
    descricao VARCHAR(200),
    precor FLOAT,
    destaque VARCHAR(20),
    foto VARCHAR(255),
    disponibilidade VARCHAR(20)
    );