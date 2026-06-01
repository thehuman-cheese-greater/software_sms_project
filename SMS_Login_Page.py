#tkinter gui
import tkinter as tk
from tkinter import *
from tkinter import messagebox


#encryption using bcrypt
import bcrypt  

#files:
import adminSMS
import studentSMS 
import classes_sms #classes python file 

#database
import database as db
db.initialise_db()# Initialise DB and default admin on run



#_______________username____________________
def uname_live_validation(*args): 
    # *args is an unknown number of arguments the function will handle. it's function comes from the (*) so it can be named anything like *items or *characters

    uname_characters = user_name.get() # get the value of the str()
    
    if uname_characters != "":
        usernameEntry.config(bg= "light green") # Turn green if valid  
        global username
        username = uname_characters      
    else:
        usernameEntry.config(bg= "firebrick2") # red if not valid
        return
#_______________username____________________


#_______________password____________________

#______password_live_validation_____#
def pdw_live_validation(*args): 

    characters = user_pdw.get() # get the value of the str()
    if characters.isdigit() and characters != "":
        passwordEntry.config(bg= "light green") # Turn green if valid  
        global idnum
        idnum = characters      
    else:
        passwordEntry.config(bg= "firebrick2") # red if not valid
        return
#_______________password____________________


def toggle_password():
    if passwordEntry.cget('show') == '*':
        passwordEntry.config(show='')
    else:
        passwordEntry.config(show='*')


def show_sign_in_fields():

    lockout_username.grid_forget()
    lockout_pdw.grid_forget()

    usernameEntry.grid(row=2, column=1, pady=10, padx=20)
    passwordEntry.grid(row=3, column=1, pady=10, padx=20)
    loginButton.grid(row=4, column=1, pady=10)


#___________check_info_to_determine_admin_or_client______________
attempt_lockout = 5
attempt_counter = 0

def check_if_admin_or_student():

    #Sign in lockout - for security 
    global attempt_counter
    attempt_counter += 1

    print(attempt_counter)
    if attempt_counter == attempt_lockout: # checking the number of times the user has clicked the button for sign in lockout to occur

        usernameEntry.grid_forget()
        passwordEntry.grid_forget()
        loginButton.grid_forget()

        lockout_username.grid(row=2, column=1, pady=10, padx=20)
        lockout_pdw.grid(row=3, column=1, pady=10, padx=20)
        
        loginButton.after(300000, show_sign_in_fields) #after 5 minutes run the show field function and reset counter
        attempt_counter = 0

    elif attempt_counter == 3:
        messagebox.showwarning("Lockout Reminder", "Warning: You have 2 attempts to left to sign in, before temporary lockout.")


    else:
        a_s_username = usernameEntry.get() # get user input of username entry 
        a_s_password = passwordEntry.get() # get user input of password entry 

        #Encrypt the password and username to check if it is the same as the stored values
        a_s_username_bytes = a_s_username.encode('utf-8') #encoding using utf-8 to get the array of bytes
        a_s_password_bytes = a_s_password.encode('utf-8')


        #get the hashed values from classes_sms file
        ad_uname_hash, ad_pdw_hash,= classes_sms.Admin.admin_login_details() #get the values of admin login details
        st_uname_hash_1, st_pdw_hash_1, st_id_1 = classes_sms.Student.student_login_details() #get the values of student login details

        if bcrypt.checkpw(a_s_username_bytes, ad_uname_hash): # checking if admin username was entered
            if bcrypt.checkpw(a_s_password_bytes, ad_pdw_hash): # checking if admin password was entered
                print("Admin Logged in")
                messagebox.showinfo("Login", "Admin login Successful")
                
                window.destroy() #destroy current window, for no overlapping windows
                attempt_counter = 0

                adminSMS.run()
        
            else: # will run if the first conditon if met and the second condition fails. ( user enters username correct and pwd wrong)
                passwordEntry.config(bg= "firebrick2")
                messagebox.showinfo("Error", "Please re-enter the password (Please type a number)")

        elif bcrypt.checkpw(a_s_username_bytes, st_uname_hash_1): # checking if studnet username was entered
            if bcrypt.checkpw(a_s_password_bytes, st_pdw_hash_1): # checking if student password was entered
                print("Student Logged in")
                messagebox.showinfo("Login", "Student login Successful")

                window.destroy()
                attempt_counter = 0

                studentSMS.start(st_id_1, student_name= a_s_username) 
            
            else:
                passwordEntry.config(bg= "firebrick2")
                messagebox.showinfo("Error", "Please re-enter the password (Please type a number)")

        else:
            print("please re-type the username")
            usernameEntry.config(bg= "firebrick2")
            messagebox.showinfo("Error", "Please re-enter the username")



