import tkinter as tk
from tkinter import messagebox

def check_credentials():
    # Replace these with your actual login credentials
    username = "user123"
    password = "password123"
    
    entered_username = username_entry.get()
    entered_password = password_entry.get()
    
    if entered_username == username and entered_password == password:
        messagebox.showinfo("Login Successful", "Welcome!")
    else:
        messagebox.showerror("Login Failed", "Invalid credentials")

# Create the main window
root = tk.Tk()
root.title("Login Screen")

# Create labels and entry widgets for username and password
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")  # Passwords are shown as asterisks
password_entry.pack()

# Create a login button
login_button = tk.Button(root, text="Login", command=check_credentials)
login_button.pack()

# Start the main loop
root.mainloop()