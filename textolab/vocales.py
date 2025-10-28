def contar_vocales(texto:str):
    texto = texto.lower()
    vocales = ["a", "e", "i", "o", "u"]
    contador_vocales = 0
    for letra in texto:
        if letra in vocales:
            contador_vocales += 1
    return contador_vocales
