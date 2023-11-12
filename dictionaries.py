# Dictionaries
student = {'name':'John', 'age':25, 'courses':['Math', 'Computer Science']}

print(student)
print(student['name'])
print(student['age'])
print(student['courses'])

# Adding a new key/value:
student['phone'] = "555-5555"
student['name'] = 'Jane'
print(student)

# Updating dict data in bulk:
student.update({'name':'Jane','age':25,'phone':'555-5655', 'address': '850A, Mount View, California'})
print(student)

# ::Methods::
print(student.get('name'))
print(student.get('phone', 'Not Found'))

# Deleting student data
# way 1
del student['age']
# print(student)

# Way 2
address = student.pop('address')
print(student)
print(address)


# Getting dict keys:
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)

# How to create empty dict?
empty_dict = dict()