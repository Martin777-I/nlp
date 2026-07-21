from modelos.cargar_modelos import cargar_qa

qa = cargar_qa()


def responder_pregunta(texto, pregunta):

    respuesta = qa(
        question=pregunta,
        context=texto
    )

    return respuesta["answer"], respuesta["score"]