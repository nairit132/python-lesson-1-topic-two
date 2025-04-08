print(" Select your ride:")
print("1. Car")
print("2 . bike")
choice = int(input("Enter your type, one or two:"))
if (choice == 1):
    print("what type of bike")
    print("1. Scooter\n")
    print("2. Scooty\n")
    choice2=int(input("Which type of bike?"))
    if choice2 == 1:
        print("you have selected scooter")
    else:
        print("You have selected scooty")
elif( choice == 2):
    print("What type of car?")
    print("1.Sedan")
    print("2.XUV")
    choice3 = int(input("Enter your choice: "))
    if choice3==1:
        print("You havw selected Sedan")
        print("You have selected XUV")
else:
    print("wrong choice! Select one of two options")