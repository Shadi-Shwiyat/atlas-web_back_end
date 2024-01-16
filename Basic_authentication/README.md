# Basic authentication
In this project we learn authentication methods to provide security in the applications we build

## Learning Objectives
- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header

## Tasks
0. [Regex-ing](#task0)
1. [Log formatter](#task1)
2. [Create logger](#task2)
3. [Connect to secure database](#task3)
4. [Read and filter data](#task4)
5. [Encrypting passwords](#task5)
6. [Check valid password](#task6)

### <a name="task0"></a>0. Regex-ing
Write a function called filter_datum that returns the log message obfuscated:

Arguments:
    - fields: a list of strings representing all fields to obfuscate
    - redaction: a string representing by what the field will be obfuscated
    - message: a string representing the log line
    - separator: a string representing by which character is separating all fields in the log line (message)
- The function should use a regex to replace occurrences of certain field values.
- filter_datum should be less than 5 lines long and use re.sub to perform the substitution with a single regex.

```
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""

filter_datum = __import__('filtered_logger').filter_datum

fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))

bob@dylan:~$
bob@dylan:~$ ./main.py
name=egg;email=eggmin@eggsample.com;password=xxx;date_of_birth=xxx;
name=bob;email=bob@dylan.com;password=xxx;date_of_birth=xxx;
bob@dylan:~$
```

### <a name="task1"></a>1. Log formatter
