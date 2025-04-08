units = int(input("Place the amount of units you have consumed"))
if (units < 50):
    amount = units * 2.60
    supercharge = 25
elif(units <= 100):
    amount = 130 +((units -50) * 3.25)
    supercharge = 35
elif(units <= 200):
    amount = 130 + 162.50  +((units -100) * 5.26)
    supercharge = 45
else:
    amount = 130 + 162.50 + 526 ((units -200) * 8.45)
    supercharge = 75
    total = amount + supercharge
    print("\nElctricity Bill = %.2f" %total)