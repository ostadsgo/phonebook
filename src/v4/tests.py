import phonebook


def run_tests():
    name = "John"
    phone = "123"
    cnt1 = phonebook.make_contact(name, phone)
    cnt2 = phonebook.make_contact(name, phone)
    new_cnt = phonebook.make_contact("Jeff", "899")
    assert phonebook.add_contact(cnt1)
    assert phonebook.add_contact(cnt2)
    assert len(phonebook.read_contacts()) == 2
    assert phonebook.search_contact(name) == 0
    assert phonebook.search_contact("Joe") == -1
    assert phonebook.update_contact(0, new_cnt)
    assert phonebook.delete_contact(0)
    assert len(phonebook.read_contacts()) == 1
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
