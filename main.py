"""
Exception: an error that occurs during program execution

Type of error:
    syntax error
    runtime error
    logical error
"""

# a = int(input("Enter a number "))
# b = int(input("Enter a number "))
# try:
#     result = a / b
# except ZeroDivisionError as e:
#     print(e)


"""
ZeroDivisionError:Raised when division or modulo(%) by zero occurs
ValueError: Raised when function receives an argument of right type but an inappropriate value
TypeError: Raised when an operation or function is applied to an object of inappropriate type
NameError: Raised when variable is not found
FileNotFoundError: Raised when a file or directory is requested but doesn't exist
IndexError:Raised when sequence index is out of range
KeyError: Raised when a dictionary key is not found
ImportError: Raised when an import statement fails to find the module


try -> risky code that might throw error
except -> error handling
finally -> always run
"""

try:
    a = int(input("Enter a number "))
    b = int(input("Enter a number "))
    result = a / b
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)

a = 10
b = "a"
try:
    sum = a + b
except TypeError:
    print("Cannot add int and str")

try:
    with open("text.txt", "r") as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)
except PermissionError as e:
    print(e)
finally:
    print("Finally block ")
