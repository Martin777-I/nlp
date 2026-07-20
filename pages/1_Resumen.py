import streamlit as st
from modelos.resumen import generar_resumen

st.title("Resumen automático")

texto = st.text_area(
    "Ingrese el texto",
    height=300
)

if st.button("Generar resumen"):

    with st.spinner("Generando resumen..."):

        resumen = generar_resumen(texto)

    st.success("Resumen generado")

    st.write(resumen)