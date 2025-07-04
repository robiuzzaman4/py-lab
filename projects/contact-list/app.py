contact_list = []


def display_menu():
    print("\n--- Contact list menu ---")
    print("1. Add new contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")
    # You'll add more options here later


def add_contact():
    print("Enter contact name:")
    name = input()
    print("Enter contact number:")
    number = input()
    print("Enter contact email:")
    email = input()

    # check for duplicates
    for contact in contact_list:
        if contact['name'].lower() == name.lower() or contact['number'] == number:
            print("❌ Contact with same name or number already exists.")
            return

    # make contact details dict
    contact_details = {
        "name": name,
        "number": number,
        "email": email
    }
    contact_list.append(contact_details)

    print("✅ New contact added to the contact list")


def delete_contact(contact_name):
    contact_name = contact_name.strip().lower()
    found = False

    for contact in contact_list:
        if contact['name'].lower() == contact_name:
            contact_list.remove(contact)
            print(f"✅ Contact '{contact_name}' deleted successfully.")
            found = True
            break

    if not found:
        print(f"❌ Contact '{contact_name}' not found.")


def view_contacts():
    print("✅ Viewed contact list")
    print(contact_list)


while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
        pass
    elif choice == '2':
        view_contacts()
        pass
    elif choice == '5':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please try again.")
