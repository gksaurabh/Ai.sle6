import unittest


from queryRAG import *

class TestRoutes(unittest.TestCase):
    def test_query_rag_handler(self):
        query = "i would like to buy some shoes"

        #probably not the correct way to do this
        # check if query_rag_handler returns a string (which is a string)
        self.assertIsInstance(query_rag_handler(query),str)

if __name__ == "__main__":
    unittest.main()