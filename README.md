
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

## Contributing
If you'd like to contribute to this project, feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- [LanceDB Documentation](https://lancedb.ai/docs)
- [Sentence Transformers](https://www.sbert.net/)
- [Ollama](https://ollama.com/)