import random
print("WELCOME TO COWS & BULLS GAME")
print("Enjoy your game")
print("----INSTRUCTION----")
print("Cow - 1 : Position of a number is correct!!!")
print("Bull - 1 : A Guessed number is correct but misplaced!!!")
print("---xxx---xxx---xxx---xxx---")
print("Let's begin..........")
sn=str(random.randint(10,99))
chances=7
while chances<=7:
    g = 8 - chances
    print("Guess ",g)
    pg = str(input("Enter Your Guess: "))
    if sn==pg:
        print("Congrats.....")
        print("You won!!!!!!")
        break
    else:
        chances-=1
        cows=0
        bulls=0
        if pg[0] == sn[0]:
            cows = 1
        if pg[1] == sn[1]:
            cows = 1
        if pg[0] == sn[1]:
            bulls = 1
        if pg[1] == sn[0]:
            bulls = 1
        print("-----------------------")
        print("Hint: ")
        print("Cows: ",cows)
        print("Bulls: ",bulls)
        print("Chances left: ",chances)
        print("-----------------------")
        if chances<1:
            print("Sorry, you lost the game")
            print("Secret number is ",sn)
            print("Better luck next time :((")
            break