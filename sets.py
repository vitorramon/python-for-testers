# Sets are unordered collections of unique elements.
#
# Sets are defined by values separated by curly braces {}. However, if you try to create an empty set using {}, you'll end up creating an empty dictionary.
#
# To create an empty set, you must use the set() function.
#
# Sets are unordered, so you cannot access items by index.
#
# Sets are unchangeable, so you cannot change the items after the set has been created.

example_set = {1, 2, 3, 4, 5}
print(example_set)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.symmetric_difference(set2))

example_set.add(6)
print(example_set)
example_set.remove(1)
print(example_set)