import tkinter as tk

import contact

from tkinter import ttk

import settings

FILENAME = settings.filename



class SearchFrame(ttk.Frame):
    def __init__(self, master, contact_frame, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.search_text = ttk.Entry(self)
        self.search_button = ttk.Button(self, text="Serach")
        self.search_text.grid(row=0, column=0, sticky="wesn", padx=(0, 5))
        self.search_button.grid(row=0, column=1, sticky="wesn")
        # contact frame
        self.contact_frame = contact_frame
        self.tree = contact_frame.tree
        self.search_text.focus_set()
        # events
        self.search_button.bind('<Button-1>', self.search)
        self.search_text.bind('<Return>', self.search)
    
    def search(self, event):
        # first thing, clear selection
        self.tree.selection_remove(self.tree.selection()) 
        search_term = self.search_text.get().lower()
        # search by name
        items = contact.search(FILENAME, name=search_term)
        self.tree.selection_add(items)


class ContactFrame(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("first", "last", "phone")
        self.tree.heading("first", text="First Name")
        self.tree.heading("last", text="Last Name")
        self.tree.heading("phone", text="Phone Number")
        self.tree.heading("#0", text="Row")
        self.tree.column("#0", width=100)
        self.tree.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        # tree scroll bar
        vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=vsb.set)

        self.insert_contacts()

    def insert_contacts(self):
        contacts = contact.read(FILENAME)
        # print(contacts)
        for index, cont in enumerate(contacts, 1):
            # print(cid, type(cid))
            cid, first, last, phone = cont
            self.tree.insert('', 'end', iid=cid, text=index, 
                             values=(first.title(), last.title(), phone.title()))

    def clear_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def refresh_tree(self):
        self.clear_tree()
        self.insert_contacts()
        
    def get_selected_item(self):
        current_item = self.tree.focus()
        item = self.tree.item(current_item)
        values = item.get('values')
        if values:
            return values

    def delete_selected_contact(self):
        pass


class ActionFrame(ttk.Frame):
    def __init__(self, master, contact_frame, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        add_button = ttk.Button(self, text="Add", command=self.add_ui)
        edit_button = ttk.Button(self, text="Edit", command=self.edit_ui)
        delete_button = ttk.Button(self, text="Delete", command=self.delete)
        add_button.pack(side="left", fill=tk.BOTH, expand=True, padx=(0, 5))
        edit_button.pack(side="left", fill=tk.BOTH, expand=True, padx=(0, 5))
        delete_button.pack(side="left", fill=tk.BOTH, expand=True)
        # contact frame to access `contact tree`
        self.contact_frame = contact_frame
        self.tree = contact_frame.tree

    def add_ui(self):
        toplevel = tk.Toplevel(self)
        toplevel.title("Add Contact")
        # widgets
        ttk.Label(toplevel, text="First Name").grid(row=0, column=0)
        ttk.Label(toplevel, text="Last Name").grid(row=1, column=0)
        ttk.Label(toplevel, text="Phone Number").grid(row=2, column=0)
        # Enteries
        first = ttk.Entry(toplevel)
        last = ttk.Entry(toplevel)
        phone = ttk.Entry(toplevel)
        first.grid(row=0, column=1)
        last.grid(row=1, column=1)
        phone.grid(row=2, column=1)
        # button
        entries = [first, last, phone]
        ttk.Button(toplevel, text="Add", command=lambda: self.add(entries)).grid(row=3, column=1)
        # applying some attribute to all widgets.
        for child in toplevel.winfo_children():
            child.grid_configure(padx=5, pady=5, sticky="ew") 

    def edit_ui(self):
        firstname, lastname, telephone = self.contact_frame.get_selected_item()
        toplevel = tk.Toplevel(self)
        toplevel.title("Add Contact")
        # widgets
        ttk.Label(toplevel, text="First Name").grid(row=0, column=0)
        ttk.Label(toplevel, text="Last Name").grid(row=1, column=0)
        ttk.Label(toplevel, text="Phone Number").grid(row=2, column=0)
        # Enteries
        first = ttk.Entry(toplevel)
        last = ttk.Entry(toplevel)
        phone = ttk.Entry(toplevel)
        first.grid(row=0, column=1)
        last.grid(row=1, column=1)
        phone.grid(row=2, column=1)
        # insert selected contact info to entries
        first.insert(0, firstname)
        last.insert(0, lastname)
        phone.insert(0,telephone)
        # button
        entries = [first, last, phone]
        ttk.Button(toplevel, text="Update", command=lambda: self.edit(entries)).grid(row=3, column=1)
        # applying some attribute to all widgets.
        for child in toplevel.winfo_children():
            child.grid_configure(padx=5, pady=5, sticky="ew") 

    def clear_entires(self, entries):
        for entry in entries:
            entry.delete(0, 'end')
        
    def add(self, entries):
        cont = [entry.get() for entry in entries]
        contact.add(FILENAME, cont)
        # refresh contact tree
        self.contact_frame.refresh_tree()
        self.clear_entires(entries)

    def edit(self, entries):
        item_id = self.tree.focus()
        new_contact = [entry.get() for entry in entries]
        res = contact.update(FILENAME, item_id, new_contact)
        self.contact_frame.refresh_tree()
        self.clear_entires(entries)

    def delete(self):
        for selected_item in self.tree.selection():
            self.tree.delete(selected_item)
            contact.delete(FILENAME, selected_item)

class MainFrame(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        # search bar
        contact_frame = ContactFrame(self)
        search_frame = SearchFrame(self, contact_frame)
        action_frame = ActionFrame(self, contact_frame)
        # grids
        search_frame.grid(row=0, column=0, sticky="enws")
        contact_frame.grid(row=1, column=0, sticky="ewsn")
        action_frame.grid(row=2, column=0, sticky="ewsn")
        # responsive stuff
        search_frame.rowconfigure(0, weight=1)
        search_frame.columnconfigure(0, weight=2)
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Contact Book")


if __name__ == "__main__":
    root = Main()
    mainframe = MainFrame(root)
    mainframe.pack(fill=tk.BOTH, expand=True)

    mainframe.rowconfigure(0, weight=1)
    mainframe.rowconfigure(1, weight=10)
    mainframe.rowconfigure(2, weight=1)
    mainframe.columnconfigure(0, weight=1)

    root.mainloop()
