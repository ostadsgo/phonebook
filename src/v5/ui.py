import os
import sys
import phonebook


def add_contact_ui():
    name = input("Name: ")
    phone = input("Phone: ")
    contact = (name, phone)
    if phonebook.add_contact(contact):
        print("Contact added successfully.")
    else:
        print("Some problem happend!!")


def update_contact_ui():
    name = input("Name to search: ")
    index = phonebook.search_contact(name)
    if index == -1:
        print("Contact not found!")
        return
    new_name = input("New name: ")
    new_phone = input("New phone: ")
    cnt = phonebook.make_contact(new_name, new_phone)
    result = phonebook.update_contact(index, cnt)
    if result:
        print("Contact updated successfully")
    else:
        print("Some problem happend!!")


def delete_contact_ui():
    name = input("Name to search: ")
    index = phonebook.search_contact(name)
    if index == -1:
        print("Contact not found!")
        return
    result = phonebook.delete_contact(index)
    if result:
        print("Contact delete successfully.")
    else:
        print("Some problem happend!!")


def search_contact_ui():
    name = input("Name to search: ")
    index = phonebook.search_contact(name)
    if index == -1:
        print("Contact not found!")
    else:
        print(phonebook.contact_list[index])


def show_contacts_ui():
    contacts = phonebook.read_contacts()
    for cnt in contacts:
        print(cnt)


def exit_program_ui():
    phonebook.write_data("contacts.pickle")
    print("Data saved successfully.\nExit program.")
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
    phonebook.contact_list = phonebook.read_data("contacts.pickle")
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
