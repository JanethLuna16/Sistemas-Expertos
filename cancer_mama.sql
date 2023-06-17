CREATE DATABASE cancer_mama;
USE cancer_mama;
-- Crear la tabla de pacientes
CREATE TABLE IF NOT EXISTS pacientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    edad INT,
    sintomas VARCHAR(255)
);
-- Crear la tabla de resultados
CREATE TABLE IF NOT EXISTS resultados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT,
    resultado VARCHAR(255),
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id)
);
SELECT * FROM pacientes;
SELECT * FROM resultados
