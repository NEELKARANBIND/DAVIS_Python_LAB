# Function to calculate compound interest
def compound_interest(principal, rate, time, n):
    # Convert rate from percentage to decimal
    rate_decimal = rate / 100
    # Calculate compound interest
    amount = principal * (1 + rate_decimal / n) ** (n * time)
    return amount
# Example usage
principal_amount = 1000  # Principal amount in dollars
annual_rate = 5          # Annual interest rate in percentage
time_years = 10         # Time in years
compounding_frequency = 4 # Compounded quarterly
final_amount = compound_interest(principal_amount, annual_rate, time_years, compounding_frequency)
print(f"The amount after {time_years} years is: ${final_amount:.2f}")
