import streamlit as st
from modelos.sentimientos import analizar_sentimiento

st.title("😊 Análisis de Sentimientos")

texto = st.text_area(
    "Ingrese el texto",
    height=250
)

if st.button("Analizar"):

    if texto.strip() == "":
        st.warning("Debe ingresar un texto.")
    else:

        with st.spinner("Analizando sentimiento..."):

            resultado = analizar_sentimiento(texto)

        resultado = analizar_sentimiento(texto)

        etiquetas = {
            "POSITIVE": "Positivo 😊",
            "NEGATIVE": "Negativo 😠",
            "NEUTRAL": "Neutro 😐"
        }

        sentimiento = etiquetas.get(
            resultado["label"],
            resultado["label"]
        )

        st.subheader("Resultado")

        st.success(sentimiento)

        st.write(
            f"Confianza: **{resultado['score']*100:.2f}%**"
        )
