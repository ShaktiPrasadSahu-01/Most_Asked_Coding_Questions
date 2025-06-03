'''factorial of number ? '''
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
n = 5
print(f"Factorial of {n} is:", factorial(n))

'''Using Recursion'''
def factorial1(n):
    if n==0 or n==1:
        return 1
    return n*factorial1(n-1);
n=5
print(factorial1(n))
