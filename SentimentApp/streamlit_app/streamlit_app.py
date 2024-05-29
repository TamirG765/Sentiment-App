import streamlit as st
import requests

logo_path = "sentiment_logo.png"

col1, col2, col3 = st.columns([2, 4, 1])
with col1:
    st.image(logo_path, width=200)

with col2:
    st.markdown("<h1 style='text-align: center; padding-top: 80px; margin:0;'>Tide of Tones</h1>", unsafe_allow_html=True)

text = st.text_area("Enter text to analyze:", "")
if st.button('Analyze Sentiment'):
    if text:
        response = requests.post('http://localhost:8000/analyze/', json={"text": text})
        if response.status_code == 200:
            result = response.json()
            st.write('Sentiment:', result[0]['label'], ' with confidence of ', 100*(round(result[0]['score'], 2)), '%')
        else:
            st.error("Failed to get response from the server")
    else:
        st.error("Please enter some text to analyze")

# streamlit run streamlit_app.py