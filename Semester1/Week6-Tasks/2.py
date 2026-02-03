def ageCheck(age:int) -> int:
    if age >= 18:
        print("You are old enough to get into nightclubs.")
    else:
        print("You are not old enough to get into nightclubs.")

    return 0

ageCheck(int(input("Please Enter Your Age: ")))
