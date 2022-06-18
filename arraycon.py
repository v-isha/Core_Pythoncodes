from array import *

std_roll = array("i",[101,102,103,104,105])

a = len(std_roll)
for i in range(a):
    print(std_roll[i])
print("***************************")

roll =array("i",[10,20,30,40])
n = len(roll)
for i in range(n):
    print(roll[i])
print("***************************")


roll.append(106)
roll.insert(0,501)
roll.insert(1,506)
n = len(roll)
for i in range(n):
    print(roll[i])



