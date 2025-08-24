# More on If-Else, Elif, Nested Conditions
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 1. Accept marks of 5 subjects and calculate total, percentage, and display division (First, Second, Third, Fail).

marks = []
for i in range(5):
    marks.append(int(input(f"Enter marks of subject {i+1}: ")))

total = sum(marks)
percentage = total / 5

print("Total =", total)
print("Percentage =", percentage, "%")

if percentage >= 60:
    print("Division: First")
elif percentage >= 45:
    print("Division: Second")
elif percentage >= 33:
    print("Division: Third")
else:
    print("Fail")

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 2. Accept temperature and display whether it is Hot, Moderate, or Cold.
temp = int(input("Enter temperature: "))

if temp > 30:
    print("Hot")
elif temp >= 15:
    print("Moderate")
else:
    print("Cold")

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 3. Accept a number and check whether it is Armstrong number or not (e.g., 153 = 1³+5³+3³).
num = int(input("Enter number: "))
power = len(str(num))
sum_val = sum(int(d)**power for d in str(num))

if num == sum_val:
    print(num, "is Armstrong")
else:
    print(num, "is not Armstrong")

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 4. Accept a number and check whether it is a perfect number (sum of divisors = number).
num = int(input("Enter number: "))
sum_div = sum(i for i in range(1, num) if num % i == 0)

if num == sum_div:
    print(num, "is a Perfect number")
else:
    print(num, "is not Perfect")

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 5. Accept a character and check whether it is uppercase, lowercase, digit, or special symbol.
ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase Letter")
elif ch.islower():
    print("Lowercase Letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Symbol")

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 6. Accept a string and check whether it is a palindrome string.
s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome String")
else:
    print("Not Palindrome")

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 7. Accept age and check the ticket price:
# Age < 5 → Free
# Age 5–12 → Rs 100
# Age 13–59 → Rs 200
# Age >=60 → Rs 150

age = int(input("Enter age: "))

if age < 5:
    print("Free Ticket")
elif age <= 12:
    print("Ticket Price = 100")
elif age <= 59:
    print("Ticket Price = 200")
else:
    print("Ticket Price = 150")

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 8. Accept income from user and calculate tax as per given slabs:
# Income ≤ 2,50,000 → No Tax
# 2,50,001–5,00,000 → 5%
# 5,00,001–10,00,000 → 20%
# Above 10,00,000 → 30%

income = int(input("Enter income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income-250000)*0.05
elif income <= 1000000:
    tax = 250000*0.05 + (income-500000)*0.2
else:
    tax = 250000*0.05 + 500000*0.2 + (income-1000000)*0.3

print("Tax =", tax)

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 9. Accept a number and check whether it is a Harshad number (divisible by sum of its digits).
num = int(input("Enter number: "))
digit_sum = sum(int(d) for d in str(num))

if num % digit_sum == 0:
    print("Harshad Number")
else:
    print("Not Harshad")

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 10. Accept 3 numbers and check whether they can form a Pythagorean triplet (a²+b²=c²).
a, b, c = map(int, input("Enter 3 numbers: ").split())
nums = sorted([a, b, c])

if nums[0]**2 + nums[1]**2 == nums[2]**2:
    print("Pythagorean Triplet")
else:
    print("Not a Triplet")

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Pass, Break, Continue (inside if-else & loops)

# 11. Print numbers from 1 to 10 but skip number 5 using continue.
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 12. Print numbers from 1 to 10 but stop when number 7 comes using break.
for i in range(1,11):
    if i == 7:
        break
    print(i)

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 13. Use a loop with pass inside if condition to demonstrate null statement.
for i in range(5):
    if i == 2:
        pass  
    print(i)

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 14. Accept a number and print whether it is prime or not, but break the loop if a factor is found.
num = int(input("Enter number: "))
for i in range(2, num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 15. Accept 10 numbers from user and print only the positive numbers (skip negatives using continue).
for i in range(10):
    n = int(input("enter number: "))
    if n < 0:
        continue
    print("Positive:", n)
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Nested If with Logic

# 16. Accept a number and check whether it is divisible by both 5 and 11.
num = int(input("Enter number: "))
if num % 5 == 0 and num % 11 == 0:
    print("Divisible by 5 and 11")
else:
    print("Not Divisible")

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 17. Accept a string and check whether it contains both alphabets and digits.
s = input("Enter string: ")

if any(ch.isalpha() for ch in s) and any(ch.isdigit() for ch in s):
    print("Contains both Alphabets & Digits")
else:
    print("Does not contain both")

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 18. Accept a number and check whether it is both a prime number and odd.
num = int(input("Enter number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        if num % 2 != 0:
            print("Odd Prime")
        else:
            print("Even Prime")
else:
    print("Not Prime")

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 19. Accept a year and check whether it is a century year (e.g., 1900, 2000).
year = int(input("Enter year: "))

if year % 100 == 0:
    print("Century Year")
else:
    print("Not Century")

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 20. Accept two numbers and check whether the first is a multiple of the second.
a, b = map(int, input("Enter two numbers: ").split())
if a % b == 0:
    print(a, "is multiple of", b)
else:
    print(a, "is not multiple of", b)

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Real-World Applications

# 21. ATM Program: Accept withdrawal amount and check conditions:
# Amount multiple of 100
# Minimum balance of 500 must remain
# Deduct and display remaining balance.

balance = 10000
amount = int(input("Enter withdrawal amount: "))

if amount % 100 == 0:
    if balance - amount >= 500:
        balance -= amount
        print("Withdrawal successful! Remaining balance =", balance)
    else:
        print("Insufficient balance (min 500 required)")
else:
    print("Amount must be multiple of 100")

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 22. Railway Ticket Discount: Accept age and class type (AC/General) → Provide discount:
# Child (<12) → 50% off
# Senior citizen (>=60) → 40% off
# Otherwise → No discount

age = int(input("Enter age: "))
cls = input("Enter class (AC/General): ")

fare = 1000 if cls == "AC" else 500

if age < 12:
    discount = 0.5 * fare
elif age >= 60:
    discount = 0.4 * fare
else:
    discount = 0

print("Final Ticket Price =", fare - discount)

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 23. Cinema Hall Program: Accept movie type (Normal/3D/IMAX) and age → Show ticket price accordingly.
movie = input("Enter movie type (Normal/3D/IMAX): ")
age = int(input("Enter age: "))

if movie == "Normal":
    price = 150
elif movie == "3D":
    price = 250
else:
    price = 350

if age < 12:
    price -= 50

print("Ticket Price =", price)

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 24. Online Shopping: Accept purchase amount →
# = 5000 → 20% discount
# = 2000 → 10% discount
# Otherwise → No discount

amt = int(input("Enter purchase amount: "))

if amt >= 5000:
    discount = 0.2 * amt
elif amt >= 2000:
    discount = 0.1 * amt
else:
    discount = 0

print("Final Amount =", amt - discount)

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 25. Grading with Remark: Accept marks and display grade + remark (e.g., A → Excellent, B → Good, etc.).
marks = int(input("Enter marks: "))

if marks >= 90:
    grade, remark = "A", "Excellent"
elif marks >= 75:
    grade, remark = "B", "Good"
elif marks >= 50:
    grade, remark = "C", "Average"
elif marks >= 33:
    grade, remark = "D", "Pass"
else:
    grade, remark = "F", "Fail"

print("Grade:", grade, "| Remark:", remark)

# --------------------------------------------------------------------------------------------------------------------------------------------------------