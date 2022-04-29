# py windchill_calc.py
def windchill_cal(temp, wind):
    return (35.74 + (0.6215 * temp) - (35.75 * (wind ** 0.16)) + (0.4275 * temp * (wind** 0.16)))

def convert_temp(temp):
    return (temp * (9/5)) + 32

temp = float(input('What is the temperature? '))
f_or_c = input('Fahrenheit or Celcius (F/C)? ')



for speed in range(5,61,5):

    if f_or_c.lower() == "c":
        temp1 = convert_temp(temp)
        windchill = windchill_cal(temp1, speed)


    else:   
        windchill = windchill_cal(temp, speed)
        temp1 = temp
    
    print(f'At temperature {temp1}F, and wind speed {speed} mph, the windchill is: {windchill:.2f}F')