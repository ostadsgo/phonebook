import os


def show_menu():
    """Print menu in consloe."""
    menu_items = [
        "Add Contact",
        "Update Contact",
        "Delete Contact",
        "Search Contact",
        "Show Contacts",
    ]
    for index, item in enumerate(menu_items, 1):
        print(f"[{index}] {item}")


def clear_screen():
    """Clear console screen."""
    command = "cls" if os.name == "nt" else "clear"
    os.system(command)


def main():
    clear_screen()
    show_menu()
    response = input("Choose from menu: ")


if __name__ == "__main__":
    main()
