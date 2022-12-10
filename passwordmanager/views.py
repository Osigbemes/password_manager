from django.shortcuts import render
import json
from tkinter import *
from tkinter import messagebox
import random
from django.contrib import messages
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# password = ""
def generate_random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '@', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    return password

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save(websiteName, emailName, password):
    website = websiteName
    email = emailName
    password = password
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        print("Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:  # Method prone to errors
                # Reading old date
                data = json.load(data_file)
        except FileNotFoundError:  # Code block that runs if try statement runs into error
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:  # code block that runs if try statement passes
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:  # Code block runs no matter what happen, deletes initial entries
            website.lstrip()
            email.lstrip()
            password.lstrip()

# # ---------------------------FIND PASSWORD------------------------------ #
def find_password(website):
    
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        print("No Data File Found. ")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            password_info = ({"title":website, "message":f"Email: {email}\n Password: {password}"})
            return password_info
            # messages.success(request, f"Email: {email}\nPassword: {password}" )
            # messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            password_info=(f"No information about {website}")
            return password_info
            # messages.success(request, f"No information about {website}" )
            # messagebox.showinfo(title="Error", message=f"No information about {website}")

# find_password()

def homepage(request):

    password=""
    if request.method == "POST":
        

        #add password
        websiteName = request.POST.get('website')
        emailName = request.POST.get('email')
        
        #add information to the data.json file
        password = request.POST.get('password')
        save(websiteName, emailName, password)

    
    context = {
        "password":password
    }
    return render(request, 'passwordmanager/index.html', context)

def search_password(request):
    if request.method=="POST":

        website = request.POST.get('website')
        password_dict=find_password(website)

        title = password_dict["title"]
        message = password_dict["message"]

        if password_dict:
            # messagebox.showinfo(title=website, message=f"{message}")
            messages.success(request, f"Information about {title}: {message}" )
        else:
            messages.error(request, f"No information about {website}" )
            # messagebox.showinfo(title="Error", message=f"No information about {website}")
    return render(request, 'passwordmanager/index.html', {})


def generate_password(request):
    password = ""
    if request.method=="POST":
        #generate password
        password = generate_random_password()

        context = {
            "password":password
        }
        return render(request, 'passwordmanager/index.html', context)
    return render(request, 'passwordmanager/index.html', {})