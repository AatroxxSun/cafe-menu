import tkinter as tk
from tkinter import messagebox
import hashlib


user_info = {}

def register():
    user = user_entry.get()
    pwd = pwd_entry.get()

    if not (user and pwd):  
        messagebox.showerror('Error', 'Username or password cannot be empty!')
    elif len(user) < 3 or len(user) > 20: 
        messagebox.showerror('Error', 'Username must be between 3 and 20 characters long!')
    elif len(pwd) < 6: 
        messagebox.showerror('Error', 'Password must be at least 6 characters long!')
    elif user in user_info: 
        messagebox.showerror('Error', 'This username has been registered!')
    else:
        pwd = hashlib.md5(pwd.encode()).hexdigest()  
        user_info[user] = pwd
        messagebox.showinfo('Success', 'Registration successful!')
       
        user_entry.delete(0, tk.END)
        pwd_entry.delete(0, tk.END)

root = tk.Tk()
root.geometry('300x200')
root.title('Registration')

user_label = tk.Label(root, text='Username:')
user_label.pack()
user_entry = tk.Entry(root)
user_entry.pack()

pwd_label = tk.Label(root, text='Password:')
pwd_label.pack()
pwd_entry = tk.Entry(root, show='*')
pwd_entry.pack()

btn = tk.Button(root, text='Register', command=register)
btn.pack()

root.mainloop()