import streamlit as st
import google.generativeai as genai

# Page ki setting
st.set_page_config(page_title="Dreamz Hunter AI", page_icon="🕵️‍♂️")
st.title("🎬 Dreamz Hunter AI Assistant")
st.caption("Munawar Khan's personal co-writer for dark suspense scripts.")

# Sidebar mein API key ka dabba
with st.sidebar:
    st.header("⚙️ Setup")
    api_key = st.text_input("Enter your Google Gemini API Key:", type="password")
    st.info("Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey)")

if api_key:
    try:
        # API configure karna
        genai.configure(api_key=api_key)
        
        # Bot ko uski pehchan batana
        instruction = (
            "Tumhara naam Dreamz Hunter AI hai. Tum Munawar Khan ke YouTube channel ke liye kaam karte ho. "
            "Tumhe dark, mysterious documentaries aur 3D animation style ki Hindi moral stories likhni hain. "
            "Tumhara tone hamesha thriller aur engaging hona chahiye."
        )

        # Model ko load karna (Sahi tareeka)
        model = genai.GenerativeModel(model_name='gemini-1.5-flash')

        # Chat history ko sambhalna
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Purani baatein screen par dikhana
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # User ka naya sawal
        if prompt := st.chat_input("Bhangarh Fort ya Amazon ki koi mystery pucho..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # AI ka jawab generate karna
            with st.chat_message("assistant"):
                # System instruction ko prompt ke sath jodna taaki error na aaye
                full_prompt = f"{instruction}\n\nUser Question: {prompt}"
                response = model.generate_content(full_prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                
    except Exception as e:
        st.error(f"Almost there! Error: {e}")
else:
    st.warning("👈 Please enter your Gemini API Key in the sidebar.")
