import mysql.connector

# Connect to XAMPP MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",           # XAMPP has no password
    database="inventory_db"
)
cursor = conn.cursor()

# Create database and table (runs only once)
cursor.execute("CREATE DATABASE IF NOT EXISTS inventory_db")
cursor.execute("USE inventory_db")
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    quantity INT NOT NULL,
    category VARCHAR(50),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()

print("Welcome to Simple Product System!\n")

# Show all products
def view():
    cursor.execute("SELECT * FROM products ORDER BY id DESC")
    data = cursor.fetchall()
    
    if not data:
        print("No products yet!\n")
        return
    
    print("ID  NAME PRICE   QTY  CATEGORY  DATE")
    print("-" * 60)
    for p in data:
        print(f"{p[0]:<3} {p[1]:<20} {p[2]:<8} {p[3]:<4} {p[4]:<12} {p[5].date()}")
    print()

# Add product
def add():
    print("=== Add New Product ===")
    name = input("Name     : ")
    if name == "":
        print("Name required!\n")
        return
    price = float(input("Price    : "))
    qty = int(input("Quantity : "))
    cat = input("Category : ")
    
    cursor.execute("INSERT INTO products (name, price, quantity, category) VALUES (%s, %s, %s, %s)",
                   (name, price, qty, cat))
    conn.commit()
    print("Product Added!\n")

# Update product
def edit():
    view()
    id = int(input("Enter ID to update: "))
    name = input("New Name (press Enter to skip): ")
    price = input("New Price (press Enter to skip): ")
    qty = input("New Quantity (press Enter to skip): ")
    cat = input("New Category (press Enter to skip): ")
    
    if name: cursor.execute("UPDATE products SET name=%s WHERE id=%s", (name, id))
    if price: cursor.execute("UPDATE products SET price=%s WHERE id=%s", (float(price), id))
    if qty: cursor.execute("UPDATE products SET quantity=%s WHERE id=%s", (int(qty), id))
    if cat: cursor.execute("UPDATE products SET category=%s WHERE id=%s", (cat, id))
    
    conn.commit()
    print("Updated!\n")

# Delete product
def remove():
    view()
    id = int(input("Enter ID to delete: "))
    yes = input("Type 'yes' to delete: ")
    if yes == "yes":
        cursor.execute("DELETE FROM products WHERE id=%s", (id,))
        conn.commit()
        print("Deleted!\n")
    else:
        print("Cancelled\n")

# Main Menu - Very Simple
while True:
    print("1. View Products")
    print("2. Add Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")
    
    choice = input("\nChoose (1-5): ")
    
    if choice == "1":
        view()
    elif choice == "2":
        add()
    elif choice == "3":
        edit()
    elif choice == "4":
        remove()
    elif choice == "5":
        print("Thank You!")
        break
    else:
        print("Wrong choice!\n")
    
    input("Press Enter to continue...")
    
conn.close()