create database db_panaderia;

use db_panaderia;
CREATE TABLE productos (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(255),
  descripcion VARCHAR(255),
  precio DECIMAL(10,2)
);

CREATE TABLE insumos (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(255),
  descripcion VARCHAR(255),
  cantidad INT
);

CREATE TABLE produccion_diaria (
  id INT PRIMARY KEY AUTO_INCREMENT,
  fecha DATE,
  producto_id INT,
  cantidad INT,
  FOREIGN KEY (producto_id) REFERENCES productos(id)
);

CREATE TABLE recetas (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(200),
  descripcion VARCHAR(200)
);