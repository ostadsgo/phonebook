"""
    Contact Book
    - Add contact [name, phone]
    - Update contact [id]
    - Delete contact [id]
    - Display contacts
    - Search contact [name or phone]
"""
import csv


def lowerise(contact:list):
    return [item.lower() for item in contact ]


def read(filename):
    try:
        with open(filename, 'r') as csvfile:
            contacts = csv.reader(csvfile)
            return list(contacts)
    except FileNotFoundError as e:
        print(f'{filename} not found!\nError message: ', e)
    except Exception as e:
        print("Unknown Error", e)
    return None

def get_last_id(filename: str) -> int:
    """ Return max id 
    """
    contacts = read(filename)
    ids = []
    if contacts:
        for contact in contacts:
            ids.append(int(contact[0]))
            # print(max)
        return max(ids)  # last line first element
    return 0  # csvfile is empty return zero as contact id

def write(filename, rows):
    contacts = read(filename)
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

def search(filename: str, contact_id: int=0, name: str='', phone: str='') -> int:
    """ Search based on the prameter and return matched indeces
        contact_id: integer
        name: return indeces that matched with name
        phone: string
        if contact not found return -1
    """
    contacts = read('contacts.csv')
    if contact_id: # if contact id passed
        print('here')
        for index, item in enumerate(contacts):
            if int(item[0]) == int(contact_id):
                return index
    matches = []
    if name:
        for index, item in enumerate(contacts):
            if item[1] + ' ' + item[2] == name.lower():
                matches.append(item[0])  # store id's of the matched contact
        return matches
    if phone:
        for index, item in enumerate(contacts):
            if item[3] == phone:
                return index
    return -1

def add(filename: str, contact:list) -> None:
    with open(filename, 'a') as csvfile:
        writer = csv.writer(csvfile)
        contact_id = get_last_id(filename) + 1
        contact.insert(0, contact_id)
        writer.writerow(contact)

def update(filename, contact_id:int, new_contact:list):
    contacts = read(filename)
    new_contact.insert(0, str(get_last_id(filename) + 1)) # add id to new contact
    # search with contact_id
    contact_index = search(filename, contact_id=contact_id)
    print(contact_index)
    if contact_index != -1:  # meaning found the contact
    #     # update operation
        contacts[contact_index] = lowerise(new_contact)
        write(filename, contacts)
        return True  # updated successfuly.
    return False  # not found

def delete(filename, contact_id):
    contacts = read(filename)
    contact_index = search(filename, contact_id=contact_id)
    if contact_index != -1:
        del contacts[contact_index]
        write(filename, contacts)
        return True
    return False

if __name__ == "__main__":
    filename = "contacts.csv"
    # some test
    # contacts = [[1, 'john', 'doe', '123213'], [2, 'kate', 'doe', '4324324']]
    # write(filename, contacts)
    add(filename, ['jemese', 'goodbridge', '234324'])
    # add('contacts.csv', 'dino', 'doe', '0922922')
    # res = search(filename, name='diz doe')
    # up_res = update(filename, 2, ['Din', 'Jackson', '324234'])
    # print(up_res)
    # dres = delete(filename, 1)
    # print(dres)
    x = get_last_id(filename)

    # search Test
    x = search(filename, name='kate doe')
    print(x)