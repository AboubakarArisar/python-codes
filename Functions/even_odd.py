#even odd in python

def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

x = int(input("Enter a number: "))

print(even_odd(x))
