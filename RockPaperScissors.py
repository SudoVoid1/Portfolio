#Rock Paper Scissors
import random
b = 0
p = 0
play = True
while play == True:
    playerchoice = int(input("\nRock[1], Paper[2], Scissors[3]\n"))
    bwin = f"Oppenent has {b+1} Wins"
    pwin = f"You have {p+1} Wins"
    # Ochoice 1=rock 2=paper 3=scissors
    #Rock > Scissors, Paper > Rock, Scissors> Paper

    if playerchoice <= 3:
        Ochoice = random.randint(1,3)
        #Ochoice = 1 #Test item

        if Ochoice == 1: #Bot Throws ROCK
            print("Oppenent Threw Rock")
            if playerchoice == 3:
                print("Rock Beats Scissors")
                b += 1
                print(bwin)
            elif playerchoice == 2:
                p += 1
                print(pwin)

        if Ochoice == 2: #Bot Throws PAPER
            print("Oppenent Threw Paper")
            if playerchoice == 1:
                print("Paper Beats Rock")
                b += 1
                print(bwin)
            elif playerchoice == 3:
                p += 1
                print(pwin)

        if Ochoice == 3: #Bot Throws Scissors
            print("Oppenent Threw Scissors")
            if playerchoice == 2:
                print("Scissors Beats Paper")
                b += 1
                print(bwin)
            elif playerchoice == 1:
                print("Rock Beats Scissors")
                p += 1
                print(pwin)

        if playerchoice == Ochoice: #If Both tie
            print("Choices Canceled, Tie")

        if b == 3: # First to 3 wins b = Bot
            print("\n Oppenent Won 3 Games")
            PlayAgain = input("Do you want to Play Again? ")
            if PlayAgain == "Yes":
                b = 0
                p = 0
                play = True
            elif PlayAgain == "No":
                play = False

        if p == 3: # First to 3 wins p= Player
            print("\nYou Won 3 Games")
            PlayAgain = input("Do you want to Play Again? ").lower()
            if PlayAgain == "yes":
                b = 0
                p = 0
                play = True
            elif PlayAgain == "no":
                play = False
    else:
        print("Please enter the correct term")
        playerchoice = input("Rock[1], Paper[2], Scissors[3]")

