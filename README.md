# Python-Application-with-MongoDB-Integration

# MongoDB CRUD Operations

This project provides a command-line interface for performing CRUD (Create, Read, Update, Delete) operations on a MongoDB database. It allows you to select a database, choose a collection, and perform various operations on the collection.

This project was done in an Ubuntu machine, therefore installing MongoDB and setting up is the first step of this project. Make sure that MongoDB service is up and running on your machine before running the code using the following:

   ```bash
      sudo systemctl start mongod
   ```
To check if it is already running, run the following:

   ```bash
      sudo systemctl status mongod
   ```

## Prerequisites

Before running the application, make sure you have the following prerequisites:

- Python 3.x installed on your system
- `pymongo` library installed. You can install it using the command `pip install pymongo`

## Getting Started

1. Clone the repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Run the following command to install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Make sure your MongoDB server is running.

## Available Operations

### MongoDB Helper Functions (CRUD_Operations.py)

#### `check_mongodb_status()`
This function checks the status of the MongoDB service and establishes a connection to the MongoDB server to test the connection. It returns a message indicating whether the database connection has been established or if there was an error.

- Establishes a connection to the MongoDB server.
- Tests the connection to the MongoDB server.
- Returns a message indicating the status of the database connection.

#### `get_databases()`
This function retrieves the list of available databases from the MongoDB server. It returns a list of database names.

- Retrieves the list of available databases.
- Returns a list of database names.

#### `get_collections(database_name)`
Retrieves the list of collections within a specified database from the MongoDB server. It returns a list of collection names within the specified database.

- Retrieves the list of collections within a specified database.
- Returns a list of collection names.

#### `create_database(database_name)`
Creates a new database with the given name in the MongoDB server.

- Creates a new database with the specified name.

#### `create_collection(database_name, collection_name)`
Creates a new collection within a specified database in the MongoDB server.

- Creates a new collection within the specified database.
- Provides the name of the collection to be created.

#### `insert_data(database, collection_name, file_path)`
Inserts data from a JSON file into a specified collection within a database in the MongoDB server.

- Inserts data from a JSON file into a specified collection.
- Requires the path to the JSON file containing the data to be inserted.

#### `create_data(database, collection_name)`
Allows the user to manually create and insert data into a specified collection within a database in the MongoDB server.

- Allows manual creation and insertion of data into a collection.
- Provides a user interface for data input.

#### `read_data(database, collection_name, criteria)`
Retrieves and displays data from a specified collection within a database based on optional filter criteria in JSON format in the MongoDB server.

- Retrieves and displays data from a collection.
- Supports optional filter criteria for data retrieval.

#### `update_data(database, collection_name)`
Allows the user to update documents in a specified collection within a database in the MongoDB server.

- Provides options for updating documents in a collection.
- Supports single document update, multiple document update, and document replacement.

#### `delete_data(database, collection_name)`
Allows the user to delete documents from a specified collection within a database in the MongoDB server.

- Provides options for deleting documents from a collection.
- Supports single document deletion and multiple document deletion.

#### `sorting_algorithm(collection)`
Sorts documents within a collection based on user-specified fields and sorting order in the MongoDB server.

- Sorts documents within a collection.
- Supports sorting by fields in ascending or descending order.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.
