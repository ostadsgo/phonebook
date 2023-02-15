import os
import sys
import contact


def make_contact(name: str, phone: str):
    return {"name": name, "phone": phone}


def add_contact_ui():
    name = input("Name: ")
    phone = input("Phone: ")
    cnt = make_contact(name, phone)
    if contact.add_contact(cnt):
        print("Contact added successfully.")
    else:
        print("Some problem happend!!")


def update_contact_ui():
    name = input("Name to search: ")
    index = contact.search_contact(name)
    if index == -1:
        print("Contact not found!")
        return
    new_name = input("New name: ")
    new_phone = input("New phone: ")
    cnt = make_contact(new_name, new_phone)
    result = contact.update_contact(index, cnt)
    if result:
        print("Contact updated successfully")
    else:
        print("Some problem happend!!")


def delete_contact_ui():
    name = input("Name to search: ")
    index = contact.search_contact(name)
    if index == -1:
        print("Contact not found!")
        return
    result = contact.delete_contact(index)
    if result:
        print("Contact delete successfully.")
    else:
        print("Some problem happend!!")


def search_contact_ui():
    name = input("Name to search: ")
    index = contact.search_contact(name)
    if index == -1:
        print("Contact not found!")
    else:
        print(contact.contacts[index])


def show_contacts_ui():
    contacts = contact.read_contacts()
    for cnt in contacts:
        print(cnt)


def exit_program_ui():
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
        "1": add_contact_ui,
        "2": update_contact_ui,
        "3": delete_contact_ui,
        "4": search_contact_ui,
        "5": show_contacts_ui,
        "6": exit_program_ui,
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
