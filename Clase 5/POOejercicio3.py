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