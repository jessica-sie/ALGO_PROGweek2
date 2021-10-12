x1 = float(input("first x-coordinate:"))
y1 = float(input("first y-coordinate:"))
#why cannot use float? can koq?

x2 = float(input("second x-coordinate:"))
y2 = float(input("second y-coordinate"))

slope = '{:.5f}'.format((y2-y1)/(x2-x1))

print("the slope of the line that connects 2 points (", x1,  ",", y1, ") and (", x2, ",", y2, ") is", slope)
