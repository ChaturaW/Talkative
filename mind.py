import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.callbacks import get_openai_callback
from memory import recall, remember

from dotenv import load_dotenv
load_dotenv()  # Load the environment variables from the .env file

apikey = os.getenv('apikey')  # Access the 'apikey' variable

os.environ['OPENAI_API_KEY'] = apikey
os.environ['TOKENIZERS_PARALLELISM'] = "false"
# Set the language for the text-to-speech conversion
language = "en"

llm = ChatOpenAI(temperature=0.9, model_name="gpt-3.5-turbo")

def think(prompt, last_response):   
    memory = recall(prompt)
    print(memory)

    promptTemplate = f"""Your name is Sarah. You are a companion for a person. You are always friendly, polite and helpful. 
    At the start of the conversation greet the person and introduce yourself. You may use the person's name in the conversation to make it more personal.            
    Have a casual conversation about family, daily activities, interests, life.  
    What you remember from your conversation so far is: "{memory}". Use your memory intelligently to 
    keep the conversation going and answer the person's questions. Do not repeat what you remember. Keep the conversation natural and limit your responses to 1-3 sentences.  
    If the person indicates they want to stop the conversation, say goodbye and end the conversation.  
    \n\n
    """ 
        
    messages = [
        SystemMessage(
            content=promptTemplate
        ),
        AIMessage(
            content=last_response
        ),
        HumanMessage(
            content=prompt
        ),
    ]
    
    remember(last_response, prompt)
    with get_openai_callback() as cb:        
        res = llm(messages)
        response = res.content   
        print(cb)        
        return response
   

   

