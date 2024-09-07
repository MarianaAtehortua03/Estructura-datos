import random

def generar_contrasena(longitud):
    caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
    contrasena = ''
    for _ in range(longitud):
        contrasena += caracteres[random.randint(0, len(caracteres) - 1)]
    return contrasena