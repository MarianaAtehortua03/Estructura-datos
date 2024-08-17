nume1 = int(input("introduce el primer numero: "))
nume2 = int(input("introduce el segundo numero: "))

operacion = input("introduce la operacion: /, *, +, - ")

if operacion == "/":
    print(nume1 / nume2)
elif operacion == "*":
    print(nume1 * nume2)
elif operacion == "+":
    print(nume1 + nume2)
elif operacion == "-":
    print(nume1 - nume2)
else:
    print("La operacion no es valida")