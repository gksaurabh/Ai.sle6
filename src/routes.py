from flask import Flask, jsonify, request
from db import *
from embeddings import *
from queryRAG import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


#initialize our API and as soon as API loads, initialize the DB with calculated embeddings. 
@app.route("/")
def initalize_API():
    try:
        print("API is now running, please wait as we load our inventory.")
        
        products = get_products()
        initializeDB(products)

        #if successful, return message with status code 200
        return (jsonify({"message": "Inventory has been initialized successfully"}), 200)
    
    except Exception as e:
        #if exception, return ERROR with status code of 500
        return (jsonify({"ERROR": f"Something went wrong: {str,e}"}), 500)

#This will handle our search and RAG component
@app.route("/search", methods=["POST"])
def search():
    #Query is loaded through the body
    data = request.json
    query = data.get('query', '')
    
    #just a check to make sure query is formatted correctly
    if not query:
        return jsonify({"error":"Please enter a query parameter"}), 400
    
    #send query through the rag_handler and return the result. if exception is thrown send ERROR 500 code.
    try:
        result = query_rag_handler(query)
        print("RESULT\n=============================\n" + result)

        return jsonify("result",result), 200

    except Exception as e:
        return jsonify({"ERROR":f"Something went wrong: {str,e}"}), 500