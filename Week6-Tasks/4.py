message = "outside the function"  # global

def my_message():
    message = "inside the function"  # local
    print(message)

my_message()
print(message)
