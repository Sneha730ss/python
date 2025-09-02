# Dataset
sales = [1200, 1500, 1700, 800, 950, 2000, 2100, 1750, 1600, 1850, 1950, 2200, 2500, 3000]

# 1. Basic Info
total_sales = sum(sales)
average_sales = total_sales / len(sales)
highest_sales = max(sales)
lowest_sales = min(sales)

print("Total Sales:", total_sales)
print("Average Sales:", round(average_sales, 2))
print("Highest Sales:", highest_sales)
print("Lowest Sales:", lowest_sales)

# 2. Loops & Control Structures
days_above_avg = sum(1 for s in sales if s > average_sales)
days_below_equal_avg = len(sales) - days_above_avg

print("Days Above Average:", days_above_avg)
print("Days Below or Equal Average:", days_below_equal_avg)

# 3. List Operations:
sales_above_2000 = [s for s in sales if s > 2000]
sorted_sales_desc = sorted(sales, reverse=True)
reversed_sales = list(reversed(sales))

print("Sales Above 2000:", sales_above_2000)
print("Sorted Sales (Descending):", sorted_sales_desc)
print("Reversed Sales:", reversed_sales)

# 4. Decision Making
if total_sales > 20000:
    performance = "Good Performance"
else:
    performance = "Needs Improvement"
print("Performance Status:", performance)

# 5. Bonus: User Input
target = int(input("Enter target sales (e.g., 1800): "))
target_days = sum(1 for s in sales if s >= target)
print(f"Target ({target}) met or exceeded on {target_days} days")

# Additional Requirements (for Advanced Testing):

# 6. Comprehensions (List, Tuple, Set, Dict):
sales_plus_10 = [round(s * 1.1, 2) for s in sales]
even_sales_tuple = tuple(s for s in sales if s % 2 == 0)
unique_sales_set = {s for s in sales if s > 1500}
day_sales_dict = {i+1: sales[i] for i in range(len(sales))}

# 7.  Built-in Functions:
print("Any sales > 2500?", any(s > 2500 for s in sales))
print("All sales > 500?", all(s > 500 for s in sales))

# 8. User defined Function:
def analyze_sales(data):
    total = sum(data)
    avg = total / len(data)
    highest = max(data)
    lowest = min(data)
    performance = "Good Performance" if total > 20000 else "Needs Improvement"
    return {
        'total': total,
        'average': round(avg, 2),
        'highest': highest,
        'lowest': lowest,
        'performance': performance
    }

# Function Output
result = analyze_sales(sales)
print("\nUser Function Output:", result)

