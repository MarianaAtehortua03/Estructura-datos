#EJERCICIOS DE CLASES PARTE 2

#Clase Persona

class Persona:
    def __init__(self, nombre: str, edad: int, genero: str):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre}, tengo {self.edad} años y soy {self.genero}.")
    
    # Métodos para obtener y establecer los atributos
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre: str):
        self.nombre = nombre
    
    def get_edad(self):
        return self.edad
    
    def set_edad(self, edad: int):
        self.edad = edad
    
    def get_genero(self):
        return self.genero
    
    def set_genero(self, genero: str):
        self.genero = genero

#Clase CuentaBancaria

class CuentaBancaria:
    def __init__(self, titular: Persona, saldo: float, numeroDeCuenta: str):
        self.titular = titular
        self.saldo = saldo
        self.numeroDeCuenta = numeroDeCuenta
    
    def depositar(self, cantidad: float):
        self.saldo += cantidad
        print(f"Se han depositado {cantidad}. El saldo actual es {self.saldo}.")
    
    def retirar(self, cantidad: float):
        if cantidad > self.saldo:
            print(f"No se puede retirar {cantidad}, saldo insuficiente.")
        else:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad}. El saldo actual es {self.saldo}.")
    
    def consultarSaldo(self):
        print(f"El saldo actual es {self.saldo}.")

#Clase Rectángulo

class Rectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

#Clase Círculo

import math

class Circulo:
    def __init__(self, radio: float):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * (self.radio ** 2)
    
    def calcular_circunferencia(self):
        return 2 * math.pi * self.radio

#Clase Libro

class Libro:
    def __init__(self, titulo: str, autor: str, genero: str, añoDePublicacion: int):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.añoDePublicacion = añoDePublicacion
    
    def mostrarDetalles(self):
        print(f"Titulo: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, Año de publicación: {self.añoDePublicacion}")
    
    # Métodos para obtener y establecer los atributos
    def get_titulo(self):
        return self.titulo
    
    def set_titulo(self, titulo: str):
        self.titulo = titulo
    
    def get_autor(self):
        return self.autor
    
    def set_autor(self, autor: str):
        self.autor = autor

#Clase Canción

class Cancion:
    def __init__(self, titulo: str, artista: str, album: str, duracion: float):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracion = duracion
    
    def reproducir(self):
        print(f"Reproduciendo {self.titulo} de {self.artista}...")
    
    # Métodos para obtener y establecer los atributos
    def get_titulo(self):
        return self.titulo
    
    def set_titulo(self, titulo: str):
        self.titulo = titulo
``

#Clase Producto

class Producto:
    def __init__(self, nombre: str, precio: float, cantidadDisponible: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidadDisponible = cantidadDisponible
    
    def calcularTotal(self, cantidad: int):
        if cantidad > self.cantidadDisponible:
            print(f"No hay suficiente stock. Solo quedan {self.cantidadDisponible} unidades disponibles.")
            return None
        else:
            total = cantidad * self.precio
            print(f"El costo total por {cantidad} {self.nombre}(s) es {total}.")
            return total
    
    # Métodos para obtener y establecer los atributos
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre: str):
        self.nombre = nombre
    
    def get_precio(self):
        return self.precio
    
    def set_precio(self, precio: float):
        self.precio = precio
    
    def get_cantidadDisponible(self):
        return self.cantidadDisponible
    
    def set_cantidadDisponible(self, cantidadDisponible: int):
        self.cantidadDisponible = cantidadDisponible

#Clase Estudiante

class Estudiante:
    def __init__(self, nombre: str, edad: int, curso: str):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.calificaciones = []  # Lista vacía para almacenar las calificaciones
    
    def agregar_calificacion(self, calificacion: float):
        self.calificaciones.append(calificacion)
        print(f"Calificación de {calificacion} agregada.")
    
    def calcular_promedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)
    
    def determinar_aprobacion(self):
        promedio = self.calcular_promedio()
        if promedio >= 3.0:  # Supongamos que la nota mínima para aprobar es 3.0
            print(f"El estudiante {self.nombre} ha aprobado con un promedio de {promedio}.")
        else:
            print(f"El estudiante {self.nombre} ha reprobado con un promedio de {promedio}.")
    
    # Métodos para obtener y establecer los atributos
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre: str):
        self.nombre = nombre
