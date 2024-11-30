import requests
import pandas as pd
from db import get_DB, create_table_from_Dataframe, get_table
from embeddings import create_embeddings, create_query_embedding
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import EmbeddingFunctionRegistry


# get data from API. Made this into a function in order to test easily. or change API
def fetchDataFromAPI():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url) #track the response from the server as a variable to help with further logic

    # If the status code is 200, meaning everything went well. Return products.json
    # else return an exception. 
    if response.status_code == 200:
        result = response.json()
        return result
    else:
        raise Exception(f"Failed to get data from {url}. Status: {response.status_code}") 


#first fetch the data from the API, raise exception if unable to fetch
try:
    products = fetchDataFromAPI()
    print("Fetched products successfully.")
except Exception as e:
    print("Error:", str(e))

# Database handling.

#initialize the data base
db = get_DB("lancedb")


# Flatten the rating into two different columns and create embeding for descriptions.
for item in products:
    item["rating_rate"] = item["rating"]["rate"]
    item["rating_count"] = item["rating"]["count"]
    del item["rating"]

    item["embedding"] = create_embeddings(item["description"])

#convert our products into a data frame.
df = pd.DataFrame(products)

#insert df into our LanceDB table.
table = create_table_from_Dataframe("products",df,db)


df = table.to_pandas()

print(df.head())