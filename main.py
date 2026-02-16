import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Dreamz Hunter AI", page_icon="🕵️‍♂️")
st.title("🎬 Dreamz Hunter AI Assistant")

with st.sidebar:
    st.header("⚙️ Setup")
    api_key = st.text_input("Enter Gemini API Key:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # Ye line sabse stable model uthayegi
        model = genai.GenerativeModel('gemini-1.5-flash')

        if prompt := st.chat_input("Bhangarh Fort ya Amazon ki mystery pucho..."):
            with st.chat_message("user"):
                st.markdown(prompt)
            
            with st.chat_message("assistant"):
                # Seedha response bina kisi extra instruction ke
                response = model.generate_content(f"You are Dreamz Hunter AI. Answer this: {prompt}")
                st.markdown(response.text)
                
    except Exception as e:
        st.error(f"Almost there! Just check the key. Error: {e}")
else:
    st.warning("👈 Please enter your Gemini API Key in the sidebar.")
