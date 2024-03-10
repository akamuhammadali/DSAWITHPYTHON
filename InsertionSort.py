def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# Input the list of numbers from the user
num_list = []
n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    num_list.append(num)

# Sort the list using Insertion Sort
insertion_sort(num_list)

# Print the sorted list
print("Sorted list in ascending order:")
for num in num_list:
    print(num, end=" ")
