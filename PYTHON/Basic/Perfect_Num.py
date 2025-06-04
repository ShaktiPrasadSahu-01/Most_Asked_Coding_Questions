''' Check wheather or not the number is perfact number'''
def perfect_num(n):
    i = 1
    total = 0
    while i <n:
        if n % i == 0:
            total += i
        i+=1
    if n == total:
        print("perfect no")
    else:
        print("Not a perfect no")
perfect_num(28)



'''Using Recursion'''
def sum_of_divisors(n,i=1):
    if i == n:
        return 0
    if n%i == 0:
        return i + sum_of_divisors(n,i+1)
    else:
        return sum_of_divisors(n,i+1)
def is_perfect_number(n):
    if sum_of_divisors(n) == n:
        print("Perfecto")
    else:
        print("Not Perfecto")
is_perfect_number(28)
