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
    array = []

    for i in range(5):
        array.append(input("Please Enter A Name: "))     

    print(bubbleSort(array))


if __name__ == "__main__":
    main()
