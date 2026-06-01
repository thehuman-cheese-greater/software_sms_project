
class User:
    def __init__(self, username, password, user_id, age ):
        self.username =  username
        self.password = password
        self.user_id = user_id
        self.age = age



class Admin(User): #admin will inherit from user
    def __init__(self, username, password): 

        super().__init__(username, password)


    def admin_login_details():  # admin login details (hashed value)
        # To uderstand how the hashed value was found to store here || (refer to the end of this file - Line 52)
        admin_dict = {"username" : b'$2b$12$Adf4pnqH/1IYRurvlJHh2O.PnAI1iFswxVyBnYL5J8e5s2vlQ6vKq', 
                      "password" : b'$2b$12$Adf4pnqH/1IYRurvlJHh2OwdN7JOp7/i1MRna7QGzKGtQUPMGtktG'}     
        return admin_dict["username"], admin_dict["password"]

    def courses_available(**course_details):
        return dict(**course_details)
    


class Student(User): # student will inherit from user
    def __init__(self, username, password, gender, dob, phonenumber, email, adress, student_id): 

        super().__init__(username, password, gender)
        self.gender = gender
        self.dob = dob
        self.phonenumber = phonenumber
        self.email = email
        self.adress = adress
        self.student_id = student_id


    def student_login_details(): # Student login details (hashed value)
        student_dict = {"username1" : b'$2b$12$kIUFejZkuGMdv3W1mSTKVu744oU138BIHCsRVughAtoZUEfVS/G36', 
                        "password1" : b'$2b$12$Adf4pnqH/1IYRurvlJHh2OwBh5hn8riOMmCnn7d5Dt3LSeJNyQkRe', 
                        "ID1" : 2}
        return student_dict["username1"], student_dict["password1"], student_dict["ID1"]

    def student_courses(**student_course_details):
        return dict(**student_course_details)
    



# #______Geting the hashed value to store in dictionary_________#
# #generating the salt (it will generate a random string, that will be added with the bytes later to get hashed value)
# generated_salt = bcrypt.gensalt()  

# #_____For_Admin_____(student is the same method)#
# #encoding the username
# new_admin_username = "mark"  #note: value is not real username as this is an example of the method
# admin_bytes_username = new_admin_username.encode('utf-8')

# # #encoding the password 
# new_admin_password = "1111"     #note: value is not real password as this is an example of the method
# admin_bytes_password = new_admin_password.encode('utf-8')

# #hash the admin details (combining the bytes and salt)
# admin_username_hashed = bcrypt.hashpw(admin_bytes_username, generated_salt) 
# admin_password_hashed = bcrypt.hashpw(admin_bytes_password, generated_salt)

# print("Admin username:", admin_username_hashed) # Show the Hashed value that will be stored in the login detail dictionaries. 

# print("Admin password:", admin_password_hashed)
