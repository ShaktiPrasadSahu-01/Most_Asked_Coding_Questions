'''Check wheather Not the number is an Automorphic or not '''
num = 376 
a = str(num)
num1 = num ** 2
b = str(num1)
if b.endswith(a):
    print("Automorphic")
else:
    print("Not an Automorphic")

def is_automorphic(n):
    square = n*n
    digits = len(str(n))
    if square % (10**digits) == n:
        print("Automorphic")
    else:
        print("Not Automorphic")
is_automorphic(5)
