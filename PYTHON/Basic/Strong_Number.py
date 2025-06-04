'''Check wheather the number is strong number or not '''
def StrongNumber(n):
    temp = n
    total = 0
    while temp>0:
        digit = temp % 10
        f = 1
        for i in range(1,digit+1):
            f = f*i
        total += f
        temp = temp //10
    if total == n:
        print("Strong")
    else:
        print("Not strong")
StrongNumber(145)


'''Recursion'''
def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x-1)
def Sum_Of_Factorial(n):
    if n== 0:
        return 0
    digit = n%10
    return factorial(digit) + Sum_Of_Factorial(n//10)
def is_Strong(n):
    if Sum_Of_Factorial(n)==n:
        print("Strong")
    else:
        print("Not Strong")
is_Strong(145)
