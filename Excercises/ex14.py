# ---------------------------------------------------------- NumPy Library – 50 Real-World Problems -----------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Part A: Array Creation, Indexing, Slicing (Basic Level)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1. Create a NumPy array of 1000 random integers and find the largest and smallest values.
import numpy as np
arr = np.random.randint(1, 1001, size=1000)
print("Array:", arr)
print("Largest value:", np.max(arr))
print("Smallest value:", np.min(arr))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2. Extract all even numbers from a NumPy array of integers.
import numpy as np
arr = np.array([10, 15, 22, 33, 44, 57, 60])
even_nums = arr[arr % 2 == 0]
print("Original Array:", arr)
print("Even Numbers:", even_nums)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3. Generate an array of 50 numbers evenly spaced between 10 and 100.
import numpy as np
arr = np.linspace(10, 100, 50)
print("Evenly spaced numbers between 10 and 100:")
print(arr)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 4. Reshape a 1D array of 36 elements into a 6x6 matrix.
import numpy as np
arr = np.arange(1, 37)
matrix = arr.reshape(6, 6)
print("6x6 Matrix:\n", matrix)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 5. Create a 5x5 identity matrix using NumPy.
import numpy as np
I = np.identity(5)
print("5*5 Identity Matirx:\n", I)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 6. Slice a 10x10 random array to extract a 3x3 block from the center.
import numpy as np
arr = np.random.randint(1, 100, (10,10))
print("Original 10*10 Array:\n", arr)

center_block = arr[3:6, 3:6]
print("3*3 Center Block:\n", center_block)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 7. Replace all negative values in an array with 0.
import numpy as np
arr = np.array([4, -3, 7, -1, 9, -6])
arr[arr < 0] = 0
print("Replaced negative values with 0:", arr)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 8. Create a 1D NumPy array and reverse it without using Python slicing.
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
reversed_arr = np.flip(arr)
print("Original Array:", arr)
print("Reversed Array:", reversed_arr)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 9. Generate a NumPy array with only prime numbers up to 100.
import numpy as np
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
        return True

primes = np.array([x for x in range(2, 101) if is_prime(x)])
print("Prime numbers up to 100:\n", primes)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
# 10. Create a diagonal matrix from a given 1D array.
import numpy as np
arr = np.array([10, 20, 30, 40])
diag_matirx = np.diag(arr)
print("1D Array:", arr)
print("Diagonal Matrix:\n", diag_matirx)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------- Part B: Aggregation & Descriptive Statistics -----------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1. Find the mean, median, and standard deviation of stock prices stored in an array.
import numpy as np

stock_prices = np.array([120, 125, 130, 128, 135, 140, 138])
print("Mean:", np.mean(stock_prices))
print("Median:", np.median(stock_prices))
print("Standard Deviation:", np.std(stock_prices))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2. Compute the cumulative sum of monthly sales data using NumPy.
import numpy as np
sales = np.array([1000, 1200, 1500, 1300, 1700, 1600])
cumulative_sales = np.cumsum(sales)
print("Monthly Sales:", sales)
print("Cumulative Sales:", cumulative_sales)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3. Find the correlation coefficient between two datasets (height and weight).
import numpy as np
height = np.array([150, 160, 165, 170, 175, 180])
weight = np.array([50, 55, 60, 65, 70, 75])

