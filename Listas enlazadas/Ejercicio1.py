#Ejercicio 1: Diseñe e implemente un sistema para el control de un sistema de un parque Zoologico 

class Animal:
    def __init__(self, tipo, edad):
        self.tipo = tipo
        self.edad = edad
        self.next = None  # Apunta al siguiente animal en la lista

# Definimos la clase ListaEnlazada para manejar los animales
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # La lista empieza vacía

    # Método para agregar un animal a la lista si no está repetido
    def agregar_animal(self, tipo, edad):
        nuevo_animal = Animal(tipo, edad)
        # Si la lista está vacía, agregamos el animal directamente
        if self.cabeza is None:
            self.cabeza = nuevo_animal
        else:
            nodo_actual = self.cabeza
            # Verificamos si el animal ya está en la lista
            while nodo_actual is not None:
                if nodo_actual.tipo == tipo:
                    print(f"El animal {tipo} ya está en la lista.")
                    return
                if nodo_actual.next is None:
                    break
                nodo_actual = nodo_actual.next
            # Agregamos el nuevo animal al final de la lista
            nodo_actual.next = nuevo_animal

    # Método para mostrar los animales usando un bucle
    def mostrar_animales_bucle(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(f"Tipo: {nodo_actual.tipo}, Edad: {nodo_actual.edad}")
            nodo_actual = nodo_actual.next

    # Método para mostrar los animales usando recursión
    def mostrar_animales_recursivo(self, nodo_actual=None):
        if nodo_actual is None:
            nodo_actual = self.cabeza  # Comenzamos desde la cabeza de la lista
        if nodo_actual is not None:
            print(f"Tipo: {nodo_actual.tipo}, Edad: {nodo_actual.edad}")
            self.mostrar_animales_recursivo(nodo_actual.next)  # Llamada recursiva

# Prueba del sistema del zoológico
zoo = ListaEnlazada()

# Agregamos animales al zoológico
zoo.agregar_animal("Águila", 5)
zoo.agregar_animal("Pantera", 3)
zoo.agregar_animal("Vaca", 2)
zoo.agregar_animal("Águila", 4)  # No se debe agregar porque ya está en la lista

# Mostramos los animales usando un bucle
print("Animales (usando bucle):")
zoo.mostrar_animales_bucle()

# Mostramos los animales usando recursión
print("Animales (usando recursión):")
zoo.mostrar_animales_recursivo()
