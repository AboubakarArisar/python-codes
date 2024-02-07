#methods in list

#append adds the element at the end of the list
list = [1, 2, 3, 4, 5]
list.append(6)
print(list)

#sort sorts the list
list = [5, 3, 1, 4, 2]
list.sort()
print(list)
list.sort(reverse=True) #sorts in descending order
print(list)


#reverse reverses the list
list.reverse()
print(list)

#insert inserts the element at the specified index
list.insert(2, 10)
print(list)

#remove removes the first occurence of the element
list.remove(10)
print(list)

#pop removes the element at the specified index
list.pop(2)
print(list)




