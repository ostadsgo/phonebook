import sqlite3



def create_connection(db_file="phonebook.db"):
    """ Create a connection to db file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

    return conn


def create_table(conn):
    sql = """
        CREATE TABLE IF NOT EXISTS contact(
            id INTEGER PRIMARY KEY,
            first TEXT NOT NULL,
            last TEXT,
            phone TEXT NOT NULL
        )
    """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        return True
    except sqlite3.Error as e:
        print(e)


def create_contact(conn, contact):
    """ get a contact: tuple a insert it to contact table

    """
    sql = """
        INSERT INTO contact(first, last, phone)
        VALUES (?, ?, ?);
    """
    try:
        cur = conn.cursor()
        cur.execute(sql, contact)
        conn.commit()
        return cur.lastrowid
    except sqlite3.Error as e:
        return False


def read_contacts(conn):
    sql = """ SELECT * FROM contact; """

    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()


def update_contact(conn, cid, new_contact):
    sql = """
        UPDATE contact
        SET first = ?,
            last = ?,
            phone = ?
        WHERE id = ?
    """
    try:
        cur = conn.cursor()
        cur.execute(sql, new_contact+(cid,))
        conn.commit()
        return True
    except sqlite3.Error as e:
        return False  # contact not found!

def find_contact(conn, cid):
    """ Return contact if found
    """

    sql = """
        SELECT first, last, phone
        FROM contact
        WHERE id = ?;
    """
    try:
        cur = conn.cursor()
        cur.execute(sql, str(cid))
        return cur.fetchone()
    except sqlite3.Error as e:
        return None  # contact not found!


def delete_contact(conn, cid):
    sql = """
        DELETE FROM contact
        WHERE id = ?;
    """
    try:
        cur = conn.cursor()
        cur.execute(sql, str(cid))
        conn.commit()
        return True
    except sqlite3.Error as e:
        return False  # contact not found!
