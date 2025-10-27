'''Create a reportcard . It must contain the name of five subjects along with marks obtained in them out of 100.
Then calculate the total marks obtained, percentage, grade.
Grade must be calculated as per below criteria :-
Percentage           Grade
 >=85                      A+
85 - 75                   A
75-65                     B
65 - 55                   C
55 - 50                  D
<50                         Fail   '''

'''# Report Card Generator
# This script generates a report card with 5 subjects inputted by the user.
# For each subject, it prompts for the name and marks (out of 100), but only accepts marks between 50 and 85 inclusive.
# Calculates total, percentage, and grade. Uses only lists.

# Lists to store subject names and marks
subjects = []
marks = []

print("=== Student Report Card ===")
print("Enter details for 5 subjects (marks must be 50-85):")

for i in range(5):
    # Input subject name
    subject = input(f"Subject {i+1} name: ")
    subjects.append(subject)
    
    # Input mark with range check (re-prompt if invalid)
    while True:
        mark = int(input(f"Marks for {subject} (50-85): "))
        if 50 <= mark <= 85:
            marks.append(mark)
            break
        else:
            print("Invalid: Marks must be between 50 and 85. Try again.")

# Calculate total marks
total_marks = 0
for j in marks:
    total_marks = total_marks + j

# Calculate percentage (total out of 500)
percentage = (total_marks / 500) * 100

# Determine grade based on criteria
if percentage >= 85:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 65:
    grade = "B"
elif percentage >= 55:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

# Display the report card
print("\n" + "="*50)
print("STUDENT REPORT CARD")
print("="*50)
for i in range(5):
    print(f"{subjects[i]:15}: {marks[i]}/100")
print("-"*50)
print(f"Total Marks: {total_marks}/500")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print("="*50) '''

# Creating a blank list for 5 subjects
subjects = []
Marks = []
print("Enter 5 subjects with marks (marks >50 and <85):")
for i in range(5):
    # Input subject name
    subject = input(f"Enter subject {i+1}: ")
    subjects.append(subject)
    
    # Input number from user with validation
    while True:
        num = int(input(f"Enter marks for {subject}: "))
        if num > 50 and num < 85:
            Marks.append(num)
            break
        else:
            print("Invalid: Marks must be greater than 50 and less than 85. Try again.")

# Displaying the subjects and marks
print("Subjects and Marks:")
for i in range(5):
    print(f"{subjects[i]}: {Marks[i]}")
# Calculating the subjects marks
total = 0
for j in Marks:
    total = total + j
print("Total marks of 5 subjects is :", total)
# Calculating the percentage
percentage = (total / 500) * 100
# Displaying the percentage
print("Percentage of 5 subjects is :", percentage)
# For grading
if percentage >= 85:
    # Display for grade A+
    print("Grade A+")
elif percentage >= 75:
    # Display for grade A
    print("Grade A")
elif percentage >= 65:
    # Display for grade B
    print("Grade B")
elif percentage >= 55:
    # Display for grade C
    print("Grade C")
elif percentage >= 50:
    # Display for grade D
    print("Grade D")
else:
    # Display for grade Fail
    print("Grade F")