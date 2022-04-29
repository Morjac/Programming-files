#questions
child_price = float(input("What is the price of a child's meal? "))
adult_price = float(input("What is the price of an Adult's meal? "))
child_num = int(input('How many children are there? '))
adult_num = int(input('How many adults are there? '))
drinks = float(input('What is the price for the drinks? '))
drinks_num = int(input('How many would you like? '))
ice_cream = float(input('What is the price for the ice cream? '))
ice_cream_num = int(input('How many would you like? '))
sales_tax_rate = float(input('What is the sales tax rate? '))
subtotal = float(child_price * child_num + adult_price * adult_num + drinks * drinks_num + ice_cream * ice_cream_num)
print()

#cost of food
print(f'Subtotal: ${subtotal:.2f}')
sales_tax = float(subtotal) * (float(sales_tax_rate) / 100)
print(f'Sales tax: ${sales_tax:.2f}')
total = subtotal + sales_tax
print(f'Total: ${total:.2f}')
print()
#payment amount
payment = float(input('What is your payment amount? '))
change = payment - total
print(f'Change: ${change:.2f}')