import unittest
import lancedb
import pandas as pd

from db import *

class TestDB(unittest.TestCase):
    def test_fetchDataFromAPI(self):
        self.assertEqual(len(fetchDataFromAPI()), 20)
        print("TEST: fetchDataFromAPI() completed. PASS")
    
    def test_fetchDataFromCSV(self):
        path = 'products.csv'
        products = []
        fetchDataFromCSV(path,products)
        self.assertEquals(len(products), 80)
        print("TEST: fetchDataFromCSV() completed. PASS")

    def test_get_db(self):
        uri = "lancedb"

        print(get_DB(uri))
        self.assertIsNot(get_DB(uri), None)
        print("TEST: get_db() completed. PASS")

    def test_create_table_from_Dataframe(self):
        uri = "lancedb"
        test_db = get_DB(uri)
        test_data = [{"test_key1":"test_value1","test_key2":"test_value2"}]
        test_dataframe = pd.DataFrame(test_data)

        create_table_from_Dataframe("test_table", test_dataframe, test_db)

        self.assertIn("test_table",test_db.table_names())
        print("TEST: create_table_from_Dataframe() completed. PASS")

    def test_get_table(self):
        uri = "lancedb"
        test_db = get_DB(uri)
        
        self.assertIsNot(get_table(test_db, "test_table", None), None)
        print("TEST: test_get_table() completed. PASS")


    def test_get_products(self):
        test_products = get_products()

        self.assertEqual(len(test_products), 100)
        print("TEST: test_get_products() completed. PASS")

    def test_initializeDB(self):
        test_products = get_products()

        test_init = initializeDB(test_products)

        self.assertEqual(test_init, None)
        print("TEST: test_initializeDB() completed. PASS")



if __name__ == "__main__":
    unittest.main()