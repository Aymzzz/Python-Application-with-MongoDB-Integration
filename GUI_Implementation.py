from tkinter import Tk, Label, Text, Button, Entry, Frame, messagebox
from tkinter.ttk import Combobox
from tkinter import simpledialog, filedialog
import CRUD_Operations

def update_status():
    status = CRUD_Operations.check_mongodb_status()
    if "established" in status.lower():
        text_status.config(text="MongoDB Status: Active", fg="green", font=("Arial", 10, "bold"))
    else:
        text_status.config(text="MongoDB Status: Inactive", fg="red", font=("Arial", 10, "bold"))

def update_databases():
    databases = CRUD_Operations.get_databases()
    combobox_databases['values'] = databases

def update_collections(event):
    selected_database = combobox_databases.get()
    collections = CRUD_Operations.get_collections(selected_database)
    combobox_collections['values'] = collections

def create_database():
    database_name = simpledialog.askstring("Create New Database", "Enter the name for the new database:")
    if database_name:
        CRUD_Operations.create_database(database_name)
        messagebox.showinfo("Success", f"Database '{database_name}' created successfully.")
        update_databases()

def create_collection():
    database_name = combobox_databases.get()
    collection_name = simpledialog.askstring("Create New Collection", "Enter the name for the new collection:")
    if collection_name:
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
    text_output.delete("1.0", "end")
    for document in data:
        text_output.insert("end", str(document) + "\n")

window = Tk()
window.title("MongoDB CRUD Operations")
window.geometry("600x500")

frame_status = Frame(window)
frame_status.pack(pady=10)

frame_database = Frame(window)
frame_database.pack(pady=10)

frame_collection = Frame(window)
frame_collection.pack(pady=10)

frame_buttons = Frame(window)
frame_buttons.pack(pady=10)

frame_output = Frame(window)
frame_output.pack(pady=10)

# Labels
#Label(frame_status, text="MongoDB Status:", font=("Arial", 10)).grid(row=0, column=1, sticky="e")

# Text boxes
text_status = Label(frame_status, text="Checking...", fg="gray", font=("Arial", 10))
text_status.grid(row=0, column=2, sticky="e")
update_status()

# Buttons for database and collection creation
Button(frame_database, text="Create New Database", command=create_database).pack(side="left", padx=5)
Button(frame_database, text="Create New Collection", command=create_collection).pack(side="left", padx=5)

# Comboboxes
Label(frame_database, text="Choose Database:").pack()
combobox_databases = Combobox(frame_database, state="readonly", width=47)
combobox_databases.pack()
Label(frame_collection, text="Choose Collection:").pack()
combobox_collections = Combobox(frame_collection, state="readonly", width=47)
combobox_collections.pack()

# Buttons
Button(frame_buttons, text="Insert Data", command=insert_data).pack(side="left", padx=5)
Button(frame_buttons, text="Create Document", command=create_document).pack(side="left", padx=5)
Button(frame_buttons, text="Read Data", command=read_data).pack(side="left", padx=5)
Button(frame_buttons, text="Update Data", command=update_data).pack(side="left", padx=5)
Button(frame_buttons, text="Delete Data", command=delete_data).pack(side="left", padx=5)
Button(frame_buttons, text="Sort Data", command=sort_data).pack(side="left", padx=5)

text_output = Text(frame_output, height=10, width=80)
text_output.pack()

update_databases()
combobox_databases.bind("<<ComboboxSelected>>", update_collections)

window.mainloop()
