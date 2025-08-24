# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Q1. Take two variables of number and character and concatenate it.
# (Example: yourname + birthdate → “Shalini1997”)

name = "Sneha"
birthdate = 2004
result = name + str(birthdate)
print(result)


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Q2. Take three variables. Example: emailid.
# (Store username, domain, extension separately and print complete email ID)

username = "snehasahu"
domain = "gmail"
extension = ".com"
emailId = username + "@" + domain + extension
print(emailId)


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Q3. Take three variables and print your full name.

Firstname = "Sneha"
Middlename = "Chitrasen"
LastName = "Sahu"
Full_name = Firstname +" " + Middlename + " " + LastName
print("Full_name:", Full_name)
 
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Q4. Find out the percentage of the student using input from users.
# (5 subjects, total marks = 500)
 
sub1 = int(input("Enter marks for English:"))
sub2 = int(input("Enter marks for Maths :"))
sub3 = int(input("Enter marks for Hindi:"))
sub4 = int(input("Enter marks for Marathi:"))
sub5 = int(input("Enter marks for Science:"))
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total/500) * 100
print("total marks:", total)
print("Percentage:", percentage, "%")

#  --------------------------------------------------------------------------------------------------------------------------------------------------------
# Q5. Find out Area of Rectangle using user input.
# (length × breadth)

length = float(input("Enter the length of rectangle: "))
breadth = float(input("Enter the breadth of rectangle: "))
area = length * breadth
print("area of Rectangle:", area)


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Q6. Find out Area of Square using user input.
# (side × side)

side = float(input("Enter the side of the square: "))
area = side * side
print("Area of Square: ", area)


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Q7. Find out Area of Circle using user input.
# (π × radius × radius)

import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius * radius
print("Area of Circle: ", area)


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Q8. Find out Perimeter of Rectangle.
# (2 × length + 2 × breadth)"""
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
perimeter = 2 * length + 2* breadth
print("Perimeter of Rectangle:", perimeter)


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Q9. Find out Perimeter of Square.
# (4 × side)

side = float(input("Enter the side of square: "))
perimeter = 4 * side
print("Perimeter of square:", perimeter)


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Find out Circumference of Circle.
# (2 × π × radius)

import math 
radius = float(input("Enter radius of circle:"))
circumference = 2 * math.pi * radius
print("Circumference of a cicle:", circumference)


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Q11. Find out Volume of Cube.
# (side × side × side)

side = float(input("Enter side of cube: "))
volume = side ** 3
print("Volume of Cube:", volume)

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Q12. Find out Volume of Cuboid.
# (length × breadth × height)

length = float(input("Enter length of cuboid: "))
breadth = float(input("Enter breadth of cuboid: "))
height = float(input("Enter height of cuboid: "))
volume_cuboid = length * breadth * height
print("Volume of Cuboid: ", volume_cuboid)

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Q13. Find out Total Surface Area of Cube.
# (6 × side × side)

side = float(input("Enter side of cube: "))
cube = 6 * side * side
print("Total Surface Area of cube: ", cube)


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Q14. Find out Total Surface Area of Cuboid.
# (2(lb + bh + lh))

length = float(input("Enter length of cuboid: "))
breadth = float(input("Enter breadth of cuboid: "))
height = float(input("Enter height of cuboid: "))
total_surface_area = 2 * (length * breadth + breadth * height + length * height)
print("Total surface area of cuboid: ", total_surface_area)


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Q15. Take a number from the user and check whether it is even or odd.
 
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Q16. Take a number from the user and check whether it is positive, negative, or zero.

num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0: 
    print("Negative number")
else:
    print("Zero")
    
     
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Q17. Take marks of 3 subjects and find the average marks.

sub1 = float(input("Enter marks of English: "))
sub2 = float(input("Enter marks of Maths: "))
sub3 = float(input("Enter marks of Science: "))
average = (sub1 + sub2 + sub3) / 3
print("average Marks: ", average)


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Q18. Take temperature in Celsius from the user and convert it into Fahrenheit.
# (C×9/5)+32

celsius = float(input("enter temperature  in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit: ", fahrenheit)


# Q19. Take temperature in Fahrenheit from the user and convert it into Celsius.
# (F−32)×5/9 """
fahrenheit = float(input(" Enter temperature in fahrenheit:"))
celsius = (fahrenheit - 32) * 5/9
print("Temperature in celsius: ", celsius)


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Q20. Take principal, rate of interest, and time from the user and calculate Simple Interest.
# (P×R×T)/100

P = float(input("Enter Principal: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time in Years: "))
SI = (P * R * T) /100
print("Simple Interest:", SI)


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Q21. Take base and height from the user and find the area of a triangle.
# (1/2 × base × height)

base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
area = 0.5 * base * height
print("Area of Triangle:", area)


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Q22. Take two numbers and find the maximum and minimum using Python functions.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Maximum:", max(a , b))
print("Minimum:", min(a , b))


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Q23. Take a string from the user and find its length.

string = input("Enter a string: ")
print("Length of String: ",len(string))


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Q24. Take a string from the user and reverse it.

string = input("Enter a string: ")
print("Reversed string: ", string[::-1])


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Q25. Take a number from the user and print its square and cube.

num = float(input("Enter a number: "))
print("Square:", num ** 2)
print("Cube:", num ** 3)