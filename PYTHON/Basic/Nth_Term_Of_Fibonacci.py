'''Find the Nth term of fibonacci Series in python'''
def Fibonacci(n):
    if n < 2:
        return n
    fs = [0, 1]
    for i in range(1, n):
        fs.append(fs[i] + fs[i - 1])
    return fs[n]

n = 6
print(Fibonacci(n-1))
