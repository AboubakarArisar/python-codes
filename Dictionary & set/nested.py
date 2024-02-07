#nested dictionary
dict = {'Name': 'Aboubakar', 'Age': 20, 'Semester': 'Fourth', 'Address': {'City': 'Sukkur', 'Country': 'Pakistan'}}

print(dict)

#accessing values
print(dict['Name'])
print(dict['Age'])
print(dict['Semester'])
print(dict['Address']['City'])
print(dict['Address']['Country'])

#updating values
dict['Age'] = 21
print(dict)

#adding new key-value pair
dict['University'] = 'IBA'
print(dict)

#deleting key-value pair
del dict['Semester']

print(dict)

#deleting nested key-value pair
del dict['Address']['City']
print(dict)

#deleting whole nested dictionary
del dict['Address']
print(dict)
