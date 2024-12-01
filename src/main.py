import requests
import pandas as pd
import csv
from db import get_DB, create_table_from_Dataframe, get_table
from embeddings import create_embeddings, create_query_embedding, combine_chunked_embeddings
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import EmbeddingFunctionRegistry, get_registry
from langchain_community.llms.ollama import Ollama



db = get_DB("lancedb")
table = get_table(db, "products", None)

#input our querries 
query = input("Please enter your query: \n")
k = 5

#calulate the text embedding for our querry
query_embedding = create_query_embedding(query)

#perform a distance search
search_result = table.search(query_embedding).limit(5).to_df()
print(search_result)

context = search_result



