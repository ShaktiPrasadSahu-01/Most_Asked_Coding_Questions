'''Check Whether or Not the number is an Abundant number in python'''
def Abundant_No(n):
    i = 1
    total = 0
    while i < n:
        if n % i == 0:
            total += i
        i+=1
    if n < total:
        print('Abundant number')
    else:
        print("Not Abundant")
Abundant_No(12)
