'''Check Whether a Year is a Leap Year or Not in Python'''
#Method 1: Using if-else statements 1
year = 2000
if (year%400 == 0) or (year%4==0 and year%100!=0):
    print("leap year")
else:
    print("Not a Leap year")




#Method 2: Using if-else statements 2
if (year%4==0 and year%100!=0) or (year%400==0):
    print("Leap Year")
else:
    print("Not leap year")



#Method 3 : Using Ternary Operator
def check_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
year = int(input("Enter a year:"))
print(f"{year} is leap year" if check_leap(year) else f"{year} is not leap year")


#Method 4 : Using Calendar Mode
import calendar 
year = int(input("Enter a year:"))
if calendar.isleap(year):
    print(year,"is a leap year")
else:
    print(year, "is not a leap year.")




#Method 5 : Using Lamda Function
