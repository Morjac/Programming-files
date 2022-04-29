# py checkpoint5.py

#1st problem
first_num = float(input('What is the first number? '))
sec_num = float(input('What is the second number? '))
print()

if first_num > sec_num:
    print('The first number is greater')
    print('The numbers are not equal')
    print('The second number is not greater')
elif first_num == sec_num:
    print('The first number is not greater')
    print('The numbers are equal')
    print('The second number is not greater')
elif first_num < sec_num:
    print('The first number is not greater')
    print('The numbers are not equal')
    print('The second number is greater')
print()

#favorite animal
fav_ani = input('What is your favorite animal? ')

if fav_ani.lower() == 'mongoose':
    print('A real animal Bert')
if fav_ani.lower() == 'cobra':
    print("That's badass, just like me")
else:
    print('Kinda lame if you ask me')