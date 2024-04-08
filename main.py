from pymongo import MongoClient
from CRUD_Operations import insert_data
import CRUD_Operations
import inspect
import json

try:
    client = MongoClient()  # normally it should be 'mongodb://localhost:27017/'

    selected_db = None
    while not selected_db: #asking the user to choose the database available
        print("Available databases:")
        databases = client.list_database_names()
        i = 0
        for db in databases:
            i += 1
            print(f"{i}. {db}")
        selected_db = input("Select a database: ")

    database = client[selected_db]
    print(f"Selected database: {selected_db}")

    selected_collection = None
    while not selected_collection: #asking the user to choose the corresponding collection
        print(f"Available collections in {selected_db}:")
        collections = database.list_collection_names()
        for collection in collections:
            print(collection)
        selected_collection = input("Select a collection: ")

    print(f"Selected collection: {selected_collection}")

    available_functions = [name for name, obj in inspect.getmembers(CRUD_Operations) if inspect.isfunction(obj)]
        
    print("Available functions:") # print available functions
    i=0
    for function_name in available_functions: 
        i += 1
        print(f"{i}. {function_name}")

    selected_function = input("Select a function: ")
    
    if selected_function in available_functions:
        
        if selected_function == "insert_data": # Prompt for additional arguments based on the selected function
            data_path = input("Enter the path of the data file: ")
            with open(data_path) as file:
                data = json.load(file)
            insert_data(data, selected_db, selected_collection) # we pass those arguments to the functios
        else:
            print("Invalid function name!")
    else:
        print("Function not found!")

except Exception as e:
    print(f"An error occurred: {e}")