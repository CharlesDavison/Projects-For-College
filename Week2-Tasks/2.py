wishlist = [str()]*5

for i in range(5):
    wishlist[i] = input(f"If you won the lottery, what would be the number {i + 1} thing you would buy? ")

print("Your wishlist: ")

for j in range(len(wishlist)):
    print(f"{j + 1}: {wishlist[j]}")
