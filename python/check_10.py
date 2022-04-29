# py check_10.py

print('\nPlease enter the items of the shopping list (type: quit to finish): ')

shopping_list=[]
item = None
#add items to shopping cart
print()
while item != 'quit':
    item = input('Item: ')

    if item != 'quit':
        shopping_list.append(item.capitalize())

#show items in cart
print()
print('The shopping list is:')
for item in shopping_list:
    print(item)

#show items in cart with index number
print('\nThe shopping list with indexes is:')
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")

#change item in cart
print()
index = int(input('Which item would you like to change? '))
new_item = input('What is the new item? ')
shopping_list[index] = new_item

print('\nThe shopping list with indexes is: ')
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")