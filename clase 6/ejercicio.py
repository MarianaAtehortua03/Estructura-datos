#ACTIVIDAD: Crear el metodo para buscar un elemento y como resultado, incluye la posicion del elemento.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaEnlazada:


    def __init__(self):
        self.cabeza = None

    def es_vacio(self):
        return self.cabeza is None

    def agregar_nodo(self, dato):
      nodo = Node(dato)
      if self.es_vacio():
          self.cabeza = nodo
      else:
          nodo_actual = self.cabeza
          while nodo_actual.next is not None:
              nodo_actual = nodo_actual.next
          nodo_actual.next = nodo

    def imprimir(self):
      nodo_actual = self.cabeza
      while nodo_actual is not None:
          print(nodo_actual.data)
          nodo_actual = nodo_actual.next

    def buscar_elemento(ListaEnlazada, dato):
        nodo_actual=ListaEnlazada.cabeza
        posicion=0
        while nodo_actual:
            if nodo_actual.data == dato:
                return posicion 
            nodo_actual=nodo_actual.next
            posicion += 1
        return -1

lista = ListaEnlazada()
print("Agregamos datos al nodo")
lista.agregar_nodo(1)
lista.agregar_nodo(2)
lista.agregar_nodo(3)

print("Imprimimos los datos")
lista.imprimir()

elemento_buscado = 1 #numer cualquiera
posicion_encontrada = buscar_elemento(lista, elemento_buscado)

if posicion_encontrada != -1:
    print(f "El elemento {elemento_buscado} esta en la posicion {posicion_encontrada}")
else:
    print(f "El elemento {elemento_buscado} no esta en la ")


print(lista.buscar(2))