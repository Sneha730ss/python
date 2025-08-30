""" 
----------------------------------------------------------------------------------------------------------------------------
1. Input/Output (10 Questions)
----------------------------------------------------------------------------------------------------------------------------
1. What is the difference between input() and print() in Python?
-->  input() is used to take input from the user as a string.
     print() is used to display output to the console.

2. How do you take integer input from the user?
--> num = int(input("Enter a number: "))

3. What happens if you take input using input() and try to perform arithmetic directly?
--> input() always returns data as a string. If we try to do arithmetic directly, Python will throw a TypeError.

4. How can you take multiple inputs in a single line?
--> a, b, c = map(int, input("Enter 3 numbers: ").split())
    print(a, b, c)

5. How do you format output using f-strings?
--> name = "John"
    age = 25
    print(f"My name is {name} and I am {age} years old.")


6. What is the difference between f-string, % formatting, and .format()?
--> f-string (Python 3.6+) → f"Hello {name}"
    % formatting → "Hello %s" % name
    .format() → "Hello {}".format(name)

7. How do you print without a newline in Python?
--> print("Hello", end=" ")
    print("World")

8. How can you print output to a file?
--> with open("output.txt", "w") as f:
    print("Hello File!", file=f)

9. What is the role of sep and end in the print() function?
--> sep → separator between values (default = space).
    end → what to print at the end (default = newline).

10. How do you read input from a file using Python?
--> with open("input.txt", "r") as f:
         data = f.read()
    print(data)

----------------------------------------------------------------------------------------------------------------------------
2. Variables and Data Types (10 Questions)
----------------------------------------------------------------------------------------------------------------------------

11. What is dynamic typing in Python?
--> In Python, we don't need to declare the type of a variable explicitly. The type is assigned automatically
at runtime and can change later.

12. How do you declare and assign a variable in Python?
--> Simply by using the = operator.
    Ex. name = "Snehaa"
        age = 21

13. What are the standard data types available in Python?
--> Numeric → int, float, complex
    Sequence → str, list, tuple 
    Set types → set, frozenset
    Mapping → dict
    Boolean → bool
    None → NoneType

14. What is the difference between mutable and immutable types? Give examples.
--> Mutable → Can be changed after creation → list, dict, set
    Immutable → Cannot be changed → int, float, str, tuple
    Ex. # Mutable
        mylist = [1,2,3]
        mylist[0] = 100   # allowed
        # Immutable
        text = "Hello"     # text[0] = "Y"    error


15. What happens when you assign one variable to another?
--> Both variables point to the same object in memory.
    ex. a = [1,2,3]
    b = a
    b[0] = 100
    print(a)  # [100,2,3] → because both point to same list


16. How do you check the data type of a variable?
--> Using type() function.
    Ex. x = 10
        print(type(x))  # <class 'int'>


17. What is the difference between int, float, and complex in Python?
--> int → Whole numbers → 10, -5
    float → Decimal numbers → 3.14, -2.7
    complex → Numbers with real & imaginary parts → 3+5j

18. What is NoneType in Python?
--> NoneType is the type of the special value None, which represents "no value" or 'null".

19. How do Python variables handle memory?
--> Python variables are references to objects stored in memory.
    Small integers and strings are cached for efficiency.
    For mutable objects, changes affect all references pointing to them.

20. Can we use reserved keywords as variable names?
--> No. Keywords like if, while, for, class, etc cannot be used as variable names.

----------------------------------------------------------------------------------------------------------------------------
3. Operators (10 Questions)
----------------------------------------------------------------------------------------------------------------------------

21. What are different types of operators in Python?
--> Arithmetic: + - * / // % **
    Relational/Comparison: < > <= >= == !=
    Logical: and, or, not
    Bitwise: & | ^ ~ << >>
    Assignment: =, +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=, <<=, >>=
    Identity: is, is not
    Membership: in, not in

22. How is == different from is?
--> == -> Checks values are equal
    is -> check memory references(object identity)
    
23. What is the use of // and % operators?
--> // -> Floor division (quotient without decimal)
    % -> Modulus (remainder)

24. Explain bitwise operators in Python with examples.
--> Bitwise operators           Ex. a = 5   # 0101
                                    b = 3   # 0011
    & (AND)                     Ex. print (a & b)  # 1 (0001)                 
    | (OR)                      Ex. print(a | b)   # 7 (0111)
    ^ (XOR)                     Ex. print(a ^ b)  # 6 (0110)
    ~ (NOT → flips bits)        Ex. print(~a)     # -6 (two’s complement)
    << (Left shift)             Ex. print(a << 1) # 10 (1010)
    >> (Right shift)            Ex. print(a >> 1) # 2 (0010)

25. What is the output of True + True and why?
--> output will be 2 , Because in python, True = 1 and False = 0
    Ex. print(True + True)   # 2

26. Explain operator precedence with an example.
--> Precedence = order of evaluation
   Ex. result = 2 + 3 * 4
   print(result)  # 14
   
27. How do comparison operators work in Python?
--> They compare values and return True/False
    Ex. print(5 > 3)   # True
        print(5 == 5)  # True
        print(5 != 2)  # True


28. What are identity and membership operators?
--> Identity: is, is not (check object identity)
    Membership: in, not in (check if element exists in a sequence)

29. What is short-circuit evaluation in logical operators?
--> In and and or, Python stops evaluation early if result is already known.
    Ex. print(False and 5/0)  # False (second part not evaluated)
        print(True or 5/0)    # True  (second part not evaluated)


30. Can we overload operators in Python?
--> Yes, using special methods in clases. 
    Ex. Overloading + operator.
        class Point:
            def __init__(self, x, y):
                self.x, self.y = x, y
    
            def __add__(self, other):
                return Point(self.x + other.x, self.y + other.y)

        p1 = Point(2,3)
        p2 = Point(4,5)
        p3 = p1 + p2
        print(p3.x, p3.y)   # 6 8


----------------------------------------------------------------------------------------------------------------------------
4. Control Structures: if, if-else, elif, nested if-else (10 Questions)
----------------------------------------------------------------------------------------------------------------------------

31. What is the syntax of if statements in Python?
--> if condition:
       # block of code
    Note: If the condition is True, the block runs; otherwise, it is skipped.       

32. How does if-else work in Python?
--> if checks teh condition.
    if True -> Executes if block
    if False -> Executes else block
    Ex. age = 18
        if age >= 18:
            print("Adult")
        else:
            print("Minor")

33. What is the role of elif and how is it different from nested if?
--> elif -> used for multiple conditions in sequence.
    nested if -> if inside another if.

34. Give a real-world example using nested if-else conditions.
--> age = 25
    gender = "F"

    if age >= 18:
        if gender == "F":
            print("Eligible for women’s scheme")
        else:
            print("Eligible for general scheme")
    else:
        print("Not Eligible")


35. How does Python evaluate chained comparison like 3 < x < 7?
--> Python evaluates both conditions together.
    ex. x = 5
        print(3 < x < 7)    # True 
    It's equivalent to (3 < x) and ( x < 7)    

36. What happens if indentation is not correct in control statements?
--> Python raises IndentationError

37. Is it necessary to use else after if?
--> No, else is optional
    We can write just if, or if-elif without else.

38. What is the output of if 0: and why?
--> Output: Nothing
    Because 0 is considered False in Boolean context.

39. Can we write if condition without a block?
--> Yes, by using pass (null Statement)

40. How do you handle multiple conditions in a single if?
--> By using logical operators: and, or, not.

----------------------------------------------------------------------------------------------------------------------------
 5. Strings (15 Questions)
 ----------------------------------------------------------------------------------------------------------------------------

41. What are different ways to create strings in Python?
--> Single quotes -> 'hello'
    Double quotes -> "hello"
    Triple quotes -> '''hello''' or (used for multi-line strings)
    Using str() constructor -> str(123) -> "123"

42. How are strings stored in memory in Python?
--> Strings are stored as a sequence of Unicode characters.
    They are immutable, meaning once created, they cannot be modified.
    If we change a string, python creates a new object.

43. What is the difference between single, double, and triple quotes?
--> Single('') and Double ("") -> No difference, both define single-line string.
    Triple(''' or "" ") -> Used for multi-line strings and docstrings.
    
44. How can you concatenate and repeat strings?
--> Concatenation -> Using +
    Repetition -> Using *

45. What are string slicing and indexing? Give examples.
--> Slicing -> Extract substring (s[start:end:step])
    Indexing -> Access single character (s[0], s[-1])

46. How do you reverse a string in Python?
--> s = "hello
    print(s[::-1])     # olleh
    OR
    print(''.join(reversed(s)))
    
47. Are strings mutable in Python?
--> No, strings are immutable. Any modification creates a new string.

48. What is the use of join() and split()?
--> join() -> joins list elements into a string.
    split() -> Splits string into a string.

49. What does strip(), lstrip() and rstrip() do?
--> strip() -> Removes whitespace from both ends.
    lstrip() -> Removes left-side spaces.
    rstrip() -> Removes reight-side spaces.

50. How can you find if a substring exists in a string?
--> s = "Python Programming"
    print("Python" in s)      # True
    print("Java" not in s)    # True

51. How do you count occurrences of a character in a string?
--> s = "banana"
    print(s.count("a))     # 3

52. What is the use of find() and index()?
--> find() -> Returns index of substring, or -1 if not found.
    index() -> Returns index, but raises ValueError if not found.

53. How can you replace a part of a string?
--> s = "I like Java"
    print(s.replace("Java", "Python"))    # I like Python

54. How to format strings using .format()?
--> name = "sneha"
    age = 22
    print("My name is {} and I am {} years old".format(name, age))    

55. What are escape sequences in strings?
--> Special characters starting with \.
    \n -> New line
    \t -> Tab
    \' -> Single quote
    \" -> Double quote
    \\ -> Backslash

----------------------------------------------------------------------------------------------------------------------------
 6. Escape Sequences (5 Questions)
 ----------------------------------------------------------------------------------------------------------------------------
56. What are escape sequences? List 5 common ones.
--> Escape sequences are special character combinations that represent things that can't be types directly in a string.
    They start with \ (backslash)
    Common ones: 
        \n -> New line
        \t -> Tab
        \' -> Single quote
        \" -> Double quote
        \\ -> Backslash
    
57. What is the difference between \n, \r, and \t?
--> \n -> New line (moves cursor to next line)
    \r -> Carriage return (moves cursor to beginning of line, overwriting)
    \t -> Horizontal tab (adds  space like pressing tab key).

58. How do you print a backslash (\) in a string?
--> using double backslash \\
    print("This is a backslash: \\")

59. How does \b behave in Python string?
--> \b is backspace -> deletes the previous character.

60. Can you use escape characters in raw strings?
--> No, raw strings (r " ") treat backslashes as literal characters, not escapes.

----------------------------------------------------------------------------------------------------------------------------
7. Dictionary (10 Questions)
----------------------------------------------------------------------------------------------------------------------------
61. What is a dictionary in Python?
--> A dictionary is an unordered collection of key-value pairs.
    Keys are unique, and values can be of any type.

62. How do you create a dictionary?
--> By using curly braces {} 

63. How can you access, add, or update values in a dictionary?
--> my_dict = {"a": 1, "b": 2}
    # Access
        print(my_dict["a"])   # 1
    # Add
        my_dict["c"] = 3
    # Update
        my_dict["b"] = 20


64. What happens when you access a key that doesn’t exist?
--> Using my_dict[key] → Raises KeyError
    Using my_dict.get(key) → Returns None (or default value if provided)
    Ex. print(my_dict.get("x"))       # None
        print(my_dict.get("x", 0))    # 0

65. What is the difference between get() and direct access?
--> get() -> Returns None or default value if key not found
    Direct access(my_dict[key]) -> KeyError if key not found

66. How do you iterate over dictionary keys and values?
--> my_dict = {"a": 1, "b": 2}
    for key in my_dict:           # keys
        print(key)
    for value in my_dict.values():  # values
        print(value)
    for k, v in my_dict.items():   # key-value pairs
        print(k, v)


67. How to merge two dictionaries?
--> using update() method:
    Ex. d1 = {"a": 1}
        d2 = {"b": 2}
        d1.update(d2)
        print(d1)  # {'a': 1, 'b': 2}


68. What is dictionary comprehension? Give an example.
--> Like list comprehension but for dictionaries.
    Ex. squares = {x: x**2 for x in range(1, 6)}
        print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
 
69. How do you delete a key from a dictionary?
--> my_dict = {"a": 1, "b": 2}
    del my_dict["a"]      # removes key 'a'
    my_dict.pop("b")      # removes key 'b'


70. Can dictionary keys be mutable? Why or why not?
--> No, keys must be immutable(like str, int, tuple)
    Mutable types(like list) cannot be keys because their hash vaue can change.

----------------------------------------------------------------------------------------------------------------------------
8. Set (10 Questions)
----------------------------------------------------------------------------------------------------------------------------
71. What is a set in Python?
--> A set is an unordered collection of unique elements.
    It does not allow duplicates and supports mathematical set operations.

72. How do you create a set?
--> using curly braces {}: 
    s = {1, 2, 3}
    Using set() constructor:
    s = set()

73. What is the difference between set and list?
--> | Feature    | List      | Set           |
| ---------- | --------- | ------------- |
| Order      | Ordered   | Unordered     |
| Duplicates | Allowed   | Not allowed   |
| Indexing   | Supported | Not supported |

74. How do you add and remove elements from a set?
-->
s = {1, 2, 3}
s.add(4)         # Add element
s.remove(2)      # Remove element (raises KeyError if not present)
s.discard(5)     # Remove element (no error if not present)


75. What are set operations: union, intersection, difference, symmetric difference?
-->
A = {1, 2, 3}
B = {2, 3, 4}

print(A | B)     # Union → {1, 2, 3, 4}
print(A & B)     # Intersection → {2, 3}
print(A - B)     # Difference → {1}
print(A ^ B)     # Symmetric Difference → {1, 4}


76. How are duplicates handled in sets?
--> Duplicates are automatically removed.
s = {1, 2, 2, 3}
print(s)  # {1, 2, 3}

77. How to check if a set is a subset/superset of another?
-->
A = {1, 2}
B = {1, 2, 3}

print(A.issubset(B))    # True
print(B.issuperset(A))  # True


78. What is a frozen set?
--> Immutable version of a set → cannot add/remove elements
    Ex.fs = frozenset([1, 2, 3])

79. Can we use set elements as dictionary keys?
--> Regular sets cannot be dictionary keys (mutable).
    Frozen sets can be used as dictionary keys.

80. How to iterate through a set?
-->
s = {1, 2, 3}
for item in s:
    print(item)

----------------------------------------------------------------------------------------------------------------------------
9. Tuple (10 Questions)
----------------------------------------------------------------------------------------------------------------------------

81. What is a tuple? How is it different from a list?
--> A tuple is an ordered, immutable collection of elements.
    and list is mutable and syntax = [] square bracket
    tuple is immutable and syntax =() round bracket

82. How do you create a tuple with a single element?
--> Add a comma after the element:
t = (5, )

83. Are tuples mutable or immutable?
--> Immutable -> Cannot modify elements after creation.

84. How can you convert a list to a tuple?
-->
lst = [1, 2, 3]
t = tuple(lst)

85. How to access elements in a tuple?
-->
t = (1, 2, 3)
print(t[0])    # 1
print(t[-1])   # 3

86. What is tuple unpacking? Give an example.
--> Assign elements of a tuple to variables directly.
t = (10, 20, 30)
a, b, c = t
print(a, b, c)  # 10 20 30

87. Can a tuple contain mutable elements?
--> Yes, e.g., a list inside a tuple:
t = (1, [2,3], 4)
t[1].append(5)
print(t)  # (1, [2, 3, 5], 4)

88. How do you iterate through a tuple?
--> 
t = (1, 2, 3)
for item in t:
    print(item)


89. When should you use a tuple over a list?
--> When data should not change (immutability).
    Useful as dictionary keys or for fixed data storage.

90. How can you concatenate or repeat tuples?
-->
t1 = (1,2)
t2 = (3,4)
print(t1 + t2)  # (1,2,3,4)
print(t1 * 3)   # (1,2,1,2,1,2)


----------------------------------------------------------------------------------------------------------------------------
 10. Type Casting (5 Questions)
----------------------------------------------------------------------------------------------------------------------------

91. What is type casting in Python?
--> Type casting is converting one data type to another.

92. How do you convert string to int, float to int, etc.?
-->
int("123")      # 123
float("3.14")   # 3.14
int(3.99)       # 3
str(100)        # "100"

93. What is the difference between int("3.14") and float("3.14")?
--> int("3.14") → Error (cannot convert decimal string to int directly)
    float("3.14") → Works → 3.14

94. How do you safely cast input values using try-except?
--> 
try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid input")


95. How do you convert list to tuple and vice versa?
-->
lst = [1,2,3]
t = tuple(lst)      # list → tuple

tup = (4,5,6)
lst2 = list(tup)    # tuple → list


----------------------------------------------------------------------------------------------------------------------------
 11. Mixed & Scenario-Based Questions (5 Questions)
----------------------------------------------------------------------------------------------------------------------------
96. What will be the output of:
a = "5"
b = 2
print(a * b)
--> 55 # multiplying a string by an integer repeats the string b times.

97. How can you count characters in a string using dictionary?
--> s = "hello"
    char_count = {}
    for ch in s:
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1
    print(char_count)  # {'h':1, 'e':1, 'l':2, 'o':1}


98. Write a program to check if a number is positive, negative, or zero.
--> 
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


99. What’s the output of:
x = None
if x:
    print("True")
else:
    print("False")
--> False

100. How would you write a program to categorize marks using nested if-else?
--> 
marks = float(input("Enter marks: "))

if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Division")
elif marks >= 50:
    print("Second Division")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")

"""
