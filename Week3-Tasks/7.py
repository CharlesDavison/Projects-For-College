names = [str()]*5
for i in range(5):
    names[i] = input("Please Enter A Name For The Football Team: ")

print("--------------------------------------------")
print("Here Is Your Team")

for j in range(5):
    print(f"{j}: {names[j]}")

print("--------------------------------------------")
