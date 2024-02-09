#factorial in python

def factorial(n):
    sum = 1
    while n > 0:
        sum = sum * n
        n = n - 1
    return sum


x = int(input("Enter a number to find factorial: "))

print("Factorial of", x, "is", factorial(x))
