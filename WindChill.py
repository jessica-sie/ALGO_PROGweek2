import math

temp = float(input("temperature (in Fahrenheit):"))
# input validation
while temp < -58 or temp > 41:
    print("Temperature must be between -58F and 41F")
    temp = float(input("temperature (in Fahrenheit):"))

v = float(input("windchill (mph): "))
# input validation
while v < 2:
    print("Speed must be greater than or equal to 2")
    v = float(input("windchill (mph): "))

windchillTemp = 35.74 + (0.6215 * temp) - 35.75 * math.pow(v, 0.16) + 0.4275 * temp * math.pow(v, 0.16)

print("the wind chill index is {:.3f}".format(windchillTemp))
