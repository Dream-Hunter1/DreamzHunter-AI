import streamlit as st
import google.generativeai as genai

# Page configuration
st.set_page_config(page_title="Dreamz Hunter AI", page_icon="🕵️‍♂️")
st.title("🎬 Dreamz Hunter AI Assistant")
st.caption("Your personal co-writer for dark, cinematic suspense scripts.")

# Sidebar for API Key
with st.sidebar:
    st.header("⚙️ Setup")
    api_key = st.text_input("Enter your Google Gemini API Key:", type="password")
    st.info("Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey)")

if api_key:
    try:
        # Initializing the SDK
        genai.configure(api_key=api_key)
        
        # System Instruction for your specific niche
        instruction = (
            "Tumhara naam Dreamz Hunter AI hai. Tum Munawar Khan ke YouTube channel ke liye kaam karte ho. "
            "Tumhe dark, mysterious documentaries (jaise Bhangarh Fort, Mary Celeste) aur "
            "3D animation style ki Hindi moral stories likhni hain. Tumhara tone hamesha thriller aur engaging hona chahiye."
        )

        # Loading the model explicitly
        model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            system_instruction=instruction
        )

        # Maintain chat history
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        # Display past messages
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # User input box
        if prompt := st.chat_input("Write your script idea here..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Generate response
            with st.chat_message("assistant"):
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.chat_history.append({"role": "assistant", "content": response.text})
                
    except Exception as e:
        st.error(f"Almost there! Please check your API key or connection. Error: {e}")
else:
    st.warning("👈 Please enter your Gemini API Key in the sidebar to wake up the assistant.")
