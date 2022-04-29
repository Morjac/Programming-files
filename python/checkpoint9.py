# py checkpoint.py
friends = []

friend = ''
while friend != 'end':
    friend = input('What is the name of our friend? ')
    if friend != 'end':
         friends.append(friend)

print()
print("Your friends are:")

for friend in friends:
    print(friend.capitalize())