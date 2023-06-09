import tkinter as tk

def register():
    username = username_entry.get()
    password = password_entry.get()
    
    if username and password:  # Both fields are not empty
        if len(password) < 8:  # The password is too short
            result_label.config(text='Password must be at least 8 characters.')
        elif username in user_data:  # The username already exists
            result_label.config(text='Username already exists.')
        else:  # Everything is fine
            user_data[username] = password
            result_label.config(text='Registration successful.')
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
    else:
        result_label.config(text='Both fields are required.')

root = tk.Tk()
root.title('User Registration')

# User data storage
user_data = {}

# Username field
username_label = tk.Label(root, text='Username')
username_label.grid(row=0, column=0)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1)

# Password field
password_label = tk.Label(root, text='Password')
password_label.grid(row=1, column=0)
password_entry = tk.Entry(root, show='*')
password_entry.grid(row=1, column=1)

# Registration button
register_button = tk.Button(root, text='Register', command=register)
register_button.grid(row=2, column=0, columnspan=2)

# Label to show the result of registration
result_label = tk.Label(root, text='')
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
