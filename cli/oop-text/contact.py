class ContactFile:
    FILENAME = "contacts.txt"

    @classmethod
    def read(cls):
        try:
            with open(cls.FILENAME) as file:
                contacts = file.readlines()
            return contacts
        except FileNotFoundError:
            return None
        except Exception as e:
            return None

    @classmethod
    def write(cls):
        pass

    @classmethod
    def append(cls, contenet: str):
        with open(cls.FILENAME, 'a') as file:
            file.write(content)


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.file = ContactFile()

    def save(self) -> bool:
        """ Save a contact object in the file """
        self.file.append(self.name + ',' + self.phone)
        return True

    def search(self, target: str) -> bool:
        contacts = self.file.read()
        for contact in contacts:
            name, phone = contact
            if name == target:
                return True
        return False


    def update(self, name: str, phone: str) -> bool:
        if self.search(self.name):
            self.delete()
            self.name = name
            self.phone = phone
            self.save()
            return True
        return False

    def delete(self, target: str) -> bool:
        if self.search(target):
            pass








