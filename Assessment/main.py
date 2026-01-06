# Imports a seperate file with all the functions and constants in it.
# This makes the code more maintainable and radable.
from functions import *

# Initaialises a dictionary(structure) called Product.
Product = {
        "Name": str(),
        "Price": float()
}

# The main function where everything gets called.
def main():
        # Creates an array of the dictionary initialised earlier.
        products = [Product.copy() for _ in range(SIZE)]

        # Get's the user's input and saves it to the array.
        for i in range(SIZE):
                products[i]["Name"] = input("Please Enter The Name Of The Product:\n> ")

                # Keep prompting until the user provides a valid, non-negative float for Price.
                while True:
                        price_input = input("Please Enter The Price Of That Product:\n> ")
                        try:
                                price_val = float(price_input)
                                # Trigger the except block if the user entered a negative price
                                if price_val < 0:
                                        raise ValueError("Price cannot be negative")
                                products[i]["Price"] = round(price_val, 2)
                                break
                        except ValueError:
                                print("You probably typed something that wasn't a non-negative number. Try again.")
                        except Exception as e:
                                # Unexpected errors: show a short message and continue prompting
                                print(f"Unexpected error: {e}")
        
        # Calls the sort function to sort the array by price.
        newProductsDict = sort(products)
        
        # Output Results in a formatted way.
        print("---------------------------------------------------")
        for i in range(SIZE):
                # Use single-quoted f-strings so the dictionary key strings don't clash with outer quotes
                print(f'\tName: {newProductsDict[i]["Name"]}')
                print(f'\tPrice: £{newProductsDict[i]["Price"]}')
                print("---------------------------------------------------")

        print(f"Total(With Discount): £{total(newProductsDict)}")

if __name__ == "__main__":
        main()