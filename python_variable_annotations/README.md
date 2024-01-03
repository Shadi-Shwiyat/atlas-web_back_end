# Python - Variable Annotations
The goal of this project is to get familiar with typings in python

## Learning Objectives
- Type annotations in Python 3
- How you can use type annotations to specify function signatures and variable types
- Duck typing
- How to validate your code with mypy

## Tasks
0. [Basic annotations - add](#task0)
1. [Basic annotations - add](#task1)
2. [Basic annotations - add](#task2)
3. [Basic annotations - add](#task3)
4. [Basic annotations - add](#task4)
5. [Basic annotations - add](#task5)
6. [Basic annotations - add](#task6)
7. [Basic annotations - add](#task7)
8. [Basic annotations - add](#task8)
9. [Basic annotations - add](#task9)

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