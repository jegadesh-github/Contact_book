import json
from random import choice

contacts={}

def load_contacts():
    try:
        with open('contacts.json','r') as f:
            contacts=json.load(f)
    except FileNotFoundError:
        contacts={}

def save_contacts():
        with open('contacts.json','w') as f:
            json.dump(contacts,f,indent=4)

def show_menu():
    print("\n=== CONTACT BOOK MENU ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def get_user_choice():
    choice=input("Enter your choice(1-6): ")
    return choice


def add_contact():
    name=input("Enter a contact name").strip().title()
    if name in contacts:
        print("Contact already Exists")
        return
    phone=input("Enter your number: ").strip()
    email=input("Enter your email").strip()
    contacts[name]={"phone":phone, "email":email}
    save_contacts()
    print(f"contact {name} added successfuly!")
def view_contact():
    if not contacts:
        print("No contacts found!")
        return
    print("\nsaved contacts")
    for name,details in contacts.items():
        print(f"Name:{name}")
        print(f"Phone:{details['phone']}")
        print(f"Email:{details['email']}")
        print("---"*20)
def search_contact():
     name=input("Enter the name of the contact you want to search: ").strip().title()
     if name not in contacts:
         print("Contacts not found!")
         return
     else:
         print(f"\nContact Found!")
         print(f"Name: {name}")
         print(f"Phone: {contacts[name]['phone']}")
         print(f"Email: {contacts[name]['email']}")

def update_contact():
    name=input("Enter the name of the contact you want to update: ").strip().title()
    if name not in contacts:
        print("Contacts not found!")
        return
    print(f"Current Details - phone: {contacts[name]['phone']}, email: {contacts[name]['email']}")
    phone = input("Enter new phone number (leave blank to keep existing): ").strip()
    email = input("Enter new email address (leave blank to keep existing): ").strip()
    if phone:
        contacts[name]['phone']=phone
    if email:
        contacts[name]['email']=email
    save_contacts()
    print(f"Contact {name} updated successfully!")

def delete_contact():
    name = input(f"Enter the name of the contact you want to delete: ").strip().title()
    if name not in contacts:
        print("Contact not found!")
        return
    confirmation=input("Are you sure you want to delete {name} contact? (yes/no):")
    if confirmation=='yes':
        del contacts[name]
        save_contacts()
        print(f"Contact {name} deleted successfully!")
    else:
        print("Deletion cancelled.")
def main():
    load_contacts()
    while True:
        show_menu()
        choice=get_user_choice()

        if choice=="1":
            add_contact()
        elif choice=="2":
            view_contact()
        elif choice=="3":
            search_contact()
        elif choice=="4":
            update_contact()
        elif choice=="5":
            delete_contact()
        elif choice=="6":
            save_contacts()
            print("Exiting Contact Book... Goodbye!")
            break  # Exit the loop
        else:
            print("Invalid choice! Please enter a number between 1-6.")
if __name__=="__main__":
    main()
