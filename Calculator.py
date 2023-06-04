def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Simple Calculator Program")
print("-------------------------")
print("Operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("-------------------------")

choice = input("Enter the operation (1-4): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == '1':
    result = add(num1, num2)
    print("Result: ", result)
elif choice == '2':
    result = subtract(num1, num2)
    print("Result: ", result)
elif choice == '3':
    result = multiply(num1, num2)
    print("Result: ", result)
elif choice == '4':
    if num2 != 0:
        result = divide(num1, num2)
        print("Result: ", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice. Please enter a number between 1 and 4.")
