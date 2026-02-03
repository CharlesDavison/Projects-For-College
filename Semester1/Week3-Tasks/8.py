import datetime

dayOfWeek = datetime.datetime.today().weekday()

match dayOfWeek:
    case 0:
        print("Today is a Monday")

    case 1:
        print("Today is a Tuesday")

    case 2:
        print("Today is a Wednesday")

    case 3:
        print("Today is a Thursday")

    case 4:
        print("Today is a Friday")

    case 5:
        print("Today is a Saturday")

    case 6:
        print("Today is a Sunday")

