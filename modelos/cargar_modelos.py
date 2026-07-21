import streamlit as st
from transformers import pipeline

@st.cache_resource
def cargar_summarizer():

    return pipeline(
        "summarization",
        model="csebuetnlp/mT5_multilingual_XLSum",
        tokenizer="csebuetnlp/mT5_multilingual_XLSum",
        use_fast=False
    )


@st.cache_resource
def cargar_qa():

    return pipeline(
        "question-answering",
        model="timpal0l/mdeberta-v3-base-squad2"
    )

@st.cache_resource
def cargar_sentimientos():

    return pipeline(
        "sentiment-analysis",
        model="tabularisai/multilingual-sentiment-analysis"
    )

@st.cache_resource
def cargar_corrector():

    return pipeline(
        "text2text-generation",
        model="juancavallotti/byt5-base-spanish-gec"
    )