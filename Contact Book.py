# Initialize an empty contact book
contact_book = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")

    contact_book[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    print("\n--- Contact List ---")
    for name, details in contact_book.items():
        print(f"{name}: {details['phone']} | {details['email']} | {details['address']}")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    for name, details in contact_book.items():
        if search_term.lower() in (name.lower(), details['phone']):
            print(f"Contact found: {name} | {details['phone']} | {details['email']} | {details['address']}")
            break
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter contact name to update: ")
    if name in contact_book:
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        address = input("Enter new address: ")

        contact_book[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print(f"Contact '{name}' updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in contact_book:
        del contact_book[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print("Contact not found.")

# Main loop
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting. Have a great day!")
        break
    else:
        print("Invalid choice. Please select 1-6.")
