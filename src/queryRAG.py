import requests
import pandas as pd
import csv
from db import get_DB, create_table_from_Dataframe, get_table
from embeddings import create_embeddings, create_query_embedding, combine_chunked_embeddings
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import EmbeddingFunctionRegistry, get_registry
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM


# This function will handle the query and push it through RAG pipeline. 
def query_rag_handler(query):

  db = get_DB("lancedb")
  table = get_table(db, "products", None)

  
  k = 5

  #calulate the text embedding for our querry
  query_embedding = create_query_embedding(query)

  #perform a distance search
  search_result = table.search(query_embedding).limit(k).to_pandas()
  

  # A prompt template is defined 
  # it is fed the search resuly (distance search from the nearest neighbours) as the context
  # the query is fed as the question.
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
    2. You must mention the specific department, and show availability and prices only for relavent products
    2. If the requested product is unavailable in the context, politely inform the customer that we do not currently have it in stock.
    3. Do not suggest products or departments unless they exist in the provided context.
    4. Always respond in a polite and conversational tone.
    5. Do not ask a question.

  Customer Question:
  "{customer_question}"

  Contextual Information:
  {context}

  Response:
  Do not mention any products that are not similar to the requested one, but If a similar product is found:
  Start your "Head over to <department name>" . Write a conversational response summarizing your findings.
  You must mention the specific department, and show availability, prices, rating, and rating count for the products  
  
  Do not end your response with any follow up questions.
  """

  
  # a prompt variable is created and the our template is fed into LangChains ChatPromptTemplate function.

  prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

  #The LLM model is defined (running locally) llama3.2
  model = OllamaLLM(model="llama3.2")

  # we define our chain saying that first the prompt is created then fed into to the model.
  chain = prompt | model

  # the chain is invoked with its parameter (search_result and query as context and question) and its response is stored as our result
  result = chain.invoke({"context" : search_result, "customer_question": query})

  # return the result as with some extra next line characters wrapped around it. 
  return ("\n" + result + "\n")


if __name__ == "__main__":
  
  query = input("\nPlease enter your query: \n")

  while query != "exit":
    query_rag_handler(query)
    query = input("Please enter your query: \n")
  
  print("Thank you for visiting the store, I will see you another time")
    