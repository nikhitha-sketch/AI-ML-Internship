#Variables and Data Types
name="abc"
age=25
cgpa=9.3
is_student=True
print("Name:",name)
print("Age:",age)
print("CGPA:",cgpa)
print("Is Student:",is_student)
#Arithmetic Operations
a=15
b=5
print("\nArithmetic Operations:")
print("Addition:",a+b)
print("Subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("Modulus:",a%b)
#Conditional Statements
number=10
if number%2==0:
    print(number,"is even")
else:
    print(number,"is odd")
#For Loop
for i in range(1,6):
    print(i)
#While Loop
count=1
while count<=5:
    print(count)
    count+=1
#Function
def square(number):
    return number*number
print("Square of 5 is:",square(5))