#EJERCICIOS DE CLASES PARTE 1

#Ejercicio 1
#Crear una clase llamada Vehículo, esta clase debe recibir 2 parámetros, marca y combustible.
#la clase también debe contener dos métodos encender y arrancar. 
#Instanciar la clase y usar el método mágico __str__ para imprimir la marca y el combustible usado

class Vehiculo:
    def __init__ (self, marca: str, combustible: str):
        self.marca = marca
        self.combustible = combustible

    def encender (self ):
        pass
    def arrancar (self ):
        pass
    def __str__ (self ):
        return f"el vehiculo {self.marca} utiliza como combustible {self.combustible}"

carro = Vehiculo("toyota", "corriente")
print(carro)
print(type(carro))

#Ejercicio 2
#Crear dos clases, Moto y Carro, estas clases deben estar heradadas de la clase Vehiculo.

class Moto(Vehiculo):
    def __init__(self, marca:str , combustible:str):
        super(). __init__ (marca, combustible)
class Carro(Vehiculo):
    pass

motocicleta = Moto("Honda" , "corriente")
mi_carro = Carro("Mazda" , "extra")

print(motocicleta)
print(mi_carro)

#Ejercicio 3: La clase Vehiculo, debe tener una propiedad llamada tipo (esta contendrá el tipo de vehiculo - Carro o Moto -), 
#esta propiedad debe ser seteada al momento de instanciar la clase Carro o Moto y al momento de imprimir el objeto debe indicar 
#el tipo de vehiculo junto con el texto mostrado anteriormente 

class Vehiculo:
    def __init__(self, marca, combustible, tipo):
        self.marca = marca
        self.combustible = combustible
        self.tipo = tipo

    def encender(self):
        return "Vehículo encendido."

    def arrancar(self):
        return "Vehículo en marcha."

    def __str__(self):
        return f"Marca: {self.marca}, Combustible: {self.combustible}, Tipo: {self.tipo}"

class Moto(Vehiculo):
    def __init__(self, marca, combustible):
        super().__init__(marca, combustible, "Moto")

class Carro(Vehiculo):
    def __init__(self, marca, combustible):
        super().__init__(marca, combustible, "Carro")

moto = Moto("Yamaha", "Gasolina")
carro = Carro("Chevrolet", "Diésel")

print(moto)
print(carro)

#ejercicio 4
#ejercicio 5
# Método para que el vehículo de marcha y consuma combustible a medida que funciona

    def en_marcha(self):
        if not self.encendido:
            print(f"El vehículo {self.marca} no puede iniciar marcha porque está apagado.")
            return
        
        while self.galones > 0:
            print(f"El vehículo {self.marca} está en marcha. Combustible restante: {self.galones:.2f} galones.")
            self.galones -= 0.5  # Consume 0.5 galones por ciclo

            if self.galones < 0.1 * self.capacidad_tanque():
                print(f"Advertencia: El vehículo {self.marca} necesita ir a la gasolinera.")

            if self.galones <= 0:
                print(f"El vehículo {self.marca} se ha detenido por falta de combustible.")
                self.encendido = False
                break