#__________GUI_stats_here______________
window = tk.Tk()
window.geometry('1280x720+0+0')
window.resizable(False, False)
titleLogo = PhotoImage(file="graduation-cap.png")
window.iconphoto(True,titleLogo)

bgImage = PhotoImage(file='bg_two.png')
bgLabel = tk.Label(window, image=bgImage)
bgLabel.place(x=0, y=0)

titleFrame = tk.Frame(window,bg="#BDE5EF",width=1280,height=90,bd=10)
titleFrame.place(x=0,y=30)
titleLabel = tk.Label(titleFrame,bg="#BDE5EF",
                    text='Student Management System',
                    font=('times new roman', 45, 'bold'))
titleLabel.place(x=260,y=0)

loginFrame = tk.Frame(window,bg="#D1D1D1")
loginFrame.place(x=650, y=200)

logoImage = tk.PhotoImage(file='profile.png')
logoLabel = Label(loginFrame, image=logoImage,bg="#D1D1D1",)
logoLabel.grid(row=0, column=0, columnspan=3, pady=10)

signInLabel = tk.Label(loginFrame,
                    text='Sign In',
                    font=('times new roman', 35, 'bold'),
                    bg="#D1D1D1")
signInLabel.grid(row=1, column=0, columnspan=3)

usernameImage = tk.PhotoImage(file='username.png')
usernameLabel = tk.Label(loginFrame,
                      image=usernameImage,
                      text='Username',
                      compound=LEFT,
                      font=('times new roman', 20, 'bold'),
                      bg="#D1D1D1")
usernameLabel.grid(row=2, column=0, pady=10, padx=20)


toggleImage = tk.PhotoImage(file='showpassword.png')
toggleButton = tk.Button(loginFrame, image=toggleImage,bg="#D1D1D1",command=toggle_password)
toggleButton.grid(row=3, column=2, pady=10, padx=10)


user_pdw = tk.StringVar() #Importing the class and setting it as the value of user_pdw
user_pdw.trace_add("write", pdw_live_validation) #setting the colour of the password entry box as the result of the validate function 

#___________________Password_Entry_____________________#
passwordEntry = tk.Entry(loginFrame, text=user_pdw,
                      font=('times new roman', 20, 'bold'),
                      bd=5, fg='black', show="*")
passwordEntry.grid(row=3, column=1, pady=10, padx=20)
#___________________Password_Entry_____________________#


#____img____
passwordImage = tk.PhotoImage(file='password.png')
passwordLabel = tk.Label(loginFrame,
                      image=passwordImage,
                      text='Password',
                      compound=LEFT,
                      font=('times new roman', 20, 'bold'),
                      bg="#D1D1D1")
passwordLabel.grid(row=3, column=0, pady=10, padx=20)
#____img____


user_name = tk.StringVar() #Importing the class that will set the colour of the username entry box as the result of the validate function 
user_name.trace_add("write", uname_live_validation) 


#___________________Username_Entry_____________________#
usernameEntry = tk.Entry(loginFrame, text=user_name,
                      font=('times new roman', 20, 'bold'), bd=5, fg='black')
usernameEntry.grid(row=2, column=1, pady=10, padx=20)
#___________________Username_Entry_____________________#


#_________________lockout_______________#
lockout_username = tk.Label(loginFrame, text= "Sign in Locked for 5 minutes", font=('times new roman', 15, 'bold'), bd=5, fg='black')
lockout_pdw = tk.Label(loginFrame, text= "Sign in Locked for 5 minutes", font=('times new roman', 15, 'bold'), bd=5, fg='black')
#_________________lockout_______________#



loginButton = tk.Button(loginFrame,
                     text='Login',
                     font=('times new roman', 14, 'bold'),
                     width=15, fg='white',
                     bg='cornflowerblue',
                     activebackground='cornflowerblue',
                     activeforeground='white',
                     cursor='hand2', command=check_if_admin_or_student)
loginButton.grid(row=4, column=1, pady=10)

window.mainloop()