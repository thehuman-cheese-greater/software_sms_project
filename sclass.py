
# class Student:
#     def __init__(self, studentID, fullname, age, grade): # paramiters
#         # attrubutes 
#         # self.attrubutes = value
#         self.studentID =  studentID
#         self.fullname = fullname
#         self.age = age
#         self.grade = grade

#     # later send values for parementers
#     # can change self to anything e.g (kale,)

#     # fuctions

#     def study(self):
#         print(self.fullname, "is studying")

#     def sleep(self):
#         print(f"{self.fullname} is sleeping")

#     def updategrade(self, amount):
#         self.grade += amount
    
#     def checkpass(self):
#         if (self.grade>=50):
#             print("Pass")
#         else:
#             print("Fail")

#     def showdetails(self):
#         print(f"ID: {self.studentID}, name = {self.fullname}, age = {self.age}, grade = {self.grade}")

# # create object: 
# # objectname = className(parameters/s if needed)

# st = Student("ST22134", "Kale M", 19, 90)
# st.study()
# st.sleep()
# st.updategrade(5)
# st.checkpass()
# st.showdetails()
# st.age = 32 # updating values
# st.showdetails() # and show change

# # create another object

# print("-------------------------")

# myStudent = Student("ST22862", "Amanda Smith", 24, 85)
# myStudent.study()
# myStudent.sleep()
# myStudent.updategrade(10)
# myStudent.checkpass()
# myStudent.studentID = "ST99555"
# myStudent.showdetails()


# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def start(self):
#         print("the car is now on")

#     def drive(self):
#         print("car is moving")

#     def stop(self):
#         print("car has stopped")

#     def displayinfo(self):
#         print(f"{self.brand}, {self.model}, {self.year}")

# # creating object

# myCar = Car("BMW", "M6", 2023)
# myCar.start()
# myCar.drive()
# myCar.stop()
# myCar.displayinfo()
# myCar.year = 2021
# myCar.displayinfo()
    
class Vehicle(): # base class, super class
    def __init__(self, brand, model, year): # intialistion 
        self.brand = brand # attricbutes, that you'll send later
        self.model = model
        self.year = year
        # pass = skip for now
        
    #methods: behaviour, functions
    def start(self):
        print("Vehicle is starting")
    def stop(self):
        print("Vehicle is stopping")
    def showDetails(self):
        print(f"{self.brand}, {self.model}, {self.year}")

class Car(Vehicle): # car inherits from vehicle
    def __init__(self, brand, model, year, fuelType): # type _init__ and python completes the rest
        super().__init__(brand, model, year) # sending those paremeters to the super class
        self.fuelType = fuelType
    
    def drive(self):
        print("Driving the car")

    def start(self):
        print("The car is starting")
    

v = Vehicle("Unknown", "Unknown", 1990)   #car or vehicle
v.start()
v.stop()
v.showDetails()
print("-"*30)
# creating object from car
# object name = any
myCar = Car("Ford", "Mustang", 2024, "Gasoline")
myCar.year = 2023 # correction / update all atributes, even inherited atributes
myCar.start() # we can call inherided methods
myCar.drive()
myCar.stop()
myCar.showDetails()



