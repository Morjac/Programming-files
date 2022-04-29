# py shopping_cart.py

items = []
prices = []
dash = '-'*40
action = None

print('\nWelcome to the Shopping Cart Program! \n \nPlease select one of the following: ')

while action != '5':
    print()
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item') 
    print('4. Compute total')
    print('5. Quit')
    action = input('\nPlease enter an action: ')

#Add item and price to their respective lists
    if action == '1':
        item = (input('\nWhat item would you like to add? '))
        price = float(input(f'What is the price of {item}? '))
        print(f'\n{item.capitalize()} has been added to your cart')
        print(dash)
        items.append(item.capitalize())
        prices.append(price)

#Inspect items in cart with index and respective price
    elif action == '2':
        print('\nThe items in the shopping cart are:')

        for i in range(len(items)):
            item = items[i]
            price = prices[i]
            print(f'{i+1}. {item} -'.ljust(15) + f'${price:.2f}')
        print(dash)
          
#Remove item from shopping cart
    elif action == '3':
        removed_item = int(input('\nWhich item would you like to remove? (Select index #): '))
        j = items.pop(removed_item - 1)
        j = prices.pop(removed_item - 1)
        print(f'The {removed_item} has been removed.')
        print(dash)

#Final Price
    elif action == '4' :
        total_price = sum(prices)
        print(f'\nThe total is: ${total_price:.2f}')
        print(dash)
              
print('Thank you, come again!')