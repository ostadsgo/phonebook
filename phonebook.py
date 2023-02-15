import os
import sys

contacts = []


def make_contact(name, phone):
    contact = {"name": name, "phone": phone}
    return contact


def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    cnt = make_contact(name, phone)
    contacts.append(cnt)


def search_contact(name):
    for index, contact in enumerate(contacts):
        cnt_name = contact.get("name")
        if cnt_name == name:
            return index
    return -1


def update_contact():
    name = input("Name to search: ")
    index = search_contact(name)
    if index != 1:
        new_name = input("New name: ")
        new_phone = input("New phone: ")
        cnt = {"name": new_name, "phone": new_phone}
        contacts[index] = cnt
        return True
    return False


def delete_contact():
    name = input("Name to search: ")
    index = search_contact(name)
    if index != -1:
        del contacts[index]
        return True
    return False


def show_contacts():
    for contact in contacts:
        print(contact)


def exit_program():
    print("Exit program.")
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
        "1": add_contact,
        "2": update_contact,
        "3": delete_contact,
        "4": search_contact,
        "5": show_contacts,
        "6": exit_program,
    }
    while True:
        clear_screen()
        show_menu()
        response = input("Choose from menu: ")
        if options.get(response) is not None:
            options[response]()
        else:
            print("Invalid choice!!!")
        input("Press any key to continue ...")


if __name__ == "__main__":
    main()
