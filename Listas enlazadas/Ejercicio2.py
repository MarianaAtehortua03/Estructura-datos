# Ejercicio 2: Diseña e implementa un sistema de gestión de tareas utilizando listas enlazadas. 

class Tarea:
    def __init__(self, descripcion, prioridad, fecha_vencimiento):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None 

    def agregar_tarea(self, descripcion, prioridad, fecha_vencimiento):
        nueva_tarea = Tarea(descripcion, prioridad, fecha_vencimiento)
        if self.cabeza is None:
            self.cabeza = nueva_tarea
        else:
            nodo_actual = self.cabeza
            if nueva_tarea.prioridad < nodo_actual.prioridad or (nodo_actual.prioridad == nueva_tarea.prioridad and nueva_tarea.fecha_vencimiento < nodo_actual.fecha_vencimiento):
                nueva_tarea.next = nodo_actual
                self.cabeza = nueva_tarea
            else:
                while nodo_actual.next is not None and (nodo_actual.next.prioridad < nueva_tarea.prioridad or (nodo_actual.next.prioridad == nueva_tarea.prioridad and nodo_actual.next.fecha_vencimiento < nueva_tarea.fecha_vencimiento)):
                    nodo_actual = nodo_actual.next
                nueva_tarea.next = nodo_actual.next
                nodo_actual.next = nueva_tarea

    def mostrar_tareas(self):
        nodo_actual = self.cabeza
        if nodo_actual is None:
            print("No hay tareas en la lista")
        else:
            print("Tareas pendientes")
            while nodo_actual is not None:
                print(f"Descripción: {nodo_actual.descripcion}, Prioridad: {nodo_actual.prioridad}, Fecha de Vencimiento: {nodo_actual.fecha_vencimiento}")
                nodo_actual = nodo_actual.next

    def eliminar_tarea(self, descripcion):
        nodo_actual = self.cabeza
        if nodo_actual is None:
            print("La lista está vacía.")
            return
        if nodo_actual.descripcion == descripcion:
            self.cabeza = nodo_actual.next
            print(f"Tarea '{descripcion}' eliminada.")
            return
        while nodo_actual.next is not None:
            if nodo_actual.next.descripcion == descripcion:
                nodo_actual.next = nodo_actual.next.next
                print(f"Tarea '{descripcion}' eliminada")
                return
            nodo_actual = nodo_actual.next
        print(f"No se encontró la tarea con descripción '{descripcion}'.")

    def buscar_tarea(self, descripcion):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.descripcion == descripcion:
                print(f"Tarea encontrada: Descripción: {nodo_actual.descripcion}, Prioridad: {nodo_actual.prioridad}, Fecha de Vencimiento: {nodo_actual.fecha_vencimiento}")
                return
            nodo_actual = nodo_actual.next
        print(f"No se encontró la tarea con descripción '{descripcion}'.")

    def completar_tarea(self, descripcion):
        self.eliminar_tarea(descripcion)  # tarea completada

lista_tareas = ListaEnlazada()

lista_tareas.agregar_tarea("Hacer compras", 2, "2024-09-25")
lista_tareas.agregar_tarea("Estudiar para el examen", 1, "2024-09-23")
lista_tareas.agregar_tarea("Pagar facturas", 2, "2024-09-24")

# Mostrar las tareas en orden
print("\nLista de tareas:")
lista_tareas.mostrar_tareas()

print("\nBuscar tarea:")
lista_tareas.buscar_tarea("Pagar facturas")

print("\nMarcar tarea como completada:")
lista_tareas.completar_tarea("Hacer compras")

# tareas después de completar una
print("\nLista de tareas actualizada:")
lista_tareas.mostrar_tareas()

print("\nEliminar una tarea:")
lista_tareas.eliminar_tarea("Estudiar para el examen")

# tareas después de eliminar una
print("\nLista de tareas final:")
lista_tareas.mostrar_tareas()
