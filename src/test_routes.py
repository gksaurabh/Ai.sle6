import unittest

from routes import app

#create the test class which will contain functions for each route.
class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    #testing hello world route with "/"
    #if status code is 200 then test will pass and 
    #if it returns "hello world" it will pass
    def test_hello_world(self):
        respone = self.app.get("/")
        self.assertEqual(respone.status_code, 200)
        self.assertEqual(respone.data.decode(), "<p>Hello, World!</p>")
    
    #this will be our clean up function. 
    def tearDown(self) -> None:
        pass

if __name__ == "__main__":
    unittest.main()