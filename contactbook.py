import tkinter as tk
from tkinter import messagebox

# Create the main application window
app = tk.Tk()
app.title("Contact Book")

# Create a list to store contact information
contacts = []

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    if name and phone:
        contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        contacts.append(contact)
        update_contact_list()
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Name and Phone are required fields.")

# Function to update the contact list
def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, contact["Name"] + " - " + contact["Phone"])

# Function to clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Function to search for a contact by name or phone
def search_contact():
    search_term = search_entry.get()
    found_contacts = []
    for contact in contacts:
        if search_term.lower() in contact["Name"].lower() or search_term in contact["Phone"]:
            found_contacts.append(contact["Name"] + " - " + contact["Phone"])
    contact_list.delete(0, tk.END)
    for contact in found_contacts:
        contact_list.insert(tk.END, contact)

# Function to delete a contact
def delete_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        del contacts[selected_index[0]]
        update_contact_list()

# Create and configure GUI elements
name_label = tk.Label(app, text="Name:")
name_label.pack()
name_entry = tk.Entry(app)
name_entry.pack()

phone_label = tk.Label(app, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(app)
phone_entry.pack()

email_label = tk.Label(app, text="Email:")
email_label.pack()
email_entry = tk.Entry(app)
email_entry.pack()

address_label = tk.Label(app, text="Address:")
address_label.pack()
address_entry = tk.Entry(app)
address_entry.pack()

add_button = tk.Button(app, text="Add Contact", command=add_contact)
add_button.pack()

search_label = tk.Label(app, text="Search by Name or Phone:")
search_label.pack()
search_entry = tk.Entry(app)
search_entry.pack()

search_button = tk.Button(app, text="Search", command=search_contact)
search_button.pack()

delete_button = tk.Button(app, text="Delete Contact", command=delete_contact)
delete_button.pack()

contact_list = tk.Listbox(app)
contact_list.pack()

update_contact_list()

# Start the application
app.mainloop()
