#This is a program to find the prime factors for numbers we input
def factor(n):
    for a in range(1, n + 1):
        if n % a == 0:
            if prime_number(a) == True:
                print a





def prime_number(a):
    if a <=1:
        return False
    elif a == 2:
        return True
    for i in range(2, a):
        if a % i == 0:
            return False
    return True



n = input("please enter a number:" )

factor(n)
