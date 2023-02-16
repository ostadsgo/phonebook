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
    try:
        cur = conn.cursor()
        cur.execute(sql)
        return True
    except SqlError:
        return False


def add_contact(conn, contact: Contact) -> int:
    sql = """
    INSERT INTO contact(name, phone)
    VALUES (?, ?);
    """
    try:
        cur = conn.cursor()
        cur.execute(sql, (*contact.values(),))
        conn.commit()
        return True
    except SqlError:
        return False


def update_contact(conn, contact_id: int, contact: Contact) -> int:
    sql = """
    UPDATE contact
    SET name=?, phone=?
    WHERE id=?
    """
    try:
        cur = conn.cursor()
        cur.execute(sql, (*contact.values(), contact_id))
        conn.commit()
        return True
    except SqlError:
        return False


def delete_contact(conn, contact_id: int):
    sql = """
    DELETE FROM contact
    WHERE id=?
    """
    try:
        cur = conn.cursor()
        cur.execute(sql, (contact_id,))
        conn.commit()
        return True
    except SqlError:
        return False


def read_contacts(conn):
    sql = """
    SELECT * FROM contact 
    """
    cur = conn.cursor()
    cur.execute(sql)
    contacts = cur.fetchall()
    return contacts


if __name__ == "__main__":
    c = create_connection("testdb.db")
    print(read_contacts(c))
