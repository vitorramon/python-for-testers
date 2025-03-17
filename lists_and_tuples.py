# Lists
# Lists are used to store multiple items in a single variable.
# Lists are created using square brackets.
# List items are ordered, changeable, and allow duplicate values.

print("Lists!!!!!!!!!!!")
empty_list = []

print(empty_list)

mylist = [1, 2, 3, 4, 5, "apple", "banana", "cherry", "grape", "kiwi" , 3.14, 2.71]

print(mylist)
print(mylist[0])
print(mylist[1])

sliced_list = mylist[1:5]
print(sliced_list)

mylist[3] = "orange"
print(mylist)

print(len(mylist))

mylist.append(6)
print(mylist)

mylist.extend([11, 12, 13, "banana"])
print(mylist)

mylist.insert(0, "zero")
print(mylist)

print(mylist.count("banana"))
print(mylist.index("banana"))

# Tuples
# Tuples are used to store multiple items in a single variable.
# Tuples are created using parentheses.
# Tuple items are ordered, unchangeable, and allow duplicate values.

print("Tuples!!!!!!!!!")
empty_tuple = ()
print(empty_tuple)

mytuple = (1, 2, 3, 4, 5, "apple", "banana", "cherry", "grape", "kiwi" , 3.14, 2.71)
print(mytuple)

print(mytuple[0])

print(mytuple[1:5])

print(len(mytuple))
print(mytuple.count("apple"))
print(mytuple.index("apple"))