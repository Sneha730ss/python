# ------------------------------------------------ Functions (Part 1) -----------------------------------------------------------------

# 1. Write a program to find the longest word in a given sentence using built-in functions.
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)
sentence = "This is a simple example sentence"
print("Longest word:", longest_word(sentence))

# 2. Find the maximum occuring element in a list using Python's built-in functions.
def max_occurrence(lst):
    return max(set(lst), key=lst.count)
lst = [1, 2, 2, 3, 4, 2, 5]
print("Maximum occuring element:", max_occurrence(lst))

# 3. Use map() to convert a list of temperatures from Celsius to Fahrenheit.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
temperatures_celsius = [0, 10, 20, 30, 40]
temperatures_fahrenheit = list(map(celsius_to_fahrenheit, temperatures_celsius))
print("Temperatures in Fahrenheit:", temperatures_fahrenheit)

# 4. Count how many unique vowels are present in a given string using set() and len().
def unique_vowels(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return len(set([char for char in string.lower() if char in vowels]))
input_string = "Hello, how are you?"
print("Unique vowels count:", unique_vowels(input_string))

# 5. Write a program to convert a dictionary into a list of tuples and back to a dictionary.
def dict_to_list_and_back(d):
    list_of_tuples = list(d.items())
    dict_from_list = dict(list_of_tuples)
    return list_of_tuples, dict_from_list

sample_dict = {'a': 1, 'b': 2, 'c': 3}
list_tuples, dict_back = dict_to_list_and_back(sample_dict)
print("List of tuples:", list_tuples)
print("Dict from list:", dict_back)

# 6. Sort a list of tuples by the second value using sorted().
tuples = [(1, 2), (3, 1), (5, 0), (2, 4)]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print("Sorted tuples by second value:", sorted_tuples)

# 7. Merge two lists into a dictionary using zip().
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
merged_dict = dict(zip(list1, list2))
print("Merged dictionary:", merged_dict)

# 8. Find the second largest number in a list using built-in functions.
def second_largest(lst):
    lst = list(set(lst))  # Remove duplicates
    lst.sort()
    return lst[-2] if len(lst) > 1 else None

numbers = [10, 20, 4, 45, 99, 99]
print("Second largest number:", second_largest(numbers))

# 9. Use filter() to get all prime numbers from a given list.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primes = list(filter(is_prime, numbers))
print("Prime numbers:", primes)

# 10. Write a program to remove all duplicates from a list using set().
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print("List with duplicates removed:", unique_numbers)

# 11. Use enumerate() to display index and value of each character in a string.
string = "Hello"
for index, char in enumerate(string):
    print(f"Index: {index}, Character: {char}")

# 12. Find the average salary from a list of employee salaries using sum() and len().
salaries = [30000, 50000, 70000, 60000, 55000]
average_salary = sum(salaries) / len(salaries)
print("Average salary:", average_salary)

# 13. Sort dictionary items by values in descending order using sorted().
sample_dict = {'a': 1, 'b': 4, 'c': 2, 'd': 3}
sorted_dict = dict(sorted(sample_dict.items(), key=lambda x: x[1], reverse=True))
print("Sorted dictionary by values (descending):", sorted_dict)

# 14. Use all() and any() to check if all students passed in a given list of marks.
marks = [85, 70, 90, 60, 50]
all_passed = all(mark >= 50 for mark in marks)
any_failed = any(mark < 50 for mark in marks)

print("All passed:", all_passed)
print("Any failed:", any_failed)

# 15. Write a program to flatten a 2D list using built-in functions.
two_d_list = [[1, 2, 3], [4, 5], [6, 7]]
flattened = [item for sublist in two_d_list for item in sublist]
print("Flattened list:", flattened)

# 16. Find the total marks of students using map() and sum().
marks = [80, 90, 100, 85, 75]
total_marks = sum(map(int, marks))
print("Total marks:", total_marks)

# 17. Write a program to find the intersection of two lists using built-in functions.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
intersection = list(set(list1) & set(list2))
print("Intersection of lists:", intersection)

# 18. Find the most frequent character in a given string using built-in functions.
from collections import Counter

string = "programming"
frequency = Counter(string)
most_frequent_char = frequency.most_common(1)[0]
print("Most frequent character:", most_frequent_char)

# 19. Use max() with key function to find the longest word in a list.
words = ["apple", "banana", "kiwi", "cherry"]
longest = max(words, key=len)
print("Longest word:", longest)

# 20. Write a program to group students based on marks using dict() and zip().
students = ["Alice", "Bob", "Charlie"]
marks = [85, 70, 95]
student_marks = dict(zip(students, marks))
print("Grouped students and marks:", student_marks)

# 21. Use filter() to remove all words shorter than 4 letters from a list.
words = ["a", "apple", "banana", "cat", "dog"]
filtered_words = list(filter(lambda word: len(word) >= 4, words))
print("Filtered words:", filtered_words)

# 22. Write a program to rotate elements of a list using slicing and built-in functions.
lst = [1, 2, 3, 4, 5]
rotated_lst = lst[1:] + lst[:1]
print("Rotated list:", rotated_lst)

# 23. Find the median of a list using built-in functions.
def find_median(lst):
    lst.sort()
    n = len(lst)
    if n % 2 == 1:
        return lst[n//2]
    else:
        return (lst[n//2 - 1] + lst[n//2]) / 2

numbers = [1, 3, 5, 7, 9]
print("Median:", find_median(numbers))

# 24. Write a program to find employees with salary above 50,000 using filter().
salaries = [45000, 55000, 70000, 60000, 40000]
high_salary_employees = list(filter(lambda x: x > 50000, salaries))
print("Employees with salary above 50,000:", high_salary_employees)

# 25. Use map() and lambda to square each element in a list.
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared_numbers)