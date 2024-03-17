from connect_db import Database
import project
from classes import Store


def select_store():
    query = "SELECT * FROM store"
    data = Database.connect(query, "select")

    for i in data:
        print(F"""
        ID: {i[0]}
        Name: {i[1]}""")
    return store()


def insert_store():
    name = input("Name: ")
    query = f"INSERT INTO store(name) VALUES ('{name}')"
    print(Database.connect(query, "insert"))
    return store()


def delete_store():
    update = input("""
    1. ID delete
    2. Data delete
            >>> """)

    if update == "1":
        column_name = "store_id"
        id = input("ID: ")
        print(Store.delete_id("store", column_name, id))
        return store()
    elif update == "2":
        column_name = "name"
        data = input("Data: ")
        print(Store.delete("store", column_name, data))
        return store()
    else:
        return store()


def update_store():
    column_name = input("Column Name: ")
    old_data = input("Old data ")
    new_data = input("New data ")
    if column_name.lower() == 'store_id':
        print(Store.update_id("store", column_name, old_data, new_data))
        return store()
    elif column_name.lower() == 'name':
        print(Store.update("store", column_name, old_data, new_data))
        return store()
    else:
        print("Error")
        return store()




def store():
    ser = input("""
    1. Select
    2. Insert
    3. Update
    4. Delete
    0. Back
        >>>""")

    if ser == "1":
        return select_store()

    elif ser == "2":
        return insert_store()

    elif ser == "3":
        return update_store()

    elif ser == "4":
        return delete_store()

    elif ser == "0":
        return project.main()

    else:
        print("Error")
        return store()

