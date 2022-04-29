max_life_exp = -1
min_life_exp = 9999
max_exp_year_of_int = -1
min_exp_year_of_int = 9999
counter = 0
total = 0


year_of_interest = int(input('Enter the year of interest: '))

with open('life-expectancy.csv') as life_exp_file:
    next(life_exp_file)
    for line in life_exp_file:
        line = line.strip()
        line = line.split(',')

# individual column info
        entity = str(line[0])
        code = str(line[1])
        year = int(line[2])
        avg_life_exp = float(line[3])

        # Overrall max and min. life expectancy for country and year, status: Working. DON'T TOUCH
        if avg_life_exp > max_life_exp:
            max_life_exp = avg_life_exp
            max_entity = entity
            max_year = year
    
        if avg_life_exp < min_life_exp:
            min_life_exp = avg_life_exp
            min_entity = entity
            min_year = year

    # SEARCH INFO FOR YEAR OF INTEREST
        if year == year_of_interest:
           
            if avg_life_exp < min_exp_year_of_int:
                    min_exp_year_of_int = avg_life_exp
                    min_entity_int = entity

            elif avg_life_exp > max_exp_year_of_int:
                    max_exp_year_of_int = avg_life_exp
                    max_entity_int = entity

            total += avg_life_exp
            counter += 1
            average = total / counter


    print(f'\nThe overall max life expectancy is: {max_life_exp:.2f} from {max_entity} in {max_year} \nThe overall min. life expectancy is: {min_life_exp:.2f} from {min_entity} in {min_year}')
    print(f'\nFor the year of {year_of_interest}:\nThe average life expectancy across all countries was: {average:.2f}\nThe max life expectancy was in {max_entity_int} with {max_exp_year_of_int:.2f}\nThe min life expectancy was in {min_entity_int} with {min_exp_year_of_int:.2f}')