corr = np.corrcoef(height, weight)
print("Correlation Coefficient Matrix:\n", corr)
print("Correlation between height and weight:", corr[0, 1])

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 4. Calculate the 25th, 50th, and 75th percentiles of employee salaries using NumPy.
import numpy as np
salaries = np.array([25000, 30000, 40000, 35000, 45000, 50000, 55000])
p25 = np.percentile(salaries, 25)
p50 = np.percentile(salaries, 50)
p75 = np.percentile(salaries, 75)
print("25th Percentile:", p25)
print("50th Percentile (Median):", p50)
print("75th Percentile:", p75)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 5. Given student marks in an array, calculate the number of students above average.
import numpy as np
marks = np.array([45, 60, 75, 50, 80, 90, 55])
average = np.mean(marks)
above_avg = np.sum(marks > average)
print("Average Marks:", average)
print("Students above average:", above_avg)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 6. Compute the moving average of a time-series data using NumPy.
import numpy as np
data = np.array([10, 20, 30, 40, 50, 60])
window_size = 3
moving_avg = np.convolve(data, np.ones(window_size)/window_size, mode='valid')
print("Original Data:", data)
print("Moving Average (window=3):", moving_avg)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 7. Find the most frequent element in a NumPy array.
import numpy as np
arr = np.array([2, 3, 4, 2, 2, 5, 3, 2, 4])
(unique, counts) = np.unique(arr, return_counts=True)
most_freq = unique[np.argmax(counts)]
print("Array:", arr)
print("Most Frequent Element:", most_freq)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 8. Normalize a NumPy array (scale values between 0 and 1).
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
normalized = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
print("Original Array:", arr)
print("Normalized Array:", normalized)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 9. Standardize a dataset (zero mean and unit variance) using NumPy.
import numpy as np
data = np.array([5, 10, 15, 20, 25])
standardized = (data - np.mean(data)) / np.std(data)
print("Original Data:", data)
print("Standardized Data:", standardized)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 10. Calculate the variance of rainfall data using NumPy.
import numpy as np
rainfall = np.array([120, 100, 80, 150, 200, 170, 130])
variance = np.var(rainfall)
print("Rainfall Data:", rainfall)
print("Variance of Rainfall:", variance)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------- Part C: Broadcasting & Vectorized Operations -----------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1. Add two matrices of different shapes using broadcasting.
import numpy as np
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[10], [20]])
result = A + B
print("1. Add two matrices of different shapes using broadcasting:\n", result)
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2. Convert temperatures from Celsius to Fahrenheit for an entire array at once.
import numpy as np
celsius = np.array([0, 20, 37, 100])
fahrenheit = celsius * 9/5 + 32
print("\n2. Celsius to Farhenheit conversion:\n", fahrenheit)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3. Multiply each column of a matrix by a different scalar using broadcasting.
import numpy as np
A = np.array([[1, 2, 3],
              [4, 5, 6]])
scalars = np.array([10, 20, 30])

result = A * scalars
print("\n3. Multiply each column by different scalar:\n", result)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 4. Calculate Body Mass Index (BMI) for 100 people using height and weight arrays.
import numpy as np
height = np.random.uniform(1.5, 2.0, 100)
weight = np.random.uniform(50, 100, 100)
BMI = weight / (height ** 2)
print("\n4. BMI for 100 people:\n", BMI[:10], "...")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 5. Perform element-wise multiplication of two 2D arrays.
import numpy as np

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

result = A * B
print("\n5. Element-wise multiplication:\n", result)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 6. Subtract row mean from each row in a matrix.
import numpy as np
A = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])

row_mean = A.mean(axis=1, keepdims=True)
normalized = A - row_mean
print("\n6. Subtract row mean from each row:\n", normalized)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 7. Create a 5x5 chessboard pattern using 0 and 1 with broadcasting.
import numpy as np
x = np.arange(5)
y = np.arange(5)
chessboard = (x[:, None] + y) % 2
print("\n7. 5x5 Chessboard pattern:\n", chessboard)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 8. Implement min-max normalization on a dataset without loops.
import numpy as np
data = np.array([[2, 4, 6],
                 [1, 3, 5],
                 [7, 9, 11]])

min_val = data.min(axis=0)
max_val = data.max(axis=0)
normalized = (data - min_val) / (max_val - min_val)
print("\n8. Min-max normalization:\n", normalized)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 9. Divide each element of a matrix by the sum of its column.
import numpy as np
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

col_sum = A.sum(axis=0, keepdims=True)
result = A / col_sum
print("\n9. Divide each element by column sum:\n", result)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 10. Compute Euclidean distance between two arrays using broadcasting.
import numpy as np
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

distance = np.sqrt(np.sum((A - B) ** 2))
print("\n10. Euclidean distance between two arrays:", distance)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------- Part D: Masking, Filtering & Conditional Selection --------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1. Filter out all negative temperatures from an array.
import numpy as np
temps = np.array([30, -5, 22, -10, 15, 40])
positive_temps = temps[temps >= 0]
print("1. Temperatures (no negatives):", positive_temps)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2. Find all employees with salary above 50,000 using NumPy masking.
import numpy as np
salaries = np.array([45000, 52000, 61000, 39000, 75000])
high_salary = salaries[salaries > 50000]
print("\n2. Employees with salary > 50,000:", high_salary)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3. Replace all odd numbers in an array with -1.
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
arr[arr % 2 != 0] = -1
print("\n3. Replace odd numbers with -1:", arr)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 4. Count how many days in a temperature dataset were above 40°C.
import numpy as np
temps = np.array([35, 42, 38, 45, 41, 39, 44])
count = np.sum(temps > 40)
print("\n4. Days with temperature > 40°C:", count)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 5. Extract all values between 100 and 200 from a dataset.
import numpy as np
data = np.array([50, 120, 180, 250, 160, 90])
filtered = data[(data >= 100) & (data <= 200)]
print("\n5. Values between 100 and 200:", filtered)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 6. Given a matrix of student marks, find which students passed all subjects (>40).
import numpy as np
marks = np.array([[45, 60, 70],
                  [30, 55, 65],
                  [50, 50, 45]])
