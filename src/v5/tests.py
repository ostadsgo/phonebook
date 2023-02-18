import phonebook
import os 


TEST_DB = "database_test.db"


def run_tests():
    conn = phonebook.create_connection(TEST_DB)
    contact = ("John Doe", "123")
    new_cnt = ("Joe Doe", "321")
    contact_id = 1
    if conn is not None:
        assert phonebook.create_contact_table(conn)
        print("✅ Create table passed!")
        assert phonebook.add_contact(conn, contact)
        print("✅ Add contact passed!")
        assert phonebook.search_by_name(conn, "John Doe") == (contact_id, *contact)
        print("✅ Search contact passed!")
        assert phonebook.read_contacts(conn) == [(contact_id, *contact)]
        print("✅ Select contact passed!")
        assert phonebook.update_contact(conn, contact_id, new_cnt)
        print("✅ Update contact passed!")
        assert phonebook.delete_contact(conn, contact_id)
        print("✅ Delete contact passed!")
        assert phonebook.read_contacts(conn) == []
        print("✅ Select contact passed!")
        print("All tests passed.")
        # remove database_test.db after passing all tests.
        os.remove(TEST_DB)
        print("Remove test database.")
    else:
        print("❌ Connection fails")


if __name__ == "__main__":
    run_tests()
