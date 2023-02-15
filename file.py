def read(filename: str) -> list:
    """Read `filename` and"""
    with open(filename, encoding="utf-8") as file:
        contacts = file.readlines()
    return contacts


def write(filename: str, contacts: list) -> bool:
    with open(filename, "w", encoding="utf-8") as file:
        for contact in contacts:
            file.write(contact)
    return True
