"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

age = int(input("What is your age? "))
maximum_heart_rate = 220 - age

ideal_min = int(maximum_heart_rate * .65)
ideal_max = int(maximum_heart_rate * .85)

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {ideal_min} and {ideal_max} beats per minute.")
#print(age)
#print(maximum_heart_rate)
#print(ideal_min)

