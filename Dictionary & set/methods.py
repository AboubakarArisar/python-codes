#dictionary methods

#keys returns all the keys in the dictionary

d = {'a': 1, 'b': 2, 'c': 3}
print(d.keys())

#values returns all the values in the  dictionary

print(d.values())

#items returns all the key value pairs in the dictionary

print(d.items())

#get returns the value of the key passed as argument

print(d.get('a'))

#setdefault returns the value of the key passed as argument if it exists, else it creates a new key value pair and returns the value

print(d.setdefault('d', 4))

#pop removes the key value pair from the dictionary and returns the value

print(d.pop('a'))

#popitem removes the last key value pair from the dictionary and returns the key value pair

print(d.popitem())

#clear removes all the key value pairs from the dictionary

d.clear()

print(d)

