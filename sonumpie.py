from numpy import *
st_roll = array([10,20,30,40,50])

a = len(st_roll)
print("number of element in list", a)
print()
for i in range(a):
    print(st_roll[i])
#


# here we modified the place
st_roll[0]=548
print("_________________________________")
for i in range(a):
    print(st_roll[i])
print(st_roll.dtype)
