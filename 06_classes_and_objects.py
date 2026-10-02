#Create a class

class myClass:
    x = 5

#Create object

p1 = myClass()
print(p1.x)

#The_init_function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)



#Object Methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello My name is " + self.name)
        print("My age is " + self.age)

p1 = Person("John", 36)
p1.myfunc()
