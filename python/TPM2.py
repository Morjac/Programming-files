# py tpm.py
print()
print('The Patriarchs Manuscript, the cheesy rip-off game of "The Elders Scrolls"')
print()

# Welcome
print("Gasp... the nightmares, they are finally over \nYou sit yourself up and notice that you're in a dimly light, cold, empty cell not understanding why you're in here.") 
print("After looking around you notice a small WINDOW in which whatever little sunlight leaks in \nand the iron gate DOOR keeping you in is rusting away")
print('"Well, I dont want to stay here for much longer..."')
print()

# First_decision
first_dec = input("Do you try to break down the DOOR, reach the WINDOW, or STAY and let your nightmares consume you? ")
print('------------------------------------------')
if first_dec.lower() == 'door':
    print("Boom...Boom...Boom... Although weak and frail the rusted door cant handle the consistent force of you blows and falls over \ngrrrrrmmmmm.... you stomach growls louder than any earthly beast you have ever heard")

elif first_dec.lower() == 'window':
    print("After multiple attempts you accept that the window is out of reach")
    first_dec_2 = input('After realizing you dont reach do you prefer to STAY or attempt to break the DOOR? ')    
    
    if first_dec_2.lower() == 'door':
        print("Boom...Boom...Boom... Although weak and frail the rusted door cant handle the consistent force of you blows and falls over \ngrrrrrmmmmm.... you stomach growls louder than any earthly beast you have ever heard")
    
    elif first_dec.lower() == 'stay':
        print('Fear of the unknown overcomes you and you coward back into the corner in which you were, \nyou try to convince yourself that the nightmare you know is better than the one you dont...')
        print('your weakened body falls victim to hunger and the elements')
    
    else:
        print("That's not going to help right now")

elif first_dec.lower() == 'stay':
    print('Fear of the unknown overcomes you and you coward back into the corner in which you were, \nyou try to convince yourself that the nightmare you know is better than the one you dont...')
    print('your weakened body falls victim to hunger and the elements')
    

else:
    print("That's not going to help right now")

print()
print('As you stumble to get up you see a long hallway with multiple cells on either side, \nas you tread forward you behold that every cell is either empty, destroyed and/or occupied by a long deceased being')
print('"What in heavens blazes happened here?" You murmur')
print('------------------------------------------')
sec_dec = input('You reach two stairways that go upward, do you take the dark stairway on the LEFT or the well lit stairs on the RIGHT? ')
print()

if sec_dec.lower() == 'left':
    print('As you make your way up the dark stairway, occasionaly tripping, you start to feel a strong odor that becomes even more overwhelming as you continue your climb')
    sec_dec_1 = input('You begin to see light and feel warmth and soon find yourself in front of a wooden door and hear voices, do you BARGE IN or do you KNOCK? ')
    print()
    if sec_dec_1.lower() == 'barge in':
        print('You ruthlessly shove the door open knocking an old man onto the ground, \nsimultaneously a larger man, maybe a cook considering his appearal, turns around and shouts "What the..." as he grabs his large cleaver')
        print('You apologize immediately, knowing you are in no condition to start a quarrel as you help the older gentleman back on his feet')
        print('"A thousand pardons sir. It was never my intention to knock you down." you say. "And I never expected you to get up" he responds. \n"Yes, Ive seen you in the cell down below. At first I believed you to be dead but your body never seemed to rot')
        print('"Time to pay up" says the larger man. The older gentleman grudgingly tosses the cook what appears to be a coin')
        print('"Where am I?" you ask. \n"In Ravenhall Castle or whats left after the war... \nHow long have you been down there?" he asks')
        print('"I wish I knew" to which he responds "Well then... you will wish you stayed asleep after knowing what you woke to" \nafter chatting for a while and an extremly questionable meal you decide to rest near the warmth of the fire knowing that you know nothing about this new world ')
    elif sec_dec_1.lower() == 'knock':
        print()