# Python - Variable Annotations
The goal of this project is to get familiar with typings in python and learn basic annotations

## Learning Objectives
- Type annotations in Python 3
- How you can use type annotations to specify function signatures and variable types
- Duck typing
- How to validate your code with mypy

## Tasks
0. [Basic annotations - add](#task0)
1. [Basic annotations - concat](#task1)
2. [2. Basic annotations - floor](#task2)
3. [Basic annotations - to string](#task3)
4. [Define variables](#task4)
5. [Complex types - list of floats](#task5)
6. [Complex types - mixed list](#task6)
7. [Complex types - string and int/float to tuple](#task7)
8. [Complex types - functions](#task8)
9. [Let's duck type an iterable object](#task9)

### <a name="task0"></a>0. Basic annotations - add
Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float.

```
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)

bob@dylan:~$ ./0-main.py
True
{'a':  <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
```