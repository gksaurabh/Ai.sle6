import pandas as pd
import lancedb
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import get_registry

#create a connection. URI example: "data/lanceDB" this also returns the DB
def get_DB(uri):
    db = lancedb.connect(uri)
    return db

#create a table using a pandas data frame passed through the parameter
#the database is also passed through the parameter.
def create_table_from_Dataframe(table_name, dataframe, database):
    if table_name in database.table_names():
        print("table already exists")
        return database.open_table(table_name)
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
    

# def configDB():
#     db = get_DB("products")
#     model = get_registry().get("sentence-transformers").create(name="all-MiniLM-L6-v2", device="cpu")

