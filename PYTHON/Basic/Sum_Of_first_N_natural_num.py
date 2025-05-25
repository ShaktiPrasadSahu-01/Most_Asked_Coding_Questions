'''Python Program to find the sum of first N natural numbers'''
#Method 1 : Using for Loop
num = 5
sum = 0
for i in range(num+1):
    sum+=i
print(sum)



#Method 2 : Using Formula for the Sum of Nth Term
''' Sum = (Num*(Num+1))/2 '''
num = 5
print(int(num*(num+1)/2))



#Method 3 : Using Recursion
def getSum(num):
    if num == 1:
        return 1
    return num + getSum(num - 1)
num = 5
print(getSum(num))
