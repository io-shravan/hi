import streamlit as st

# Built-in translations for common phrases
translations = {
    "hello": {
        "English": "hello",
        "Spanish": "hola",
        "French": "bonjour",
        "German": "hallo",
        "Italian": "ciao"
    },
    "goodbye": {
        "English": "goodbye",
        "Spanish": "adiós",
        "French": "au revoir",
        "German": "auf wiedersehen",
        "Italian": "arrivederci"
    },
    # Add more common phrases here
}

st.title("Simple Translator")
languages = ["English", "Spanish", "French", "German", "Italian"]

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("From:", languages)
with col2:
    target_lang = st.selectbox("To:", languages)

text = st.text_input("Enter a word or phrase:")

if st.button("Translate"):
    text_lower = text.lower()
    if text_lower in translations and target_lang in translations[text_lower]:
        st.success(f"Translation: {translations[text_lower][target_lang]}")
    else:
        st.error("Translation not available for this phrase")
