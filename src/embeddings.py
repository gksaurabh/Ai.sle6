from sentence_transformers import SentenceTransformer
import numpy as np


# defining my model from the SentenceTransformers library.
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# the following functions will create embeddings based on input text parameter
def create_embeddings(text):
    return model.encode(text)

#create an embedding for our querries
def create_query_embedding(query):
    return model.encode(query)

# going to create a chunked embedding to improve search accuracy and take in other fields as embeddings such as title, price, rating, etc. 
# takes in a diction of headers (ex. title, description, price, rating) along with their weights, and the individual item.  
def combine_chunked_embeddings(headersWeights, product):
    chunk_embeddings = []

    #itterate through the headers in the item and calculate the embeddings and append them into one. 
    for header, weight in headersWeights.items():
        text = str(product[header])
        embedding = create_embeddings(text) * weight
        chunk_embeddings.append(embedding)
    # take the vector mean and calculate the combined embedding.    
    combined_embeddings = np.sum(chunk_embeddings, axis=0)
    return combined_embeddings
