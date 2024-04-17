from pymongo import MongoClient
from CRUD_Operations import delete_data, insert_data, read_data, create_data, update_data, create_database
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

    match selected_function:
        case "create_database":
            database = input("Enter a name for your database: ")
            create_database(database)

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
    
    # if selected_function in available_functions:
        
    #         # initial operation which is data insertion
    #     if selected_function == "insert_data":
    #         file_path = input("Enter the path of the data file: ")
    #         insert_data(database, selected_collection, file_path)
    #         # create
    #     elif selected_function == "create_data":
    #         create_data(database, selected_collection)   
            
    #         # read      
    #     elif selected_function == "read_data":
    #         criteria = input("Enter the criteria: ")
    #         read_data(database, selected_collection, criteria)
            
    #         # update
    #     elif selected_function == "update_data":
    #         update_data(database, selected_collection)
            
    #         # delete
    #     elif selected_function == "delete_data":
    #         delete_data(database, selected_collection)
            
    #     else:
    #         print("Invalid function name!")
        
    # else:
    #     print("Function not found!")

except Exception as e:
    print(f"An error occurred: {e}")