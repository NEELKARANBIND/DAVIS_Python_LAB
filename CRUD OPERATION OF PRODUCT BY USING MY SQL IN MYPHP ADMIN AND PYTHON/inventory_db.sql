-- Create database (optional)
CREATE DATABASE IF NOT EXISTS inventory_db;
USE inventory_db;

-- Create products table
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL,
    category VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert some sample data (optional)
INSERT INTO products (name, description, price, quantity, category) VALUES
('Laptop', 'High-performance gaming laptop', 1299.99, 15, 'Electronics'),
('Wireless Mouse', 'Ergonomic wireless mouse', 29.99, 100, 'Accessories'),
('USB Cable', 'USB-C Fast Charging Cable', 9.99, 200, 'Accessories');