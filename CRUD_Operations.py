import pymongo
from pymongo import MongoClient, errors
import importlib
import inspect

try:
    client = MongoClient()  # normally it should be 'mongodb://localhost:27017/'

    db_name = 'Project-Sensors'
    database = client[db_name]
    
    print("Database connection has been established!")
    
    def insert_data(collection_name, data): # insert data into database
        try:
            collection = database[collection_name]
            inserted_id = collection.insert_one(data).inserted_id
            print(f"Data inserted with ID: {inserted_id}")
        except Exception as e:
            print(f"Error: {e}")
    
    def list_databases(): # list available databases
        databases = client.list_database_names()
        print("Available databases:")
        for db in databases:
            print(db)
    
    
    def list_collections(db_name): # list collections in a database
        db = client[db_name]
        collections = db.list_collection_names()
        print(f"Collections in database '{db_name}':")
        for collection in collections:
            print(collection)

    
except (pymongo.errors.ConnectionFailure, pymongo.errors.ServerSelectionTimeoutError) as e:
    print(f"An error occurred while connecting to MongoDB: {e}")
    
except Exception as e:
    print(f"An unexpected error occurred: {e}")