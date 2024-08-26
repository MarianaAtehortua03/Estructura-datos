cupo = int(input("Ingrese el cupo máximo: "))

control = 0

while control < cupo:
    valido = input("Ingrese el boleto (enter): ").lower()
    if valido == " ":
        control += 1
        print("Ingreso permitido. Cupo actual: ", control)
    else:
        print("Acceso no permitido")

print("No se permiten más ingresos.")