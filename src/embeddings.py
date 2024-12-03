from sentence_transformers import SentenceTransformer
from langchain_openai import OpenAIEmbeddings
import os
import numpy as np


# defining my model from the SentenceTransformers library.
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')


#model = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key=os.getenv('OPENAI_API_KEY')) #experimented with different model - lower accuracy


# the following functions will create embeddings based on input text parameter
def create_embeddings(text):
    return model.encode(text)   #return np.array(model.embed_documents(text)[0]) #use only if using openAI embedding model

#create an embedding for our querries
def create_query_embedding(query):
    return model.encode(query)  #return np.array(model.embed_query(query))  #use only if using openAI embedding model


# going to create a chunked embedding to improve search accuracy and take in other fields as embeddings such as title, price, rating, etc. 
# takes in a diction of headers (ex. title, description, price, rating) along with their weights, and the individual item.  
def combine_chunked_embeddings(headersWeights, product):
    chunk_embeddings = []

    for header, weight in headersWeights.items():   #itterate through the headers in the item and calculate the embeddings and append them into one. 
        text = str(product[header])
        embedding = create_embeddings(text) * weight
        chunk_embeddings.append(embedding)

    # take the vector weighted sum and calculate the combined embedding.
    combined_embeddings = np.sum(chunk_embeddings, axis=0)  #chunk_embeddings = np.array(chunk_embeddings)    #use only if using openAI embedding model
    print(combined_embeddings)
    return combined_embeddings
