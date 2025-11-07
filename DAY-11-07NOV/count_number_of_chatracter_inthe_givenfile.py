# Count the number of characters in the given file
fileobj = open(r"C:\Users\NEEL KARAN BIND\OneDrive\Desktop\DAVIS_PYTHON_LAB\file1.txt", "r")
data = fileobj.read()
char_count = len(data)
print("Number of characters in the file:", char_count)
fileobj.close()
