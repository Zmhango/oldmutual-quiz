import time  # Used to measure how long the sort takes

# Function that sorts the list using Bubble Sort
def bubble_sort(numbers):
    comparisons = 0
    swaps = 0
    n = len(numbers)

    for i in range(n):
        for j in range(n - i - 1):
            comparisons += 1
            if numbers[j] > numbers[j + 1]:
                # Swap the two numbers
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swaps += 1
        print(f"Pass {i + 1}: {numbers}")

    return comparisons, swaps

# Main program
print("===== BUBBLE SORT ALGORITHM =====")

# Ask the user to enter numbers
user_input = input("Enter numbers separated by spaces: ")

# Convert the input into a list of integers
try:
    numbers = list(map(int, user_input.strip().split()))
except ValueError:
    print("Invalid input. Please enter numbers only.")
    exit()

original = numbers.copy()  # Save original for comparison

# Show the original list
print(f"\nOriginal array: {numbers}")

# Start timer for bubble sort
start = time.time()
comparisons, swaps = bubble_sort(numbers)
end = time.time()
bubble_time = round(end - start, 5)

# Show sorted list and stats
print(f"\nFinal sorted array: {numbers}")
print(f"Total comparisons: {comparisons}")
print(f"Total swaps: {swaps}")
print(f"Time taken: {bubble_time} seconds")

# Compare with built-in sort
start_builtin = time.time()
sorted_builtin = sorted(original)
end_builtin = time.time()
builtin_time = round(end_builtin - start_builtin, 5)

print(f"\nBuilt-in sorted array: {sorted_builtin}")
print(f"Built-in sort time: {builtin_time} seconds")

if builtin_time > 0:
    slower = round(bubble_time / builtin_time, 2)
    print(f"Bubble sort is {slower}x slower than built-in sort.")
else:
    print("Built-in sort was too fast to measure.")
