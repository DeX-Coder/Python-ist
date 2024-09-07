"""
Constructors are special methods used to initialize objects of a class.
There are different types of constructors. 
Constructor is invoked automatically when an object of a class is created.

A constructor is a unique function that gets called automatically when an object is created of a class.

The main purpose of a constructor is to initialise or assign values to the data members of that class.
It cannot return any value other than `None`.


They are denoted by the special method name __init__
They take the parameter 'self' which is a reference to the object being created.
They do not have a return type and their purpose is to initialize the object.

There are two types of Constructors:
1. Parameterised constructors (When a constructor accepts other arguments along with `self`)
sample code:
```
class Student:
    def init(self, name, roll):
        self.name = name
        self.rollno = roll
st1 = Student("Himangshu", 101)
print(st1.name, st1.rollno)
```

2. Default constructors (When a constructor does not accept any arguments other than `self`)
sample code:
```
class XYZ:
    def init(self):
        print("Hello World!")

obj = XYZ()
```

"""


class Person:
    def __init__(self, name, occ):
        print("Hey I am a person")
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person("Harry", "Developer")
b = Person("Divya", "HR")
a.info()
b.info()
# print(a.name)
