"""
Contact Book Application
------------------------
A beginner-friendly command-line contact management system using Python dictionaries.
Week 2 - Python Programming Internship
"""

def add_contact(contacts):
    """Add a new contact to the dictionary."""
    name = input("Enter contact name: ").strip()
    if not name:
        print("Error: Contact name cannot be empty.")
        return

    # Case-insensitive duplicate check key
    name_lower = name.lower()
    for existing_name in contacts:
        if existing_name.lower() == name_lower:
            print(f"Error: Contact '{existing_name}' already exists.")
            return

    phone = input("Enter phone number: ").strip()
    if not phone:
        print("Error: Phone number cannot be empty.")
        return

    email = input("Enter email address (optional, press Enter to skip): ").strip()
    if not email:
        email = "N/A"

    contacts[name] = {"phone": phone, "email": email}
    print(f"Success: Contact '{name}' added successfully!")


def search_contact(contacts):
    """Search for a contact by name."""
    if not contacts:
        print("Contact book is empty.")
        return

    query = input("Enter contact name to search: ").strip()
    if not query:
        print("Error: Search query cannot be empty.")
        return

    found = False
    for name, details in contacts.items():
        if query.lower() == name.lower():
            print("\n--- Contact Found ---")
            print(f"Name : {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print("---------------------")
            found = True
            break

    if not found:
        print(f"Error: Contact '{query}' not found in contact book.")


def update_contact(contacts):
    """Update details of an existing contact."""
    if not contacts:
        print("Contact book is empty.")
        return

    query = input("Enter contact name to update: ").strip()
    if not query:
        print("Error: Contact name cannot be empty.")
        return

    target_name = None
    for name in contacts:
        if query.lower() == name.lower():
            target_name = name
            break

    if not target_name:
        print(f"Error: Contact '{query}' not found.")
        return

    print(f"Updating details for '{target_name}'. Leave blank to keep current value.")
    current_phone = contacts[target_name]["phone"]
    current_email = contacts[target_name]["email"]

    new_phone = input(f"New phone number [{current_phone}]: ").strip()
    new_email = input(f"New email address [{current_email}]: ").strip()

    if new_phone:
        contacts[target_name]["phone"] = new_phone
    if new_email:
        contacts[target_name]["email"] = new_email

    print(f"Success: Contact '{target_name}' updated successfully!")


def delete_contact(contacts):
    """Delete a contact by name."""
    if not contacts:
        print("Contact book is empty.")
        return

    query = input("Enter contact name to delete: ").strip()
    if not query:
        print("Error: Contact name cannot be empty.")
        return

    target_name = None
    for name in contacts:
        if query.lower() == name.lower():
            target_name = name
            break

    if target_name:
        del contacts[target_name]
        print(f"Success: Contact '{target_name}' deleted successfully!")
    else:
        print(f"Error: Contact '{query}' not found.")


def display_all_contacts(contacts):
    """Display all stored contacts."""
    if not contacts:
        print("Contact book is empty.")
        return

    print("\n================ Contact List ================")
    print(f"{'Name':<20} | {'Phone':<15} | {'Email':<25}")
    print("-" * 66)
    for name, details in contacts.items():
        print(f"{name:<20} | {details['phone']:<15} | {details['email']:<25}")
    print("=" * 66)


def display_menu():
    """Display the main menu options."""
    print("\n--- CONTACT BOOK MENU ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View All Contacts")
    print("6. Exit")


def main():
    """Main program loop."""
    contacts = {
        "Alice Smith": {"phone": "123-456-7890", "email": "alice@example.com"},
        "Bob Johnson": {"phone": "987-654-3210", "email": "bob@example.com"}
    }

    print("Welcome to Contact Book Application!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            display_all_contacts(contacts)
        elif choice == "6":
            print("Thank you for using Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
