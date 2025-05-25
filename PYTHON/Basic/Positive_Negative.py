'''Check if a Number is Positive or Negative in Python.'''
# Method 1: Using Brute Force
num = 15
if num > 0:
    print('Positive')
elif num < 0:
    print('Negative')
else:
    print('Zero')

# Method 2: Using Nested if-else Statements
num = 15
if num>=0:
    if num==0:
        print('Zero')
    else:
        print("Positive")
else:
    print("Negative")
# Method 3: Using ternary operator
'''
syntax for ternary operator:
    value_if_true if condition else value_if_false '''
num = 15
print("Positive" if num>=0 else "Negative")
