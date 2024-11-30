import lancedb
import time
import ollama
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import EmbeddingFunctionRegistry
import pandas as pd
import pyarrow as pa
import requests


def fetchDataFromAPI():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url) #track the response from the server as a variable to help with further logic

    # If the status code is 200, meaning everything went well. Return products.json
    # else return an exception. 
    if response.status_code == 200:
        result = response.json()
        return result
    else:
        raise Exception("Failed to get data from {url}. Status: {response.status_code}") 
        
