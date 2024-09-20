#EJERCICIO 1: Calcular el factorial de un número (n)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

#EJERCICIO 2: Generar los primeros n números de la serie Fibonacci. La serie comienza con 0 y 1 y cada numero siguiente es la suma de los dos anteriores

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#EJERICIO 3: Sumar los elementos de un Arreglo

def suma_arreglo(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + suma_arreglo(arr[1:])

#EJERCICIO 4: Realizar una multiplicación a base de sumas

def multiplicacion (a:int, b:int) -> int:
    if a == 0:
        return 0
    return b + multiplicacion(a - 1, b)

print(multiplicacion(4, 5))

#EJERCICIO 5: Realizar una división a base de restas

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre 0")
    if abs(a) < abs(b):
        return 0
    if (a > 0 and b > 0) or (a < 0 and b < 0):
        return 1 + dividir(abs(a) - abs(b), abs(b))
    else:
        return -1 + dividir(abs(a) - abs(b), abs(b))