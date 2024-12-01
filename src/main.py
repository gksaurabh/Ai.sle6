import requests
import pandas as pd
import csv
from db import get_DB, create_table_from_Dataframe, get_table
from embeddings import create_embeddings, create_query_embedding, combine_chunked_embeddings
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import EmbeddingFunctionRegistry, get_registry


# get data from API. Made this into a function in order to test easily. or change API
def fetchDataFromAPI():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url) #track the response from the server as a variable to help with further logic

    # If the status code is 200, meaning everything went well. Return products.json
    # else return an exception. 
    if response.status_code == 200:
        result = response.json()

        # Flatten the rating into two different columns 
        for item in result:
            item["rating_rate"] = item["rating"]["rate"]
            item["rating_count"] = item["rating"]["count"]
            del item["rating"]

        return result
    else:
        raise Exception(f"Failed to get data from {url}. Status: {response.status_code}") 


def fetchDataFromCSV(csv_file_path, products):
    with open(csv_file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert row into the desired dictionary structure
            product = {
                "id": int(row["id"]),
                "title": row["title"],
                "price": float(row["price"]),
                "description": row["description"],
                "category": row["category"],
                "image": row["image"],
                "rating_rate": float(row["rating_rate"]),
                "rating_count": int(row["rating_count"])
            }
            products.append(product) 



#first fetch the data from the API, raise exception if unable to fetch
try:
    products = fetchDataFromAPI()
    print("Fetched products from API successfully.")

    #add products from the CSV
    fetchDataFromCSV('products.csv', products)
    print("Fetched products from CSV successfully.")
except Exception as e:
    print("Error:", str(e))



# Database handling.

#initialize the data base
db = get_DB("lancedb")

headers = ["title", "description", "price", "rating_rate", "category"]
#itterate through each item and calculate the combined chunked embeddings
for item in products:

    item["vector"] = combine_chunked_embeddings(headers, item)

#convert our products into a data frame.
df = pd.DataFrame(products)

#insert df into our LanceDB table.
table = create_table_from_Dataframe("products",df,db)

#input our querries 
query = "what womens pants do you have that i can wear exercising?"
k = 5

#calulate the text embedding for our querry
query_embedding = create_query_embedding(query)

#perform a distance search
search_result = table.search(query_embedding).limit(5).to_df()
print(search_result)

context = search_result

