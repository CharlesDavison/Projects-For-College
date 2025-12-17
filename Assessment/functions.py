# Define the size i want the array of structure to be as a constant. 
# This will cause the program to be more readable as I am not referencing any magic numbers.
SIZE = 5

# Calculate the total of all the products with the discount.
def total(products):
        TotalPrice = 0
        pricesLen = len(products)

        for i in range(pricesLen):
                TotalPrice += products[i]["Price"]

        return TotalPrice - products[pricesLen-1]["Price"]

# Sorts the products array by it's price.
def sort(products):
        n = len(products)

        sorted = False

        for i in range(0, n - 1):
                sorted = True

                for j in range(0, n - i - 1):
                        if products[j]["Price"] < products[j + 1]["Price"]:
                                products[j], products[j + 1] = products[j + 1], products[j]
                                sorted = False

                if sorted: break

        return products