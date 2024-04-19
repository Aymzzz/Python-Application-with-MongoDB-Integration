import os
import json
from CRUD_Operations import *

# This part is about preparing certain functions that will help us during the execution of the operations.
def print_menu(): #prints the available functions
    print("\nMenu:")
    print("1. Insert JSON document into database")
    print("2. CRUD Operations")
    print("3. Sort Data")
    print("0. Exit")

def check_mongodb_service():
    #Check MongoDB service status 
    status = os.system("systemctl is-active --quiet mongod")
    if status == 0:
        print("MongoDB service is running.")
    else:
        print("MongoDB service is not running. Starting the service...")
        os.system("sudo systemctl start mongod") #to start the service for the user
        print("MongoDB service has been started.")

def list_databases(): # lists all databases
    print("\nAvailable databases:")
    databases = get_databases()
    for i, db in enumerate(databases, start=1):
        print(f"{i}. {db}")
    return databases

def list_collections(database_name): #lists all collections
    print("\nAvailable collections:")
    collections = get_collections(database_name)
    for i, collection in enumerate(collections, start=1):
        print(f"{i}. {collection}")
    return collections

def beautify_json(data): #cleans the output
    for doc in data:
        if '_id' in doc:
            doc['_id'] = str(doc['_id'])
    return json.dumps(data, indent=4)
    
'''
This upcoming part will be provide the user with a Menu full of possible operations to be performed on the database.
These operations include: Creating, Reading, Updating and Deleting data as part of CRUD operations.
Data insertion from a given JSON file is also included as an option to quickly populate the collection withint the database.
The operations will prompt the user to enter the chosen database and collection.
'''
def main():
    
    check_mongodb_service() # checking the mongodb service if it is available
    databases = list_databases() #lists the databases to give the user an idea of the existing ones.
    
    #this next part will ask the user if they would like to create a new database or use an existing one;
    create_db = input("\nDo you want to create a new database? (Type 'n' if you want to choose an existing one) (y/n): ")

    if create_db.lower() == "y":
        print("\nCreating New Database:")
        database_name = input("Enter the name of the new database: ")
        create_database(database_name)
        collection_name = input("Enter the name of the collection: ")
        create_collection(database_name, collection_name)
        
    else:
        # Validate the user's input for the database and collection names
        
        while True:

            database_name = input("Enter the name of the database: ")
            if database_name not in databases:
                print(f"Database {database_name} does not exist. Please try again.")
                continue
            else:
                collections = list_collections(database_name) #if the input correct then the collections show
                
                while True: #similarly, we do the same thing for collections
                    collection_name = input("Enter the name of the collection: ")
                    if collection_name not in collections:
                        print(f"Collection {collection_name} does not exist in database {database_name}. Please try again.")
                    else:
                        break
    
                if collection_name in collections:
                    break
    
    while True: # Once everything is good, we can move to this step!!
        
        print_menu()
        
        database = MongoClient()[database_name]    
        
        # Possible operations are, as mentioned above, the following:       
        choice = input("Enter your choice: ")
   
        # and now for every choice its implementation from the CRUD_operations.py
        if choice == "1":
                file_path = input("Enter the path of the data file: ") 
                database = MongoClient()[database_name]
                insert_data(database, collection_name, file_path)

        elif choice == "2":
            print("\nCRUD Operations:")
            if not databases:
                print("No databases available. Please create a database first.")
            else:
                print("1. Create Data")
                print("2. Read Data")
                print("3. Update Data")
                print("4. Delete Data")
                
                crud_choice = input("Enter your choice: ")
                
                if crud_choice == "1":
                    database = MongoClient()[database_name]
                    create_data(database, collection_name)
                    
                elif crud_choice == "2":
                    criteria = input("Enter the criteria (leave empty to retrieve all): ")
                    database = MongoClient()[database_name]
                    result = read_data(database, collection_name, criteria)
                    if result:
                        print("Retrieved data:")
                        print(beautify_json(result))
                        
                elif crud_choice == "3":
                    database = MongoClient()[database_name]
                    update_data(database, collection_name)
                    
                elif crud_choice == "4":
                    database = MongoClient()[database_name]
                    delete_data(database, collection_name)
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "3":
            print("\nSorting Data:")
            database = MongoClient()[database_name]
            result = sorting_algorithm(database[collection_name])
            if result:
                print("Sorted data:")
                print(beautify_json(result))

        elif choice == "0": # once the user is done, they can exit.
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()