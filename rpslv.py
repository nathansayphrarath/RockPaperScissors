#
#       project: 100_Days.py
#        author: Nathan Sayphrarath and Nolan Pierce
#  date written: 10/08/2024
#
#   description: Rock, Paper, Scissors, Lizard, Spock

from getpass import getpass 

print("A game of Rock, Paper, Scissors, Lizard, and Spock!")
print()
print("Select your move (R)ock, (P)aper or (S)cissors, (L)izard, (V)Spock")

print()
isPlaying = True

P1w = 0
P2w = 0
while isPlaying:
## start of code 1

    Player1 = getpass("Player 1: ")
    Player2 = getpass("Player 2: ")
    if Player1 == "R":
        if Player2 == "R":
            print("Draw")
            print("Score", P1w, "-", P2w)

        elif Player2 == "P":
            print("Player 2 wins!")
            P2w += 1
            print("Score", P1w, "-", P2w)

        elif Player2 == "L":
            print("Player 1 wins!")
            P1w += 1
            print("Score", P1w, "-", P2w)
        elif Player2 == "V":
            print("Player 2 wins!")
            P2w += 1
            print("Score", P1w, "-", P2w)
        else:
            print("Player 1 wins!")
            P1w += 1
            print("Score", P1w, "-", P2w)
    # end of code 1

## start of code 2
    if Player1 == "P":
        if Player2 == "P":
            print("Draw")
            print("Score", P1w, "-", P2w)

        elif Player2 == "R":
            print("Player 1 wins!")
            P1w += 1
            print("Score", P1w, "-", P2w)

        elif Player2 == "L":
            print("Player 2 wins!")
            P2w += 1
            print("Score", P1w, "-", P2w)
        elif Player2 == "V":
            print("Player 1 wins!")
            P1w += 1
            print("Score", P1w, "-", P2w)
        else:
            print("Player 2 wins!")
            P2w += 1
            print("Score", P1w, "-", P2w)
## end of code 2

## start of code 3
    if Player1 == "L":
        if Player2 == "L":
            print("Draw")
            print("Score", P1w, "-", P2w)

        elif Player2 == "R":
            print("Player 2 wins!")
            P2w += 1
            print("Score", P1w, "-", P2w)

        elif Player2 == "P":
            print("Player 1 wins!")
            P1w += 1
            print("Score", P1w, "-", P2w)
        elif Player2 == "V":
            print("Player 1 wins!")
            P1w += 1
            print("Score", P1w, "-", P2w)
        else:
            print("Player 2 wins!")
            P2w += 1
            print("Score", P1w, "-", P2w)
## end of code 3

## start of code 4
    if Player1 == "V":
        if Player2 == "V":
            print("Draw")
            print("Score", P1w, "-", P2w)

        elif Player2 == "P":
            print("Player 2 wins!")
            P2w += 1
            print("Score", P1w, "-", P2w)

        elif Player2 == "L":
            print("Player 2 wins!")
            P2w += 1
            print("Score", P1w, "-", P2w)
        elif Player2 == "R":
            print("Player 1 wins!")
            P1w += 1
            print("Score", P1w, "-", P2w)
        else:
            print("Player 1 wins!")
            P1w += 1
            print("Score", P1w, "-", P2w)
## end of code 4

## start of code 5
    if Player1 == "S":
        if Player2 == "S":
            print("Draw")
            print("Score", P1w, "-", P2w)

        elif Player2 == "P":
            print("Player 1 wins!")
            P1w += 1
            print("Score", P1w, "-", P2w)

        elif Player2 == "L":
            print("Player 1 wins!")
            P1w += 1
            print("Score", P1w, "-", P2w)
        elif Player2 == "V":
            print("Player 2 wins!")
            P2w += 1
            print("Score", P1w, "-", P2w)
        else:
            print("Player 2 wins!")
            P2w += 1
            print("Score", P1w, "-", P2w)




    playAgain = input("Do you want to play again? (Y/N)")
    if playAgain == "Y" or playAgain == "y":
        isPlaying = True
    elif playAgain == "N" or playAgain == "n":
        isPlaying = False
        print()
        print("BORINGGGGGGGG!!!!!!")
        if P1w > P2w:
            print()
            print("Player 1 beats Player 2! Player 2 sucks.💩")
        elif P1w < P2w:
            print()
            print("Player 2 beats Player 1! Player 1 sucks.💩")
