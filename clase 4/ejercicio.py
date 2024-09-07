def calcular_factorial (numero: int)-> str | int:
    resultado = 1
    if numero < 0 :
        return "No se puede, valores negativos"
    elif numero == 0:
        return 1
    for n in range(1, numero + 1):
            resultado = resultado * n
            return resultado

numero = int(input("Introduce un numero: "))
numero_factorial = calcular_factorial(numero)
print(calcular_factorial(numero))