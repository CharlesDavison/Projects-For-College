def printName() -> int:
    print(f"Hello, {input("Please Enter Your Name: ")}")

    return 0

def twoNumbers():
    print(f"The total of the two numbers you entered are: {int(input("Please Enter a number: ")) + int(input("Please Enter another Number: "))}")

    return 0

def closingMessage():
    print("Goodbye.")
    exit
    
    return 0

ans = input("Enter 1, 2 or 3: ").strip()

if ans not in ("1","2","3"):
    print("Input Doesn't Exist.")
    exit
else:
    match ans:
        case "1":
            printName()

        case "2":
            twoNumbers() 

        case "3":
            closingMessage()
