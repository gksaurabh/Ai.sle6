import pandas as pd
import requests
import csv
import lancedb
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import get_registry
from embeddings import create_embeddings, create_query_embedding, combine_chunked_embeddings

# method to fetch data from the fake store API
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
        return Exception(f"Failed to get data from {url}. Status: {response.status_code}") 

#  void method to load any local products we have in our products.csv
# but uses parameter variable manipulation.
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



#create a connection. URI example: "data/lanceDB" this also returns the DB
def get_DB(uri):
    db = lancedb.connect(uri)
    return db

#create a table using a pandas data frame passed through the parameter
#the database is also passed through the parameter.
def create_table_from_Dataframe(table_name, dataframe, database):
    if table_name in database.table_names():
        print("table already exists, updating table with new content")
        database.drop_table(table_name)
        return database.create_table(table_name, data=dataframe)
    else:
        # here I am using only the synchrounous client for LanceDB
        return database.create_table(table_name, data=dataframe)

#get table if table name is found in the data base
    # if not found create a table given the schema. 
def get_table(database, table_name, schema):
    if table_name in database.table_names():
        return database.open_table(table_name)
    else:
        return database.create_table(table_name, schema)

# get all the products as the default value which is an array of arrays. 
    # [ [   
    #       {"id":1,
    #        "name": name,
    #        ...
    #       }   
    # ] ]
def get_products():
    try:
        products = fetchDataFromAPI()
        print("Fetched products from API successfully.")

        #add products from the CSV
        fetchDataFromCSV('products.csv', products)
        print("Fetched products from CSV successfully.")
        return products
    except Exception as e:
        print("Error:", str(e))
        return e
    

def initializeDB(products):

    # Database handling.

    #initialize the data base
    db = get_DB("lancedb")
    
    # A dictionary is created to help with finetuning our embeddings. 
        # the advandage of this is that we can choose different weights for future queries.
        # For example if a customer asks what is your lowest price shoes, then we can use entity recognition to 
        # recognize the words "price" and "show" along with the descriptive "low" to change the weightage of 
        # the price to a higher value. 
        # we can also add more headers to consider into our embeddings. 
    if "products" not in db.table_names():
        print("Creating Table - please wait")
        headersWeights = {
            "title": 0.6,
            "description": 0.4,
            "price": 0.0,
            "rating_rate": 0.0,
            "category": 0.00
            }

        print("Calculating Embeddings")
        #itterate through each item and calculate the combined chunked embeddings
        for item in products:
            #item["vector"] = create_embeddings(item["title"])
            item["vector"] = combine_chunked_embeddings(headersWeights, item)

        #convert our products into a data frame.
        df = pd.DataFrame(products)

        #insert df into our LanceDB table.
        table = create_table_from_Dataframe("products",df,db)
        print("Table has been created")


if __name__ == "__main__":
    products = get_products()
    initializeDB(products)