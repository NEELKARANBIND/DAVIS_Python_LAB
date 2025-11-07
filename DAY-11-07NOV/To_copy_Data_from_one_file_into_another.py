
# A program in Python to copy data from one file to another file

# Open the source file in read mode
fileobj = open(r"C:\Users\NEEL KARAN BIND\OneDrive\Desktop\DAVIS_PYTHON_LAB\file1.txt", "r")
data = fileobj.read()

if len(data) > 0:
    print("Data read from file1.txt:")
    print(data)

fileobj.close()

# Open the destination file in write mode
fileobj = open(r"C:\Users\NEEL KARAN BIND\OneDrive\Desktop\DAVIS_PYTHON_LAB\file2.txt", "w")
fileobj.write(data)
fileobj.close()
print("Data copied successfully from file1.txt to file2.txt")
