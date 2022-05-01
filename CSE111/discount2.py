# Get the day of the week
from datetime import datetime 
current_day_of_week = datetime.now().weekday()

# Ask for the subtotal amount
subtotal = float(input("Please enter the subtotal: "))

# If it's Tue or Wed we'll give a 10% discount
if current_day_of_week in (1, 4) and subtotal >= 50:
    with_sale = (subtotal * .10)
    subtotal = subtotal - with_sale
    print(f"Discount: {with_sale:.2f}")

# Compute and print the sales tax
sales_tax_amount = (subtotal * .06)
print(f"sales_tax_amount: {sales_tax_amount:.2f}")

# Compute and print the total
total = subtotal + sales_tax_amount
print(f"Total: {total:.2f}")