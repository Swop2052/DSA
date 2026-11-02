# Level :- 1 Basic
# Objective: Understand class creation, object creation and accessing attributes.
# class student:
#     name = "swop"
#     age = 20
# s1 = student()
# print(s1.name)
# print(s1.age)

# Multiple Object in One Class
# class Car:
#     brand = "BMW"
# c1 = Car()
# c2 = Car()
# print(c1.brand)
# print(c1.brand)


# Object-specific attributes -  Assigning attributes to individual objects.
# class Student:
#     pass

# s1 = Student()
# s2 = Student()

# s1.name = "Swop"
# s2.name = "Rahul"

# print(s1.name)
# print(s2.name)

# Creating Method - Defining and calling methods.
# class Emp:
#     def display(self):
#         print("Hello")

# e1 = Emp()
# e1.display()


# Mutiple Method in one class
# class Calculator:
#     def add(self):
#         print(10 + 20)

#     def multiply(self):
#         print(10 * 20)

# c1 = Calculator()
# c1.add()
# c1.multiply()
# ------------------------------------------------------------------------------------------------------------------

# Level 2 - Constructors and self
# Objective: Understand __init__(), parameters and instance attributes.
# Basic Constructor
# class student:
#     def __init__(self):
#         print("Obj Created")
# s1 = student()


# Constructor with parameters  - Passing values during object creation.
# class student:
#     def __init__(self,name):
#         self.name = name
       
# s1 = student("swop")
# print(s1.name)

# Multiple atrributes
# class Employee:
#     def __init__(self, name, salary, age):
#         self.name = name
#         self.salary = salary
#         self.age = age

#     def display(self):
#         print(self.name)
#         print(self.salary)
#         print(self.age)

# e1 = Employee("Swop", 30000, 20)
# e1.display()

# ---------------------------------------------------------------------------------------

# Level - 3 Methods and object behaviour
# Addition using Obj
# class add:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def calculate(self):
#         return self.a + self.b
# obj = add(10,20)
# print(obj.calculate())
        
# Bank account deposit 
# class Bank:
#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def display(self):
#         print("Balance:", self.balance)

# b1 = Bank(5000)
# b1.deposit(2000)
# b1.display()

# Bank account withdrawal

class Bank:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def display(self):
        print(self.balance)

b1 = Bank(10000)
b1.withdraw(3000)
b1.display()