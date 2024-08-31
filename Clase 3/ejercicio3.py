import random

numeros = []
for _ in range(10):
    numeros.append(random.randint(1, 100))

suma = 0
for numero in numeros:
    suma += numero

promedio = suma / len(numeros)

print("Números generados:", numeros)
print("Suma de los números:", suma)
print("Promedio de los números:", promedio)
