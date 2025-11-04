def bubbleSort(array):
    for i in range(len(array)):
        swapped = False
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if swapped == False:
            break
                
    return(array)

def main():
    array = [int()]*5
   
    for i in range(len(array)):
        tempVar = ""
        tempVar = input("Please Enter A Number: ")
    
        while tempVar.isnumeric() == False:
            tempVar = input("Please Enter An Actual Number: ")
    
        array[i] = int(tempVar)
    
    print(bubbleSort(array))


if __name__ == "__main__":
    main()
