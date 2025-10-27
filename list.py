# Creating a blank list for 5 subjects
data = []
print("Enter 5 subjects with marks:")
for i in range(5):
    # Input subject name
    subject = input(f"Enter subject {i+1}: ")
    
    # Input number from user
    num = int(input(f"Enter marks for {subject}: "))
    
    # Check for individual mark conditions
    if num < 50:
        print(f"Fail for {subject}")
    elif num > 85:
        print(f"Out of range marks for {subject}")
    
    # Append regardless
    data.append([subject, num])

# Displaying the subjects and marks
print("Subjects and Marks:")
for i in range(5):
    print(f"{data[i][0]}: {data[i][1]}")
# Calculating the subjects marks
total = 0
for j in data:
    total = total + j[1]
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