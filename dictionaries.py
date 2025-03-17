# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values.
#
# *As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
#
# Example
# Create and print a dictionary:
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)


empty_dict = {}
print(empty_dict)

my_dict = {
    "name": "Vitor Ramon",
    "age": 23,
    "city": "Manaus"
}
print(my_dict)

print(my_dict["name"])
print(my_dict["age"])
print(my_dict["city"])

print(f"Hello, I'm {my_dict['name']} and I'm {my_dict['age']} years old. I live in {my_dict['city']}.")

my_dict["language"] = "Python"
print(my_dict)

my_dict["language"] = "Python and JavaScript"
print(my_dict)

del my_dict["language"]
print(my_dict)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())