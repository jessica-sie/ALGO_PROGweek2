sub = float(input("enter the subtotal $"))
percent = float(input("enter the tip amount (as a %)"))


tip = sub * (percent/100)


sub2 = '{:.2f}'.format(sub)
tip2 = '{:.2f}'.format(tip)
tot2 = '{:.2f}'.format(tip+sub)


print("Subtotal: $", sub2)
print("tip $", tip2)
print("total $", tot2)

