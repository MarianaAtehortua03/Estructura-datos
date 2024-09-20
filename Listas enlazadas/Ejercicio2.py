# Clase Tarea que representa una tarea individual en la lista enlazada
class Tarea:
    def __init__(self, descripcion, prioridad, fecha_vencimiento):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento
        self.next = None  # Apunta al siguiente nodo (tarea)

# Clase ListaEnlazada que gestiona todas las tareas
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # La lista empieza vacía

    # Método para agregar una nueva tarea
    def agregar_tarea(self, descripcion, prioridad, fecha_vencimiento):
        nueva_tarea = Tarea(descripcion, prioridad, fecha_vencimiento)
        # Si la lista está vacía, agregamos la tarea directamente
        if self.cabeza is None:
            self.cabeza = nueva_tarea
        else:
            nodo_actual = self.cabeza
            # Insertamos la nueva tarea ordenada por prioridad y fecha de vencimiento
            if nueva_tarea.prioridad < nodo_actual.prioridad or (nodo_actual.prioridad == nueva_tarea.prioridad and nueva_tarea.fecha_vencimiento < nodo_actual.fecha_vencimiento):
                nueva_tarea.next = nodo_actual
                self.cabeza = nueva_tarea
            else:
                while nodo_actual.next is not None and (nodo_actual.next.prioridad < nueva_tarea.prioridad or (nodo_actual.next.prioridad == nueva_tarea.prioridad and nodo_actual.next.fecha_vencimiento < nueva_tarea.fecha_vencimiento)):
                    nodo_actual = nodo_actual.next
                nueva_tarea.next = nodo_actual.next
                nodo_actual.next = nueva_tarea

    # Método para mostrar todas las tareas
    def mostrar_tareas(self):
        nodo_actual = self.cabeza
        if nodo_actual is None:
            print("No hay tareas en la lista.")
        else:
            print("Tareas pendientes:")
            while nodo_actual is not None:
                print(f"Descripción: {nodo_actual.descripcion}, Prioridad: {nodo_actual.prioridad}, Fecha de Vencimiento: {nodo_actual.fecha_vencimiento}")
                nodo_actual = nodo_actual.next

    # Método para eliminar una tarea por descripción
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
                print(f"Tarea '{descripcion}' eliminada.")
                return
            nodo_actual = nodo_actual.next
        print(f"No se encontró la tarea con descripción '{descripcion}'.")

    # Método para buscar una tarea por descripción
    def buscar_tarea(self, descripcion):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.descripcion == descripcion:
                print(f"Tarea encontrada: Descripción: {nodo_actual.descripcion}, Prioridad: {nodo_actual.prioridad}, Fecha de Vencimiento: {nodo_actual.fecha_vencimiento}")
                return
            nodo_actual = nodo_actual.next
        print(f"No se encontró la tarea con descripción '{descripcion}'.")

    # Método para marcar una tarea como completada (la elimina de la lista)
    def completar_tarea(self, descripcion):
        self.eliminar_tarea(descripcion)  # Eliminar es lo mismo que marcar como completada

# Ejemplo de uso del sistema de gestión de tareas
lista_tareas = ListaEnlazada()

# Agregar algunas tareas
lista_tareas.agregar_tarea("Hacer compras", 2, "2024-09-25")
lista_tareas.agregar_tarea("Estudiar para el examen", 1, "2024-09-23")
lista_tareas.agregar_tarea("Pagar facturas", 2, "2024-09-24")

# Mostrar las tareas en orden
print("\nLista de tareas:")
lista_tareas.mostrar_tareas()

# Buscar una tarea
print("\nBuscar tarea:")
lista_tareas.buscar_tarea("Pagar facturas")

# Marcar una tarea como completada
print("\nMarcar tarea como completada:")
lista_tareas.completar_tarea("Hacer compras")

# Mostrar tareas después de completar una
print("\nLista de tareas actualizada:")
lista_tareas.mostrar_tareas()

# Eliminar una tarea
print("\nEliminar una tarea:")
lista_tareas.eliminar_tarea("Estudiar para el examen")

# Mostrar tareas después de eliminar una
print("\nLista de tareas final:")
lista_tareas.mostrar_tareas()
