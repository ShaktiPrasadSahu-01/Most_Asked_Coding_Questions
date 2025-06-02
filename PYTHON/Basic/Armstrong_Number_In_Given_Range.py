'''Find the Armstrong Number in a given range in Python'''
#Method1
low, high = 10, 10000
for n in range(low, high + 1):
    #order of number 
    order = len(str(n))

    #initialize sum
    sum = 0
    temp = n
    while temp>0:
        digit = temp % 10
        sum  += digit ** order
        temp //= 10
    if n == sum:
        print(n, end=", ")


#Method2
import math

first, second = 150, 10000


def is_Armstrong(val):
    sum = 0

    # this splits the val into its digits
    # example val : 153 will become [1, 5, 3]
    arr = [int(d) for d in str(val)]

    # now we iterate on array items (digits)
    # add these (digits raised to power of len i.e order) to sum
    for i in range(0, len(arr)):
        sum = sum + math.pow(arr[i], len(arr))

    # if sum == val then its armstrong
    if sum == val:
        print(str(val) + ", ", end="")


for i in range(first, second + 1):
    is_Armstrong(i)
