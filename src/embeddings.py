from sentence_transformers import SentenceTransformer


# defining my model from the SentenceTransformers library.
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# the following functions will create embeddings based on input text parameter
def create_embeddings(text):
    return model.encode(text)

#create an embedding for our querries
def create_query_embedding(query):
    return model.encode(query)