#syntax is easier using with

with open("ab.txt", "r") as f:
    data = f.read()
    print(data)

with open("ab.txt", "r") as f:
    f.write("writing this again in the file")
