# creating a blank list
list = []
print("Enter 10 numbers:")
for i in range (10):
    #input number from user
    num = int(input())
    #append number to list
    print("----------------------")
    list.append(num)
    #displaying the list
    print("list is :",list)
    #calculating the sum of list
    sum = 0
    for j in list:
        sum = sum + j
    #calculating the average    
    avg = sum / len(list)
    print("Average of 10 numbers is :",avg)
        