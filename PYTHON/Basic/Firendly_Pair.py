''' Python Program to check wheather two number are friendly pair?'''
def sum_of_divisors(n):
    total = 0
    for i in range(1,n):
        if n%i == 0:
            total += i
    return total
def is_friendly_pair(a,b):
    if sum_of_divisors(a) == b and sum_of_divisors(b) == a:
        print("friendly pair")
    else:
        print("Not Friendly pair")
is_friendly_pair(220,284)
