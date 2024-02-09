#opening file in write mode

file = open("ab.txt", "r+")

#writing and reading in the file

file.write("hello ")

print(file.read())

#closing the file 


file.close()

#in r+ stream is positioned at starting position
