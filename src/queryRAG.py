import requests
import pandas as pd
import csv
from db import get_DB, create_table_from_Dataframe, get_table
from embeddings import create_embeddings, create_query_embedding, combine_chunked_embeddings
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import EmbeddingFunctionRegistry, get_registry
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM


def query_rag_handler(query):

  db = get_DB("lancedb")
  table = get_table(db, "products", None)

  
  k = 5

  #calulate the text embedding for our querry
  query_embedding = create_query_embedding(query)

  #perform a distance search
  search_result = table.search(query_embedding).limit(k).to_pandas()
  #print(search_result)

  # context = search_result


  PROMPT_TEMPLATE = """
  You are an assistant for a general store, similar to Walmart. Your role is to interpret and route the question to a specific department, and show availability and prices for the products. You are to only provide accurate responses strictly based on the provided context.

  Store Departments:
    1. Electronics
    2. Men's Clothing
    3. Women's Clothing
    4. Jewelry
    5. Home Decor
    6. Grocery
    7. Toys
    8. Sports Equipment

  **Important Instructions**:
    1. Use only the provided context for your response. Do not fabricate or infer additional information.
    2. You must mention the specific department, and show availability and prices for the products
    2. If the requested product is unavailable in the context, politely inform the customer that we do not currently have it in stock.
    3. Do not suggest products or departments unless they exist in the provided context.
    4. Always respond in a polite and conversational tone.
    5. Never end your response with a question.

  Customer Question:
  "{customer_question}"

  Contextual Information:
  {context}

  Response:
  Write a conversational response summarizing your findings or explaining that no match was found. If no products match, respond like this: 
  "I'm sorry, but we currently do not have any products matching your request." You must mention the specific department, and show availability and prices for the products

  """

  prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

  model = OllamaLLM(model="llama3.2")

  chain = prompt | model

  result = chain.invoke({"context" : search_result, "customer_question": query})

  print("\n" + result + "\n")


if __name__ == "__main__":
  
  query = input("\nPlease enter your query: \n")

  while query != "exit":
    query_rag_handler(query)
    query = input("Please enter your query: \n")
  
  print("Thank you for visiting the store, I will see you another time")
    