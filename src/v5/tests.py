import phonebook


TEST_DB = "database_test.db"


def run_tests():
    conn = phonebook.create_connection(TEST_DB)
    contact = {"name": "Test user", "phone": "1234"}
    new_contact = {"name": "New test user", "phone": "01234"}
    if conn is not None:
        assert phonebook.create_contact_table(conn)
        print("✅ Create table passed!")
        assert phonebook.add_contact(conn, contact)
        print("✅ Add contact passed!")
        assert phonebook.read_contacts(conn) == [(1, "Test user", "1234")]
        print("✅ Select contact passed!")
        assert phonebook.update_contact(conn, 1, new_contact)
        print("✅ Update contact passed!")
        assert phonebook.delete_contact(conn, 1)
        print("✅ Delete contact passed!")
        assert phonebook.read_contacts(conn) == []
        print("✅ Select contact passed!")
    else:
        print("❌ Connection fails")


if __name__ == "__main__":
    run_tests()
