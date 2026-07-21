import streamlit as st
from modelos.idioma import detectar_idioma, traducir_texto

st.title("Detección y Traducción de Idiomas")

st.write(
    "Detecta automáticamente el idioma del texto y tradúcelo al idioma que desees."
)

texto = st.text_area(
    "Ingrese el texto",
    height=250
)

idiomas = {
    "Español 🇪🇸": "es",
    "Inglés 🇺🇸": "en",
    "Francés 🇫🇷": "fr",
    "Italiano 🇮🇹": "it",
    "Alemán 🇩🇪": "de",
    "Portugués 🇵🇹": "pt"
}

destino = st.selectbox(
    "Traducir a:",
    list(idiomas.keys())
)

if st.button("Traducir"):

    if texto.strip() == "":
        st.warning("Debe ingresar un texto.")
        st.stop()

    try:

        codigo, idioma = detectar_idioma(texto)

        st.subheader("Idioma detectado")
        st.success(idioma)

        # Si el idioma detectado y el seleccionado son iguales
        if codigo == idiomas[destino]:

            st.info(
                "El texto ya está en el idioma seleccionado. No es necesario traducirlo."
            )

        else:

            with st.spinner("Traduciendo..."):

                traduccion = traducir_texto(
                    texto,
                    idiomas[destino]
                )

            st.subheader("Traducción")

            st.info(traduccion)

    except Exception as e:

        st.error("Ocurrió un error durante la traducción.")
        st.error(e)