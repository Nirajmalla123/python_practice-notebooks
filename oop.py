"""
Object oreinted Programming
class: blueprint of an object
obkect: instance of a clss

syntax:
class ClassName:
    Attributes
    properties
    methods
    constructors


obj = ClassName()


"""

# class Student:
#     pass

# Student1= Student()
# print(Student1)

#methods
# class Student:
#     def greet(self, name):
#         print(f"welcome{name}")

# #name = input("Enter name: ")
# std = Student()
# std.greet("Ram")

#constructor:
#runs automatically when object is created
#__init__(): is the initializer that runs automatically

# class person:
#     def __init__(self):
#         print("Object Created..........")

# p1 = person()
# p2 = person()
# p3 = person()


# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"age: {self.age}")

# p1 = person("ram",21)


# class Student:
#     def set_name(self,name):
#         self.name = name

#     def show(self):
#         pass

# s1 = Student()
# s1.set_name("Ram")
# s1.show()


class Demo:
    def __init__(self):
        self.name = "Ram" # public attribute
        self._age =20 # protected attribute
        self.__salary = 10000 # private attribute
        
    def show_name(self): # public method
        print(self.name)
    
    def _show_age(self): # protected method
        print(self._age)
        
    def __show_salary(self): # private method
        print(self.__salary)

    def show(self):
        self.__show_salary()

d = Demo()
print(d.show_name())
print(d._show_age())
print(d.show()) # private method can be accessed by public method of the same class



'''

Inheritance: mechanism where one class acquires the properties and mathods of another class. 
the properties and methods of parent class can be accessed by child class.  
syntax:
class parent_class:
    pass
class child_class(parent_class):
    pass

'''

class Person:
    def show(self):
        print("This is a peerson")

class Student(Person):
    def display(self):
        print("This is a student")

student = Student()
student.show()
student.display()


# inheritance with constructor 

class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def display(self):
        print(self.name)
        
s = Student("Ram")
s.display()

# super() keyword: used to call the constructor of parent class from child class. (if both child and parent class have constructor then we can use super() to call the constructor of parent class from child class )

class Person:
    def __init__(self, name):
        self.name = name
    def show(self):
        print("This is a person")
        
class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll
    def display(self):
        super().show()
        print(self.name)
        print(self.roll)

s = Student("Ram",101)
s.display()


# multileve inheritance:Grandfather ->Father-> Child:A->B->C when a class is derived from another derived class.

class Grandfather:
    def land(self):
        print("Grandfather has 10 acres of land")

class Father(Grandfather):
    def house(self):
        print("Father has a house")

class Child(Father):
    def car(self):
        print("Child has a car")


son = Child()
son.car()
son.house()
son.land()



class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
        
    def show_employee(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")

class Developer(Employee):
    def __init__(self, name, emp_id, programming_language):
        super().__init__(name, emp_id)
        self.programming_language = programming_language
        
    def write_code(self):
        print(f"{self.name} is writing code in {self.programming_language}")

class BackendDev(Developer):
    def __init__(self, name, emp_id, programming_language, database):
        super().__init__(name, emp_id, programming_language)
        self.database = database
        
    def build_backend(self):
        print(f"{self.name} is building backend using {self.programming_language} and {self.database}")
        

# multiple inheritance: one child-> multiple parents: A->B, C->D

class Developer:
    def write_code(self):
        print("Developer is writing code")
    
class Manager:
    def manage_team(self):
        print("Manager is managing the team")

class Techlead(Developer, Manager):
    def lead_team(self):
        print("Techlead is leading the team")
