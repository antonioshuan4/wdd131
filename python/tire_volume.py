from datetime import datetime
import math

# Get the current date and time
current_date_and_time = datetime.now()

# Ask the user for tire dimensions
width = float(input("Enter the width of the tire in mm (ex 205): "))
ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate the approximate tire volume
volume = (math.pi * width**2 * ratio * (width * ratio + 2540 * diameter) / 10000000000)

# Display the result
print(f"the approximate volume is {volume:.2f} liters")

# Save the information in the volumes file
with open("volumes.txt", mode="at") as volumes_file:
    print(f"{current_date_and_time:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume:.2f}", file=volumes_file)

print("Thank you for using the Tire Volume Calculator!")