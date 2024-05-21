import os  # import os module for system operations
from tkinter import *  # import tkinter library for GUI
from tkinter import messagebox  # import messagebox from tkinter for message popups
from customtkinter import *  # import customtkinter library for custom GUI elements
import customtkinter as c  # import customtkinter library with alias c for easier reference
from PIL import Image, ImageTk  # import Image and ImageTk classes from PIL for image handling
from tkinter import IntVar, Checkbutton  # import IntVar and Checkbutton from tkinter for checkboxes
import time  # import time module for delays
import webbrowser  # import webbrowser module for opening web pages
import wikipedia  # import wikipedia module for searching Wikipedia

# Set appearance mode to grey and default color theme to green
c.set_appearance_mode("grey")
c.set_default_color_theme("green")

# Create a custom tkinter application
app = c.CTk()

# Function to show the options frame
def show_options():
    global options_frame, back_button, menu_button
    button_height = 30  # Height of the buttons
    num_buttons = 4  # Number of buttons
    options_height = num_buttons * (button_height + 10)  # Height of the options frame

    # Calculate the width of the options frame based on the question frame width
    question_frame_width = frame_question.winfo_width()
    options_width = question_frame_width // 2

    if 'options_frame' in globals() and options_frame.winfo_exists():
        options_frame.destroy()

    # Create the options frame
    options_frame = c.CTkFrame(frame_main, width=options_width, height=options_height)
    options_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    def create_button(parent, text, icon, command):
        button = c.CTkButton(parent, text=text, width=20, height=button_height, image=icon, compound=LEFT)
        button.pack(pady=10)
        button.configure(command=command)
        return button

    # Create buttons for profile, developer, settings, and logout
    profile_button = create_button(options_frame, "Profile", profile_photo, show_profile_frame)
    developer_button = create_button(options_frame, "Developer", developer_photo, show_developer_frame)
    settings_button = create_button(options_frame, "Settings", settings_photo, show_settings_frame)
    logout_button = create_button(options_frame, "Logout", logout_photo, logout)

    back_button = create_button(options_frame, "Back", back_photo, hide_options)

    menu_button.grid_forget()

# Function to hide the options frame
def hide_options():
    options_frame.grid_forget()
    menu_button.grid(row=0, column=0, padx=5)

# Function to show the profile frame
def show_profile_frame():
    global profile_frame
    profile_frame = c.CTkFrame(frame_main)
    profile_frame.grid(row=0, column=0, sticky="nsew")
    profile_frame.grid_rowconfigure(0, weight=1)
    profile_frame.grid_columnconfigure(0, weight=1)

    # Display profile information
    username_label = c.CTkLabel(profile_frame, text="NAME: Mark Renier B. Fostanes")
    username_label.pack(padx=1, pady=2)

    course_label = c.CTkLabel(profile_frame, text="COURSE: Bachelor of Sciene in Computer Science")
    course_label.pack(padx=10, pady=2)

    age_label = c.CTkLabel(profile_frame, text="AGE: 18")
    age_label.pack(padx=10, pady=2)

    status_label = c.CTkLabel(profile_frame, text="STATUS: Online")
    status_label.pack(padx=10, pady=2)

    back_button = c.CTkButton(profile_frame, text="Back", command=hide_profile_frame)
    back_button.pack(pady=10)

# Function to hide the profile frame
def hide_profile_frame():
    profile_frame.grid_forget()
    show_options()

# Function to show the developer frame
def show_developer_frame():
    global developer_frame
    developer_frame = c.CTkFrame(frame_main)
    developer_frame.grid(row=0, column=0, sticky="nsew")
    developer_frame.grid_rowconfigure(0, weight=1)
    developer_frame.grid_columnconfigure(0, weight=1)

    # Display developer contact information
    email_label = c.CTkLabel(developer_frame, text="Contact via email: fostanesmarkrenier@gmail.com")
    email_label.pack(padx=10, pady=10)

    phone_label = c.CTkLabel(developer_frame, text="Phone: +639709575227")
    phone_label.pack(padx=10, pady=10)

    fb_label = c.CTkLabel(developer_frame, text="FB: Renier Fostanes")
    fb_label.pack(padx=10, pady=10)

    back_button = c.CTkButton(developer_frame, text="Back", command=hide_developer_frame)
    back_button.pack(pady=10)

