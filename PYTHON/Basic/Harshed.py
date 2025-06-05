'''Write a program to check a given number is a harshed number '''
def is_harshed(n):
    temp = n
    digit_sum = 0
    while temp > 0:
        digit_sum += temp %10
        temp //=10
    if n%digit_sum == 0:
        print("Haeshed Number")
    else:
        print("Not a harshed Number")
is_harshed(18)
