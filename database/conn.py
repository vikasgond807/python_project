import certifi
import os
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv


load_dotenv()


class DBConnection:
    def __init__(self,connection_string=None) -> None:
        self.url=connection_string or os.getenv("DB_CONNECTION_STRING")
        self.create_database()

    def get_client(self):
        try:
            client = MongoClient(self.url,tlsCAFile=certifi.where())
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            return client
        except DBConnectionError as err:
            raise DBConnectionError('Failed to connect to the Mongo database',err)
        
    def create_database(self):
        client=self.get_client()

        if 'mydatabase' not in client.list_database_names():
            print('Creating a new database {}'.format("mydatabase"))
            db = client["mydatabase"]
        else:
            print('Database already exists')

        #Check if the collection exists in the table 
        if "goals" not in client['mydatabase'].list_collection_names():
            print("creating collection {} in the database {}".format("goals","mydatabase"))
        else:
            print("Collection already exists ")


        
            
class DBConnectionError(Exception):
    pass


