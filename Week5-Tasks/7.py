theDictionary = {
    'a': 0,
    'i': 0,
    'u': 0,
    'e': 0,
    'o': 0,
}

fullName = input("Please Enter your full name: ").lower()

for i in range(len(fullName)):
    match fullName[i]:
        case 'a':
            theDictionary['a'] += 1
        case 'i':
            theDictionary['i'] += 1
        case 'u':
            theDictionary['u'] += 1
        case 'e':
            theDictionary['e'] += 1
        case 'o':
            theDictionary['o'] += 1

for i, j in theDictionary.items():
    print(f"{i}: {j}")
