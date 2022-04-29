def calculate_wind_chill(temperature, wind_speed):
    return(35.74 + (0.6215 * temperature) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * temperature * (wind_speed** 0.16)))

def celsius_to_fahrenheit(temperature):
    return (temperature * (9/5)) + 32

temperature = float(input("What is the temperature?"))
wich_temperature = input("Fahrenheit or Celcius (F/C)")

if wich_temperature.upper() == "F":
    temperature = celsius_to_fahrenheit(temperature)

for i in range(5, 61, 5):
    wind_speed = i
    windchill = calculate_wind_chill(temperature, wind_speed)
    print(f"{i} {windchill}")