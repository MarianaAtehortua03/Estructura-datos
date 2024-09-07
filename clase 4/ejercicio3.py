def es_palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    longitud = len(palabra)
    for i in range(longitud // 2):
         if palabra[i] != palabra[longitud - i - 1]:
            return False
    return True