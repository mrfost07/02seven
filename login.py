import customtkinter as c  # import customtkinter module as c
from tkinter import messagebox  # import messagebox from tkinter module
import sqlite3  # import sqlite3 module
import subprocess  # import subprocess module
import json  # import json module

c.set_appearance_mode("grey")  # set appearance mode to grey
c.set_default_color_theme("green")  # set default color theme to green

conn = sqlite3.connect('login.db')  # connect to SQLite database named login.db
co = conn.cursor()  # create a cursor object

# create users table if not exists
co.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT, password TEXT, email TEXT, full_name TEXT, age INTEGER, course TEXT, status TEXT)''')  # define columns for users table
conn.commit()  # commit changes to the database

app = c.CTk()  # create a custom tkinter application

def show_hide_password():  # define function show_hide_password
    if password_entry.cget("show") == "":  # if password is shown
        password_entry.configure(show="*")  # hide password
        show_password_button.configure(text="Show Password")  # change button text to "Show Password"
    else:  # otherwise
        password_entry.configure(show="")  # show password
        show_password_button.configure(text="Hide Password")  # change button text to "Hide Password"

def show_hide_password_signup():  # define function show_hide_password_signup
    if password_entry_signup.cget("show") == "":  # if password is shown
        password_entry_signup.configure(show="*")  # hide password
        show_password_button_signup.configure(text="Show Password")  # change button text to "Show Password"
    else:  # otherwise
        password_entry_signup.configure(show="")  # show password
        show_password_button_signup.configure(text="Hide Password")  # change button text to "Hide Password"

def open_signup_window():  # define function open_signup_window
    global signup_window, username_entry_signup, password_entry_signup, show_password_button_signup, email_entry_signup, full_name_entry_signup, age_entry_signup, course_entry_signup, status_entry_signup  # declare global variables
    app.withdraw()  # hide the main window
    signup_window = c.CTk()  # create a new custom tkinter window for sign up
    signup_window.title("Sign Up")  # set the title of the window
    signup_window.geometry("400x300")  # set the size of the window
    signup_window.pack_propagate(0)  # prevent window from resizing

    username_label_signup = c.CTkLabel(signup_window, text="Username:")  # create a label for username
    username_label_signup.pack(padx=10, pady=5)  # add padding and pack the label

    username_entry_signup = c.CTkEntry(signup_window, width=20)  # create an entry field for username
    username_entry_signup.pack(fill="x", padx=10, pady=5)  # fill the entry field horizontally and pack it

    password_label_signup = c.CTkLabel(signup_window, text="Password:")  # create a label for password
    password_label_signup.pack(padx=10, pady=5)  # add padding and pack the label

    password_entry_signup = c.CTkEntry(signup_window, show="*", width=20)  # create an entry field for password
    password_entry_signup.pack(fill="x", padx=10, pady=5)  # fill the entry field horizontally and pack it

    show_password_button_signup = c.CTkButton(signup_window, text="Show Password", command=show_hide_password_signup)  # create a button to show password
    show_password_button_signup.pack(padx=10, pady=5)  # add padding and pack the button

    email_label_signup = c.CTkLabel(signup_window, text="Email:")  # create a label for email
    email_label_signup.pack(padx=10, pady=5)  # add padding and pack the label

    email_entry_signup = c.CTkEntry(signup_window, width=40)  # create an entry field for email
    email_entry_signup.pack(fill="x", padx=10, pady=5)  # fill the entry field horizontally and pack it

    full_name_label_signup = c.CTkLabel(signup_window, text="Full Name:")  # create a label for full name
    full_name_label_signup.pack(padx=10, pady=5)  # add padding and pack the label

    full_name_entry_signup = c.CTkEntry(signup_window, width=40)  # create an entry field for full name
    full_name_entry_signup.pack(fill="x", padx=10, pady=5)  # fill the entry field horizontally and pack it

    age_label_signup = c.CTkLabel(signup_window, text="Age:")  # create a label for age
    age_label_signup.pack(padx=10, pady=5)  # add padding and pack the label

    age_entry_signup = c.CTkEntry(signup_window, width=40)  # create an entry field for age
    age_entry_signup.pack(fill="x", padx=10, pady=5)  # fill the entry field horizontally and pack it

    course_label_signup = c.CTkLabel(signup_window, text="Course:")  # create a label for course
    course_label_signup.pack(padx=10, pady=5)  # add padding and pack the label

    course_entry_signup = c.CTkEntry(signup_window, width=40)  # create an entry field for course
    course_entry_signup.pack(fill="x", padx=10, pady=5)  # fill the entry field horizontally and pack it

    status_label_signup = c.CTkLabel(signup_window, text="Status:")  # create a label for status
    status_label_signup.pack(padx=10, pady=5)  # add padding and pack the label

    status_entry_signup = c.CTkEntry(signup_window, width=40)  # create an entry field for status
    status_entry_signup.pack(fill="x", padx=10, pady=5)  # fill the entry field horizontally and pack it

    signup_button_signup = c.CTkButton(signup_window, text="Sign Up", command=signup)  # create a button to sign up
    signup_button_signup.pack(pady=5)  # add padding and pack the button

    signup_window.mainloop()  # start the main event loop for the window

signup_data = {}  # initialize an empty dictionary for signup data

def signup():  # define function signup
    global signup_data  # declare global variable
    username = username_entry_signup.get()  # get username from entry field
    password = password_entry_signup.get()  # get password from entry field
    email = email_entry_signup.get()  # get email from entry field
    full_name = full_name_entry_signup.get()  # get full name from entry field
    age = age_entry_signup.get()  # get age from entry field
    course = course_entry_signup.get()  # get course from entry field
    status = status_entry_signup.get()  # get status from entry field

    signup_data = {  # store signup data in a dictionary
        "username": username,
        "password": password,
        "email": email,
        "full_name": full_name,
        "age": age,
        "course": course,
        "status": status
    }

    co.execute('''CREATE TABLE IF NOT EXISTS users  # create users table if not exists
             (username TEXT, password TEXT, email TEXT, full_name TEXT, age INTEGER, course TEXT, status TEXT)''')  # define columns for users table
    conn.commit()  # commit changes to the database

    messagebox.showinfo("Sign Up", "Sign Up Successful")  # show a message box indicating successful sign up
    signup_window.destroy()  # destroy the sign up window
    app.deiconify()  # show the main window

def login():  # define function login
    username = username_entry.get()  # get username from entry field
    password = password_entry.get()  # get password from entry field

    co.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))  # select user with matching username and password
    result = co.fetchone()  # fetch the result of the query

    if result:  # if result is not empty
        messagebox.showinfo("Login", "Login Successful")  # show a message box indicating successful login
        app.destroy()  # destroy the main window
        subprocess.Popen(['python', 'C:/Users/fosta/OneDrive/Desktop/Programming.BSCS/Intro.Prog1/2nd sem menuoriented.exercises/guiproject/2nd Project/finalgui/main.py'])  # open the main program
    else:  # otherwise
        messagebox.showerror("Login", "Login Failed. Please check your username and password.")  # show a message box indicating failed login

username_label = c.CTkLabel(app, text="Username:")  # create a label for username
username_label.pack(pady=5)  # add padding and pack the label

username_entry = c.CTkEntry(app)  # create an entry field for username
username_entry.pack(pady=5)  # add padding and pack the entry field

password_label = c.CTkLabel(app, text="Password:")  # create a label for password
password_label.pack(pady=5)  # add padding and pack the label

password_entry = c.CTkEntry(app, show="*")  # create an entry field for password
password_entry.pack(pady=5)  # add padding and pack the entry field

show_password_button = c.CTkButton(app, text="Show Password", command=show_hide_password)  # create a button to show password
show_password_button.pack(pady=5)  # add padding and pack the button

login_button = c.CTkButton(app, text="Login", command=login)  # create a button to login
login_button.pack(pady=5)  # add padding and pack the button

signup_link = c.CTkLabel(app, text="Sign Up", cursor="hand2")  # create a label for sign up
signup_link.pack(pady=5)  # add padding and pack the label
signup_link.bind("<Button-1>", lambda e: open_signup_window())  # bind the label to open the sign up window

app.title("Login Form")  # set the title of the main window
app.geometry("800x400")  # set the size of the main window
app.mainloop()  # start the main event loop for the main window
