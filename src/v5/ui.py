import os
import sys
import phonebook


def add_contact_ui(conn):
    name = input("Name: ")
    phone = input("Phone: ")
    contact = (name, phone)
    if phonebook.add_contact(conn, contact):
        print("Contact added successfully.")
    else:
        print("Some problem happend!!")


def search_contact_ui(conn):
    name = input("Name to search: ")
    found = phonebook.search_by_name(conn, name)
    if not found:
        print("Contact not found!")
        return
    print(found)


def update_contact_ui(conn):
    name = input("Name to search: ")
    found = phonebook.search_by_name(conn, name)
    if not found:
        print("Contact not found!")
        return
    new_name = input("New name: ")
    new_phone = input("New phone: ")
    contact = (new_name, new_phone)
    contact_id = found[0]
    result = phonebook.update_contact(conn, contact_id, contact)
    if result:
        print("Contact updated successfully")
    else:
        print("Some problem happend!!")


def delete_contact_ui(conn):
    name = input("Contact name to search: ")
    found = phonebook.search_by_name(conn, name)
    if not found:
        print("Contact not found.")
        return
    contact_id = found[0]
    result = phonebook.delete_contact(conn, contact_id)
    if result:
        print("Contact delete successfully.")
    else:
        print("Some problem happend!!")


def show_contacts_ui(conn):
    contacts = phonebook.read_contacts(conn)
    for cnt in contacts:
        print(cnt)


def exit_program_ui(conn):
    conn.close()
    print("Bye.")
    sys.exit()


def show_menu():
    menu_items = [
        "Add Contact",
        "Update Contact",
        "Delete Contact",
        "Search Contact",
        "Show Contacts",
        "Exit",
    ]
    for index, item in enumerate(menu_items, 1):
        print(f"[{index}] {item}")


def clear_screen():
    command = "cls" if os.name == "nt" else "clear"
    os.system(command)


def main():
    options = {
        "1": add_contact_ui,
        "2": update_contact_ui,
        "3": delete_contact_ui,
        "4": search_contact_ui,
        "5": show_contacts_ui,
        "6": exit_program_ui,
    }
    conn = phonebook.create_connection("phonebook.db")
    while True:
        clear_screen()
        show_menu()
        response = input("Choose from menu: ")
        if options.get(response) is not None:
            options[response](conn)
        else:
            print("Invalid choice!!!")
        input("Press any key to continue ...")


if __name__ == "__main__":
    main()
