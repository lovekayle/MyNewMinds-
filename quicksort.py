#This is a program to quick sort the list we creat
def path_sort(a, start_index, end_index):
    flag = a[end_index]
    i = start_index - 1
    for j in range(start_index, end_index):
        if a[j] > flag:
            pass
        else:
            i = i + 1
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
    tmp = a[end_index]
    a[end_index] = a[i + 1]
    a[i + 1] = tmp
    print a
    return i + 1

def quick_sort(a, start_index, end_index):
    if start_index >= end_index:
        return
    middle = path_sort(a, start_index, end_index)
    quick_sort(a, start_index, middle - 1)
    quick_sort(a, middle + 1, end_index)ll_the_text.upper()






n = input("please enter a number:" )
a = []
for i in range(1, n + 1):
    data = input("the '%s' time:" % (i) )
    a.append(data)
import pdb;pdb.set_trace()
quick_sort(a, 0, len(a) - 1)
