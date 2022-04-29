from calendar import weekday
from datetime import datetime

#current_time = datetime.now()

#current_weekday = current_time.weekday()

#if current_weekday == 0:
    #print("monday")
#elif current_weekday == 3:
    
#print(current_time)
#print(current_weekday)

subtotal = float(input("Please enter the subtotal: "))

sales_tax_amount = (subtotal * .06)


total = subtotal + sales_tax_amount

print(f"sales_tax_amount: {sales_tax_amount:.2f}")
print(total)




