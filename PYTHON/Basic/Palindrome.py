#Method 1:  Using Simple Iteration.
num = 1221
temp = num
reverse= 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse *  10) + remainder
    temp = temp // 10
if num == reverse:
    print('Palindrome')
else:
    print("not Palindrome")

#Method 2: Using String Slicing.
num = 1234
reverse = int(str(num)[::-1])
if num == reverse:
    print('Palindrome')
else:
    print("Not Palindrome")

#Method 3: Using Recursion
def recurrev(number, rev):
    if number == 0:
        return rev
    remainder = int(number % 10)
    rev = (rev * 10) + remainder
    return recurrev(int(number/10), rev)
num = 12321
rev = 0
reverse = recurrev(num, rev)

print(str(num) + "is:", end = " ")
print("Palindrome") if reverse == num else print("Not Palindrome")
