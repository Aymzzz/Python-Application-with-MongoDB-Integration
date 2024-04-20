from pymongo import MongoClient
from CRUD_Operations import delete_data, insert_data, read_data, create_data, update_data
import CRUD_Operations
import inspect
import json

try:
    client = MongoClient()  # normally it should be 'mongodb://localhost:27017/'

    selected_db = None
    while not selected_db: #asking the user to choose the database available
        print("Available databases:")
        databases = client.list_database_names()
        for i, db in enumerate(databases, 1):
            print(f"{i}. {db}")
        selected_db_index = int(input("Select a database number: ")) - 1
        selected_db = databases[selected_db_index]

    print(f"Selected database: {selected_db}")

    database = client[selected_db]

    print(f"Available collections in {selected_db}:")
    collections = database.list_collection_names()
    for i, collection in enumerate(collections, 1):
        print(f"{i}. {collection}")

    selected_collection_index = int(input("Select a collection number: ")) - 1
    if selected_collection_index < 0 or selected_collection_index >= len(collections):
        raise ValueError("Invalid collection number!")
    selected_collection = collections[selected_collection_index]

    print(f"Selected collection: {selected_collection}")

    available_functions = [name for name, obj in inspect.getmembers(CRUD_Operations) if inspect.isfunction(obj)]
        
    print("Available functions:") # print available functions
    for i, function_name in enumerate(available_functions, 1): 
        print(f"{i}. {function_name}")

    selected_function_index = int(input("Select a function number: ")) - 1
    selected_function = available_functions[selected_function_index]

    match selected_function:
        case "insert_data":
            file_path = input("Enter the path of the data file: ")
            insert_data(database, selected_collection, file_path)
            
        case "create_data":
            create_data(database, selected_collection)
            
        case "read_data":
            criteria = input("Enter the criteria: ")
            read_data(database, selected_collection, criteria)
            
        case "update_data":
            update_data(database, selected_collection)
            
        case "delete_data":
            delete_data(database, selected_collection)
            
        case _:
            print("Invalid function name!")

except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An error occurred: {e}")