"""
Python decorators:
Python decorators are a powerful and versatile tool that allow you to modify the behavior of function and
methods. They are a way to extend the functionality of a function or method without modifying its source
code.

A decorator is a function that takes another function as an argument and returns a new function that 
modifies the behavior of the original function. The new function is often referred to as a "decorated"
function. The basic syntax for using decorators is the following:
```
@decorator_function
def my_function():
    pass
```
the `@decorator_function` notation is just the shorthand for the following code:
```
def my_function():
    pass
my_function = decorator_function(my_function)
```
Decorators are often used to add functionality to functions or methods, such as logging, memoization,
and access control.
"""


def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")

    return mfx


@greet
def hello():
    print("hello world")


@greet
def add(a, b):
    print(a + b)


# greet(hello)()
hello()
# greet(add)(1, 3)
add(1, 3)
