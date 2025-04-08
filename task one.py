medical_cause = input("Do you have a medical cause? Yes or No?")
atten = int(input("Enter attendance of the student :"))
if medical_cause == 'Y':
    print("you are allowed")
else:
    if atten>= 75:
        print(("allowed"))
    else:
        print("not allowed")