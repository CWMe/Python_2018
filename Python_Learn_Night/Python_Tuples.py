# Tuples are Python's Immutable version of the Sequence Data Type

tuple1 = (1, 2, "Hello")
tuple2 = (100, )
tuple3 = 10, 20, 30
empty_tuple = tuple()

# because they are immutable we cannot add or remove individual elements
del tuple2

# We still have the basic methods from lists that can be applied to tuples
# len()
# concatenation (+)
# repetition (*)
# "in" method

# Why use tuples?
# - Certain major functions in different modules return data in the form of a tuple
# - Tuples are comparable:
if (0, 1, 2) < (0, 10, 20):
    print("The above statement evaluated to true.")

# How? - comparing each element to see which is greater, if tied then moves to the next, and continues.

# Tuple assignments:
x, y = ["hello", "world"]

# Dictionaries and Tuples
# dictionaries have a method called .items() which return the key-value pair in the form of a tuple.
# since tuples are comparable the dictionary elements get ordered.
