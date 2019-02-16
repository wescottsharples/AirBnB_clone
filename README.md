# AirBnB_clone
## The console
### Project description
This project is the first part of the **AirBnB clone** project (our first full web application) for [Holberton School](https://www.holbertonschool.com/).
For this project we wrote a command interpreter to manage our AirBnB objects. This command interpreter will:
- create a new object (ex: a new User or new Place)
- retrieve an object from a file, a database, etc..
- update attributes of an object
- do operations on objects (count, compute stats, etc..)
- destroy an object

### Requirements
**Python Scripts**
- all files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- code will use `PEP 8` style (version 1.7 or higher)
- all modules will have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- all classes will have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- all functions will have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)

**Python Unit Tests**
- all test files are inside a folder `tests`
- all test files and folders start by `test_`
- file organization in the `tests` folder is same as project (for `models/base_model.py` unit tests must be in `tests/test_models/test_base_model.py`)
- all tests will be executed by this command: `python3 -m unittest discover tests`
- all modules will have documentation
- all classes will have documentation
- all functions will have documentation

### Execution
The command interpreter should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$ 
```
It should also work in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$ 
$ cat test_help
help
$ 
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$ 
```

### Authors
[Athena Deng](https://github.com/ad-egg)

[Wescott Sharples](https://github.com/wescottsharples)
