import tkinter as tk

class userDB:
    def __init__(self):
        self._username = "John Doe"
        self._password = "secretpassword"
        self.captcha = "1234"

    def showUser(self):
        name_label.config(text="Name: " + self._username)
        password_label.config(text="Password: " + self._password)
        captcha_label.config(text="Captcha: " + self.captcha)

def addUser():
    global user
    user._username = name_entry.get()
    user._password = password_entry.get()
    user.captcha = captcha_entry.get()
    print("Details Updated")

# Create the root window
root = tk.Tk()
root.geometry("400x300")
root.title("User Profile")

# Create an instance of userDB class
user = userDB()

# Create and place the labels and entry fields
name_label = tk.Label(root, text="Name : ")
name_label.place(x=180, y=20, anchor= "center")

name_entry = tk.Entry(root)
name_entry.place(x=180, y=50, anchor= "center")

password_label = tk.Label(root, text="Password : ")
password_label.place(x=180, y=100, anchor="center")

password_entry = tk.Entry(root)
password_entry.place(x=180, y=130, anchor="center")

captcha_label = tk.Label(root, text="Captcha : ")
captcha_label.place(x=180, y=180, anchor="center")

captcha_entry = tk.Entry(root)
captcha_entry.place(x=180, y=210, anchor="center")

# Create and place the labels to display the user details
user_label = tk.Label(root)
user_label.place(x=180, y=260, anchor="center")

password_display_label = tk.Label(root)
password_display_label.place(x=180, y=290, anchor="center")

captcha_display_label = tk.Label(root)
captcha_display_label.place(x=180, y=320, anchor="center")

# Create the buttons
update_button = tk.Button(root, text="Update Login Details", command=addUser)
update_button.place(x=90, y=260)

show_button = tk.Button(root, text="Show Profile", command=user.showUser)
show_button.place(x=270, y=260)

root.mainloop()
