# ------------------------------------------------------------- Functions (Part 2) -----------------------------------------------------------------

# 1. Write a function to check if a number is Armstrong or not.
def is_armstrong(number):
    power = len(str(number))
    return number == sum(int(digit) ** power for digit in str(number))
print(is_armstrong(153))

# 2. Create a function to calculate factorial of a number using recursion.
def factorial(n):
    if n ==0 or n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))

# 3. Write a function that accepts a string and returns it in reverse order.
def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))

# 4. Define a function to check if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print(is_prime(17))
    
# 5. Write a function that counts how many vowels are in a string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
print(count_vowels("Hello World"))

# 6. Define a function to calculate compound interest.
def compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time)
print(compound_interest(1000, 5, 2)) 

# 7. Write a funtcion that check if a string is a palindrome.
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("madam"))

# 8. Define a function to calculate the greatest common divisor (GCD).
def gcd(a,b):
    while b:
        a, b = b, a % b
    return a
print(gcd(54, 24))

# 9. Write a function that returns Fibonacci series up to n terms.
def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series
print(fibonacci_series(7))
    
# 10. Define a function to check whether a year is leap year or not.
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(is_leap_year(2024))
    
# 11. Write a function that finds the maximum of three numbers.
def max_of_three(a, b, c):
    return max(a,b,c)
print(max_of_three(10, 20, 15))

# 12. Define a function that removes all punction from a string.
import string

def remove_punctuation(s):
    return ''.join(char for char in s if char not in string.punctuation)

print(remove_punctuation("Hello, World!"))  # "Hello World"

# 13.  Write a function to return the largest word in a sentence.
def largest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print(largest_word("Python is awesome"))  # "awesome"

# 14. Define a recursive function to find the sum of digits of a number.
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(1234))  # 10

# 15. Write a function that accepts a list and returns a new list with only even numbers.
def filter_even(numbers):
    return [num for num in numbers if num % 2 == 0]

print(filter_even([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]

# 16. Define a function to count the frequency of each word in a sentence.
def word_frequency(sentence):
    words = sentence.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

print(word_frequency("Python is fun and Python is powerful"))

# 17. Write a function that checks if two strings are anagrams.
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

print(is_anagram("listen", "silent"))  # True

# 18. Create a function to calculate the area of a circle.
import math

def area_of_circle(radius):
    return math.pi * radius ** 2

print(area_of_circle(5))  # 78.5398...

# 19. Write a function that returns the nth Fibonacci number.
def nth_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

print(nth_fibonacci(7))  # 13

# 20. Define a function that converts decimal number into binary.
def decimal_to_binary(n):
    return bin(n)[2:]

print(decimal_to_binary(10))  # '1010'

# 21. Write a function to find the smallest element in a list without using min().
def smallest_element(lst):
    smallest = lst[0]
    for num in lst[1:]:
        if num < smallest:
            smallest = num
    return smallest

print(smallest_element([3, 1, 4, 0, -5]))  # -5

# 22. Define a function to remove duplicate characters from a string.
def remove_duplicates(s):
    result = ''
    for char in s:
        if char not in result:
            result += char
    return result

print(remove_duplicates("aabbccddeeff"))  # 'abcdef'

# 23. Write a recursive function to calculate power (x^n).
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

print(power(2, 3))  # 8

# 24. Define a function to find the sum of elements in a list.
def sum_of_list(lst):
    return sum(lst)

print(sum_of_list([1, 2, 3, 4]))  # 10

# 25. Write a function to generate a random OTP of 6 digits.
import random

def generate_otp():
    otp = ''.join(str(random.randint(0, 9)) for _ in range(6))
    print("Your OTP is:", otp)
    return otp

generate_otp()

