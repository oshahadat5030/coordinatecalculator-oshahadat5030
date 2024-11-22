##-------------------------------------------------------------------------------------
## Name:  CoordinateCalculator.py
## Description:  Converts geographic coordinates in DDMMSS format to DD
## Created:  11/22/2024
## Author:  Shahadat Hossain
##-------------------------------------------------------------------------------------

# Use the Python input function to prompt a user to enter a geographic coordinate in DDMMSS format (e.g., 391120).
x= input('Please enter a coordinate value in DDMMSS format:' )

#Step 2 - Determine the data type of x and print its value before moving forward.
print(f"Data type of x: {type(x)}")
print(f"Entered coordinate: {x}")

dd = int(x[:2])        # First two character are degrees
mm = int(x[2:4])       # Next two characters are minutes
ss = int(x[4:])        # Last two characters are seconds

# Convert to decimal degrees
decimal_degrees = dd + (mm / 60) + (ss / 3600)

#  Round the result to two decimal places
decimal_degrees_rounded = round(decimal_degrees, 3)

# Print the final result
print(f"Final result is: {decimal_degrees_rounded} degrees")
