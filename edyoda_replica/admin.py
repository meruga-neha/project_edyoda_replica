import json
import random
import datetime
class Admin_panel:
    def __init__(self):
        self.module_details = {}
        self.count = 0
        self.trainer_details = {}
        self.batch_details = {}
        self.student_details = {}
    def admin_login(self,username,passcode):
        if username == 'admin' and passcode == 'admin123':
            return True
        return False
    def add_module(self):
        self.count = self.count+1
        module_name = input('enter module name: ')
        duration = input('enter the duration period: ')
        topic_list = []
        topic_size = int(input('enter the topic size you want to add: '))
        for i in range(1,topic_size+1):
            topic = input(f"enter topic {i} name")
            topic_list.append(topic)
        module_items = {'module_name':module_name,'duration':duration,'topics':topic}
        self.module_details[self.count] = module_items
        with open('add_module.json','w') as f:
            json.dump(self.module_details,f,indent=4)
            return self.module_details
    def add_trainer(self):
        self.count = self.count+1
        name = input('enter the trainer name: ')
        gender = input('enter the trainer gender: ')
        qualification = input('enter the trainer qualification: ')
        mob = int(input('enter the trainer mobile number: '))
        email = input('enter the email id: ')
        password = input('enter the password: ')
        trainer_data = {'trainer_name': name,'trainer_gender': gender,'trainer_qualification': qualification,'mobile_number': mob,'email': email,'password': password}
        self.trainer_details[self.count] = trainer_data
        with open('trainer_Details.json','w') as f:
            json.dump(self.trainer_details,f,indent=4)
        return self.trainer_details
    def add_batch(self):
        self.count = self.count+1
        std_list = []
        module_name = input('enter module name: ')
        trainer_name = input('enter trainer name for that batch: ')
        student_size = int(input('enter the no of students: '))
        for i in range(1, student_size+1):
            std = input('enter student {i} name  ')
            std_list.append(std)
        batch_data = {'module_name': module_name,'trainer_name':trainer_name,}
        self.batch_details[self.count] =batch_data
        with open('batch_Details.json','w') as f:
            json.dump(self.batch_details,f,indent=4)
        return self.batch_details
    def read_trainer_details(self):
        with open('E:/trainer_details.json','r') as f:
            data = json.load(f)
        for k,v in data.items():
            print(f'trainer_id: {k} || trainer_details: {v}')
            print('*'*100)
    def read_module_details(self):
        with open('add_module.json','r') as f:
            data = json.load(f)
            for k,v in data.items():
                print(f'module_id: {k} || module_details: {v}')
                print('* *100')
    def add_student(self):
        current_date = datetime.datetime.now()
        exact_date = str(current_date.day)+str(current_date.month)+str(current_date.year)[2::]
        if len(exact_date)==4:
            exact_date = "0"+str(current_date.day)+"0"+str(current_date.month)+str(current_date.year)[2::]
        else:
            exact_date = str(current_date.day)+str(current_date.month)+str(current_date.year)[2::]
        
        key = "ds"+str(exact_date)
        student_list = []
        student_size = int(input('enter the student which you want to add: '))
        for i in range(1,student_size+1):
            print(f"enter the details of student {i}  ")
            name = input(f"enter the name of student {i}  ")
            gender = input(f"enter the gender {i}  ")
            age = int(input(f"enter the age of student {i}  "))
            qualification = input(f"enter the qualification {i}  ")
            experience = input(f"enter the experience {i}  ")
            mob = int(input(f"enter the mobile no {i}  "))
            email = input(f"enter the email id {i}  ")
            password = input(f"enter the password {i}  ")
            student_data = {'name':name,'gender':gender,'age':age,'qualification':qualification,'experience':experience,'mob':mob,'email':email,'password':password}
            student_list.append(student_data)
        self.student_details[key] =student_list
        with open('student_Details.json','w') as f:
            json.dump(self.student_details,f,indent=4)
        return self.student_details
    def read_Student_details(self):
        with open('student_details.json','r') as f:
            data = json.load(f)
            for k,v in data.items():
                print(f"student_id: {k} || student_details: {v}")
                print("*"*100)
    def update_trainer_Details(self):
        with open("trainer_details.json","r") as f:
            data = json.load(f)
            for k,v in data.items():
                print(f"trainer_id: {k} || trainer_details: {v}")
                print("*"*100)
            id = input("enter the trainer id which u want to update: ")
            field = input("enter the field which you want to update: ")
            updated_value = input("enter the updated value: ")
            data[id][field] = updated_value
            with open("trainer_details.json","w") as f:
                json.dump(data,f,indent=4)
            return data
    def remove_module(self):
        with open("add_module.json","r") as f:
            data = json.load(f)
        for k,v in data.items():
            print(f"Module_id : {k}  || Module Details : {v}")
            print("*"*100)
        id = input("Enter Module ID which you want to remove :")
        del data[id]
        with open("add_module.json","w") as f:
            json.dump(data,f,indent=4)
        return data
x = Admin_panel()
print(x.read_module_details())
