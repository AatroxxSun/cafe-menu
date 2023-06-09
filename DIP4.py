import tkinter as tk
from tkinter import messagebox
import json
import os

class RegisterApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Register")
        self.window.geometry('300x200')
        
        if os.path.exists('user_data.json'):
            with open('user_data.json', 'r') as file:
                self.user_data = json.load(file)
        else:
            self.user_data = {}
        
        self.username_label = tk.Label(window, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(window)
        self.username_entry.pack()
        
        self.password_label = tk.Label(window, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(window, show="*")
        self.password_entry.pack()
        
        self.register_button = tk.Button(window, text="Register", command=self.register)
        self.register_button.pack()
        
    def register(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if not username or not password:
            messagebox.showerror("Error", "Both fields must be filled in.")
            return
        
        if username in self.user_data:
            messagebox.showerror("Error", "This user already exists.")
            return
        
        self.user_data[username] = password
        
        with open('user_data.json', 'w') as file:
            json.dump(self.user_data, file)
        
        messagebox.showinfo("Success", "User registered successfully!")
        

if __name__ == "__main__":
    root = tk.Tk()
    app = RegisterApp(root)
    root.mainloop()
