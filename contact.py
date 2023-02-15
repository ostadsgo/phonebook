contacts = []

Contact = dict[str, str]


def add_contact(contact: Contact) -> int:
    try:
        contacts.append(contact)
        return True
    except ValueError:
        return False


def search_contact(name: str) -> int:
    for index, contact in enumerate(contacts):
        cnt_name = contact.get("name")
        if cnt_name == name:
            return index
    return -1


def update_contact(index: int, contact: Contact) -> bool:
    try:
        contacts[index] = contact
        return True
    except ValueError:
        return False


def delete_contact(index: int) -> bool:
    try:
        del contacts[index]
        return True
    except ValueError:
        return False


def read_contacts() -> list[Contact]:
    return contacts
