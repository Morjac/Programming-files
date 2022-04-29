def cel_temperature(temp, wind):
    return (35.74 + (0.6215 * temp) - (35.75 * (wind ** 0.16)) + (0.4275 * temp * (wind** 0.16)))

def far_temperature(temp):
    return (temp * (9/5)) + 32

temp = float(input("What is the temperature?"))
forc = input("Fahrenheit or Celcius (F/C)?")



for speed in range(5,61,5):

    if forc.lower() == "c":
        temp1 = far_temperature(temp)
        windchill = cel_temperature(temp1, speed)


    else:   
        windchill = cel_temperature(temp, speed)
        temp1 = temp
    
    print(f"At temperature {temp1}F,and wind speed {speed} mph, the windchill is: {windchill:.2f}F")