from modelos.cargar_modelos import cargar_summarizer

summarizer = cargar_summarizer()


def generar_resumen(texto):

    resumen = summarizer(
        texto,
        max_length=60,
        min_length=40
    )

    return resumen[0]["summary_text"]