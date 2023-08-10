import speech_recognition as sr

r = sr.Recognizer()

class SpeechRecognitionError(Exception):
    pass

def listen(): 
    try:         
      with sr.Microphone() as source:  
          print("r.listen..")    
          audio = r.listen(source)       
          # Convert the speech to text
          print("r.recognize_google..")
          text = r.recognize_google(audio)
          return text
    except sr.UnknownValueError:
        raise SpeechRecognitionError("Sorry, I didn't hear what you said. Can you please repeat?")
    