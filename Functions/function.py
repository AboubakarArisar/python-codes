#functions in python

#function is a block of code that only runs when it is called.
# You can pass data, known as parameters, into a function. A function can return data as a result.

#Creating a function
def my_function():
  print("Hello from a function")

#Calling a function
my_function()

#Arguments
#Information can be passed into functions as arguments.

def my_function(fname):
    print(fname + " How are you?")

my_function("Aboubakar")

#Number of Arguments
#By default, a function must be called with the correct number of arguments.
# Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments,
# not more, and not less.

def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Aboubakar", "Arisar")

#Arbitrary Arguments, *args
#If you do not know how many arguments that will be passed into your function,

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


#Keyword Arguments
#You can also send arguments with the key = value syntax.

def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


#returning values
#To let a function return a value, use the return statement:

def my_function(x):
    return 5 * x

print(my_function(3))
