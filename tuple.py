# Program to create a list from user input, remove a specified value if present, and print the updated list

# Creating a blank list
my_list = []
print("Enter the number of elements in the list:")
n = int(input())

print("Enter the elements one by one:")
for i in range(n):
    element = int(input())
    my_list.append(element)

print("Original list:", my_list)

# Take input for value to remove
print("Enter the value to remove:")
value = int(input())

# Check if value is present and remove the first occurrence
if value in my_list:
    my_list.remove(value)
    print("List after removing the value:", my_list)
else:
    print("Value not found in the list. List remains:", my_list)