import speech_recognition as sr

r = sr.Recognizer()
# m = sr.Microphone()

# with m as source:
#     r.adjust_for_ambient_noise(source)

class SpeechRecognitionError(Exception):
    pass

def listen(): 
    try:         
      with sr.Microphone() as source:  
        r.adjust_for_ambient_noise(source)
        print("r.listen..")         
        audio = r.listen(source)       
        # Convert the speech to text
        print("r.recognize_google..")
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        raise SpeechRecognitionError("Sorry, I didn't hear what you said. Can you please repeat?")
    