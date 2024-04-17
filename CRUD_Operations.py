import pymongo
from pymongo import MongoClient, errors
import importlib
import inspect
#from getpass import getpass
import json

try:
    client = MongoClient()  # normally it should be 'mongodb://localhost:27017/'

    print("Database connection has been established!")
#================================Create Database & Collections=======================================   

    def create_database(database_name):
        try:
            database = client[database_name]
            print(f"Database {database_name} has been created!")
        except errors.DuplicateKeyError:
            print(f"Database {database_name} already exists!")
        except Exception as e:
            print(f"Error: {e}")

    def create_collection(database_name, collection_name):
        try:
            database = client[database_name]
            collection = database[collection_name]
            print(f"Collection {collection_name} has been created!")
        except errors.DuplicateKeyError:
            print(f"Collection {collection_name} already exists!")
        except Exception as e:
            print(f"Error: {e}")
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
            field_names = collection.find_one().keys()
            
            while True:
                data = {}
                for field in field_names:
                    value = input(f"Enter the value for {field}: ")
                    data[field] = None if value == '' else value

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
#================================Update Data======================================= 
    def update_data(database, collection_name):
        try:
            collection = database[collection_name]
        # all the possible "update" ops
            print("Choose the update operation:")
            print("1. Update a single document")
            print("2. Update multiple documents")
            print("3. Replace a document")
            
            choice = input("Enter your choice (1/2/3): ")

            if choice == '1':
                filter_query = input("Enter the filter query for the document to update: ")
                filter_query = json.loads(filter_query)
                update_query = input("Enter the update query: ")
                update_query = json.loads(update_query)
                update_result = collection.update_one(filter_query, update_query)
                print("Data updated successfully!")
                print("Number of documents matched:", update_result.matched_count)
                print("Number of documents modified:", update_result.modified_count)
                
            elif choice == '2':
                filter_query = input("Enter the filter query for multiple documents to update: ")
                filter_query = json.loads(filter_query)
                update_query = input("Enter the update query: ")
                update_query = json.loads(update_query)
                update_result = collection.update_many(filter_query, update_query)
                print("Data updated successfully!")
                print("Number of documents matched:", update_result.matched_count)
                print("Number of documents modified:", update_result.modified_count)
                
            elif choice == '3':
                filter_query = input("Enter the filter query for the document to replace: ")
                filter_query = json.loads(filter_query)
                replacement_data = {}
                field_names = collection.find_one(filter_query).keys()
                for field in field_names:
                    value = input(f"Enter the new value for {field}: ")
                    replacement_data[field] = value
                replace_result = collection.replace_one(filter_query, replacement_data)
                print("Data replaced successfully!")
                print("Number of documents matched:", replace_result.matched_count)
                print("Number of documents modified:", replace_result.modified_count)
            else:
                print("Invalid choice. Please try again.")
                
        except Exception as e:
            print(f"Error: {e}")
#================================Delete Data======================================= 
    def delete_data(database, collection_name):
        try:
            collection = database[collection_name]
            print("Choose the delete operation:")
            print("1. Delete a single document")
            print("2. Delete multiple documents")
            choice = input("Enter your choice (1/2): ")

            if choice == '1':
                filter_query = input("Enter the filter query for the document to delete: ")
                filter_query = json.loads(filter_query)
                documents = list(collection.find(filter_query))
                print("Matching documents:")
                for document in documents:
                    print(document)
                delete_result = collection.delete_one(filter_query)
                print("Data deleted successfully!")
                print("Number of documents deleted:", delete_result.deleted_count)
                
            elif choice == '2':
                filter_query = input("Enter the filter query for multiple documents to delete: ")
                filter_query = json.loads(filter_query)
                delete_result = collection.delete_many(filter_query)
                print("Data deleted successfully!")
                print("Number of documents deleted:", delete_result.deleted_count)
            else:
                print("Invalid choice. Please try again.")
                
        except Exception as e:
            print(f"Error: {e}")
                
 
except (pymongo.errors.ConnectionFailure, pymongo.errors.ServerSelectionTimeoutError) as e:
    print(f"An error occurred while connecting to MongoDB: {e}")
    
except Exception as e:
    print(f"An unexpected error occurred: {e}")