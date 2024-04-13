from math import sqrt

n = int(input("Enter the position of the Fibonacci number to find: "))

if n <= 0:
    result = 0
elif n == 1:
    result = 1
else:
    result = round((((1 + sqrt(5)) / 2) ** n - ((1 - sqrt(5)) / 2) ** n) / sqrt(5))

print(f"The {n}th Fibonacci number is: {result}")