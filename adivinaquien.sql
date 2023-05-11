CREATE DATABASE adivinaquien;
USE adivinaquien;
CREATE TABLE personajes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL,
  tiene_bigote BOOLEAN NOT NULL,
  usa_gorra BOOLEAN NOT NULL,
  es_rojo BOOLEAN NOT NULL,
  tiene_arma BOOLEAN NOT NULL,
  es_heroe BOOLEAN NOT NULL,
  es_villano BOOLEAN NOT NULL
);
INSERT INTO personajes (nombre, tiene_bigote, usa_gorra, es_rojo, tiene_arma, es_heroe, es_villano)
VALUES ('Mario', 1, 1, 1, 0, 1, 0);

INSERT INTO personajes (nombre, tiene_bigote, usa_gorra, es_rojo, tiene_arma, es_heroe, es_villano)
VALUES ('Luigi', 1, 1, 0, 1, 1, 0);

INSERT INTO personajes (nombre, tiene_bigote, usa_gorra, es_rojo, tiene_arma, es_heroe, es_villano)
VALUES ('DannyPhanton', 0, 1, 0, 1, 1, 0);

INSERT INTO personajes (nombre, tiene_bigote, usa_gorra, es_rojo, tiene_arma, es_heroe, es_villano)
VALUES ('SamBigotes', 1, 1, 1, 1, 0, 1);

INSERT INTO personajes (nombre, tiene_bigote, usa_gorra, es_rojo, tiene_arma, es_heroe, es_villano)
VALUES ('DeadPool', 0, 0, 1, 1, 1, 0);

INSERT INTO personajes (nombre, tiene_bigote, usa_gorra, es_rojo, tiene_arma, es_heroe, es_villano)
VALUES ('Bowser', 1, 1, 0, 1, 0, 1);

INSERT INTO personajes (nombre, tiene_bigote, usa_gorra, es_rojo, tiene_arma, es_heroe, es_villano)
VALUES ('Dr. Eggman', 1, 0, 0, 1, 0, 1);

SELECT * FROM personajes
