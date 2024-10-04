import heapq #esta biblioteca ayuda a implementar la cola de prioridad
from queue import Queue #implementación de colas FIFO

class Tarea:
    def __init__(self, nombre, prioridad, tiempo_ejecucion):
        self.nombre = nombre
        self.prioridad = prioridad
        self.tiempo_ejecucion = tiempo_ejecucion
    
    def __lt__(self, otra): #Metodo especial que permite comparar 2 objetos con el operador 
        return self.prioridad > otra.prioridad  # Para manejar prioridades, mayor valor -> mayor prioridad

# Cola de prioridad utilizando heapq
class ColaPrioridad:
    def __init__(self):
        self.cola = [] #inicializa la cola como una lista vacia

    def agregar_tarea(self, tarea):
        heapq.heappush(self.cola, tarea) #Utilizar la funcion heapq.heappush para insertar tarea en la cola manteniendo la propiedad de la cola de prioridad

    def obtener_siguiente_tarea(self): #metodo que devuelve la siguiente tarea en la cola de prioridad, la tarea con mayor prioridad
        if not self.esta_vacia():
            return heapq.heappop(self.cola) #extrae y devuelve la tarea con la mayor prioridad de la cola
        return None

    def esta_vacia(self):
        return len(self.cola) == 0

# Cola FIFO utilizando queue
class ColaFIFO:
    def __init__(self):
        self.cola = Queue() #inicializa la cola como una instancia de la clase Queue

    def agregar_tarea(self, tarea):
        self.cola.put(tarea) #inserta la tarea al final de la cola

    def obtener_siguiente_tarea(self): #metodo para extraer la tarea que esta al frente de la cola
        if not self.esta_vacia():
            return self.cola.get() #saca y devuelve la tarea que esta al principio de la cola
        return None

    def esta_vacia(self):
        return self.cola.empty()

# Simulación del procesador
def simular_procesador(cola_prioridad, cola_fifo):
    while not cola_prioridad.esta_vacia() or not cola_fifo.esta_vacia():
        # Procesar primero las tareas de alta prioridad
        if not cola_prioridad.esta_vacia():
            tarea = cola_prioridad.obtener_siguiente_tarea()
            print(f"Ejecutando tarea prioritaria: {tarea.nombre} (Tiempo de ejecución: {tarea.tiempo_ejecucion})")
        elif not cola_fifo.esta_vacia():
            tarea = cola_fifo.obtener_siguiente_tarea()
            print(f"Ejecutando tarea regular: {tarea.nombre} (Tiempo de ejecución: {tarea.tiempo_ejecucion})")

# Crear algunas tareas de ejemplo
tareas_prioridad = [
    Tarea("Seguridad", 5, 2),
    Tarea("Actualización", 4, 3),
    Tarea("Mantenimiento", 3, 4)
]

tareas_fifos = [
    Tarea("Tarea 1", 1, 6),
    Tarea("Tarea 2", 1, 8),
    Tarea("Tarea 3", 1, 5)
]

# Crear colas
cola_prioridad = ColaPrioridad()
cola_fifo = ColaFIFO()

# Agregar tareas a las colas
for tarea in tareas_prioridad:
    cola_prioridad.agregar_tarea(tarea)

for tarea in tareas_fifos:
    cola_fifo.agregar_tarea(tarea)

# Simular el procesador
simular_procesador(cola_prioridad, cola_fifo)
