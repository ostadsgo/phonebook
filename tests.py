import phonebook


def add_contact_test(name, phone):
    cnt = {"name": name, "phone": phone}
    phonebook.contacts.append(cnt)


def search_contact_test(name):
    return phonebook.search_contact(name)


def make_contact_test(name, phone):
    return phonebook.make_contact(name, phone)


def run_test():
    name = "John"
    phone = "123"
    # Test
    assert make_contact_test(name, phone) == {"name": name, "phone": phone}
    print("✅ make contact passed")
    # Test
    add_contact_test(name, phone)
    assert phonebook.contacts[0] == {"name": name, "phone": phone}
    print("✅ Add contact passed")
    # Test
    assert search_contact_test(name) == 0
    print("✅ search contact passed")


if __name__ == "__main__":
    run_test()
