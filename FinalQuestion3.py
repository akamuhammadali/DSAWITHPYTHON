num_list = []

# Input data from the user
n = int(input("Enter the number of elements: "))

for i in range(n):
    num = float(input(f"Enter element {i+1}: "))
    num_list.append(num)

# Calculate sum
total_sum = sum(num_list)

# Calculate average
average = total_sum / n

# Find the smallest and largest value
smallest = min(num_list)
largest = max(num_list)

# Print the results
print("Sum:", total_sum)
print("Average:", average)
print("Smallest value:", smallest)
print("Largest value:", largest)
