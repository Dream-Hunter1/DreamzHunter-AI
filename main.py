import streamlit as st
import google.generativeai as genai

# Page setup
st.set_page_config(page_title="Dreamz Hunter AI", page_icon="🕵️‍♂️", layout="centered")
st.title("🎬 Dreamz Hunter AI Assistant")
st.caption("Your personal co-writer for dark, cinematic suspense scripts.")

# Sidebar for API Key
with st.sidebar:
    st.header("⚙️ Setup")
    api_key = st.text_input("Enter your Google Gemini API Key:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # Sahi model name: 'gemini-1.5-flash'
        instruction = "Tumhara naam Dreamz Hunter AI hai. Tumhe mere YouTube channel ke liye dark, mysterious documentaries aur 3D animation style ki Hindi moral stories likhni hain."
        model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=instruction)

        # Chat session initialize
        if "chat_session" not in st.session_state:
            st.session_state.chat_session = model.start_chat(history=[])

        # Display chat history
        for message in st.session_state.chat_session.history:
            role = "Assistant 🤖" if message.role == "model" else "You 👤"
            with st.chat_message(role):
                st.markdown(message.parts[0].text)

        # User input
        user_prompt = st.chat_input("Write a script idea here...")
        if user_prompt:
            with st.chat_message("You 👤"):
                st.markdown(user_prompt)
            
            with st.chat_message("Assistant 🤖"):
                # Response generation
                response = st.session_state.chat_session.send_message(user_prompt)
                st.markdown(response.text)
                
    except Exception as e:
        st.error(f"Ek choti si ghalti hui hai: {e}")
else:
    st.warning("👈 Please enter your Gemini API Key in the sidebar to start.")
