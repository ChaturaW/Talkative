import os
import streamlit as st

from mouth import speak
from ears import listen, SpeechRecognitionError
from mind import think, initialize_conversation, end_conversation

title = "Speak now.."

st.title("Hello, let's talk")
last_response = ""
person_said = ""

no_response_count = 0
initialize_conversation()

while True:  
    print("started thinking...") 
    new_response = think(person_said, last_response)
    print("ended thinking!") 
    
    st.write(new_response)  
    
    print("started speaking...")
    speak(new_response)    
    print("ended speaking!")
    
    if "goodbye" in new_response.lower():
        break

    try:
        print("listening started...")
        person_said = listen()
        print("listening over!")
          
        st.write(f"You: {person_said}")        
        last_response = new_response
    except SpeechRecognitionError as e:        
        errorMessage = str(e)        
        st.write(errorMessage)        
        no_response_count += 1
        if no_response_count < 2:
            speak(errorMessage)
        else:
            speak("I'm sorry, I can't hear you. let's talk later. Goodbye.")
            break       

end_conversation()  
print("end conversation!")
