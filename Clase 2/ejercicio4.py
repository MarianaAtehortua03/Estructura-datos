peso = float(input("introduce peso"))
altura = float(input("introduce altura"))

imc = peso / (altura * altura)

if imc >= 25.0:
    print("Estas en sobrepeso")
else:
    print("No estas en sobrepeso")