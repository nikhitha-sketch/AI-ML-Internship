# AI & ML Internship - Day 2
# Topic : Python Basics
# Description : Demonstration of Python fundamentals
# Variables and Data Types
student_name = "John Doe"
student_age = 19
cgpa = 9.20
is_intern = True

print("=" * 50)
print("        PYTHON BASICS DEMONSTRATION")
print("=" * 50)

print("\nStudent Information")
print(f"Name       : {student_name}")
print(f"Age        : {student_age}")
print(f"CGPA       : {cgpa}")
print(f"Intern     : {is_intern}")

# Arithmetic Operators
num1 = 20
num2 = 6

print("\nArithmetic Operations")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} % {num2} = {num1 % num2}")

# Functions
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"

def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

# Conditional Statement
number = 7

print("\nConditional Statement")
print(f"{number} is {check_even_odd(number)}")

# For Loop
print("\nFor Loop (Numbers 1 to 5)")
for i in range(1, 6):
    print(i, end=" ")

# While Loop
print("\n\nWhile Loop (Countdown)")
count = 5
while count > 0:
    print(count, end=" ")
    count -= 1

# Simple Python Programs
print("\n\nSimple Programs")
print(f"Factorial of 5 : {factorial(5)}")

print("\nSquares of numbers from 1 to 5")
for i in range(1, 6):
    print(f"{i} -> {i ** 2}")

print("\n" + "=" * 50)
print("Python Basics Completed Successfully")
print("=" * 50)