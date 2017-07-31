#This is a program to do bubble sort the list we creat
def bubble(a):
    for index in range(len(a) - 1, 0, -1):
        for two_index in range(index):
            if a[two_index] > a[two_index + 1]:
                a[two_index], a[two_index + 1] = a[two_index +1], a[two_index]



n = input("please enter a number:" )
a = []
for i in range(1, n + 1):
    data = input("the '%s' time:" % (i) )
    a.append(data)
import pdb;pdb.set_trace()
bubble(a)
print a

