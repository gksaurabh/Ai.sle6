
# Retail Store RAG Model (readme created by ChatGPT)

This project implements a Retrieval-Augmented Generation (RAG) model for a retail store with 120 products across 8 departments. The model accepts customer queries, directs them to the appropriate department, and displays related products with their prices and availability. It provides a seamless, AI-enhanced product search experience.

## Features
- **Query Routing**: Directs customers to the most relevant department based on their queries.
- **Product Recommendations**: Displays related products, including their prices and availability.
- **AI-Powered Search**: Utilizes LanceDB for vector storage, Sentence Transformers' `all-miniLM-L6-v2` for text embedding, and `llama3.2` as the LLM for query generation and enhancement.
- **Similarity Search**: Employs nearest neighbor search from LanceDB's documentation with weighted embeddings calculated from product attributes.

## Technologies Used
- **Vector Store**: [LanceDB](https://lancedb.ai)
- **Text Embedding**: [Sentence Transformers - `all-miniLM-L6-v2`](https://www.sbert.net/)
- **Language Model**: `llama3.2` (via Ollama)
- **Backend Framework**: Flask

## Requirements
- Python 3.8 or above
- [Ollama](https://ollama.com/) (for `llama3.2` LLM)
- LanceDB
- Flask
- Other dependencies listed in `requirements.txt`

## Installation and Usage

### Step 1: Install Ollama and Setup Llama3.2
1. Install [Ollama](https://ollama.com/).
2. Install the `llama3.2` model:
   ```bash
   ollama serve
   ```

### Step 2: Install Dependencies
Install all required Python packages:
```bash
pip install -r requirements.txt
```

### Step 3: Run the Flask Server
Start the Flask server:
```bash
flask --app routes run
```

## How It Works
1. The customer inputs a query (e.g., "Show me summer dresses").
2. The model calculates embeddings using a weighted sum of product attributes.
3. LanceDB performs a similarity search to find the most relevant products.
4. The results, including department, product details, prices, and availability, are returned to the customer.

## Acknowledgements
- [LanceDB Documentation](https://lancedb.ai/docs)
- [Sentence Transformers - all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- [Ollama](https://ollama.com/)
- [Ollama Documentation](https://python.langchain.com/v0.1/docs/integrations/llms/ollama/)
- [Flask Documentation](https://flask.palletsprojects.com/en/stable/)


## Inspiring and Informative Videos

Below is a list of insightful and detailed videos that greatly influenced and guided the development of this project:

- [Python RAG Tutorial (with Local LLMs): AI For Your PDFs | pixegami](https://www.youtube.com/watch?v=2TJxpyO3ei4&t=834s&ab_channel=pixegami)
- [Understanding Vector Similarity Search | KX](https://www.youtube.com/watch?v=qQ8HNRHRRQw&ab_channel=KX)
- [Chang She - LanceDB: lightweight billion-scale vector search for multimodal AI | PyData Global 2023 | PyData](https://www.youtube.com/watch?v=kF1IFBQ_KD4&t=826s&ab_channel=PyData)
- [Ollama and LanceDB: The best combination for Local RAG?| Learn Data with Mark](https://www.youtube.com/watch?v=HcqGiCu2Bjs&ab_channel=LearnDatawithMark)
- [Intro to LanceDB in 2 Minutes | LanceDB](https://www.youtube.com/watch?v=6SweXJhboTA&ab_channel=LanceDB)
- [Learn RAG From Scratch – Python AI Tutorial from a LangChain Engineer | freeCodeCamp.org](https://www.youtube.com/watch?v=sVcwVQRHIc8&t=1148s&ab_channel=freeCodeCamp.org)
- [Flask REST API Python series: How to unit test for your API | unittest Python](https://www.youtube.com/watch?v=dTvJwxrM1VY&ab_channel=CodeWithPrince)
