message = 'Hello World'

print(len(message)) # len() returns the length of a string. Count starts from 1.

print(message[10]) # accessing elements in strings!

print(message[0:5]) # acessing a part of the string!

print(message[:5]) # the same thing would return like one in line 7

print(message[6:]) 

# ======================= METHODS ==========================

print(message.lower())
# where .lower() is a string method, returns the string in lower case format.

print(message.count('l'))
# .count() takes a string character or a string, returns the number of times it is present in a string.

print(message.find('Universe'))
# .find() takes a character or string phrase, it returns the starting index of the string or a character specified, returns -1 if not found.

# message = message.replace('World', 'Universe')
print(message)


# ========================== CONCATENATION ============================

greeting = 'Hello'
name = "Bill"

message = greeting + ", " + name + '. Welcome!' # Concatenation using + sign "Old Zindagi"
print(message)

"NOTE" """The below code will work on previous python versions"""
message = "{}, {}. Welcome!".format(greeting, name) # Concatenation using .format() method "Mentos Zindagi"
print(message)

"NOTE" """The below code will work on python version above 3.6.*"""
message = f"{greeting}, {name.upper()}. Welcome!"# Concatenation using f-string formatting method "Ultra Mentos Zindagi"

print(message)

print(dir(name)) # List outs all the possible attributes for the given string.