class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Libro:
    def __init__(self, titulo, autor, isbn, paginas, edicion, editorial, ciudad, pais, fecha_edicion):
        self.titulo = titulo
        self.autor = autor  # objeto Persona
        self.isbn = isbn
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.ciudad = ciudad
        self.pais = pais
        self.fecha_edicion = fecha_edicion

    
    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_isbn(self):
        return self.isbn

    def get_paginas(self):
        return self.paginas

    
    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_autor(self, autor):
        self.autor = autor

    
    def leer(self):
        self.titulo = input("Título: ")
        nombre = input("Nombre del autor: ")
        apellido = input("Apellido del autor: ")
        self.autor = Persona(nombre, apellido)
        self.isbn = input("ISBN: ")
        self.editorial = input("Editorial: ")
        self.ciudad = input("Ciudad: ")
        self.pais = input("País: ")
        self.fecha_edicion = input("Fecha de edición: ")
        self.paginas = int(input("Cantidad de páginas: "))
        self.edicion = input("Edición: ")

   
    def mostrar(self):
        print(f"Título: {self.titulo} {self.edicion}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"{self.editorial}, {self.ciudad} ({self.pais})")
        print(f"{self.fecha_edicion}")
        print(f"{self.paginas} páginas")

autor = Persona("Y. Daniel", "Liang")

libro = Libro(
    "Introduction to Java Programming",
    autor,
    "0-13-031997-X",
    784,
    "3a. edición",
    "Prentice-Hall",
    "New Jersey",
    "USA",
    "viernes 16 de noviembre de 2001"
)

libro.mostrar()