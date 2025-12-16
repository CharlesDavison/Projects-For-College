import random

def win():
        print("yay")
        if input("Play again? (y/n): ") == "y":
                start()

def draw():
        print("draw")
        if input("Play again? (y/n): ") == "y":
                start()

def loss():
        print("you failed")
        if input("Play again? (y/n): ") == "y":
                start()

def start():
        humanChoice = int(input("Enter Your Choice (0 - rock, 1 - paper, 2 - scissors): "))
        compChoice = random.randint(0,2)

        match humanChoice:
                case 0:
                        match compChoice:
                                case 0: draw()
                                case 1: loss()
                                case 2: win()
                
                case 1:
                        match compChoice:
                                case 0: win()
                                case 1: draw()
                                case 2: loss()
                
                case 2:
                        match compChoice:
                                case 0: loss()
                                case 1: win()
                                case 2: draw()
        return 0

if __name__ == "__main__":
        start()