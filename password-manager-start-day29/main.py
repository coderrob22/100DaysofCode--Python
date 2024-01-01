from tkinter import *
from tkinter import messagebox
from random import shuffle, choice, randint
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter= [choice(letters) for _ in range(randint(8,10))]
    password_symbol= [choice(symbols) for _ in range(randint(2,4))]
    password_number= [choice(numbers) for _ in range(randint(2,4))]

    password_list= password_letter + password_symbol + password_number
    shuffle(password_list)

    new_pass = "".join(password_list)
    password_input.insert(0, new_pass)
    pyperclip.copy(new_pass)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_it():
    site_name = website_input.get()

    try:
        with open("secret.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No data found')

    else:
        if site_name in data:
            email = data[site_name]['email']
            password = data[site_name]['password']
            messagebox.showinfo(title=site_name, message=f"Email: {email}\n Password:{password}")
        else:
            messagebox.showinfo(title='Website not found', message='There was no info for that website')

def save():
    web_info = website_input.get()
    email_info = email_input.get()
    secret = password_input.get()

    new_dictionary ={
        web_info: {
            "email": email_info,
            "password": secret,
        }
    }
    
    if len(web_info)==0 or len(secret)==0 or len(email_info) == 0:
        messagebox.showerror(title='Uh-oh', message="Please don't leave any boxes empty!")
    else:
        # save_info = messagebox.askokcancel(title=web_info, message=f"These are the details you entered: \nEmail: {email_info}" f"\nPassword: {secret}")

        # #if save_info:
            # Read and update the json data
            try:
                with open("secret.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("secret.json", "w") as file:
                    json.dump(new_dictionary, file, indent=4)
            
            else:
                data.update(new_dictionary)
            ## file.write(f"{web_info} | {email_info} | {secret}\n")

                with open("secret.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_input.delete(0, END)
                # #email_input.delete(0, END)
                password_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=20)

canvas = Canvas(width=200, height=200)
pic = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image= pic)
canvas.grid(column=1, row=0)

web_label = Label(text='Website:')
web_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

pw_label = Label(text='Password:')
pw_label.grid(column=0, row=3)

website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, 'newemail@gmail.com')

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

generate_password = Button(text='Generate Password', command=generate_pw)
generate_password.grid(column=2, row=3)

search_button = Button(text='Search', command=find_it, width= 12)
search_button.grid(column=2, row=1)

add_button= Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()