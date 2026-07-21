import streamlit as st
from spellchecker import SpellChecker

st.set_page_config(
    page_title="Corrector Ortográfico",
    page_icon="📝",
    layout="wide"
)

spell = SpellChecker(language="es")

def corregir_texto(texto):
    palabras = texto.split()

    texto_corregido = []
    correcciones = []

    for palabra in palabras:

        # Guardar signos de puntuación
        inicio = ""
        final = ""

        while len(palabra) > 0 and not palabra[0].isalnum():
            inicio += palabra[0]
            palabra = palabra[1:]

        while len(palabra) > 0 and not palabra[-1].isalnum():
            final = palabra[-1] + final
            palabra = palabra[:-1]

        if palabra == "":
            continue

        sugerencia = spell.correction(palabra)

        if sugerencia is None:
            sugerencia = palabra

        if palabra.lower() != sugerencia.lower():

            correcciones.append({
                "Error": palabra,
                "Corrección": sugerencia
            })

        texto_corregido.append(inicio + sugerencia + final)

    return " ".join(texto_corregido), correcciones


st.title("📝 Corrector Ortográfico")
st.write("Escriba o pegue un texto para revisar su ortografía.")

st.divider()

texto = st.text_area(
    "✍️ Texto",
    height=220,
    placeholder="Escriba aquí su texto..."
)

if st.button("🔍 Corregir texto", use_container_width=True):

    if texto.strip() == "":
        st.warning("Ingrese un texto para analizar.")
        st.stop()

    texto_corregido, correcciones = corregir_texto(texto)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📄 Texto original")
        st.text_area(
            "",
            texto,
            height=220,
            disabled=True,
            label_visibility="collapsed"
        )

    with col2:
        st.subheader("✅ Texto corregido")
        st.text_area(
            "",
            texto_corregido,
            height=220,
            disabled=True,
            label_visibility="collapsed"
        )

    st.divider()

    if len(correcciones) == 0:
        st.success("🎉 ¡Excelente! No se encontraron errores ortográficos.")
    else:
        st.warning(f"Se encontraron **{len(correcciones)}** errores ortográficos.")

        st.subheader("📋 Palabras corregidas")

        st.table(correcciones)