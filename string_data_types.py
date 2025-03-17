str1 = "Hello, I'm Vitor Ramon!"
str2 = "Hello World!"

print(str1, str2)

print(type(str1))
print(type(str2))
print(f"The length of str1 is {len(str1)}")
print(f"The length of str2 is {len(str2)}")
print(str1[0])
print(str1[1])


new_str1 = str1.replace("o", "0")
print(new_str1)

new_str1 = str1.replace("o", "0", 1)
print(new_str1)

print(str1.split(","))

str3 = str1 + " " + str2
print(str3)

text = 'Movie "The Godfather" was released in 1972.'
text2 = "Movie 'The Godfather' was released in 1972."
text3 = "Movie \"The Godfather\" was released in 1972."
print(text)
print(text2)
print(text3)