# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# A) Sets – 25 Questions
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1. Find all elements that are present in two sets but not in a third.
A, B, C = {1,2,3,4}, {3,4,5,6}, {4,6}
print((A & B) - C)

# 2. Remove duplicates from a list using sets and return a sorted set.
lst = [4,2,2,3,1,4]
print(sorted(set(lst)))

# 3. Check if one set is a subset of another without using built-in methods.
A, B = {1,2}, {1,2,3}
is_subset = all(x in B for x in A)
print(is_subset)

# 4. Union two sets without using the union() method.
A, B = {1,2}, {2,3}
print(A | B)

# 5. Find symmetric difference between two sets.
A, B = {1,2,3}, {3,4}
print(A ^ B)

# 6. Count common elements between multiple sets.
A, B, C = {1,2,3}, {2,3,4}, {2,3,5}
print(len(A & B & C))

# 7. Check if a set is disjoint with another set.
A, B = {1,2}, {3,4}
print(A.isdisjoint(B))

# 8. Remove all elements from a set that are divisible by 3.
S = {1,2,3,4,6,9}
S = {x for x in S if x % 3 !=0}
print(S)

# 9. Create a set of all unique words from a given paragraph.
para = "this is a test this is code"
print(set(para.split()))

# 10. Find maximum and minimum element in a set without max() or min().
S = {4,2,7,1}
mx, mn = None, None
for x in S:
    if mx is None or x > mx: mx = x
    if mn is None or x < mn: mn = x
print(mx, mn)
    
# 11. Merge multiple sets and remove duplicates.
sets = [{1,2}, {2,3}, {3,4}]
merged = set()
for S in sets: merged |= S
print(merged)

# 12. Generate a set of squares of numbers from 1 to 50.
print({x*x for x in range(1,51)})

# 13. Count the number of vowels in a set of characters.
chars = {'a', 'b', 'e','i', 'x'}
print(len(chars & set('aeiou')))

# 14. Check whether a set is empty or not.
S = set()
print(len(S) == 0)

# 15. Remove the smallest element from a set.
S = {4, 1, 7, 2}
S.remove(min(S))
print(S)

# 16. Find elements present in the first set but not in the second.
A, B = {1,2,3}, {2,3}
print(A - B)

# 17. Convert a list of tuples into a set of tuples.
lst = [(1,2), (2,3), (1,2)]
print(set(lst))

# 18. Find elements that appear only once among multiple sets.
A, B, C = {1,2,3}, {2,4}, {3,5}
all_items = A | B | C
unique = {x for x in all_items if [x in s for s in (A,B,C)].count(True) == 1}
print(unique)

# 19. Generate a set of numbers divisible by 5 up to 200.
print({x for x in range(1, 201) if x%5==0})

# 20. Implement set intersection using loops instead of built-ins.
A, B ={1,2,3}, {2,3,4}
inter = {x for x in A if x in B}
print(inter)

# 21. Count elements greater than 10 in a set.
S = {4,12,15,7}
print(sum(1 for x in S if x > 10))

# 22. Find the sum of all elements in a set.
S = {1,2,3}
print(sum(S))

# 23. Identify duplicates in a list using sets.
lst = [1,2,2,3,3,3,4]
seen, dup = set(), set()
for x in lst:
    if x in seen: dup.add(x)
    else: seen.add(x)
print(dup)    

# 24. Replace all odd numbers in a set with their square.
S = {1,2,3,4}
S = {x*x if x%2 else x for x in S}
print(S)

# 25. Check whether a set contains any prime number.
def is_prime(x):
    if x < 2: return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: return False
    return True
S = {4,6,7,10}
print(any(is_prime(x) for x in S))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------    
# B) Tuples – 25 Questions
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1. Reverse a tuple without using slicing.
t = (1,2,3,4)
rev = tuple(reversed(t))
print(rev)

# 2. Count occurrences of a specific element in a tuple.
t = (1,2,2,3,4,2)
print(t.count(2))

# 3. Convert a tuple of integers into a tuple of strings.
t = (1,2,3)
print(tuple(str(x) for x in t))

