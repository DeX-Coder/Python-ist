# Sets
cs_courses = {'History', 'Math', 'Physics','Computer Science'}
art_courses = {'History', 'Math', 'Art','Design'}

print(cs_courses) # Prints the set
print(len(cs_courses)) # Prints length of the set
print('Math' in cs_courses) # Prints boolean value if the value is present in set

# Sets methods
print(cs_courses.intersection(art_courses)) # Returns all the elements present in two or more sets

print(cs_courses.difference(art_courses)) # Returns the elements not present in two or more sets

print(cs_courses.union(art_courses)) # Returns all the elements present in all sets.

# How to create an empty set?
empty_set = {}
empty_set = set()