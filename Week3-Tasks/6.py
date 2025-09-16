gender = input("What is your gender? (Male, Female): ").upper()
units = int(input("Please Enter the amount of units of alcohol you have had: "))

if gender == "Male".upper():
    if units > 4:
        print("You are over the alcohol units limit for a male.")
    else:
        print("You are within the alcohol units limit.")
elif gender == "Female".upper():
    if units > 3:
        print("You are over the alcohol units limit for a male.")
    else:
        print("You are within the alcohol units limit.")
else:
    print("Please enter either Female, or Male: ")
