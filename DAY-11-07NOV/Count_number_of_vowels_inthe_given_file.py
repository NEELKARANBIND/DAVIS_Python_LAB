# conunt the number of vowels in the given file
fileobj = open(r"C:\Users\NEEL KARAN BIND\OneDrive\Desktop\DAVIS_PYTHON_LAB\file1.txt", "r")
data = fileobj.read()
vowels = "aeiouAEIOU"
count = 0
for char in data:
    if char in vowels:
        count += 1
print("Number of vowels in the file:", count)
fileobj.close()