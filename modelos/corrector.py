from modelos.cargar_modelos import cargar_corrector

modelo = cargar_corrector()


def corregir_texto(texto):

    entrada = f"fix grammar: {texto}"

    resultado = modelo(
        entrada,
        max_new_tokens=256,
        do_sample=False
    )

    return resultado[0]["generated_text"]