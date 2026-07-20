from modelos.cargar_modelos import cargar_sentimientos

modelo = cargar_sentimientos()

def analizar_sentimiento(texto):

    resultado = modelo(texto)

    return resultado[0]