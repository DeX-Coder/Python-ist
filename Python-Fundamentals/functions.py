
# def keyword stand for definition, used for creating custom functions in python
def hello_func(greeting, name='You'):
    return '{}, {} Function.'.format(greeting, name)

print(hello_func('Hi', name = 'Himangshu'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math','Art']
info = {'name':'John', 'age':22}
student_info(*courses, **info)