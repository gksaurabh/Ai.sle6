import unittest
import requests

from routes import app

#create the test class which will contain functions for each route.
class TestRoutes(unittest.TestCase):
    URL = "http://127.0.0.1:5000"

    # test the initailize API route which is the base url.
    def test_initialize_API(self):
        response = requests.get(self.URL)
        result = (response.json())

        #check if status code is 200, meaning everything worked out
        self.assertEqual(response.status_code, 200)
        
        #check if the response is {'message': 'Inventory has been initialized successfully'}
        self.assertEqual(result.get('message'), "Inventory has been initialized successfully")
        
        print("TEST: initialize_API() completed. PASS")

    # test the search Rag API.
    def test_search(self):
        #defint the query
        query = {'query':"i am looking for some shoes"}

        #We use the requests body parameter and set content type to json and build our url
        response = requests.get(self.URL + "/search",json=query)
       
       #if we get a status code of 200 then our test has passed.
        self.assertEqual(response.status_code, 200)

        print("TEST: search() completed. PASS")



if __name__ == "__main__":
    unittest.main()