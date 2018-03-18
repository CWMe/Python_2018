import random


# Sequence data type in Python.
# We can index, slice, add, and other build in methods for lists

# We can add in ANY data type into the list
my_list = [1, 3.1415, "Hello CWM", [1, 2, 3]]

# Lists are mutable, they can be updated at any time
my_list[0] = "15"
# print(my_list)

# Python has built in methods for the list
# .append()
my_list.append(random.randint(0, 10))
print(my_list)

# deleting an element from a list
del my_list[0]
# my_list.remove()

# other important methods:
# Length of list
print(len(my_list))

list1 = [10, 20, 30]
list2 = [40, 50, 60]

# concatenate (+), repeat (*), and "in" method
if 20 in list1:
    print("True: 20 is in list1")

# max()
# min()

my_string = "Hello World"
print(list(my_string))

# list.index()
# list.insert()
# list.reverse()
# list.sort()
