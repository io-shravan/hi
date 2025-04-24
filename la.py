import streamlit as st
import requests

# Set page title and configuration
st.set_page_config(page_title="Simple Language Translator", layout="wide")

# App title and description
st.title("Simple Language Translator")
st.markdown("A simple tool to translate text between different languages")

# Language options
languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Japanese": "ja",
    "Chinese": "zh",
    "Arabic": "ar",
    "Hindi": "hi",
    "Korean": "ko"
}

# Create two columns for source and target language selection
col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox(
        "Translate from:",
        options=list(languages.keys()),
        index=0
    )

with col2:
    target_language = st.selectbox(
        "Translate to:",
        options=list(languages.keys()),
        index=1
    )

# Text input area
input_text = st.text_area("Enter text to translate:", height=150)

# Function to translate text using LibreTranslate API
def translate_text(text, source, target):
    # Using the public LibreTranslate API
    url = "https://libretranslate.com/translate"
    
    payload = {
        "q": text,
        "source": languages[source],
        "target": languages[target],
        "format": "text"
    }
    
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            return response.json()["translatedText"]
        else:
            return f"Error: API responded with status code {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"

# Create columns for action buttons
button_col1, button_col2 = st.columns(2)

with button_col1:
    translate_button = st.button("Translate", use_container_width=True)

with button_col2:
    clear_button = st.button("Clear", use_container_width=True)

# Initialize session state for translation history
if 'history' not in st.session_state:
    st.session_state.history = []

# Clear functionality
if clear_button:
    st.session_state.history = []
    input_text = ""
    st.experimental_rerun()

# Translate functionality
if translate_button and input_text:
    with st.spinner("Translating..."):
        translated_text = translate_text(input_text, source_language, target_language)
        
        # Add to history
        st.session_state.history.append({
            "original": input_text,
            "from": source_language,
            "translated": translated_text,
            "to": target_language
        })
        
        # Show translation result
        st.success(f"Translation: {translated_text}")

# Display translation history
if st.session_state.history:
    st.markdown("---")
    st.subheader("Translation History")
    
    for i, entry in enumerate(reversed(st.session_state.history)):
        with st.expander(f"Translation {len(st.session_state.history) - i}"):
            st.markdown(f"**From {entry['from']}:** {entry['original']}")
            st.markdown(f"**To {entry['to']}:** {entry['translated']}")
