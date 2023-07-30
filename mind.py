import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.callbacks import get_openai_callback

from dotenv import load_dotenv

load_dotenv()  # Load the environment variables from the .env file

apikey = os.getenv('apikey')  # Access the 'apikey' variable

os.environ['OPENAI_API_KEY'] = apikey
# Set the language for the text-to-speech conversion
language = "en"

llm = ChatOpenAI(temperature=0.9, model_name="gpt-3.5-turbo")

def think(prompt, conversation_history):           
    promptTemplate = f"""Your name is Sarah. You are a companion for a person. You are always friendly, polite and helpful. Start the conversation by saying hello and introducing yourself only at the start.        
    Have a casual conversation about family, daily activities, interests, life. Keep the conversation going. 
    If the person asks you questions, answer them. You may talk about family, hobbies, fassion, life and etc. Do not repeat the same answer.
    \n\n
    """ 

    print(conversation_history)
    
    messages = [
        SystemMessage(
            content=promptTemplate
        ),
        AIMessage(
            content=conversation_history
        ),
        HumanMessage(
            content=prompt
        ),
    ]
    
    with get_openai_callback() as cb:
        res = llm(messages)
        response = res.content   
        print(cb)
        return response
   

   

