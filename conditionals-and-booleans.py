
# Comparisons:
# Equal:                ==
# Not Equal:            !=
# Greater Than:         >
# Less Than:            <
# Greater or Equal:     >=
# Less or Equal:        <= 
# Object identity:      is

# language = 'JavaScript'

# if language == 'Python':
#     print('Language is Python')

# elif language == 'Java':
#     print('Language is Java')

# elif language == 'JavaScript':
#     print('Language is JavaScript')

# else:
#     print('No Match!')

# Just Another way of doing if else: (Available in Python version 3.10 and Onwards!)

# print()
# print('Doing using match case statement')
# print()
# match language:
#     case 'Python':
#         print('Language is Python')
#     case 'Java':
#         print('Language is Java')
#     case 'JavaScript':
#         print('Language is JavaScript')
#     case _:
#         print('No match')

# If one's got their hands dirty with C or C++, then you're tired of adding break statement in
# the end of every case statement's block. In Python, you don't have to do that. 
# Sit back! Relax! Chill! 
# Happy Coding


# and -- both the statements have to be true
# or -- either of the statements have to be true
# not 

# user = 'Admin'
# logged_in = False

# if user == 'Admin' and logged_in:
    # print('Admin Page')
# if user == 'Admin' or logged_in:
    # print('Admin Page')
# if not logged_in:
    # print('Please Log In!')
    
# else:
    # print('Welcome!')
# ==============================================================================

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition = "Test"

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')



# a = [1,2,3]
# # b = [1,2,3]
# b = a

# print(id(a))
# print(id(b))
# print(a is b)
# print(id(a) == id(b))