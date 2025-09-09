foods = [str()] * 3

for i in range(3):
    foods[i] = input(f"Enter your number {i + 1} favourite food: ")

for j in range(len(foods)):
    print(f"{j+1}: {foods[j]}")
