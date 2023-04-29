from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    print("*** Welcome to the PyPassword Generator ***")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    symbols = ["!","@","#","$","%","^", "&", "*", "(", ")", "+", "-", "/", "|"]
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [str(random.choice(numbers)) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input_field.insert(0, password)
    pyperclip.copy(password)


# -------------------------FIND PASSWORD-------------------------------------#

def find_password():
    website = website_input_field.get()
    try:
        with open("Day_29/data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassowrd: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input_field.get()
    email = email_input_field.get()
    password = password_input_field.get()
    new_data = {
         website: {
         "email": email,
         "password": password
         }
    }


    if len(website)== 0 or len(email)== 0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please fill the blank fields")
    else:
        # is_ok = messagebox.askokcancel(title=website, 
        #                             message=f"These are the details entered: " 
        #                             f"\nEmail: {email}\nPassword: {password}\nIs it ok to save? ")
        
        # if is_ok:
        try:
            with open("Day_29/data.json", mode="r") as file:
                # json.dump(new_data, file, indent=4)
                # reloading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("Day_29/data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            with open("Day_29/data.json", "w") as file:
                    # saving updated data
                    json.dump(data, file, indent=4)
                    
        finally:
                # file.write(f"{website} | {email} | {password}\n")
                website_input_field.delete(0, END)
                email_input_field.delete(0, END)
                password_input_field.delete(0, END)     
    
# ---------------------------- UI SETUP ------------------------------- #

# creating the GUI
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# adding image
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="Day_29/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# adding labels
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1, padx=5, pady=5)
email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# adding input fields
website_input_field = Entry(width=30)
website_input_field.grid(column=1, row=1, sticky="W")
website_input_field.focus()
email_input_field = Entry(width=35)
email_input_field.grid(column=1, row=2, columnspan=2, sticky="W")
email_input_field.insert(0, "fidelis@gmail.com")
password_input_field = Entry(width=21)
password_input_field.grid(column=1, row=3, sticky="W")

# Buttons
search_button = Button(text="Search", width=9, command=find_password)
search_button.grid(column=1, row=1, sticky="E")
generate_password_button = Button(text="Generate password", command=generate_password, cursor="hand2")
generate_password_button.grid(column=1, row=3, sticky="E")
add_button = Button(text="Add", width=36, command=save, cursor="hand2")
add_button.grid(column=1, row=4, sticky="W")


    





window.mainloop()
