# Define function
def myfunction():
    print("Hello from a function")

#Calling Function
myfunction()

#Function parameters

print("\nFunction Parameters")

def myfunction(fname):
    print(fname + "Refsnes")

myfunction("Email")
myfunction("Tobias")
myfunction("Linux")

#Default parametes
def my_function(country="Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Passing list as a parameter
print("\nPassing list as a parameter")
def listFunc(food):
    for i in food:
        print("Fruit_name: ",i)

fruits = ["apple","banana","orange"]
listFunc(fruits)

#Return value
print("\nReturn value")
def return_func(x):
    return 5*x

print(return_func(3))
print(return_func(5))
print(return_func(9))

def returnFunc(child3,child2,child1):
    print("The youngest child is " + child3)

returnFunc(child1 = "Emil", child2="Tobias", child3="Linus")