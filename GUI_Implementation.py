from tkinter import simpledialog
from tkinter.ttk import Combobox
import CRUD_Operations
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

def update_status():
    status = CRUD_Operations.check_mongodb_status()
    text_status.delete("1.0", END)
    text_status.insert(END, status)

def update_databases():
    databases = CRUD_Operations.get_databases()
    combobox_databases['values'] = databases

def update_collections(event):
    selected_database = combobox_databases.get()
    collections = CRUD_Operations.get_collections(selected_database)
    combobox_collections['values'] = collections

def create_database():
    database_name = entry_new_database.get()
    CRUD_Operations.create_database(database_name)
    messagebox.showinfo("Success", f"Database '{database_name}' created successfully.")
    update_databases()

def create_collection():
    database_name = combobox_databases.get()
    collection_name = entry_new_collection.get()
    CRUD_Operations.create_collection(database_name, collection_name)
    messagebox.showinfo("Success", f"Collection '{collection_name}' created successfully.")
    update_collections(None)

def insert_data():
    database_name = combobox_databases.get()
    collection_name = combobox_collections.get()
    file_path = filedialog.askopenfilename()
    CRUD_Operations.insert_data(database_name, collection_name, file_path)
    messagebox.showinfo("Success", "Data inserted successfully.")

def create_document():
    database_name = combobox_databases.get()
    collection_name = combobox_collections.get()
    CRUD_Operations.create_data(database_name, collection_name)
    messagebox.showinfo("Success", "Document created successfully.")

def read_data():
    database_name = combobox_databases.get()
    collection_name = combobox_collections.get()
    criteria = simpledialog.askstring("Read Data", "Enter the filter criteria (e.g., {'field': 'value'}):")
    CRUD_Operations.read_data(database_name, collection_name, criteria)

def update_data():
    database_name = combobox_databases.get()
    collection_name = combobox_collections.get()
    CRUD_Operations.update_data(database_name, collection_name)

def delete_data():
    database_name = combobox_databases.get()
    collection_name = combobox_collections.get()
    CRUD_Operations.delete_data(database_name, collection_name)

def sort_data():
    database_name = combobox_databases.get()
    collection_name = combobox_collections.get()
    collection = CRUD_Operations.client[database_name][collection_name]
    data = CRUD_Operations.sorting_algorithm(collection)
    text_output.delete("1.0", END)
    for document in data:
        text_output.insert(END, str(document) + "\n")

# Create the main window
window = Tk()
window.title("MongoDB CRUD Operations")
window.geometry("600x500")

# Create labels
label_status = Label(window, text="MongoDB Status:")
label_status.pack()
text_status = Text(window, height=2)
text_status.pack()
update_status()

label_new_database = Label(window, text="Create New Database:")
label_new_database.pack()
entry_new_database = Entry(window)
entry_new_database.pack()

label_new_collection = Label(window, text="Create New Collection:")
label_new_collection.pack()
entry_new_collection = Entry(window)
entry_new_collection.pack()

# Create comboboxes
label_choose_database = Label(window, text="Choose Database:")
label_choose_database.pack()
combobox_databases = Combobox(window, state="readonly")
combobox_databases.pack()
update_databases()
combobox_databases.bind("<<ComboboxSelected>>", update_collections)

label_choose_collection = Label(window, text="Choose Collection:")
label_choose_collection.pack()
combobox_collections = Combobox(window, state="readonly")
combobox_collections.pack()

# Create buttons
button_create_database = Button(window, text="Create Database", command=create_database)
button_create_database.pack()

button_create_collection = Button(window, text="Create Collection", command=create_collection)
button_create_collection.pack()

button_insert_data = Button(window, text="Insert Data", command=insert_data)
button_insert_data.pack()

button_create_document = Button(window, text="Create Document", command=create_document)
button_create_document.pack()

button_read_data = Button(window, text="Read Data", command=read_data)
button_read_data.pack()

button_update_data = Button(window, text="Update Data", command=update_data)
button_update_data.pack()

button_delete_data = Button(window, text="Delete Data", command=delete_data)
button_delete_data.pack()

button_sort_data = Button(window, text="Sort Data", command=sort_data)
button_sort_data.pack()

# Create output text box
text_output = Text(window)
text_output.pack()

# Start the main loop
window.mainloop()