# Function to hide the developer frame
def hide_developer_frame():
    developer_frame.grid_forget()
    show_options()

# Function to show the settings frame
def show_settings_frame():
    global settings_frame, dark_mode_var, light_mode_var
    settings_frame = c.CTkFrame(frame_main)
    settings_frame.grid(row=0, column=0, sticky="nsew")
    settings_frame.grid_rowconfigure(0, weight=1)
    settings_frame.grid_columnconfigure(0, weight=1)

    # Display settings options for dark and light mode
    theme_label = c.CTkLabel(settings_frame, text="Theme:")
    theme_label.pack(padx=10, pady=10)

    dark_mode_var = IntVar()
    light_mode_var = IntVar()

    def toggle_dark_mode():
        if light_mode_var.get() == 1:
            light_mode_var.set(0)
        c.set_appearance_mode("dark")

    def toggle_light_mode():
        if dark_mode_var.get() == 1:
            dark_mode_var.set(0)
        c.set_appearance_mode("light")

    dark_mode_checkbox = Checkbutton(settings_frame, text="Dark Mode", variable=dark_mode_var, command=toggle_dark_mode)
    dark_mode_checkbox.pack(padx=10, pady=5)

    light_mode_checkbox = Checkbutton(settings_frame, text="Light Mode", variable=light_mode_var, command=toggle_light_mode)
    light_mode_checkbox.pack(padx=10, pady=5)

    back_button = c.CTkButton(settings_frame, text="Back", command=hide_settings_frame)
    back_button.pack(pady=10)

# Function to hide the settings frame
def hide_settings_frame():
    settings_frame.grid_forget()
    show_options()

# Function to logout and close the application
def logout():
    app.destroy()

# Function to open an application
def open_application(app_name):
    try:
        os.system(app_name)  # Execute the command to open the application
        response_text.insert(END, f"\nOpening {app_name}...")
    except Exception as e:
        response_text.insert(END, f"\nFailed to open {app_name}: {e}")

# Function to open a URL in a web browser
def open_url(url):
    try:
        webbrowser.open_new(url)
        response_text.insert(END, f"\nOpening {url}...")
    except Exception as e:
        response_text.insert(END, f"\nFailed to open {url}: {e}")

# Define image paths for icons
icon_image = Image.open("C:/Users/fosta/OneDrive/Pictures/m_icon.png")
icon_image = icon_image.resize((20, 20), Image.LANCZOS)
icon_photo = CTkImage(light_image=icon_image)

profile_icon = Image.open("C:/Users/fosta/OneDrive/Pictures/p_icon.png")
profile_icon = profile_icon.resize((20, 20), Image.LANCZOS)
profile_photo = CTkImage(light_image=profile_icon)

developer_icon = Image.open("C:/Users/fosta/OneDrive/Pictures/d_icon.png")
developer_icon = developer_icon.resize((20, 20), Image.LANCZOS)
developer_photo = CTkImage(light_image=developer_icon)

settings_icon = Image.open("C:/Users/fosta/OneDrive/Pictures/s_icon.png")
settings_icon = settings_icon.resize((20, 20), Image.LANCZOS)
settings_photo = CTkImage(light_image=settings_icon)

logout_icon = Image.open("C:/Users/fosta/OneDrive/Pictures/lo_icon.png")
logout_icon = logout_icon.resize((20, 20), Image.LANCZOS)
logout_photo = CTkImage(light_image=logout_icon)

back_icon = Image.open("C:/Users/fosta/OneDrive/Pictures/b_icon.png")
back_icon = back_icon.resize((20, 20), Image.LANCZOS)
back_photo = CTkImage(light_image=back_icon)

# Create the menu frame
menu_frame = c.CTkFrame(app)
menu_frame.pack(fill=X)

# Create the menu button
menu_button = c.CTkButton(menu_frame, text="Menu", command=show_options, image=icon_photo, compound=LEFT)
menu_button.grid(row=0, column=0, padx=5)
menu_button.configure(width=20, height=20)

