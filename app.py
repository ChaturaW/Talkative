import os
import streamlit as st
from langchain.llms import OpenAI
import speech_recognition as sr

from io import BytesIO
from audio import speak

from dotenv import load_dotenv

load_dotenv()  # Load the environment variables from the .env file

apikey = os.getenv('apikey')  # Access the 'apikey' variable

os.environ['OPENAI_API_KEY'] = apikey
# Set the language for the text-to-speech conversion
language = "en"

# Initialize the speech recognizer
r = sr.Recognizer()

title = "Speak now.."

st.title("Hello, let's talk")
conversation_history = ""
prompt = ""
# Use the default microphone as the audio source

while True:   
    try:
        # use llms
        llm = OpenAI(temperature=0.9, max_tokens=100)
       
        promptTemplate = f"""Your name is Sarah. You are a companion for a person. You are always friendly, polite and helpful. Start the conversation by saying hello and introducing yourself only at the start.        
        Have a casual conversation about family, daily activities, interests, life. Keep the conversation going. 
        If the person asks you questions, answer them. You may talk about family, hobbies, fassion, life and etc. Do not repeat the same answer.
        \n\n
        """ 

        if conversation_history != "":
            promptTemplate += f"Here is the conversation history so far: \n {conversation_history} \n"

        if prompt != "":
            promptTemplate += f"\nThe last response or the question from the person was: {prompt}\n"

        response = llm(promptTemplate)
        st.write(response)  
        speak(response)    

        with sr.Microphone() as source:      
            st.write("Speak now...")
            audio = r.listen(source)       

            # Convert the speech to text
            text = r.recognize_google(audio)

            prompt = text
            st.write(f"You: {text}")
            conversation_history += f"\n person: {prompt}\n Sarah: {response}\n"


    except sr.UnknownValueError:
        st.write("Sorry, I didn't hear you. Please speak again.")


