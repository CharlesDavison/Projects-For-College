SIZE = 5

Product = {
        "Name": str(),
        "Price": int()
}

def total(products):
        TotalPrice = 0
        pricesLen = len(products)

        for i in range(pricesLen):
                TotalPrice += products[i]["Price"]

        return TotalPrice - products[0]["Price"]

def sort(products):
        n = len(products)

        sorted = False

        for i in range(0, n - 1):
                sorted = True

                for j in range(0, n - i - 1):
                        if products[j]["Price"] > products[j + 1]["Price"]:
                                products[j], products[j + 1] = products[j + 1], products[j]
                                sorted = False

                if sorted: break

        return products

def main():
        products = [Product.copy() for _ in range(SIZE)]

        for i in range(SIZE):
                products[i]["Name"] = input("Please Enter The Name Of The Product:\n")
                products[i]["Price"] = int(input("Please Enter The Price Of That Product:\n"))
        
        newProductsDict = sort(products)
        
        print("---------------------------------------------------")
        for i in range(SIZE):
                print(f"\tProduct: {newProductsDict[i]["Name"]}")
                print(f"\tPrice: £{newProductsDict[i]["Price"]}")
                print("---------------------------------------------------")

        print(f"Total(With Discount): £{total(newProductsDict)}")





if __name__ == "__main__":
        main()