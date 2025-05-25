'''Check whether a number is even or odd in python'''
#Method 1 : Using Brute Force
num = int(input("Enter a Number:"))
if num % 2 == 0:
    print("Given number is Even")
else:
    print("Given number is odd")


#Method 2 : Using Ternary Operator
num = 17
print("Even") if num%2 == 0 else print("odd")


#Method 3 : Using Bitwise Operators
def isEven(num):
    return not num&1
if __name__ == "__main__":
    num = 13
    if isEven(num):
        print('Even')
    else:
        print('Odd')
