# Class is a collection of objects. and it is BluePrints
# A class is a user-defined template for creating objects. It bundles data and functions together, making it easier to manage and use them. When we create a new class, we define a new type of object. We can then create multiple instances of this object type.
# Define a Class
# class Dog:
#     sound = "Bark"  # class attribute


class Emp:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display(self):
        print("Name:",self.name)
        print("Name:",self.salary)

e1 = Emp("Swop", 30000)
e1.display()

'''
Line-by-line explanation
Line 1: class Emp:
- class – A Python keyword used to create a class.
- Emp – Name of our class.
- : – Indicates the beginning of the class body.
Why do we use it?

A class acts as a blueprint for creating objects. Here, Emp is the blueprint for employee objects.

Line 2: def __init__(self, name, salary):

Let's break it down:
- def – Keyword used to define a function or method.
- __init__ – A special method called automatically when a new object is created.
- self – Refers to the current object.
- name – Parameter that receives the employee's name.
- salary – Parameter that receives the employee's salary.
- : – Starts the method body.
Why do we use it?

We use __init__() to initialize an object's attributes when it is created.

Line 3: self.name = name
- self – Refers to the current object.
- self.name – An instance attribute belonging to that object.
- = – Assignment operator.
- name – Value received through the constructor parameter.
Why do we use it?

To store the employee's name inside the object so that we can access it later.

Line 4: self.salary = salary
- self.salary – Creates an instance attribute called salary.
- salary – Receives the salary value from the constructor.
Why do we use it?

To store the employee's salary inside the object.

Line 5: def display(self):
- def – Defines a method.
- display – Name of the method.
- self – Refers to the object calling the method.
Why do we use it?

To define an operation that displays employee information.

Line 6: print("Name:", self.name)
- print() – Displays information on the screen.
- "Name:" – A text label.
- self.name – Retrieves the name stored in the current object.
Why do we use it?

To display the employee's name.

Line 7: print("Salary:", self.salary)
- "Salary:" – Label displayed on the screen.
- self.salary – Retrieves the salary stored in the object.
Why do we use it?

To display the employee's salary.

Line 9: e1 = Emp("Swop", 30000)
- e1 – Variable storing the object reference.
- Emp() – Calls the class to create a new object.
- "Swop" – Passed as the name argument.
- 30000 – Passed as the salary argument.
Why do we use it?

To create an employee object with its own name and salary.

When this executes, Python automatically calls __init__().

Line 10: e1.display()
- e1 – Refers to our employee object.
- . – Accesses an attribute or method of the object.
- display() – Calls the display method.
Why do we use it?

To execute the method and display the employee's information.

'''