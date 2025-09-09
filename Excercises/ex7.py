"""
==================================================================
Python Loop & Logic Questions
==================================================================
"""

# 1. Write a program to print the first 10 even numbers
print("First 10 even numbers:")
for i in range(1,11):
    print(i * 2)
    
# 2. Write a program to print the first 10 odd numbers
print("First 10 odd numbers:")
for i in range(1, 11):
    print((i * 2) - 1)    
    
# 3. Write a program to print the first 10 even numbers in reverse order.
print("First 10 Even numbers in Reverse Order:")
for i in range(10, 0 , -1):
    print( i * 2)
    
# 4. Write a program to find the factorial of a number using a for loop.
num = int(input("Enter a number:"))
factorial = 1

for i in range(1, num + 1):
    factorial *=i
print("Factorial of", num, "is:", factorial)      

# 5. Write a program to check whether a number is prime or not.
num = int(input("enter a number:"))
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(num, "is a Prime Number")
else:
    print(num, "is NOT a Prime Number")            
    
# 6. Write a program to print numbers from 1 to 20 except multiples of 2 and 3.
print("Numbers from 1 to 20 except multiples of 2 and 3:")
for i in range(1,21):
    if i % 2 != 0 and i % 3 !=0:
        print(i, end=" ")

# 7. Write a program to accept 10 numbers from the user and display their average.
total = 0
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    total += num
    
average = total / 10
print("Average of 10 numbers is:", average)    

# 8. Write a program to accept 10 numbers from the user and display the largest and smallest numbers.
numbers = []
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)
    
print("Largest number is:", max(numbers))
print("Smallest number is:", min(numbers))    

# 9. Write a program to print only odd numbers from the given list using a for loop.
  # L = [23, 45, 32, 25, 46, 33, 71, 90] 
L = [23, 45, 32, 25, 46, 33, 71, 90] 
print("Odd numbers from the list:")
for num in L:
    if num % 2 != 0:
        print(num, end=" ")  
  
# 10. Reverse the word "develearn" and print it using a for loop.       
word = "develearn"
reversed_word =""
for ch in word:
    reversed_word = ch + reversed_word
print("Reversed word:", reversed_word)    

# 11. Count the number of vowels in the word "education"
word = "education"
vowels = "aeiou"
count = 0

for ch in word:
    if ch in vowels:
        count += 1

print("Number of vowels in 'education':", count)

# 12. Print all prime numbers up to a number (input from user).
num = int(input("Enter a number: "))

print("Prime numbers up to", num, ":")
for n in range(2, num + 1):
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=" ")

# 13. Print odd numbers from 1 to 10 using a while loop.
i = 1
print("Odd numbers from 1 to 10:")
while i <= 10:
    if i % 2 != 0:
        print(i, end=" ")
    i += 1

# 14. Find the factorial of a number using a while loop.
num = int(input("Enter a number: "))
factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print("Factorial of", num, "is:", factorial)

# 15. emails = {'aman@xmail.com','devesh@gmail.com','diya@ymail.com','jeba@zmail.com'}  
   #  Print only the domain names using set comprehension. 
emails = {'aman@xmail.com','devesh@gmail.com','diya@ymail.com','jeba@zmail.com'}

domains = {email.split('@')[1] for email in emails}
print("Domain names:", domains)
   
   
# 16. Write a program to print the following pattern.
# 55555
# 4444
# 333
# 22
# 1
for i in range(5, 0, -1):
    print(str(i) * i)


# 17. Predit the output:
x=5
while(x<15):
    print(x**2)
    x+=3    
    
# output: 25    64    121    196

# 18. Predict the output:
a=7
b=5
while(a<9):
    print(a+b)
    a+=1  
    
# Output: 12    13

# 19. Predict the output:
b=15
while(b>9):
    print("Hello")
    b=b-2    
    
# Output: Hello    Hello    Hello

# 20. Convert the following while loop into a for loop.
x=4
while(x<=8):
        print(x*10)
        x+=2

# output: 40    60     80

# Q21. Predict the output:
x=3
if x>2 or x<5 and x==6:
        print("Bye")
else:
        print("Thankyou")

# Output: Bye

# Q22. Predict the output:
x,y=2,4
if(x+y==10):
        print("Thankyou")
else:
        print("Bye")

# Output: Bye

# Q23. Trace the output:
x=10
y=1
while x>y:
    x=x-4
    y=y+3
    print(x)

# Output: 6     2

# Q24. Trace the output:
i=9
while True:
    if i%3==0:
        break
print("A")

# Output: A

# Q25. Trace the output:
n=20
for i in range(2, n//4):
    if n%i == 0:
        print("Python output based questions")
    else:
        print("Bye") 

# Output: Python output based questions        
        
              