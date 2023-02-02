import sys
import os

import contact

FILENAME = "contacts.csv"
Contact = contact.Contact


def message(result):
    messages {
        "succ": "Operation was successful.",
        "err": "Some error happend.",
        "nf": "Contact not found.",
    }
    if result:
        return messages.get("succ")
    return messages.get("err")


def menu():
    items = [
        "Add Contact",
        "Update Contact",
        "Delete Contact",
        "Search Contact",
        "Display Contacts",
        "Exit",
    ]
    for index, item in enumerate(items, 1):
        print(f"{[index]} {item}")
    user_response = input("> ")
    return user_response


def add_contact_ui(contacts):
    first = input("First Name: ")
    last = input("Last Name: ")
    phone = input("Phone Number: ")
    result: bool = contact.add(contacts, [first, last, phone])
    msg: str = message(result)
    print(msg)


def update_contact_ui(contacts: list[Contact]):
    cid = input("Enter a person id: ")
    index = contact.search_by_id(contacts, cid)
    if index:
        # get new contact info
        new_first = input("First Name: ")
        new_last = input("Last Name: ")
        new_phone = input("Phone Number: ")
        contact.update(contacts, index, [cid, new_first, new_last, new_phone])
        msg = message("succ")
        return
    msg = message("nf")
    print(msg)


def delete_contact_ui(contacts: list[Contact]):
    cid = input("Contact id: ")
    index = contact.search_by_id(contacts, cid)
    if index:
        res: bool = contact.delete(contacts, cid)
        if res:
            print(message("succ"))
        return
    print(message("err"))


def search_contact_ui(contacts: list[Contact]):
    name = input("Contact first name: ")
    result: Contact = contact.search_by_name(contacts, name)
    if result:
        print(result)
        return
    print(message("nf"))


def display_contact_ui(contacts: list[Contact]):
    for contact in contacts:
        cid, name, fname, phone = contact
        print(f"{cid}) {name.title()} {fname.title()} {phone} ")


def exit_program(contacts: list[Contact]) -> bool | None:
    result: bool = contact.write(FILENAME, contacts)
    if result:
        print("Data store succesfuly.")
        exit()
    else:
        print("Errr, Some problem happend data not saved!")
    return False


options = {
    "1": lambda contacts: add_contact_ui(contacts),
    "2": lambda contacts: update_contact_ui(contacts),
    "3": lambda contacts: delete_contact_ui(contacts),
    "4": lambda contacts: search_contact_ui(contacts),
    "5": lambda contacts: display_contact_ui(contacts),
    "6": lambda contacts: exit_program(contacts),
}


def main(contacts):
    running = True
    while running:
        os.system("cls") if sys.platform == "win32" else os.system("clear")
        user_response: str = menu()
        if options.get(user_response) is not None:
            options[user_response](contacts)
        else:
            print("Wrong opiton, plz choice from menu.")
        input("Enter any key to continue...")


if __name__ == "__main__":
    contacts = contact.read(FILENAME)
    main(contacts)
