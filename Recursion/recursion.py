#recursion in python

#in recursion function calls itself
#in recursion there is a base case and a recursive case
#base case is the condition where the function stops calling itself
#recursive case is the condition where the function calls itself

#printing numbers from 1 to 10 using recursion

def printing(n):
    if (n == 0):
        return
    printing(n-1)
    print(n , end=" ")


printing(10)

print()
#Printing numbers from 10 to 1 using recursion

def printing(n):
    if (n == 0):
        return
    print(n , end=" ")
    printing(n-1)


printing(10)
