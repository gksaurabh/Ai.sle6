import requests
import pandas as pd
import csv
from db import get_DB, create_table_from_Dataframe, get_table
from embeddings import create_embeddings, create_query_embedding, combine_chunked_embeddings
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import EmbeddingFunctionRegistry, get_registry
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM



db = get_DB("lancedb")
table = get_table(db, "products", None)

#input our querries 
query = input("Please enter your query: \n")
k = 5

#calulate the text embedding for our querry
query_embedding = create_query_embedding(query)

#perform a distance search
search_result = table.search(query_embedding).limit(5).to_df()
#print(search_result)

# context = search_result


PROMPT_TEMPLATE = """You are an assistant for a general store, similar to Walmart. Your role is to interpret customer requests, identify the relevant department, and provide availability and pricing information based on the following context:

Store Departments:
1. Electronics
2. Men's Clothing
3. Women's Clothing
4. Jewelry
5. Home Decor
6. Grocery
7. Toys
8. Sports Equipment

Instructions:
1. Carefully analyze the customer's question and determine which department their request falls under.
2. If the product is not explicitly mentioned, use reasoning to infer the appropriate department and suggest relevant products.
3. Provide availability and pricing details in a natural, conversational tone.
4. If you cannot find any relevant products, respond politely and let the customer know.
5. Do not ask any follow up questions.

Customer Question:
"{customer_question}"

Contextual Information:
{context}

Response Format:
- **Natural Language Response**: Write a conversational response summarizing your findings.
- **Details**:
  - **Department**: [Department Name]
  - **Product(s)**: [List of product names and descriptions if available]
  - **Price(s)**: [List of product prices, or indicate "Unavailable"]
  - **Availability**: [In Stock/Out of Stock/Unavailable]

"""

prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

model = OllamaLLM(model="llama3.2")

chain = prompt | model

result = chain.invoke({"context" : search_result, "customer_question": query})

print(result)
