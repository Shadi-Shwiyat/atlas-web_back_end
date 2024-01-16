# Basic authentication
In this project we learn authentication methods to provide security in the applications we build

## Learning Objectives
- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header

## Tasks
0. [Simple-basic-API](#task0)
1. [Error handler: Unauthorized](#task1)
2. [Error handler: Forbidden](#task2)
3. [Auth class](#task3)
4. [Define which routes don't need authentication](#task4)
5. [Request validation!](#task5)
6. [Basic auth](#task6)
7. [Basic - Base64 part](#task7)
8. [Basic - Base64 decode](#task8)
9. [Basic - User credentials](#task9)
10. [Basic - User object](#task10)
11. [Basic - Overload current_user - and BOOM!](#task11)

### <a name="task0"></a>0. Simple-basic-API
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

### <a name="task1"></a>1. Error handler: Unauthorized
Download and start your project from this archive.zip

In this archive, you will find a simple API with one model: User. Storage of these users is done via a serialization/deserialization in files.

<b>Setup and start server</b>

```
bob@dylan:~$ pip3 install -r requirements.txt
...
bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Serving Flask app "app" (lazy loading)
...
bob@dylan:~$
```

<b>Use the API (in another tab or in your browser)</b>

```
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status" -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/status HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.54.0
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 16
< Access-Control-Allow-Origin: *
< Server: Werkzeug/1.0.1 Python/3.7.5
< Date: Mon, 18 May 2020 20:29:21 GMT
< 
{"status":"OK"}
* Closing connection 0
bob@dylan:~$
```

