import pickle

contact_list = []

Contact = dict[str, str]


def make_contact(name: str, phone: str):
    return {"name": name, "phone": phone}


def add_contact(contact: Contact) -> int:
    try:
        contact_list.append(contact)
        return True
    except ValueError:
        return False


def search_contact(name: str) -> int:
    for index, contact in enumerate(contact_list):
        cnt_name = contact.get("name")
        if cnt_name == name:
            return index
    return -1


def update_contact(index: int, contact: Contact) -> bool:
    try:
        contact_list[index] = contact
        return True
    except ValueError:
        return False


def delete_contact(index: int) -> bool:
    try:
        del contact_list[index]
        return True
    except ValueError:
        return False


def read_contacts() -> list[Contact]:
    return contact_list


def write_data(filename: str):
    with open(filename, "wb") as file:
        pickle.dump(contact_list, file)
    return True


def read_data(filename: str) -> list[Contact]:
    contacts = []
    try:
        with open(filename, "rb") as file:
            contacts = pickle.load(file)
        return contacts
    except FileNotFoundError:
        return contacts
