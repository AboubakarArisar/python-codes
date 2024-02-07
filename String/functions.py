#functions of string in python

#endswith() method

#The endswith() method returns True if a string ends with the 
#specified suffix. If not, it returns False.
#Example
txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)

#capitalize() method
name = "hello, and welcome to my world."
print(name.capitalize())

#replace() method
a = "Hello, World!"
print(a.replace("H", "J"))
print(a.replace("Hello", "Bye"))

#find() method
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

#count() method
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
