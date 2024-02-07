#dictionary is a collection of key-value pairs
#dictionary is a mutable, unordered collection of key-value pairs

dict = {'Name': 'Aboubakar', 'Age': 20, 'Semester': 'Fourth'}

print(dict)

#accessing values
print(dict['Name'])
print(dict['Age'])
print(dict['Semester'])

#updating values
dict['Age'] = 21
print(dict)

#adding new key-value pair
dict['University'] = 'IBA'
print(dict)

#deleting key-value pair
del dict['Semester']
print(dict)
