import sqlite3
from sqlite3 import Error as SqlError

Contact = dict[str, str]
FILENAME = "phonebook.db"


def create_connection(filename: str):
    conn = None
    try:
        conn = sqlite3.connect(filename)
    except SqlError as err:
        print(err)
    return conn


def create_contact_table(conn):
    sql = """
        CREATE TABLE IF NOT EXISTS contact (
        id	integer PRIMARY KEY,
        name	text,
        phone	text
    );
    """
    cur = conn.cursor()
    cur.execute(sql)
    return True


def add_contact(conn, contact: Contact) -> int:
    sql = """
    INSERT INTO contact(name, phone)
    VALUES (:name, :phone);
    """
    cur = conn.cursor()
    cur.execute(sql, contact)
    conn.commit()
    return True


# def make_contact(name: str, phone: str):
#     return {"name": name, "phone": phone}


# def search_contact(name: str) -> int:
#     for index, contact in enumerate(contact_list):
#         cnt_name = contact.get("name")
#         if cnt_name == name:
#             return index
#     return -1


# def update_contact(index: int, contact: Contact) -> bool:
#     try:
#         contact_list[index] = contact
#         return True
#     except ValueError:
#         return False


# def delete_contact(index: int) -> bool:
#     try:
#         del contact_list[index]
#         return True
#     except ValueError:
#         return False


# def read_contacts() -> list[Contact]:
#     return contact_list


# def write_data(filename: str):
#     with open(filename, "wb") as file:
#         pickle.dump(contact_list, file)
#     return True


# def read_data(filename: str) -> list[Contact]:
#     contacts = []
#     try:
#         with open(filename, "rb") as file:
#             contacts = pickle.load(file)
#         return contacts
#     except FileNotFoundError:
#         return contacts
