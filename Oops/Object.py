'''
Object
An object is a specific instance of a class. It holds its own set of data (instance variables) and can invoke methods defined by its class. Multiple objects can be created from same class, each with its own unique attributes.
'''
# Let's create an object from Dog class.

class Dog:
    sound = "bark"

# Creating object from class
dog1 = Dog()  
print(dog1.sound)