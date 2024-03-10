# Input student details
name = input("Enter student name: ")
roll_number = input("Enter roll number: ")
subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))

# Calculate total marks and average
total_marks = subject1 + subject2 + subject3
average = total_marks / 3

# Print the marksheet
print("\n-------- Marksheet --------")
print("Name:", name)
print("Roll Number:", roll_number)
print("Subject 1:", subject1)
print("Subject 2:", subject2)
print("Subject 3:", subject3)
print("Total Marks:", total_marks)
print("Average Marks:", average)
print("---------------------------")
