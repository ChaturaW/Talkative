from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

faiss = FAISS.from_texts([""], embeddings)

def remember(i_said, person_said):    
    faiss.add_texts([f"AIMessage: {i_said}, person:{person_said} \n"])   

def recall(prompt):
    memory = ""
    chunks = faiss.similarity_search_with_score(prompt)
    for chunk in chunks:          
        score = chunk[1]                
        if score < 1.5:            
            memory += chunk[0].page_content
    
    return memory