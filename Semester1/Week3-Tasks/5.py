import random

chosenSubject = input("Please Enter your favourite subject in college: ")
array = ["Animation", "JavaScript"]

if chosenSubject.upper() not in ["ANIMATION", "JAVASCRIPT"]:
    print(f"Really? Wow. Lame. It should be {array[random.randint(0,1)]}.")
else:
    print("Really? That's my favourite too!")
