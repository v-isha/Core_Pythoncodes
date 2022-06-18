from array import *
blank_arr = array("i",[])
a = int(input("how many element do you want to add"))

for i in range(a):
        blank_arr.append(int(input("Enter your number")))

for i in range(len(blank_arr)):
    print(blank_arr[i])

