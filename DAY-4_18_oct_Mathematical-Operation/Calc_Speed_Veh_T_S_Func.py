# Function to calculate speed of a vehicle whose time and distance are given by functions
def distance(t):
    # Example distance function: d = 5 * t^2 (distance in meters)
    return 5 * t ** 2 
def time(t):
    # Example time function: t = t (time in seconds)
    return t    
def speed(t):
    # Speed = distance / time
    d = distance(t)
    ti = time(t)
    if ti == 0:
        return 0
    return d / ti
# Input from the user
time_input = float(input("Enter the time in seconds: "))
print("Speed of the vehicle:", speed(time_input), "m/s")  
