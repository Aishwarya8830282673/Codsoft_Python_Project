import tkinter as kint
from tkinter import ttk
import tkinter.messagebox
import csv

class ContactBook:
    def read_from_csv(self):
        try:
            with open("contacts.csv", "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.contacts_tree.insert(parent="", index="end", values=(
                        str(row["Name"]), str(row["Phone"]), str(row["Address"]), str(row["Email"])))
        except FileNotFoundError:
            pass

    def save_contacts(self):
        with open("contacts.csv", "w", newline="") as file:
            column_names = ["Name", "Phone", "Address", "Email"]
            writer = csv.DictWriter(file, fieldnames=column_names)
            writer.writeheader()
            for c_id in self.contacts_tree.get_children():
                contact = self.contacts_tree.item(c_id)["values"]
                writer.writerow({column_names[h]: contact[h] for h in range(len(column_names))})

    def __init__(self, window):
        self.window = window
        self.window.title("Contact-Book")
        self.window.geometry("1000x410+300+150")
        self.window.resizable(False, False)
        self.window.config(bg="Yellow")

        self.label_frame = kint.LabelFrame(
            window, text="Enter Contact Details", font=("Ariel", "12", "bold"), padx=15, pady=15)
        self.label_frame.grid(padx=15, pady=15)

        self.label_2 = kint.Label(self.label_frame, text="Name:", font=("Ariel", "10", "bold"))
        self.label_2.grid(row=0, column=0, padx=5, pady=5, sticky="ne")

        name_var = kint.StringVar()
        self.name = kint.Entry(
            self.label_frame, textvariable=name_var, width=20)
        self.name.grid(row=0, column=1, padx=5, pady=5)

        self.label_2  = kint.Label(self.label_frame, text="Phone:", font=("Ariel", "10", "bold") )
        self.label_2.grid(row=1, column=0, padx=5, pady=5)

        phone_var = kint.StringVar()
        self.phone = kint.Entry(
            self.label_frame, textvariable=phone_var, width=20)
        self.phone.grid(row=1, column=1, padx=5, pady=5)

        self.label_3 = kint.Label(self.label_frame, text="Address:", font=("Ariel", "10", "bold"))
        self.label_3.grid(row=2, column=0, padx=5, pady=5)

        address_var = kint.StringVar()
        self.address = kint.Entry(
            self.label_frame, textvariable=address_var, width=20)
        self.address.grid(row=2, column=1, padx=5, pady=5)

        self.label_4 = kint.Label(self.label_frame, text="Email:", font=("Ariel", "10", "bold"))
        self.label_4.grid(row=3, column=0, padx=5, pady=5)

        email_var = kint.StringVar()
        self.email = kint.Entry(
            self.label_frame, textvariable=email_var, width=20)
        self.email.grid(row=3, column=1, padx=5, pady=5)

        self.contacts_tree = ttk.Treeview(self.window, columns=("Name", "Phone", "Address", "Email"))

        self.contacts_tree.heading("Name", text="Name")
        self.contacts_tree.heading("Phone", text="Phone")
        self.contacts_tree.heading("Address", text="Address")
        self.contacts_tree.heading("Email", text="Email")

        self.contacts_tree.column("#0", width=20)
        self.contacts_tree.column("Name", width=150)
        self.contacts_tree.column("Phone", width=100)
        self.contacts_tree.column("Address", width=100)
        self.contacts_tree.column("Email", width=200)
        self.contacts_tree["displaycolumns"] = (
            "Name", "Phone", "Address", "Email")
        self.contacts_tree.place(x=370, y=20)

        style = ttk.Style()
        style.configure("Treeview",
                        font=("Ariel", "10", "bold"),
                        background="Yellow",
                        foreground="Black",)

        y_scrollbar = ttk.Scrollbar(
            self.window, orient="vertical", command=self.contacts_tree.yview)
        self.contacts_tree.configure(yscroll=y_scrollbar.set)

        self.contacts_tree.grid(row=0, column=1, sticky="nsew")
        y_scrollbar.grid(row=0, column=2, sticky="ns")

        self.read_from_csv()

        self.matching_contacts_text = kint.Text(window)
        self.matching_contacts_text.place(x=530, y=320, width=270, height=70)

        def add_contact():
            name = self.name.get()
            phone = self.phone.get()
            address = self.address.get()
            email = self.email.get()

            if name == "" or phone == "" or address == "" or email == "":
                tkinter.messagebox.showerror(
                    "Sorry","Please Fill All The Fields")
            else:
                self.contacts_tree.insert(
                    parent="", index="end",text="1", values=(name, phone, address, email))
                tkinter.messagebox.showinfo(
                    "Contact Has Been Added Successfully","Contact Saved!!!")
                self.save_contacts()

        def delete_contact():
            selected_contact = self.contacts_tree.selection()[0]
            if not selected_contact:
                tkinter.messagebox.showerror(
                    "Please Select A Contact To Delete","Sorry")

            else:
                self.contacts_tree.delete(selected_contact)
                tkinter.messagebox.showinfo(
                 "Contact Has Been Deleted Successfully","Done")
                self.save_contacts()

        def update_contact():
            selected_contact = self.contacts_tree.selection()
            if not selected_contact:
                tkinter.messagebox.showerror("Please select a contact to update","Error")
            else:
                contact_details = self.contacts_tree.item(selected_contact)["values"]
                self.name.delete(0, 'end')
                self.phone.delete(0, 'end')
                self.address.delete(0, 'end')
                self.email.delete(0, 'end')

                self.name.insert(0, contact_details[0])
                self.phone.insert(0, contact_details[1])
                self.address.insert(0, contact_details[2])
                self.email.insert(0, contact_details[3])

                self.contacts_tree.item(selected_contact, values=(
                    self.name.get(),
                    self.phone.get(),
                    self.address.get(),
                    self.email.get()
        ))
                self.save_contacts()

        def clear_fields():
            self.name.delete(0, 'end')
            self.phone.delete(0, 'end')
            self.address.delete(0, 'end')
            self.email.delete(0, 'end')

        def search_contact():
            search_term = self.search_var.get().lower()
            self.matching_contacts_text.delete('1.0', kint.END)
            self.contacts_tree.delete(*self.contacts_tree.get_children())
            self.read_from_csv()
            for c_id in self.contacts_tree.get_children():
                contact = self.contacts_tree.item(c_id)["values"]
                phone_str = str(contact[2])
                if isinstance(contact[0], str) and isinstance(contact[2], (str, int)):
                    if search_term in contact[0].lower() or search_term in str(phone_str).lower():

                        formatted_contact = f"Name: {contact[0]}\nphone {contact[1]}\nAddress: {contact[2]}\nEmail: {contact[3]}\n\n"
                        self.matching_contacts_text.insert(
                            kint.END, formatted_contact)
                else:
                    print("Invalid contact", contact)

        '''Creating Buttons'''

        self.button_frame = kint.Frame(window, bg="Yellow")
        self.button_frame.grid(row=1, column=0, padx=15, pady=15, sticky="sw")

        self.add_button = kint.Button(
            self.button_frame, text="Save Contact",command=add_contact, width=13, bd=5, fg="Red")
        self.add_button.grid(row=0, column=0, padx=5, pady=5, sticky="sw")

        self.update_button = kint.Button(
            self.button_frame, text="Update Contact", command=update_contact, width=13, bd=5, fg="Red")
        self.update_button.grid(row=0, column=1, padx=5, pady=5, sticky="sw")

        self.delete_button = kint.Button(
            self.button_frame, text="Delete Contact", command=delete_contact, width=13, bd=5, fg="Red",)
        self.delete_button.grid(row=1, column=0, padx=5, pady=5, sticky="sw")

        self.exit_button = kint.Button(
            self.button_frame, text="Exit", width=13, bd=5, fg="Red", command=self.window.destroy)
        self.exit_button.grid(row=1, column=1, padx=5, pady=5, sticky="sw")

        self.clear_button = kint.Button(
            self.button_frame, text="Clear", width=13, bd=5, fg="Red", command=clear_fields)
        self.clear_button.grid(row=2, column=0, padx=5, pady=5, sticky="sw")

        # Search Bar
        self.label_5 = kint.Button(self.window, text="Search Contact:",
                                   command=search_contact, width=13, bd=5, fg="White", bg="Green")
        self.label_5.place(x=370, y=265)

        self.search_var = kint.StringVar()
        self.search_entry = kint.Entry(
            self.window, textvariable=self.search_var, width=40)
        self.search_entry.place(x=505, y=270)


def interface():
    window = kint.Tk()
    contact_book = ContactBook(window)
    window.mainloop()


if __name__ == "__main__":
    interface()