# 4. Find the second largest number in a tuple.
t = (4,1,7,3,7,6)
unique = sorted(set(t))
print(unique[-2])

# 5. Concatenate multiple tuples into one.
t1, t2, t3 = (1,2) (3,4), (5,)
print(t1 + t2 + t3)

# 6. Slice a tuple to get alternate elements.
t = (1,2,3,4,5,6)
print(t[::2])

# 7. Find all tuples of length 3 from a list of tuples.
lst = [(1,2,3), (4,5), (6,7,8,9)]
print([x for x in lst if len(x)==3])

# 8. Check if a tuple contains all unique elements.
t = (1,2,3,4)
print(len(t) == len(set(t)))
# 9. Swap first and last elements of a tuple.
t = (1,2,3,4)
swapped = (t[-1],) + t[1:-1] + (t[0],)
print(swapped)

# 10. Sort a tuple of integers without converting to a list.
t = (4,1,3,2)
sorted_t = tuple(sorted(t))
print(sorted_t)

# 11. Count the number of tuples where the first element is larger than the last.
lst = [(5,1), (2,3), (9,0)]
print(sum(1 for x in lst if x[0] > x[-1]))

# 12. Find elements common in two tuples.
t1, t2 = (1,2,3), (2,3,4)
print(tuple(set(t1) & set(t2)))

# 13. Create a tuple from user input until "stop" is entered.
inputs = ["a", "b", "stop"]
t = tuple(x for x in inputs if x!="stop")
print(t)

# 14. Find the sum of elements in a tuple of numbers.
t = (1,2,3,4)
print(sum(t))

# 15. Flatten a tuple of tuples into a single tuple.
t = ((1,2), (3,4), (5,))
flat = tuple(x for sub in t for x in sub)
print(flat)

# 16. Replace a specific value in a tuple (immutability challenge).
t = (1,2,3)
lst = list(t)
lst[1] = 99
t = tuple(lst)
print(t)

# 17. Find tuples whose sum is even in a list of tuples.
lst = [(1,2), (2,3), (4,4)]
print([x for x in lst if sum(x)%2==0])

# 18. Group tuple elements into pairs.
t = (1,2,3,4,5,6)
pairs = tuple((t[i], t[i+1]) for i in range(0, len(t),2))
print(pairs)

# 19. Convert a tuple into a dictionary with indexes as keys.
t = ('a', 'b', 'c')
d = {i: t[i] for i in range(len(t))}
print(d)

# 20. Remove all duplicates from a tuple.
t = (1,2,2,3,1)
print(tuple(dict.fromkeys(t)))

# 21. Count vowels in a tuple of characters.
t = ('a', 'b','e','i','o')
print(sum(1 for x in t if x in 'aeiou'))

# 22. Find the tuple with the maximum sum from a list of tuples.
lst =[(1,2), (4,5), (10,11)]
print(max(lst, keys=sum))

# 23. Rotate a tuple n places to the right.
t = (1,2,3,4,5)
n = 2
n %= len(t)
rot = t[-n:] + t[:-n]
print(rot)

# 24. Convert a tuple of key-value pairs into a dictionary.
t = (("a",1), ("b",2))
print(dict(t))

# 25. Extract all tuples with an odd sum from a list of tuples.
lst = [(1,2), (3,3), (4,5)]
print([x for x in lst if sum(x)%2==1])

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# C) Dictionaries – 25 Questions
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1. Merge two dictionaries and sum values for duplicate keys.
d1, d2 = {"a":2, "b":3}, {"b":4, "c":5}
merged = d1.copy()
for k,v in d2.items():
    merged[k] = merged.get(k,0) + v
print(merged)
    
# 2. Sort a dictionary by keys.
d = {"b":2, "a":1, "c":3}
print(dict(sorted(d.items())))

# 3. Sort a dictionary by values.
d = {"a":5, "b":1, "c":3}
print(dict(sorted(d.items(), key=lambda x: x[1])))

# 4. Find keys with maximum values.
d ={"a":10, "b":15, "c":15}
mx = max(d.values())
print([k for k, v in d.items() if v==mx])

# 5. Swap keys and values in a dictionary.
d = {"a":1, "b":2}
print({v:k for k, v in d.items()})

