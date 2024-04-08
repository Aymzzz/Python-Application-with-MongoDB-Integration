import pymongo
from pymongo import MongoClient, errors
import importlib
import inspect
#from getpass import getpass
import json

try:
    client = MongoClient()  # normally it should be 'mongodb://localhost:27017/'

    print("Database connection has been established!")
#================================Insert Data=======================================    
    def insert_data(database, collection_name, file_path):
        try:
            collection = database[collection_name]
            
            with open(file_path) as file:
                data = json.load(file)
                
            if isinstance(data, list):
                result = collection.insert_many(data)
                print(f"Inserted {len(result.inserted_ids)} documents.")
            else:
                print("Invalid data format. Expected a list of documents.")
        except Exception as e:
            print(f"Error: {e}")
#================================Create Data=======================================
    def create_data(database, collection_name):
        try:
            collection = database[collection_name]
            while True:
                data = {}
                for field in ['type_measure', 'sensor_name', 'time', 'dev_id', 'battery', 'temperature', 'humidity', 'solarpanel']:
                    data[field] = input(f"Enter the value for {field}: ")

                insert_result = collection.insert_one(data)
                print("Data created successfully!")
                
                print("Inserted document ID:", insert_result.inserted_id)

                choice = input("Do you want to insert another document? (y/n): ")
                if choice.lower() != 'y':
                    break
        except Exception as e:
            print(f"Error: {e}")
#================================Read Data=======================================            
    def read_data(database, collection_name, criteria):
        try:
            collection = database[collection_name]
            query = {} # this will show everything
            if criteria:
                query = eval(criteria) # Example: criteria = "{'field': 'value'}"
            result = collection.find(query)
            if result:
                print("Retrieved data:")
                for document in result:
                    print(document)
            else:
                print("No matching documents found.")
        except Exception as e:
            print(f"Error: {e}")

except (pymongo.errors.ConnectionFailure, pymongo.errors.ServerSelectionTimeoutError) as e:
    print(f"An error occurred while connecting to MongoDB: {e}")
    
except Exception as e:
    print(f"An unexpected error occurred: {e}")