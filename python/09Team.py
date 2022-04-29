Numbers = []

Enter_Number = None
Sumar = 0
Average = 0
maximum = 0
minimum = 0


print ("Enter a list of numbers, Type 0 When it's done!") 
print ()

while Enter_Number != 0 :
    Enter_Number = float(input("Enter a number: "))
    
    if Enter_Number != 0 :
        Numbers.append(Enter_Number)

for Number in Numbers :
    Sumar = sum(Numbers)
    Average = sum(Numbers) / len(Numbers)
    maximum = max(Numbers)
    minimum = min(Numbers)    
    Pminimum = min([i for i in Numbers if i > 0])    

print(f"The Sum of the Numbers is: {Sumar:.2f}")
print(f"The Average Number is: {Average:.2f}")
print(f"The Largest Number is: {maximum:.2f}")
print(f"The Lowest Number is: {minimum:.2f}")
print(f"The Smallest Positive Number is: {Pminimum:.2f}")
print('')

print(f"The Sorted List is: ")
sorted_numbers = sorted(Numbers)

for number in sorted_numbers:
    print(number)
