contact_list = []


def display_menu():
    print("\n--- Contact List Menu ---")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    # You'll add more options here later


def add_contact():
    print("Enter contact name:")
    name = input()
    print("Enter contact number:")
    number = input()
    print("Enter contact email:")
    email = input()

    contact_details = {
        "name": name,
        "number": number,
        "email": email
    }
    contact_list.append(contact_details)

    print("✅ New contact added to the contact list")


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
