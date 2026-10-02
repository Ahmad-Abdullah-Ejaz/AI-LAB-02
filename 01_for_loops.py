#List Iteration

print("List Iteration")
I = ["geeks","for","geeks"]

for i in I:
    print(i)

print(type(I))

#Tuple Iteration

print("\nTuple Iteration")
t = ("geeks","for","geeks")

for i in t:
    print(i)

print(type(t))

#Iteration over a String

print("\nString Iteration")
s="Geeks"

for i in s:
    print(i)

print(type(s))

#Iterating by index

list = ["geeks","for","geeks"]

for index in range(len(list)):
    print(list[index])