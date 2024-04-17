from pymongo import MongoClient
from CRUD_Operations import *
import CRUD_Operations
import inspect
import json

try:
    client = MongoClient()  # normally it should be 'mongodb://localhost:27017/'

    # ======== Database selection/creation part ========= #
    
    selected_db = None
    while not selected_db:  # asking the user to choose the database available
        print("Available databases:")
        databases = client.list_database_names()
        i = 0
        for db in databases:
            i += 1
            print(f"{i}. {db}")
        print(f"{i+1}. Create a new database")
        selected_db = input("Select a database: ")

        if selected_db == str(i+1):
            selected_db = input("Enter a name for your new database: ") #in case the user wants to create a new database
            create_database(selected_db)

    database = client[selected_db]
    print(f"Selected database: {selected_db}")
    
    # ======== Collection selection/creation part ========= #
    selected_collection = None
    while not selected_collection:  # asking the user to choose the corresponding collection
        print(f"Available collections in {selected_db}:")
        collections = database.list_collection_names()
        i = 0
        for collection in collections:
            i += 1
            print(f"{i}. {collection}")
        print(f"{i+1}. Create a new collection") # this is an option to let the user create a new collection
        selected_collection = input("Select a collection: ")

        if selected_collection == str(i+1):
            selected_collection = input("Enter a name for your new collection: ")
            create_collection(database, selected_collection)  # Create the new collection

    print(f"Selected collection: {selected_collection}")
    
    
    # ======== Priting and prompting the user to choose an operation or function to perforn ========= #
    
    available_functions = [name for name, obj in inspect.getmembers(CRUD_Operations) if inspect.isfunction(obj)]

    print("Available functions:")  # print available functions
    i = 0
    for function_name in available_functions:
        i += 1
        print(f"{i}. {function_name}")

    selected_function = input("Select a function: ")

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

        case "sorting_algorithm":
            field = input("Enter the field to sort by: ")
            order = int(input("Enter the sorting order (1 for ascending, -1 for descending): "))
            sorting_algorithm(collection, field, order)

        case _:
            print("Invalid function name!")

except Exception as e:
    print(f"An error occurred: {e}")