import unittest
from sentence_transformers import SentenceTransformer

from embeddings import *

class TestEmbeddings(unittest.TestCase):
    #this is to test if the embedding model has been installed correctly by checking if model return type is of SentenceTransformer
    def test_model(self):
        self.assertIsInstance(model, SentenceTransformer)
        print("TEST: model completed. PASS")

    def test_create_embeddings(self):
        test_embedding = create_embeddings("Blue Brown Bear")
        self.assertEqual(len(test_embedding), 384)# 384 is chosen since that is the dimension size for this embedding
        print("TEST: create_embeddings() completed. PASS")

    def test_create_query_embedding(self):
        test_query_embedding = create_query_embedding("Would you consider this a query?")
        self.assertEqual(len(test_query_embedding), 384) #same logic as the above test function.
        print("TEST: create_query_embedding() completed. PASS")

    def test_combine_chunked_embeddings(self):
        test_headersWeights = {
            "title": 0.6,
            "description": 0.4,
            "price": 0.0,
            "rating_rate": 0.0,
            "category": 0.00
            }
        
        test_product = {
                "id": 1,
                "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
                "price": 109.95,
                "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
                "category": "men's clothing",
                "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg",
                "rating_rate": 3.2,
                "count": 120
                }
        
        # same logic as before since the embedding dimensions do not change.
        self.assertEqual(len(combine_chunked_embeddings(test_headersWeights, test_product)), 384) 
    