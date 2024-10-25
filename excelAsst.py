import pandas as pd

file = 'users.xlsx'

# Function to add user data
def add_user():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    df = pd.DataFrame([[name, email, phone]], columns=['Name', 'Email', 'Phone'])
    try:
        old_data = pd.read_excel(file)
        new_data = pd.concat([old_data, df], ignore_index=True)
    except FileNotFoundError:
        new_data = df
    new_data.to_excel(file, index=False)
    print("User added successfully.")

# Function to display user data
def show_users():
    try:
        users = pd.read_excel(file)
        print(users)
    except FileNotFoundError:
        print("No users found.")

# Main program loop
while True:
    choice = input("\nPress 'A' to Add User, 'D' to Display Users, or 'E' to Exit: ").upper()
    if choice == 'A':
        add_user()
    elif choice == 'D':
        show_users()
    elif choice == 'E':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")