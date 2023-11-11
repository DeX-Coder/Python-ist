
courses = ['History', 'Math', 'Physics', 'Computer Science'] # This is a list

# print(courses) # Printing whole list
# print(len(courses)) # Printing length of list
# print(courses[2]) # Accessing particular item in list
# print(courses[0:2]) #Printing range of values
# print(courses[2:]) #Printing range of values

# Methods:
# courses.append('Art') # Adds item in the end of the list
# print(courses)

# courses.insert(0, "Art") # Adds item at the specified index in the list
# print(courses)

# courses_2 = ['Art', 'Education']
# courses.extend(courses_2) # Adds item from an iterable in the end of the list
# print(courses)

# courses.remove("Math") # Removes the first occurance of the specified item, returns error if not found
# print(courses)

# popped = courses.pop() 
# Removes the item present at the last index in the list by default, index can be specified otherwise.
# Also the item so removed is returned.
# print(popped)
# print(courses)

# courses.reverse() # Reverses the order of elements in the list.
# print(courses)


# nums = [1,5,3,4,2]

# print("Before Sort")
# print(courses)
# print(nums)

# courses.sort()
# courses.sort(reverse=True) 
# nums.sort()
# nums.sort(reverse=True)

# Sorts the items in the list alphabetically. 
# We can specify whether to sort it in ascending or descending order or reverse alphabetical order.

# print("After Sort")
# print(courses)
# print(nums)


# nums = [1,5,3,4,2]

# sorted_courses = sorted(courses)
# Return a new list containing all items from the iterable in ascending order.
# print(sorted_courses)

# print(max(nums))
# print(min(nums))
# print(sum(nums))


# print(courses.index('Computer Science')) # Returns the index value of specified item.
# print('Math' in courses)


course_str = ' - '.join(courses)
print(course_str)

new_list = course_str.split(' - ')
print(new_list)
