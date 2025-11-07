# a program to create  a list of 10 numbers given by user and display 2nd and 3rd greatest value without sorting

# Creating an empty list to store numbers
numbers = []
# Taking input from user
print("Enter 10 numbers:")
for i in range(10):
    num = int(input())
    # Appending the number to the list
    numbers.append(num)

# Finding 2nd and 3rd greatest values without sorting
first = second = third = float()

for n in numbers:
    if n > first:
        third = second
        second = first
        first = n
    elif n > second:
        third = second
        second = n
    elif n > third:
        third = n
# Displaying the results FOR 2ND  GREATEST VALUE
print(f"2nd greatest value: {second}")
# Displaying the results FOR 3RD GREATEST VALUE
print(f"3rd greatest value: {third}")