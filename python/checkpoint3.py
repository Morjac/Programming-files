#age- tested and working
user_age = input('How old are you? ')
nxt_bday =(int(user_age) + 1)
print('On your next b-day you will be ' + str(nxt_bday))
print()

#eggs-tested and working
cartons = input('How many egg cartons do you have? ')
total_eggs = (int(cartons)*12)
print ('You have ' + str(total_eggs) + ' eggs')
print()

#cookies
cookies = input('How many cookies do you have? ')
people = input('How many people are there? ')
result = float(cookies)/float(people)
print('Each person may have ' + str(result) + ' cookies.')