import mysql.connector
import pandas as pd
def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password123!",
    )
    cursor = conn.cursor()


    create_db_query = "CREATE DATABASE IF NOT EXISTS contact_book"
    cursor.execute(create_db_query)
    cursor.execute("USE contact_book")


    create_table_query = """
        CREATE TABLE IF NOT EXISTS contacts (
            name VARCHAR(100) PRIMARY KEY,
            email VARCHAR(100),
            phone VARCHAR(10)
        )
    """
    cursor.execute(create_table_query)

    conn.commit()
    conn.close()

def export_contacts():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password123!",
        database="contact_book"
    )
    cursor = conn.cursor()
    contacts="SELECT*FROM contacts"
    cursor.execute(contacts)
    result=cursor.fetchall()
    if not result:
        print("No contacts found! Cannot export.")
        return

    df = pd.DataFrame(result, columns=["Name", "Email", "Phone"])
    df.to_csv("contacts.csv", index=False)

    print("Contacts exported successfully as 'contacts.csv'! You can find the file in your working directory.")

    conn.close()

def add_contact():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password123!",
        database="contact_book"
    )
    cursor = conn.cursor()

    name = input("Enter contact name: ").strip().title()
    email = input("Enter email: ").strip()
    phone = input("Enter phone number: ").strip()

    add_contact_query = "INSERT INTO contacts (name, email, phone) VALUES (%s, %s, %s)"

    try:
        cursor.execute(add_contact_query, (name, email, phone))
        conn.commit()
        print(f"Contact '{name}' added successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    conn.close()



def view_contact():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password123!",
        database="contact_book"
    )
    cursor = conn.cursor()

    view_contacts_query = "SELECT * FROM contacts"
    cursor.execute(view_contacts_query)
    result = cursor.fetchall()

    if not result:
        print("No contacts found!")
        return

    print("\nSaved Contacts:")
    for row in result:
        name, email, phone = row
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print("-" * 20)  # Separator for better formatting

    conn.close()



def search_contact():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password123!",
        database="contact_book"
    )
    cursor = conn.cursor()

    name = input("Enter the name of the contact you want to search: ").strip().title()
    search_contact_query = "SELECT * FROM contacts WHERE name LIKE %s"

    cursor.execute(search_contact_query, (f"%{name}%",))
    result = cursor.fetchall()

    if not result:
        print("No matching contacts found!")
    else:
        for row in result:
            print(f"Name: {row[0]}, Email: {row[1]}, Phone: {row[2]}")

    conn.close()


def update_contact():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password123!",
        database="contact_book"
    )
    cursor = conn.cursor()

    search_name = input("Enter the name of the contact you want to update: ").strip().title()
    check_contact_query = "SELECT * FROM contacts WHERE name=%s"
    cursor.execute(check_contact_query, (search_name,))
    result = cursor.fetchall()

    if not result:
        print("Contact not found!")
        return

    name = input("Enter new name (leave blank to keep existing): ").strip().title() or search_name
    email = input("Enter new email (leave blank to keep existing): ").strip() or result[0][1]
    phone = input("Enter new phone number (leave blank to keep existing): ").strip() or result[0][2]

    update_contact_query = "UPDATE contacts SET name=%s, email=%s, phone=%s WHERE name=%s"

    cursor.execute(update_contact_query, (name, email, phone, search_name))
    conn.commit()
    print(f"Contact '{search_name}' updated successfully!")

    conn.close()



def delete_contact():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password123!",
        database="contact_book"
    )
    cursor = conn.cursor()

    name = input("Enter the name of the contact you want to delete: ").strip().title()
    delete_contact_query = "DELETE FROM contacts WHERE name=%s"

    cursor.execute(delete_contact_query, (name,))
    conn.commit()
    print(f"Contact '{name}' deleted successfully!")

    conn.close()



def show_menu():
    print("\n=== CONTACT BOOK MENU ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")


def get_user_choice():
    choice=input("Enter your choice (1-6): ").strip()
    return choice


# Main program loop
def main():
    connect_db()

    while True:
        show_menu()
        choice = get_user_choice()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            export_contacts()
            print("Exiting Contact Book... Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-6.")


if __name__ == "__main__":
    main()