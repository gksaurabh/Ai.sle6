import unittest


from queryRAG import *

class TestQueryRAG(unittest.TestCase):
    def test_query_rag_handler(self):
        query = "i would like to buy some shoes"

        #probably not the correct way to do this
        # check if query_rag_handler returns a string (which is a string)
        self.assertIsInstance(query_rag_handler(query),str)
        print("TEST: query_rag_handler() completed. PASS")

if __name__ == "__main__":
    unittest.main()