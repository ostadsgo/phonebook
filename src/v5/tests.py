import phonebook


TEST_DB = "testdb.db"


def run_tests():
    conn = phonebook.create_connection(TEST_DB)
    if conn is not None:
        assert phonebook.create_contact_table(conn)
        print("✅ Create table passed!")
        assert phonebook.create_contact_table(conn)
    else:
        print("❌ Connection fails")


if __name__ == "__main__":
    run_tests()
