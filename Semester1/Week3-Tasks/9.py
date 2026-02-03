import datetime;

dayOfWeek = datetime.datetime.today().weekday();

if dayOfWeek in range(3, 4):
        print("Soon it is the weekend!");
    
elif dayOfWeek in range(5, 6):
        print("It is the weekend!");

elif dayOfWeek in range(0, 2):
        print("Looking forward to the weekend!");
