def factorial(n):
    if n == 0:
        return 1
    else:
        factores = [i for i in range(1, n + 1)]
        resultado = 1
        for factor in factores:
            resultado *= factor
        return resultado

numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")