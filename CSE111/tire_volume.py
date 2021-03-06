from cmath import pi
import math
from datetime import datetime
#print("math imported")

tire_width = int(input("Enter the width of the tire in mm (ex 205): "))
tire_aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
wheel_diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

tire_volume = (pi * (tire_width ** 2) * tire_aspect_ratio * (tire_width * tire_aspect_ratio + 2540 * wheel_diameter)) / 10000000000

print()
print(f"The aproximate volume in the tires is: {tire_volume:.2f} liters")

#date and time
current_date_and_time = datetime.now()
print(f"{current_date_and_time:%Y-%m-%d}")



with open("volumes.txt", "at") as volumes_file:
    print(current_date_and_time, file=volumes_file)
    print(f"{tire_width}, {tire_aspect_ratio}, {wheel_diameter},{tire_volume:.2f}")