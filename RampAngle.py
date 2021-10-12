import math
m = eval(input("mass (Kg):"))
F = eval(input("force (N):"))


ACC = 9.8

theta = math.asin(F/(m*ACC))
degrees = "{:.1f}".format(math.degrees(theta))
print("the angle of the ramp is", degrees, "degrees")