# 6. Count the frequency of each character in a string using a dictionary.
s = "hello"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch,0)+1
print((freq))

# 7. Combine two lists into a dictionary.
keys = ["a", "b", "c"]
vals = [1,2,3]
print(dict(zip(keys,vals)))

# 8. Remove all items with value less than 10.
d = {"a":5, "b":15, "c":8}
print({k:v for k,v in d.items() if v>=10})

# 9. Check if a key exists in a dictionary without in.
d = {"x":1, "y":2}
key = "x"
print(key in list(d.keys()))

# 10. Sum all the values in a dictionary.
d = {"a":1,"b":2}
print(sum(d.values()))

# 11. Find the difference between two dictionaries (keys/values).
d1, d2 = {"a":1,"b":2}, {"b":3,"c":4}
print(set(d1.items()) ^ set(d2.items()))

# 12. Create a nested dictionary for student marks.
students = {
    "A":{"Math":90,"Eng":85},
    "B":{"Math":75,"Eng":80}
}
print(students)

# 13. Find duplicate values in a dictionary.
d = {"a":1,"b":2,"c":1}
seen, dup = set(), set()
for v in d.values():
    if v in seen: dup.add(v)
    else: seen.add(v)
print(dup)

# 14. Count total vowels in all dictionary keys.
d = {"apple":1,"mango":2}
print(sum(ch in 'aeiou' for k in d for ch in k))

# 15. Increment each value in a dictionary by 1.
d = {"a":1,"b":2}
print({k:v+1 for k,v in d.items()})

# 16. Merge multiple dictionaries using loops.
dicts = [{"a":1},{"b":2},{"a":3}]
merged = {}
for d in dicts:
    for k,v in d.items():
        merged[k] = merged.get(k,0)+v
print(merged)

# 17. Get a list of all keys having even values.
d = {"a":2,"b":5,"c":6}
print([k for k,v in d.items() if v%2==0])

# 18. Reverse the order of dictionary items.
d = {"a":1,"b":2,"c":3}
print(dict(reversed(d.items())))

# 19. Create a dictionary from a string where keys are letters and values are counts.
s = "banana"
d = {}
for ch in s:
    d[ch] = d.get(ch,0)+1
print(d)

# 20. Remove a key from dictionary only if it exists.
d = {"a":1,"b":2}
d.pop("a", None)
print(d)

# 21. Filter dictionary items where values are prime numbers.
def is_prime(x):
    if x<2: return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0: return False
    return True
d = {"a":2,"b":4,"c":5}
print({k:v for k,v in d.items() if is_prime(v)})

# 22. Find the key with minimum value.
d = {"a":3,"b":1,"c":7}
print(min(d, key=d.get))

# 23. Multiply all numeric values by 2.
d = {"a":2,"b":'x',"c":3}
print({k:(v*2 if isinstance(v,int) else v) for k,v in d.items()})

# 24. Check if two dictionaries are equal.
d1, d2 = {"a":1,"b":2}, {"b":2,"a":1}
print(d1 == d2)

# 25. Convert a list of dictionaries into a single dictionary with lists as values.
lst = [{"a":1,"b":2},{"a":3,"b":4}]
merged = {}
for d in lst:
    for k,v in d.items():
        merged.setdefault(k,[]).append(v)
print(merged)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# D) Lists – 25 Questions
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1. Find all pairs of numbers whose sum equals a target.
lst = [2,4,3,7,5,8]
target = 10
pairs = [(lst[i], lst[j]) for i in range(len(lst)) for j in range(i+1,len(lst)) if lst[i]+lst[j]==target]
print(pairs)

# 2. Remove all duplicates from a list without using set().
lst = [1,2,2,3,1]
unique = []
for x in lst:
    if x not in unique:
        unique.append(x)
print(unique)

# 3. Flatten a nested list.
nested = [[1,2],[3,4],[5,[6,7]]]
flat = []
def flatten(lst):
    for i in lst:
        if isinstance(i, list):
            flatten(i)
        else:
            flat.append(i)
flatten(nested)
print(flat)

