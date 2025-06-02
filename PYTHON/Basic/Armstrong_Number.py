'''Check wheather a given number is an Armstrong number or not ? '''
number = 371
num = number
digit, sum = 0, 0
length = len(str(num))
for i in range(length):
    digit = int(num % 10)
    num = num / 10
    sum = sum + pow(digit, length)
if sum == number :
    print("Armstrong")
else:
    print("Not Armstrong")
