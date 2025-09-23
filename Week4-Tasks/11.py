nums = [int()]*10

for i in range(10):
    nums[i] = int(input(f"Please Enter the number {i + 1} number: "))

total = 0
for j in range(10):
    total = total + nums[j]

for k in range(10):
    print(f"{nums[k]}")

print(f"The total is {total}")