# 4. Rotate a list n positions to the left.
lst = [1,2,3,4,5]
n = 2
print(lst[n:] + lst[:n])

# 5. Find the longest increasing subsequence.
def LIS(nums):
    dp = [1]*len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i]>nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)
print(LIS([10,9,2,5,3,7,101,18]))

# 6. Count frequency of each element.
lst = [1,2,2,3,3,3]
freq = {}
for x in lst:
    freq[x] = freq.get(x,0)+1
print(freq)

# 7. Merge two sorted lists into a sorted list.
a, b = [1,3,5], [2,4,6]
i=j=0
merged = []
while i<len(a) and j<len(b):
    if a[i]<b[j]:
        merged.append(a[i]); i+=1
    else:
        merged.append(b[j]); j+=1
merged.extend(a[i:]); merged.extend(b[j:])
print(merged)

# 8. Find the maximum sum of contiguous sublist (Kadane’s algorithm).
lst = [-2,1,-3,4,-1,2,1,-5,4]
max_sum = cur = lst[0]
for x in lst[1:]:
    cur = max(x, cur+x)
    max_sum = max(max_sum, cur)
print(max_sum)

# 9. Split a list into chunks of size n.
lst, n = [1,2,3,4,5,6,7], 3
chunks = [lst[i:i+n] for i in range(0,len(lst),n)]
print(chunks)

# 10. Find common elements in two lists.
a, b = [1,2,3,4],[3,4,5,6]
print([x for x in a if x in b])

# 11. Find all prime numbers in a list.
lst = [2,3,4,5,6,7,8,9,10]
def is_prime(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True
print([x for x in lst if is_prime(x)])

# 12. Replace all negative numbers with zero.
lst = [1,-2,3,-4]
print([x if x>=0 else 0 for x in lst])

# 13. Move all zeros to the end of a list.
lst = [0,1,0,3,12]
non_zero = [x for x in lst if x!=0]
zeros = [0]*(len(lst)-len(non_zero))
print(non_zero+zeros)

# 14. Sort a list of tuples by second element.
lst = [(1,3),(2,1),(4,2)]
print(sorted(lst, key=lambda x:x[1]))

# 15. Find missing numbers in a sequence.
lst = [1,2,4,6,7,10]
full = set(range(min(lst), max(lst)+1))
print(sorted(full-set(lst)))

# 16. Reverse a list without using reverse().
lst = [1,2,3,4]
rev = []
for i in range(len(lst)-1,-1,-1):
    rev.append(lst[i])
print(rev)

# 17. Find second largest element.
lst = [10,20,4,45,99]
print(sorted(set(lst))[-2])

# 18. Generate a list of squares of even numbers.
print([x*x for x in range(1,11) if x%2==0])

# 19. Count elements greater than a given number.
lst, num = [1,10,20,5,30], 10
print(len([x for x in lst if x>num]))

# 20. Merge multiple lists into one sorted list.
lists = [[1,4,5],[2,3,8],[6,7]]
merged = []
for l in lists: merged.extend(l)
print(sorted(merged))

# 21. Remove elements at odd indices.
lst = [10,20,30,40,50,60]
print([lst[i] for i in range(len(lst)) if i%2==0])

# 22. Find pairs with the smallest difference.
lst = [4,9,1,32,13]
lst.sort()
min_diff = float("inf")
pairs = []
for i in range(len(lst)-1):
    diff = lst[i+1]-lst[i]
    if diff<min_diff:
        min_diff = diff
        pairs = [(lst[i],lst[i+1])]
    elif diff==min_diff:
        pairs.append((lst[i],lst[i+1]))
print(pairs)

# 23. Implement a stack using a list.
stack = []
stack.append(10)  # push
stack.append(20)
print(stack.pop()) # pop
print(stack)

# 24. Implement a queue using a list.
queue = []
queue.append(10)  # enqueue
queue.append(20)
print(queue.pop(0)) # dequeue
print(queue)

# 25. Find duplicate elements and their indices.
lst = [1,2,3,2,4,1,5]
dups = {}
for i,x in enumerate(lst):
    if lst.count(x)>1:
        if x not in dups: dups[x]=[]
        dups[x].append(i)
print(dups)