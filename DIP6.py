import pickle
import getpass

def register():
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")
    confirm_password = getpass.getpass("Confirm your password: ")

    if not username or not password or not confirm_password:
        print("Fields cannot be empty!")
        return

    elif len(username) < 5 or len(password) < 5:
        print("Username and password should be at least 5 characters long!")
        return

    elif password != confirm_password:
        print("Passwords do not match!")
        return

    else:
        user_data = {}
        try:
            with open('user_data.pickle', 'rb') as file:
                user_data = pickle.load(file)
        except FileNotFoundError:
            pass

        if username in user_data:
            print("User already exists!")
        else:
            user_data[username] = password
            with open('user_data.pickle', 'wb') as file:
                pickle.dump(user_data, file)
            print("Registration successful!")

while True:
    register()
