message = "outside the function"  # global

def my_message() -> int:
    message = "inside the function"  # local
    print(message)

    return 0

my_message()
print(message)
