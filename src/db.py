import lancedb
import pandas as pd
import requests

#create anmd connect to a local lanceDB database
    # unable to use the asynchronous function as the documentation for LanceDB
    # mentioned that embeddings are only available for synchronous. 
def connectDB(uri):
    db = lancedb.connect(uri)

# the below function will get all the product data from the fakestoreAPI
def fetchDataFromAPI():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url) #track the response from the server as a variable to help with further logic

    # If the status code is 200, meaning everything went well. Return products.json
    # else return an exception. 
    if response.status_code == 200:
        productsJSON = response.json()
        return productsJSON
    else:
        return Exception("Failed to get data from {url}. Status: {response.status_code}") 


def populateProductsInDB(uri):
    connectDB(uri)
    products = fetchDataFromAPI()



