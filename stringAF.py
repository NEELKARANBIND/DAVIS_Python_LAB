'''str = "Neel"
print(str.isalpha()) 
#True if all characters in the string are alphabetic
str1 = "Neel123"
print(str1.isalpha()) -------------

str2 = "12345"
print(str2.isdigit())
#True if all characters in the string are digits
----------------
str3 = "Neel123"
print(str3.isalnum())
------------------------
#True if all characters in the string are alphanumeric

str4 = "   "
print(str4.isspace())   
#True if all characters in the string are whitespaces
----------------
str5 = "Hello World"
print(str5.islower())

#True if all characters in the string are lowercase
-------------
str6 = "hello world"
print(str6.isupper())
#True if all characters in the string are uppercase
----------------
str7 = "Hello World"
print(str7.istitle())   
#True if the string follows the rules of a title
----------------
str8 = "Hello World"
print(str8.startswith("Hello"))
#True if the string starts with the specified prefix 
------------------
Que. Write a Python program to count the number of alphabets in a sentence entered by the user.

sentencre = input("Enter a sentence: ")
#initializing number of alphabets as 0
alphabets = 0
#Extracting each character from the sentence
for x in sentencre:
    #Checking if the character is an alphabet
    if (x.isalpha()):
        alphabets += 1
#Printing the number of alphabets
print("Number of alphabets in the sentence:", alphabets)
-----------------

sentence = input("Enter a sentence: ")
# initializing number of alphabets as 0
alphabets = 0
# Extracting each character upper case from the sentence                            
for x in sentence:
    # Checking if the character is an alphabet
    if (x.isupper()):
        alphabets += 1
# Printing the number of alphabets  
print("Number of upper case alphabets in the sentence:", alphabets)
--------------------

sentence = input("Enter a sentence: ")
# initializing number of alphabets as 0
alphabets = 0
# Extracting each character vowels  from the sentence
for x in sentence:
    # Checking if the character is an alphabet
    if (x in 'aeiouAEIOU'):
        alphabets += 1
# Printing the number of alphabets  
print("Number of vowels in the sentence:", alphabets)   


'''
sentence = input("Enter a sentence: ")
# initializing number of alphabets as 0     
alphabets = 0   
# Extracting each character  frequency the sentence
for x in sentence:
    # Checking if the character is an alphabet
 if x in 'aeiouAEIOU':
        
        alphabets += 1
        print(x, " frequency:", alphabets)