# Create the main frame
frame_main = c.CTkFrame(app)
frame_main.pack(fill=BOTH, expand=True)

# Create the question frame
frame_question = c.CTkFrame(frame_main)
frame_question.grid(row=0, column=0, sticky="nsew")
frame_main.grid_rowconfigure(0, weight=1)
frame_main.grid_columnconfigure(0, weight=1)

# Create the response frame
frame_response = c.CTkFrame(frame_main)
frame_response.grid(row=0, column=1, sticky="nsew")
frame_main.grid_rowconfigure(0, weight=1)
frame_main.grid_columnconfigure(1, weight=1)

entry_height = 3
entry_width = 50

# Create the question label and entry field
question_label = c.CTkLabel(frame_question, text="Question")
question_label.pack(padx=10, pady=10)

question_entry = c.CTkTextbox(frame_question, height=entry_height, width=entry_width)
question_entry.pack(padx=10, pady=(20, 5), fill=BOTH, expand=True)
question_entry.insert(END, "\n")

# Create the submit and clear buttons
button_frame = c.CTkFrame(frame_question)
button_frame.pack(pady=10)

submit_button = c.CTkButton(button_frame, text="Submit", width=10)
submit_button.pack(side=LEFT, padx=10)

clear_button = c.CTkButton(button_frame, text="Clear Response", width=15)
clear_button.pack(side=LEFT, padx=10)

# Create the response label and text box
response_label = c.CTkLabel(frame_response, text="AI Response")
response_label.pack(padx=10, pady=10)

response_frame = c.CTkFrame(frame_response)
response_frame.pack(padx=10, pady=5, fill=BOTH, expand=True)

response_text = c.CTkTextbox(response_frame, height=entry_height, width=entry_width)
response_text.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = c.CTkScrollbar(response_frame, command=response_text.yview)
scrollbar.pack(side=RIGHT, fill=Y)

response_text.configure(yscrollcommand=scrollbar.set)

# Function to animate text insertion
def animate_text(text_widget, text):
    for i in range(len(text)):
        text_widget.insert(END, text[i])
        text_widget.update_idletasks()
        time.sleep(0.03)

# Function to submit a question
def submit_question():
    question = question_entry.get(1.0, END).strip().lower()
    if question:
        response_text.delete(1.0, END)
        response_text.update_idletasks()

        # Check if the question matches any predefined actions
        if 'open camera' in question:
            open_application("camera")
        elif 'open youtube' in question:
            open_url("https://www.youtube.com")
        elif 'open google' in question:
            open_url("https://www.google.com")
        elif 'open notes' in question:
            open_application("notepad.exe")
        elif 'open facebook' in question:
            open_url("https://www.facebook.com")
        elif 'open chatgpt' in question:
            open_url("https://www.chatgpt.com")
        elif 'open vscode' in question:
            open_application("code")
        elif 'open pycharm' in question:
            open_application("pycharm")
        elif 'open word' in question:
            open_application("word")
        elif 'open powerpoint' in question:
            open_application("powerpoint")
        elif 'open excel' in question:
            open_application("excel")
        elif 'open file folder' in question:
            open_application("explorer")
        elif 'open netflix' in question:
            open_url("https://www.netflix.com")
        else:
            try:
                # Search Wikipedia for the user's query
                search_results = wikipedia.search(question)
                if not search_results:
                    response_text.insert(END, "\nNo results found on Wikipedia.")
                else:
                    # Get the summary for the first search result
                    page_summary = wikipedia.summary(search_results[0])
                    # Animate the text before inserting
                    animate_text(response_text, f"\n{page_summary}")
            except wikipedia.exceptions.DisambiguationError as e:
                # If the query is ambiguous, display the options
                response_text.insert(END, f"\n{e.options}")

    else:
        messagebox.showinfo("Error", "Please enter a question")

# Function to clear the response text box
def clear_response():
    response_text.delete(1.0, END)

# Configure the submit and clear buttons with their respective commands
submit_button.configure(command=submit_question)
clear_button.configure(command=clear_response)

# Set the title and geometry of the application
app.title("02-Seven")
app.geometry("800x400")

# Start the main event loop
app.mainloop()

