#basic methods of sets in python

#add() method

my_set = {1, 3}

my_set.add(2)

print(my_set)

#remove() method

my_set.remove(3)

print(my_set)

#discard() method

my_set.discard(2)

print(my_set)


#pop() method randomly removes an element from the set

my_set.add(2)
my_set.add(9)
my_set.add(5)

print(my_set.pop())

#union() method returns a new set with all items from both sets

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))

#intersection method returns a new set with items that are in both sets

print(set1.intersection(set2))



