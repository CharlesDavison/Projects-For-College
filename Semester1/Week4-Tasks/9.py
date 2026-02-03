items = [str()]*5

for i in range(5):
    items[i] = input(f"Please Enter The number {i + 1} item: ")

print("----------------------------------")
for j in range(5):
    print(f"{j + 1}: {items[j]}")
print("----------------------------------")
