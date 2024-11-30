import lancedb

#create a connection. URI example: "data/lanceDB" this also returns the DB
def get_DB(uri):
    db = lancedb.connect(uri)
    return db

#create a table using a pandas data frame passed through the parameter
#the database is also passed through the parameter.
def create_table_from_Dataframe(table_Name, dataframe, database):
    # here I am using only the synchrounous client for LanceDB
    table = database.create_table(table_Name, data=dataframe)

#get table if table name is found in the data base
# if not found create a table given the schema. 
def get_table(database, table_name, schema):
    if table_name in database.table_names():
        return database.open_table(table_name)
    else:
        return database.create_table(table_name, schema)
    

    