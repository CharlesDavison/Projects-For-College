def timesTable(number:int) -> int:
    for i in range(12 + 1):
        print(f"{number * i}")

    return 0

timesTable(int(input("Please Enter A Number: ")))
