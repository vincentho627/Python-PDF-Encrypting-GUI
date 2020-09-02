import os

import tkinter as tk
from tkinter import filedialog, messagebox

import writer


class Encryption:

    def __init__(self, user_password="", owner_password=""):
        """initialise layout and provides buttons for execution"""

        self.user_password = user_password
        self.owner_password = owner_password
        # self.file_name = file_name
        self.file_list = []
        self.file_label_list = ""
        self.first = False

        self.root = tk.Tk()
        self.root.title("-PDF Encrypter-")
        tk.Label(self.root, text="User Password:    ", padx=10, pady=10).grid(row=0)
        tk.Label(self.root, text="Owner Password: ", padx=10, pady=10).grid(row=1)
        tk.Label(self.root, text="File Name: ", padx=10, pady=5).grid(row=2, sticky='w')
        user_password_entry = tk.Entry(self.root)
        owner_password_entry = tk.Entry(self.root)
        file_name_label = tk.Label(self.root, text="", padx=10, pady=5)
        user_password_entry.grid(row=0, column=1)
        owner_password_entry.grid(row=1, column=1)
        file_name_label.grid(row=2, column=1)

        # initialise button for opening files
        tk.Button(self.root, text="Browse...", command=lambda: self
                  .open_file(file_name_label), padx=10, pady=20).grid(rows=3, column=0, sticky='ew')

        tk.Button(self.root, text="Encrypt", command=lambda: self
                  .set_password(file_name_label, user_password_entry, owner_password_entry), padx=10, pady=20) \
            .grid(row=3, column=1, sticky='ew')

        self.root.mainloop()

    def set_password(self, file_name_label, user_password_entry, owner_password_entry):
        """sets passwords for both user and owner from the entries and encrypts files"""
        self.user_password = user_password_entry.get()
        self.owner_password = owner_password_entry.get()

        if self.file_label_list == "" or self.file_list == []:
            messagebox.showerror("Error", "File not selected!")
        elif self.user_password == "" or self.owner_password == "":
            messagebox.showerror("Error", "Empty password, please input password!")
        else:
            self.encrypt_file(file_name_label, user_password_entry, owner_password_entry)

    def encrypt_file(self, file_name_label, user_password_entry, owner_password_entry):
        """encrypts file and removes all inputs"""
        dg = writer.Writer()
        # refers to the writer file class
        for file_name in self.file_list:
            dg.encrypting(file_name, self.user_password, self.owner_password)
        user_password_entry.delete(0, tk.END)
        owner_password_entry.delete(0, tk.END)
        file_name_label['text'] = ""
        self.file_list, self.user_password, self.owner_password, self.file_label_list = [], "", "", ""

    def open_file(self, file_name_label):
        """opens a file and writes in file name input"""
        file_name = filedialog.askopenfilename(initialdir="shell:MyComputerFolder", title="Select file",
                                                    filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))

        if os.path.isfile(file_name):
            if not self.file_list:
                self.file_list = [file_name]
            else:
                self.file_list.append(file_name)
            path, file_name_without_path = os.path.split(file_name)
            if self.first:
                self.file_label_list += '\n'
            self.file_label_list += file_name_without_path
            self.first = True

            file_name_label['text'] = self.file_label_list
        else:
            pass


# running the code
if __name__ == '__main__':
    e = Encryption()