passed_students = np.all(marks > 40, axis=1)
print("\n6. Students who passed all subjects:", passed_students)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 7. Find the index positions of all maximum values in an array.
import numpy as np
arr = np.array([10, 25, 30, 25, 30, 15])
indices = np.where(arr == arr.max())
print("\n7. Index positions of max values:", indices[0])

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 8. Replace missing values (NaN) with the mean of the array.
import numpy as np
arr = np.array([10, np.nan, 20, 30, np.nan, 40])
mean_val = np.nanmean(arr)
arr[np.isnan(arr)] = mean_val
print("\n8. Replace NaN with mean:", arr)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 9. Find all outliers beyond 3 standard deviations in a dataset.
import numpy as np
data = np.array([10, 12, 13, 11, 12, 300, 14, 15])
mean = np.mean(data)
std = np.std(data)
outliers = data[np.abs(data - mean) > 3 * std]
print("\n9. Outliers beyond 3 std deviations:", outliers)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 10. Split an array into two parts: values above and below the median.
import numpy as np
arr = np.array([5, 10, 15, 20, 25, 30])
median = np.median(arr)
above = arr[arr > median]
below = arr[arr <= median]
print("\n10. Values below/equal to median:", below)
print("Values above median:", above)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------- Part E: Random, Linear Algebra, Performance (Advanced Level) ---------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1. Generate 1000 random numbers following a normal distribution.
import numpy as np
data = np.random.normal(loc=0, scale=1, size=1000)
print("1. 1000 random numbers (Normal Distribution):")
print(data[:10], "...")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2. Simulate 10 coin tosses and count heads vs tails.
import numpy as np
coins = np.random.choice(['Heads', 'Tails'], size=10)
heads = np.sum(coins == 'Heads')
tails = np.sum(coins == 'Tails')
print("\n2. 10 coin tosses:", coins)
print("Heads:", heads, "| Tails:", tails)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3. Create a random walk of 100 steps using NumPy.
import numpy as np
steps = np.random.choice([-1, 1], size=100)
random_walk = np.cumsum(steps)
print("\n3. Random walk (first 20 steps):", random_walk[:20])

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 4. Compute dot product of two vectors.
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
dot_product = np.dot(a, b)
print("\n4. Dot product of vectors:", dot_product)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 5. Solve a system of linear equations using NumPy (np.linalg.solve).
import numpy as np

A = np.array([[2, 1],
              [1, -1]])
B = np.array([5, 1])

solution = np.linalg.solve(A, B)
print("\n5. Solution of linear equations (x, y):", solution)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 6. Compute eigenvalues and eigenvectors of a given matrix.
import numpy as np
matrix = np.array([[4, -2],
                   [1, 1]])

eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("\n6. Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 7. Perform matrix multiplication between two large matrices and compare performance with Python lists.
import numpy as np
import time

# NumPy method
A = np.random.rand(500, 500)
B = np.random.rand(500, 500)

start = time.time()
np_result = np.dot(A, B)
numpy_time = time.time() - start

# Python list method
A_list = A.tolist()
B_list = B.tolist()

start = time.time()
list_result = [[sum(x*y for x, y in zip(A_row, B_col)) for B_col in zip(*B_list)] for A_row in A_list]
list_time = time.time() - start

print("\n7. Matrix multiplication performance:")
print(f"NumPy time: {numpy_time:.5f} sec")
print(f"Python lists time: {list_time:.5f} sec")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 8. Simulate rolling two dice 1000 times and count frequency of sums.
import numpy as np
die1 = np.random.randint(1, 7, 1000)
die2 = np.random.randint(1, 7, 1000)
sums = die1 + die2

unique, counts = np.unique(sums, return_counts=True)
print("\n8. Dice roll sum frequencies:")
for u, c in zip(unique, counts):
    print(f"Sum {u}: {c}")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 9. Generate a random dataset of 100 students with marks in 3 subjects and compute average per student.
import numpy as np
marks = np.random.randint(30, 100, size=(100, 3))
average = marks.mean(axis=1)
print("\n9. Average marks of first 10 students:\n", average[:10])

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 10. Compare execution time of summing 1 million elements using NumPy vs Python list.
import numpy as np
# NumPy array
import time
arr_np = np.arange(1_000_000)
start = time.time()
sum_np = np.sum(arr_np)
time_np = time.time() - start

# Python list
arr_list = list(range(1_000_000))
start = time.time()
sum_list = sum(arr_list)
time_list = time.time() - start

print("\n10. Summing 1 million elements:")
print(f"NumPy sum time: {time_np:.6f} sec")
print(f"Python list sum time: {time_list:.6f} sec")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
