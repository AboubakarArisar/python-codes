#input in python

name = input("Enter your name: ")
print("Hello", name)

#problem is that input() function always returns a string. So, if you want to take an integer input from the user, you need to typecast it to int.
age = int(input("Enter your age: "))
print("Your age is", age)

