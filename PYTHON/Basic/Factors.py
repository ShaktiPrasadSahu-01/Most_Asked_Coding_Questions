'''Python program to find the factor/divisors of a number'''
def printDivisors(n):
    i = 1
    while i <= n:
        if(n%i == 0):
            print(i,end=" ")
        i = i + 1
printDivisors(100)
