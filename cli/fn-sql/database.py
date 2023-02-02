import sqlite3


class Database:
    db_filename = "contacts.db"

    def __init__(self, dbname=None):
        if dbname is not None:
            self.db_filename = dbname

    def create_table(self, create_table_sql):
        """Create contact table if not exist."""
        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(create_table_sql)
        print("Table created successfuly.")

    def create_contact(self, contact):
        """Get a contact(name, phone) and save it on the database."""
        sql = """ INSERT INTO contact (name, phone)
                   VALUES (?, ?)"""
        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, contact)
        conn.commit()
        print(f"`{contact}` created.")
        return cur.lastrowid

    def update_contact(self, contact):
        """Update contact by contact id."""
        sql = """ UPDATE contact
                  SET name=?,
                      phone=?
                  WHERE cid=?
        """
        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, contact)
        conn.commit()
        print(f"{contact} update successfuly.")

    def delete_contact(self, cid):
        """Get contact id and remove it from the database."""
        sql = "DELETE FROM contact WHERE cid=?"
        conn = self._create_connection()
        cur = conn.cursor()
        cur.execute(sql, (cid,))
        conn.commit()
        print(f"Contat with the id of {cid} removed successfuly.")

    @classmethod
    def _create_connection(cls):
        """Create connection to a sqlite database."""
        try:
            with sqlite3.connect(cls.db_filename) as connection:
                print(f"Connect to {cls.db_filename}", sqlite3.version)
                return connection
        except sqlite3.Error as e:
            return None


if __name__ == "__main__":
    pass
