#recursive function that takes an integer n and returns the sum of all numbers from 1 to n.
sum = 0

def sum(n):
    if(n == 0):
        return 0
    else:
        return n + sum(n-1)
    

n = int(input("Enter a number: "))
print(sum(n))
