# 0x10. Python - Network #0

## Bash

## Python

## Back-end

## API

## Requirements

## General

- Allowed editors: vi, vim, emacs
- A README.md file, at the root of the folder of the project, is mandatory
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your Bash scripts should be exactly 3 lines long (wc -l file should print 3)
- All your files should end with a new line
- All your files must be executable
- The first line of all your bash files should be exactly #!/bin/bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing
- All curl commands must have the option -s (silent mode)
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- The first line of all your Python files should be exactly #!/usr/bin/python3
- Your code should use the pycodestyle (version 2.8.*)
- All your modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
- All your classes should be documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
- All your functions (inside and outside a class) should be documented: python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
- A documentation is not a simple word, its a real sentence explaining whats the purpose of the module, class or method (the length of it will be verified)

## TASKS

## 0. cURL body size
mandatory
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

The size must be displayed in bytes
You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000

## 1. cURL to the end
mandatory
Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response

Display only body of a 200 status code response
You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000

## 2. cURL Method
mandatory
Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000

## 3. cURL only methods
mandatory
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000

## 4. cURL headers
mandatory
Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response

A header variable X-School-User-Id must be sent with the value 98
You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000

## 5. cURL POST parameters
mandatory
Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response

A variable email must be sent with the value test@gmail.com
A variable subject must be sent with the value I will always be here for PLD
You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000

## 6. Find a peak
mandatory
Technical interview preparation:

You are not allowed to google anything
Whiteboard first
Write a function that finds a peak in a list of unsorted integers.

Prototype: def find_peak(list_of_integers):
You are not allowed to import any module
Your algorithm must have the lowest complexity (hint: you dont need to go through all numbers to find a peak)
6-peak.py must contain the function
6-peak.txt must contain the complexity of your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2)
Note: there may be more than one peak in the list

## 7. Only status code
#advanced
Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.

You are not allowed to use any pipe, redirection, etc.
You are not allowed to use ; and &&
You have to use curl
Please test your script in the sandbox provided, using the web server running on port 5000

## 8. cURL a JSON file
#advanced
Write a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.

Your script must send a POST request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request
You have to use curl
Please test your scripts in the sandbox provided, using the web server running on port 5000

## 9. Catch me if you can!
#advanced
Write a Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.

You have to use curl
You are not allow to use echo, cat, etc. to display the final result
Please test your script in the sandbox provided, using the web server running on port 5000

## HTTP (HyperText Transfer Protocol)

## The WEB

- Internet (or The Web) is a massive distributed client/server information system as depicted in the following diagram.

![SERVER](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/images/TheWeb.png)

## HyperText Transfer Protocol (HTTP)

- HTTP is an asymmetric request-response client-server protocol as illustrated.  An HTTP client sends a request message to an HTTP server.  The server, in turn, returns a response message.  In other words, HTTP is a pull protocol, the client pulls information from the server (instead of server pushes information down to the client).

![SERVER](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/images/HTTP.png)

Happy Coding


