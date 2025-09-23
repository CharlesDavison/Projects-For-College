items = [str()]*5
longestWord = 0
longestWordCharCount = 0

for i in range(5):
    items[i] = input(f"Please Enter The number {i + 1} item: ")

for l in range(5):
    if len(items[l]) > longestWordCharCount:
        longestWordCharCount = len(items[l])
        longestWord = l

print("-" * (longestWordCharCount + 8))
for j in range(5):
    print(f"{j + 1}: {items[j].ljust(longestWordCharCount + 4)}|")
print("-" * (longestWordCharCount + 8))
