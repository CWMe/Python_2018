# Dictionaries in Python
# { }
# Map data type in Python
# key : value paris for data.

my_dictionary = {"name": "CodeWithMe", "location": "library", "learning": "Python"}

# dictionaries may not retain the order in which they were created (before python 3.6.X).
# print(my_dictionary)

# accessing VALUES from a dictionary.
print(my_dictionary["learning"])

# we can add new key value pairs.
my_dictionary["date"] = "April"
del my_dictionary["date"]

# only 1 value per key
# the keys must be IMMUTABLE (strings, numbers, or tuples)

# useful methods for dictionaries
# .items()
# .keys()
# .values()

for key in my_dictionary.keys():
    if key == "location":
        continue
    else:
        print(key, my_dictionary[key])

