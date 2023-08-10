import os

from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.callbacks import get_openai_callback
from memory import initialize, recall, remember, rememberLongTerm, recallLongTermMemories, organiseLongTermMemory

from dotenv import load_dotenv
load_dotenv()  # Load the environment variables from the .env file

apikey = os.getenv('apikey')  # Access the 'apikey' variable

os.environ['OPENAI_API_KEY'] = apikey
os.environ['TOKENIZERS_PARALLELISM'] = "false"
# Set the language for the text-to-speech conversion
language = "en"

llm = ChatOpenAI(temperature=0.9, model_name="gpt-3.5-turbo")

def initialize_conversation():
    initialize()  
    long_term_memory = recallLongTermMemories()
    print(f"long term memory---\n{long_term_memory}")  

def think(prompt, last_response):   
    if prompt == "":
        memory = recallLongTermMemories()        
    else:
        memory = recall(prompt)
    
    promptTemplate = f"""Your name is Sarah. You are a companion for a person. You are always friendly, polite and helpful. 
    At the start of the conversation greet the person and introduce yourself. You may use the person's name in the conversation to make it more personal.            
    Have a casual conversation about family, daily activities, interests, life.  
    What you remember from your conversation so far is: "{memory}". Use your memory to 
    relate to things you talked about before. Keep the conversation natural and limit your responses to 1-2 sentences.  
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
   

def end_conversation(): 
    rememberLongTerm()   
    # memory = recallLongTermMemories()
    # print("current memory:\n" + memory)
    # prompt = f"Summarize the following conversation: {memory}"
    # openAILLM = OpenAI(temperature=0.9, model_name="gpt-3.5-turbo")

    # with get_openai_callback() as cb:        
    #     summary = openAILLM(prompt)
    #     # response = res.content   
    #     print(cb)        
    #     print(summary)
        
    # organiseLongTermMemory(summary)
   

