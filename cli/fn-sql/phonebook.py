from database import Database


class Contact:
    db = Database("phonebook.db")

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def save(self):
        contact = (self.name, self.phone)
        self.db.create_contact(contact)

    @classmethod
    def create_by(cls, name, phone):
        contact = (name, phone)
        cls.db.create_contact(contact)

    @classmethod
    def update_by(cls, cid, new_name, new_phone):
        contact = (new_name, new_phone, cid)
        cls.db.update_contact(contact)

    @classmethod
    def delete_by(cls, cid):
        cls.db.delete_contact(cid)


if __name__ == "__main__":
    pass
