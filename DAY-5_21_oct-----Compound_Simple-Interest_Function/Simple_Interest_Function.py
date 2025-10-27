# Function to calculate simple interest
def simple_interest(principal, rate, time):
    # Convert rate from percentage to decimal
    rate_decimal = rate / 100
    # Calculate simple interest
    interest = principal * rate_decimal * time
    return interest
# From user input
principal_amount = 1500  # Principal amount in dollars
annual_rate = 4          # Annual interest rate in percentage
time_years = 5           # Time in years        
interest_amount = simple_interest(principal_amount, annual_rate, time_years)
print(f"The simple interest for a principal amount of ${principal_amount} at an annual rate of {annual_rate}% over {time_years} years is: ${interest_amount:.2f}") 
