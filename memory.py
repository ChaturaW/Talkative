from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import faiss
import os
import numpy as np

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
VECTOR_DB_DIR = "faiss_memory"

# faissDb = FAISS.from_texts([""], embeddings)

def initialize():
    global faissDb
    print("initializing memory...")
    indexfile = os.path.join(VECTOR_DB_DIR,'index.faiss')
    if os.path.exists(indexfile):
        faissDb = FAISS.load_local(VECTOR_DB_DIR, embeddings)
    else:
        faissDb = FAISS.from_texts([""], embeddings)
        faissDb.save_local(VECTOR_DB_DIR)
    

def remember(i_said, person_said):    
    faissDb.add_texts([f"AIMessage: {i_said}, person:{person_said} \n"])   

def recall(prompt):
    memory = ""
    chunks = faissDb.similarity_search_with_score(prompt)
    for chunk in chunks:          
        score = chunk[1]                
        if score < 1.5:            
            memory += chunk[0].page_content
    
    return memory

def recallLongTermMemories():
    indexfile = os.path.join(VECTOR_DB_DIR,'index.faiss')    
    # load index, index will be of type IndexPreTransform
    index = faiss.read_index(indexfile, faiss.IO_FLAG_ONDISK_SAME_DIR)
    # print(index.ntotal)
    num_vectors = index.ntotal
    # Create arrays to store embeddings    
    saved_embeddings = np.zeros((num_vectors, index.d), dtype=np.float32)

    vector_db = FAISS.load_local(VECTOR_DB_DIR, embeddings)
    memory = ""
    K = len(saved_embeddings)
    print(f"K: {K}")
    if K > 0:
        chunks = vector_db.similarity_search_by_vector(saved_embeddings[0], K)
        for chunk in chunks:                            
            memory += chunk.page_content

    return memory
    

def eraseLongTermMemory():
    # Delete the index.faiss file
    indexfile = os.path.join(VECTOR_DB_DIR, 'index.faiss')
    if os.path.exists(indexfile):
        os.remove(indexfile)

    # Delete the index.pkl file
    pklfile = os.path.join(VECTOR_DB_DIR, 'index.pkl')
    if os.path.exists(pklfile):
        os.remove(pklfile)

def rememberLongTerm():    
    faissDb.save_local(VECTOR_DB_DIR)

def organiseLongTermMemory(memory):
    eraseLongTermMemory()
    initialize()
    faissDb.add_texts([memory])    
    faissDb.save_local(VECTOR_DB_DIR)