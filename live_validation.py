# python3 functions_folder/live_validation.py

import tkinter as tk
from tkinter.constants import * #used to import the class that we will call later

root = tk.Tk()
root.title("Live Validation")

def uname_live_validation(*args): 
    uname_characters = user_name.get() # get the value of the str()
    
    if uname_characters != "":
        usernameEntry.config(bg= "light green") # Turn green if valid  
        global username
        username = uname_characters      
    else:
        usernameEntry.config(bg= "firebrick2") # red if not valid
        return

def pdw_live_validation(*args): 
    characters = passwordEntry.get() # get the value of the str()
    if characters.isdigit() and characters != "":
        passwordEntry.config(bg="light green") # Turn green if valid
    else:
        passwordEntry.config(bg="firebrick2") # red if not valid




#__________username_________#
user_name = tk.StringVar() #Importing the class that will set the colour of the username entry box as the result of the validate function 
user_name.trace_add("write", uname_live_validation) 

usernameEntry = tk.Entry(root, text=user_name, font=('times new roman', 15, 'bold'), bd=5, fg='black')
usernameEntry.grid(row=2, column=3, pady=10, padx=20)


uname_label = tk.Label(root, text="Please enter the username:", font=('times new roman', 15, 'bold'))
uname_label.grid(row=2, column=1, pady=10, padx=20)





#__________password____________#
user_pdw = tk.StringVar() #Importing the class and setting it as the value of user_pdw
user_pdw.trace_add("write", pdw_live_validation) #setting the colour of the password entry box as the result of the validate function 

passwordEntry = tk.Entry(root, text=user_pdw, font=('times new roman', 15, 'bold'),bd=5, fg='black')
passwordEntry.grid(row=5, column=3, pady=10, padx=20)


uname_label = tk.Label(root, text="Please enter the password:", font=('times new roman', 15, 'bold'))
uname_label.grid(row=5, column=1, pady=10, padx=20)




root.geometry("800x400")
root.mainloop()