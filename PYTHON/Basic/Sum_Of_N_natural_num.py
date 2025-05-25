'''Python program to print sum of N natural numbers '''
#Method 1: Using for Loop
number,sum = 6, 0
for i in range(number+1):
    sum+=i
print(sum)



#Method 2: Using Formula
number = 6
sum = int((number*(number + 1))/2)
print(sum)




#Method 3: Using Recursion
def recursum(number):
    if number == 0:
        return number
    return number + recursum(number-1)
number = 6
print(recursum(number))

