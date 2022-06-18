from cupshelpers import Printer
from regex import P


a=10
b=10
print(id(b))
a=20
print(id(a))
y=a
print(id(y))

# string

str="hello world"
print(str)
print(type(str))

# list
list =[10,20,30,"vishal"]
print(type(list))
print(list[1])
# tuple
tu =(10,20)
print(type(tu))

# range
rg = range(5)
for i in rg:
    print(i)



# membership operator


str = "hello world how are you"
print("wo" in str) 
if "wo" in str :
    print("welcome")


# identity operator

x=10
y=10
print(x is not y)

list=[10,20,30,40,50]
print(type(list))
tu =tuple(list)
print(type(tu))

print(tu)
