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

## Usage

1. Open a terminal and navigate to the project directory.
2. Run the following command to start the application:

   ```bash
   python main.py
   ```

3. The application will prompt you to select a database from the available options.
4. After selecting a database, you will be asked to choose a collection.
5. Once you have selected a collection, the application will display the available CRUD operations.
6. Enter the number corresponding to the operation you want to perform.
7. Follow the prompts and provide the required information for the selected operation.
8. The application will execute the operation and display the results.

## Available Operations

The following CRUD operations are available:

1. Insert Data: Allows you to insert data from a JSON file into the selected collection.
2. Create Data: Allows you to manually create a new document in the selected collection.
3. Read Data: Allows you to retrieve data from the selected collection based on specified criteria.
4. Update Data: Allows you to update documents in the selected collection.
5. Delete Data: Allows you to delete documents from the selected collection.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.
