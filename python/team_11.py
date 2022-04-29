# py team_11.py

with open("hr_system.txt") as hr_file:
    #print(hr_file)
    
    for hr in hr_file:
        hr_part = hr.split()

        name = hr_part[0]
        id = hr_part[1]
        title = hr_part[2]
        salary = float(hr_part[3])

        paycheck = salary/24

        
        print(f'Name:{name} (ID: #{id}), Title: {title} \nSalary: ${salary:.2f} Paycheck: ${paycheck:.2f}')
        
        if title.lower() == 'engineer':
            paycheck_bonus = paycheck + 1000
            print(f'Paycheck bonus: ${paycheck_bonus:.2f}')
        print()
       
            