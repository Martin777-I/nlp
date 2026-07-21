from langdetect import detect, DetectorFactory
from deep_translator import GoogleTranslator

DetectorFactory.seed = 0

idiomas = {
    "es": "Español 🇪🇸",
    "en": "Inglés 🇺🇸",
    "fr": "Francés 🇫🇷",
    "it": "Italiano 🇮🇹",
    "de": "Alemán 🇩🇪",
    "pt": "Portugués 🇵🇹"
}


def detectar_idioma(texto):

    codigo = detect(texto)

    return codigo, idiomas.get(codigo, codigo)


def traducir_texto(texto, destino):

    return GoogleTranslator(
        source="auto",
        target=destino
    ).translate(texto)