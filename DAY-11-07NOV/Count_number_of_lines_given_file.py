# Count the number of lines in the given file
fileobj = open(r"C:\Users\NEEL KARAN BIND\OneDrive\Desktop\DAVIS_PYTHON_LAB\file1.txt", "r")
lines = fileobj.readlines()
line_count = len(lines)
print("Number of lines in the file:", line_count)
fileobj.close()