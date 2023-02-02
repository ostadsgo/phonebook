"""
    Contact Book
    - Add contact [name, phone]
    - Update contact [id]
    - Delete contact [id]
    - Display contacts
    - Search contact [name or phone]
"""
import csv

Contact = list[str]
FIRST_ID = 1


def lowerise(contact: list):
    return [item.lower() for item in contact]


def read(filename: str) -> list:
    try:
        with open(filename, "r") as csvfile:
            contacts = csv.reader(csvfile)
            return list(contacts)
    except FileNotFoundError as e:
        print(f"{filename} not found!\nError message: ", e)
    except Exception as e:
        print("Unknown Error", e)
    return []


def get_last_id(contacts: list[Contact]) -> int:
    """Return max id"""
    if contacts:
        last_item: Contact = contacts[-1]
        last_id: int = int(last_item[0])
        return last_id + 1
    else:
        return FIRST_ID


def write(filename: str, contacts: list[Contact]):
    print(contacts)
    try:
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(contacts)
        return True
    except Exception:
        return False


def search_by_id(contacts: list[Contact], contact_id: str) -> int | bool:
    for index, contact in enumerate(contacts):
        cid, *_ = contact
        if contact_id == cid:
            return index
    return False


def search_by_name(contacts: list[Contact], name: str) -> Contact | bool:
    for contact in contacts:
        _, cname, *_ = contact
        if name == cname:
            return contact
    return False


def add(contacts: list[Contact], contact: Contact) -> bool:
    cid = get_last_id(contacts)
    contact.insert(0, cid)
    contacts.append(contact)
    return True


def update(contacts: list[Contact], index: int, new_contact: list) -> bool:
    try:
        contacts[index] = new_contact
        return True
    except Exception as e:
        print(e)
        return False


def delete(contacts: list[Contact], contact_id: str) -> bool:
    try:
        del contacts[contact_id]
        return True
    except Exception as e:
        print(f"Exception {e} happend")
    return False


if __name__ == "__main__":
    filename = "contacts.csv"
    x = search_by_name("john")
    print(x)
