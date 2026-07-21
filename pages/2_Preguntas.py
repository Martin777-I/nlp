import streamlit as st
from modelos.preguntas import responder_pregunta

st.title("Preguntas y respuestas")

texto = st.text_area(
    "Ingrese el texto",
    height=300
)

pregunta = st.text_input("Pregunta")

if st.button("Responder"):

    with st.spinner("Buscando respuesta..."):

        respuesta, confianza = responder_pregunta(
            texto,
            pregunta
        )

    st.write("### Respuesta")

    st.success(respuesta)

    st.write(f"Confianza: {confianza*100:.2f}%")