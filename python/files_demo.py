# py files_demo.py
with open('test_file.txt') as test_file:
    for line in test_file:

        clean_line = line.split(',')
        #print(clean_line)
        #clean_line = ['Intro,6.72']['Matematica,9.85']['ingles,10']['Psicologia,9']

        #parts
        topic = clean_line[0] 
        grades = float(clean_line[1])

        bonus_grade = grades + 3

        print(f'{topic} - Grade:{grades} --- Bonus grade is {bonus_grade:.2f}')