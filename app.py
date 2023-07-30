import os
import streamlit as st

from mouth import speak
from ears import listen, SpeechRecognitionError
from mind import think

title = "Speak now.."

st.title("Hello, let's talk")
conversation_history = ""
prompt = ""


while True:   
    response = think(prompt, conversation_history)
    
    st.write(response)  
    
    speak(response)    

    try:
        textHeard = listen()
        prompt = textHeard
        st.write(f"You: {textHeard}")
        conversation_history += f"\n person: {textHeard}\n Sarah: {response}\n"
    except SpeechRecognitionError as e:
        errorMessage = str(e)
        st.write(errorMessage)
   

