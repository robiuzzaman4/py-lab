contact_list = []


def display_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    # You'll add more options here later


def add_contact():
    contact_list.append("ruhan")


def view_contacts():
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
