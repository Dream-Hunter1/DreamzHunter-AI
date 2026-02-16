import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Dreamz Hunter AI", page_icon="🕵️‍♂️")
st.title("🎬 Dreamz Hunter AI Assistant")

with st.sidebar:
    api_key = st.text_input("Enter Gemini API Key:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # Sahi model loading
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        if prompt := st.chat_input("Write your script idea..."):
            with st.chat_message("user"):
                st.markdown(prompt)
            with st.chat_message("assistant"):
                # Seedha jawab generate karna
                response = model.generate_content(f"Tum Dreamz Hunter AI ho. Munawar Khan ke liye ye script likho: {prompt}")
                st.markdown(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.warning("👈 Please enter your Gemini API Key in the sidebar.")
