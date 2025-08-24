# Basic if and if-else
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 1. Check whether a number is divisible by 7.

num = int(input("Enter a number:"))
if num % 7 == 0:
    print(num, "is divisible by 7")
else:
    print(num, "is not divisible by 7")
    
# --------------------------------------------------------------------------------------------------------------------------------------------------------    
# 2. Check whether a given number is even or odd.

num = int(input("Enter a number"))
if num % 2 == 0:
    print(num, "is even number")
else:
    print(num, "is odd number")  

# --------------------------------------------------------------------------------------------------------------------------------------------------------    
# 3. Check whether a given number is positive, negative, or zero.

num = int(input("Enter a number: "))

if num > 0:
    print(num, "is positive")
else:
    if num < 0:
        print(num, "is negative")
    else:
        print(num, "is zero")


# --------------------------------------------------------------------------------------------------------------------------------------------------------    
# 4. Check whether the character 'a' is present in the string "Python" or not.    

s = "Python"
if 'a' in s:
    print("'a' is present in the string")
else:
    print("'a' is not present in the string")

# --------------------------------------------------------------------------------------------------------------------------------------------------------    
# 5. Accept three numbers and find the largest number among them.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b:
    if a >= c:
        print("Largest number is:", a)
    else:
        print("Largest number is:", c)
else:
    if b >= c:
        print("Largest number is:", b)
    else:
        print("Largest number is:", c)
  

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 6. Check whether a given year is a leap year or not.

year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 7. Accept total working days and present days, calculate attendance percentage and check eligibility for exams (>=75%).
total_days = int(input("Enter total working days: "))
present_days = int(input("Enter number of days present: "))
attendance = (present_days / total_days) * 100
print("Attendance Percentage:", attendance, "%")
if attendance >= 75:
    print("Eligible for Exams")
else:
    print("Not Eligible for Exams")

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 8. Check whether the entered character is a vowel or not.
char = input("Enter a Character: ")
char = char.lower()
if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print("It is a vowel")
else:
    print("It is not a vowel")

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 9. Accept a number from 1 to 7 and print the day of the week (1=Sunday, 2=Monday, …).
num = int(input("Enter a nummber (1-7): "))

if num == 1:
    print("Sunday")
else:
    if num == 2:
        print("Monday")
    else:
        if num == 3:
            print("Tuesday")
        else:
            if num == 4:
                print("Wednesday")
            else:
                if num == 5:
                    print("Thursday")
                else:
                    if num == 6:
                        print("Friday")
                    else:
                        if num == 7:
                            print("Saturday")
                        else:
                            print("Invalid input! Please enter 1–7 only.")

    
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 10. Accept a city name and display its monument.
# Delhi → Red Fort
# Agra → Taj Mahal
# Jaipur → Jal Mahal

city = input("Enter city name: ")
if city == "Delhi":
    print("Monument: Red Fort")
else: 
    if city == "Agra":
        print("Monument: Taj Mahal")
    else:
        if city == "Jaiput":
            print("Monuemnt: Jal Mahal")
        else:
            print("Monument not found")
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Nested If-Else & Elif


# 11. Check whether a person is eligible to vote (age >=18).
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")  

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 12. Make a simple calculator (add, subtract, multiply, divide) using if-elif.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == '+':
    print("Result:", a+b)
elif op == '-':
    print("Result:" , a-b)
elif op == '*':
    print("Result:" , a*b)
elif op == "/":
    print("Result:" , a/b)
else:
    print("Invalid operation")
     
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 13. Check whether a figure is square or not by comparing length and breadth.
length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
if length == breadth:
    print("It is a Square")
else:
    print("It is a Rectangle")
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 14.Accept percentage from user and display grade:
# Below 25 → D
# 25–45 → C
# 45–50 → B
# 50–60 → B+
# 60–80 → A
# Above 80 → A+

percent = int(input("Enter percentage: "))
if percent < 25:
    print("Grade: D")
elif percent < 45:
    print("Grade: C")
elif percent < 50:
    print("Grade: B")
elif percent < 60:
    print("Grade: B+")
elif percent < 80:
    print("Grade: A")
else:
    print("Grade: A+")  

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 15. Accept three sides of a triangle and check whether it is equilateral, isosceles, or scalene.
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 16. Accept three sides of a triangle and check whether the triangle is valid (sum of any two sides > third side).
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
else:
    print("Not a Valid Triangle")

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 17. Check whether a key exists in a dictionary or not.
d = {"name": "Sneha", "age": 21, "city": "Mumbai"}
key = input("Enter key to check: ")

if key in d:
    print("Key exists in dictionary")
else:
    print("Key does not exist")

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 18. Check whether a number is a three-digit number or not.
num = int(input("Enter a number: "))
if num >= 100 and num <= 999:
    print("It is a three-digit number")
else:
    print("It is not a three-digit number")

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 19. Accept electricity units and calculate bill:
# First 100 units → Free
# Next 200 units → Rs 2/unit
# Above 300 units → Rs 5/unit

units = int(input("Enter electricity units: "))
if units <= 100:
    bill = 0
elif units <= 300:
    bill = (units - 100) * 2
else:
    bill = (200 * 2) + (units - 300) * 5
print("Electricity Bill = Rs", bill)

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Logical & Nested Structures 

# 20. Accept age, sex (M/F), number of working days, and
# calculate wages/day as per rules:
# Age 18–30: M → 700/day, F → 750/day 
# Age 30–40: M → 800/day, F → 850/day 
# Otherwise → Print “Enter appropriate age”

age = int(input("Enter age: "))
sex = input("Enter sex (M/F): ").upper()
days = int(input("Enter number of working days: "))

if 18 <= age <= 30:
    if sex == "M":
        wage = 700
    else:
        wage = 750
elif 30 < age <= 40:
    if sex == "M":
        wage = 800
    else:
        wage = 850
else:
    print("Enter appropriate age")
    wage = 0

if wage > 0:
    print("Total wages =", wage * days)

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 21. Accept three numbers and display the second largest number.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a > b and a < c) or (a > c and a < b):
    second = a
elif (b > a and b < c) or (b > c and b < a):
    second = b
else:
    second = c

print("Second largest number is:", second)

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 22. Accept number of days late for library book submission and calculate fine:
# Up to 5 days → Rs 2/day
# 6–10 days → Rs 3/day
# 11–15 days → Rs 4/day
# More than 15 days → Rs 5/day

days = int(input("Enter number of late days: "))

if days <= 5:
    fine = days * 2
elif days <= 10:
    fine = (5 * 2) + (days - 5) * 3
elif days <= 15:
    fine = (5 * 2) + (5 * 3) + (days - 10) * 4
else:
    fine = (5 * 2) + (5 * 3) + (5 * 4) + (days - 15) * 5

print("Library Fine = Rs", fine)

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 23. Accept a number and check whether it is a prime number.
num = int(input("Enter a number: "))

if num > 1:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is a Prime number")
    else:
        print(num, "is NOT a Prime number")
else:
    print("Not a Prime number")

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 24. Accept a number and check whether it is a palindrome number (same when reversed).
num = int(input("Enter a number: "))
rev = int(str(num)[::-1])

if num == rev:
    print(num, "is a Palindrome number")
else:
    print(num, "is NOT a Palindrome number")

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 25. Accept a string and check whether it is an anagram of another string (e.g., "care" → "race").
str1 = input("Enter first string: ").lower()
str2 = input("Enter second string: ").lower()

if sorted(str1) == sorted(str2):
    print("The strings are Anagrams")
else:
    print("The strings are NOT Anagrams")
    
   

