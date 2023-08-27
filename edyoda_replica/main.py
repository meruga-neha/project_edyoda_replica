import sys
from admin import *
admin1 = Admin_panel()

while True:
    print("press 1 for admin login!")
    print("press 2 for student login!")
    print("press 3 for trainer login!")
    print("press 4 for exit!")
    choice = int(input("enter your choice: "))
    print("*"*100)
    if choice == 1:
        print("*************************ADMIN LOGIN********************************")
        username = input("enter admin username: ")
        password = input("enter admin password: ")
        temp = admin1.admin_login(username,password)
        if temp:
            print("logged in successfully!")
            print("press 1 for add module")
            print("press 2 for add trainer")
            print("press 3 for add student")
            print("press 4 for add batch")
            print("press 5 to get module details")
            print("press 6 to get trainer details")
            print("press 7 to get batch details")
            print("press 8 to get student details")
            print("press 9 to remove module")
            print("press 10 to update trainer details")
            print("*"*100)
            option = int(input('enter your choice: '))
            if option == 1:
                print(admin1.add_module())
                print("*"*100)
                print("module added successfully!")
                print("*"*100)
            elif option == 2:
                print(admin1.add_trainer())
                print("*"*100)
                print("trainer added susscesfully!")
                print("*"*100)
            elif option == 3:
                print(admin1.add_student())
                print("*"*100)
                print("student added successfully!")
                print("*"*100)
            elif option == 4:
                print(admin1.add_batch())
                print("*"*100)
                print("batch added successfully!")
                print("*"*100)
            elif option == 5:
                print(admin1.read_module_details())
                print("*"*100)
            elif option == 6:
                print(admin1.read_trainer_details())
                print("*"*100)
            elif option == 8:
                print(admin1.read_Student_details())
                print("*"*100)
            elif option == 9:
                print(admin1.remove_module())
                print("*"*100)
                print("module updated!")
                print("*"*100)
            elif option == 10:
                print(admin1.update_trainer_Details())
                print("*"*100)
                print("trainer details updated successfully!")
                print("*"*100)
            else:
                print("please give valid input!")
        else:
            print("please enter valid username and password!")
    elif choice == 2:
        print("************************STUDENT LOGGED SUCCESSFULLY**********************************")
    elif choice == 3:
        print("***********************TRAINER LOGGED SUCCESSFULY************************************")
    elif choice == 4:
        print("************************THANK YOU FOR USING OUR APPLICATION***************************")

