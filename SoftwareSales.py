qtty = int(input("number of packages purchased:"))

if qtty < 10:
    print("discount amount @ 0%: $0.00")
    print("total amount: $", "{:.2f}".format(qtty*99))
elif qtty <= 19:
    disc = qtty*99 * (10/100)
    print("discount amount @ 10%: $", "{:.2f}".format(disc))
    print("total amount: $", "{:.2f}".format((qtty*99) - disc))
elif qtty <= 49:
    disc = qtty * 99 * (20/100)
    print("discount amount @ 20%: $", "{:.2f}".format(disc))
    print("total amount: $", "{:.2f}".format(qtty*99*(80/100)))
elif qtty <= 99:
    disc = qtty * 99 * (30/100)
    print("discount amount @ 30%: $", "{:.2f}".format(disc))
    print("total amount: $", "{:.2f}".format(qtty*99*(70/100)))
else:
    disc = qtty * 99 * (40/100)
    print("discount amount @ 40%: $", "{:.2f}".format(disc))
    print("total amount: $", "{:.2f}".format(qtty*99*(60/100)))

