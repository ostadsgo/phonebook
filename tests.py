import contact


def run_tests():
    name = "John"
    phone = "123"
    cnt1 = contact.make_contact(name, phone)
    cnt2 = contact.make_contact(name, phone)
    new_cnt = contact.make_contact("Jeff", "899")
    assert contact.add_contact(cnt1)
    assert contact.add_contact(cnt2)
    assert len(contact.read_contacts()) == 2
    assert contact.search_contact(name) == 0
    assert contact.search_contact("Joe") == -1
    assert contact.update_contact(0, new_cnt)
    assert contact.delete_contact(0)
    assert len(contact.read_contacts()) == 1
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
