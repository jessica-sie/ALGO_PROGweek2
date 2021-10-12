S1 = eval(input("edge1:"))
S2 = eval(input("edge2:"))
S3 = eval(input("edge3:"))

if S1+ S2 > S3 and S1+S3 > S2 and S2+S3 > S1:
    print("perimeter:", S1+S2+S3)
else:
    print("peimeter cannot be calculated: input is invalid")


