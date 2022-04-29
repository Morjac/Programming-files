# py checkpoint12.py
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Jacob 10"
]

#variable name for youngest person & age
youngest_age = 9999
youngest_person = ''

for line in people:
    #lines are split (name,age)
    line = line.split()
    
    #name and age each have own variable in list
    name = line[0]
    age = int(line[1])   
   
#for each line of info in list(person, age) check if {age} is smaller than {youngest_age}, if it is that age becomes the new {youngest_age} and the {name} of said person in that line becomes the {youngest_person}
for line in people:
    if age < youngest_age:
        youngest_age = age
        youngest_person = name


print(f'The youngest person is {youngest_person}')
