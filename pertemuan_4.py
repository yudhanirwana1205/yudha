# class Person:

#     def __init__(self, first_name, last_name, age, address, hobby="Tidak Ada Hobby"):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.address = address
#         self.hobby = hobby

#     def my_full_name(self):
#         return self.first_name + " " + self.last_name

#     def my_hobby(self):
#         print("My hobby is " + self.hobby)


# person_1 = Person('John',
#                   'Doe',
#                   36,
#                   'Bandung')

# person_1.my_hobby()


# class Student(Person):

#     def __init__(self, nisn, first_name, last_name, age, address, hobby):
#         super().__init__(first_name, last_name, age, address, hobby)
#         self.nisn = nisn

#     def my_hobby(self):
#         return 'Hobi saya adalah ' + self.hobby

#     def data_diri_dict(self):
#         return {
#             'nama': self.my_full_name(),
#             'umur': self.age,
#             'hobby': self.my_hobby()
#         }


# student_1 = Student('1234', 'yudha', 'Nirwana', 15 , 'KAWALI', 'Berolahraga')

# student_1.my_hobby()

# print(student_1.data_diri_dict())


# car_1 = car('Honda', 2022)
# car_1.open_door()
# car_1.close_door()
# car_1.start_engine()
# car_1.step_engin() 



