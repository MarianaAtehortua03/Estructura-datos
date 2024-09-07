#ejercicio 1
def operaciones_basicas(a, b, operacion):
    if operacion == 'suma':
        return a + b
    elif operacion == 'resta':
        return a - b
    elif operacion == 'multiplicacion':
        return a * b
    elif operacion == 'division':
        if b != 0:
             return a / b
        else:
              return "No se puede dividir por cero"
    else:
        return "Operación no válida"