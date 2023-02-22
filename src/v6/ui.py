import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox

import phonebook

# Sticky vertical and horizontal.
VERTICAL = (tk.N, tk.S)
HORIZONTAL = (tk.E, tk.W)
HV = HORIZONTAL + VERTICAL


class SearchFrame(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        ttk.Label(self, text="Enter conact name to search: ").grid(
            row=0,
            column=0,
            sticky=HV,
        )
        self.search_entry = ttk.Entry(self)
        self.search_button = ttk.Button(self, text="Search", command=self.search)
        self.search_entry.grid(row=1, column=0, sticky=HV)
        self.search_button.grid(row=1, column=1, sticky=HV)
        # row and column configure
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def search(self):
        search_text = self.search_entry.get()
        if not search_text:
            msgbox.showerror("No Search Term", "Contact name must be entered")
            return


class ContactFrame(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.contact_tree = ttk.Treeview(self)
        self.contact_tree["columns"] = ("row", "contact", "phone")
        self.contact_tree["show"] = "headings"
        self.contact_tree.heading("row", text="Row")
        self.contact_tree.heading("contact", text="Contact")
        self.contact_tree.heading("phone", text="Phone")
        self.contact_tree.column("row", width=50)
        self.contact_tree.pack(fill=tk.BOTH, expand=True)
        self.fill_contact_tree()

    def fill_contact_tree(self):
        conn = phonebook.create_connection("phonebook.db")
        contacts = phonebook.read_contacts(conn)
        for index, contact in enumerate(contacts, 1):
            contact_id, contact, phone = contact
            contact_row = (index, contact, phone)
            self.contact_tree.insert("", "end", iid=contact_id, values=contact_row)
        conn.close()


class ActionFrame(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.conn = phonebook.create_connection("phonebook.db")
        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.add_button = ttk.Button(self, text="Add Contact", command=self.add_contact)
        self.edit_contact = ttk.Button(self, text="Edit Contact")
        self.delete_contact = ttk.Button(self, text="Delete Contact")
        self.add_button.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        self.edit_contact.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        self.delete_contact.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

    def add_contact(self):
        toplevel = tk.Toplevel()
        toplevel.title("Add Contact")
        frame = ttk.Frame(toplevel, padding=(5, 10))
        frame.pack(fill=tk.BOTH, expand=True)
        ttk.Label(frame, text="Name: ").pack(fill=tk.BOTH, expand=True)
        name_entry = ttk.Entry(frame, textvariable=self.name_var)
        name_entry.pack(fill=tk.BOTH, expand=True)
        ttk.Label(frame, text="Phone: ").pack(fill=tk.BOTH, expand=True)
        phone_entry = ttk.Entry(frame, textvariable=self.phone_var)
        phone_entry.pack(fill=tk.BOTH, expand=True)
        save_button = ttk.Button(frame, text="Save", command=self.save_contact)
        save_button.pack(fill=tk.BOTH, expand=True, pady=(10, 5))
        close_button = ttk.Button(frame, text="Close", command=lambda: toplevel.destroy)
        close_button.pack(fill=tk.BOTH, expand=True)

    def save_contact(self):
        contact = (self.name_var.get(), self.phone_var.get())
        phonebook.add_contact(self.conn, contact)
        msgbox.showinfo("Save Contact", "Contact save successfully.")
        # Clear name and phone entry
        self.name_var.set("")
        self.phone_var.set("")


class MainFrame(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        # search frame
        search_frame = SearchFrame(self, padding=(5, 10))
        search_frame.grid(row=0, column=0, sticky=HV)
        # Contact Frame
        contact_frame = ContactFrame(self, padding=(5, 10))
        contact_frame.grid(row=1, column=0, sticky=HV)
        # Action frame
        action_frame = ActionFrame(self, padding=(5, 10))
        action_frame.grid(row=2, column=0, sticky=HV)
        # row and column configure
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=2)
        self.rowconfigure(1, weight=6)
        self.rowconfigure(2, weight=2)


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Phonebook")
        mainframe = MainFrame(self)
        mainframe.grid(row=0, column=0, sticky=HV, padx=10, pady=10)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
