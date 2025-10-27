# module Numerical Calculations functions 
#Addition of two numbers
def add(a, b):
    # Return the sum of a and b
    return a + b

#Subtraction of two numbers
def subtract(a, b):
    # Return the difference of a and b
    return a - b
#Multiplication of two numbers
def multiply(a, b):
    # Return the product of a and b
    return a * b

#Division of two numbers
def divide(a, b):
    # Return the quotient of a and b
    if b == 0:
        return "Error! Division by zero."
    return a / b
#Exponentiation of two numbers
def power(a, b):
    # Return a raised to the power of b
    return a ** b

#Modulus of two numbers
def modulus(a, b):
    # Return the remainder of a divided by b
    return a % b

# Floor division of two numbers
def floor_divide(a, b):
    # Return the floor division of a by b
    if b == 0:
        # Handle division by zero
        return "Error! Division by zero."
    return a // b

# Square root of a number
def square_root(a):
    # Return the square root of a
    if a < 0:
        # Handle negative input
        return "Error! Cannot compute square root of negative number."
    return a ** 0.5

# Calculate percentage
def percentage(part, whole):
    # Return the percentage of part with respect to whole
    if whole == 0:
        return "Error! Division by zero."
    return (part / whole) * 100

# Calculate average of a list of numbers
def average(numbers):
    # Return the average of a list of numbers
    if len(numbers) == 0:
        return "Error! No numbers provided."
    return sum(numbers) / len(numbers)

# Calculate factorial of a number
def factorial(n):
    # Return the factorial of n
    if n < 0:
        return "Error! Factorial of negative number not defined."
    # Base case
    if n == 0 or n == 1:
        return 1
    result = 1
    # Calculate factorial iteratively
    for i in range(2, n + 1):
        result *= i
    return result

# Calculate greatest common divisor (GCD) of two numbers
def gcd(a, b):
    # Return the GCD of a and b
    while b:
        a, b = b, a % b
    return a

# Calculate least common multiple (LCM) of two numbers
def lcm(a, b):
    # Return the LCM of a and b
    if a == 0 or b == 0:
        return "Error! LCM of zero not defined."
    return abs(a * b) // gcd(a, b)


# Check if a number is prime
def is_prime(n):
    # Return True if n is prime, else False
    if n <= 1:
        return False
    # Check for factors from 2 to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        # If i is a factor of n, then n is not prime
        if n % i == 0:
            return False
    return True

# Find all prime factors of a number
def prime_factors(n):
    # Return a list of prime factors of n
    factors = []
    for i in range(2, n + 1):
        # Check if i is a factor of n
        while n % i == 0:
            factors.append(i)
            n //= i
            # Continue dividing n by i
    return factors
# Fibonacci sequence
def fibonacci(n):
    # Generate Fibonacci sequence up to n terms
    fib_sequence = []
    # Initial two terms
    a, b = 0, 1
    # Generate terms
    for _ in range(n):
        # Append current term to the sequence
        fib_sequence.append(a)
        a, b = b, a + b
        # Update to next terms
    return fib_sequence
