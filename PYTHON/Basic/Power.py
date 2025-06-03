'''Python code to find power of number using recursion'''
num, power = 3, 2
def powerrcur(num, power):
    if power == 0:
        return 1
    return num * powerrcur(num, power-1)
print(powerrcur(num,power))
