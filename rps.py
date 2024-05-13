from random import randint

l = ["Rock", "Paper", "Scissors"]
comp = l[randint(0,2)]
play = False

while play == False:
    play = input("Rock, Paper, Scissors?")
    if play == comp:
        print("Its a Tie!")
    elif play == "Rock":
        if comp == "Paper":
            print("You lose!", comp," covers ", play)
        else:
            print("You win!", play, " Smashes ", comp)
    elif play == "Paper":
        if comp == "Scissors":
            print("You lose!", comp, " Cuts ", play)
        else:
            print("You win!", play, " Covers ", comp)
    elif play == "Scissors":
        if comp == "Rock":
            print("You lose!", comp, " Smashes ", play)
        else:
            print("You win!", play, " Cuts ", comp)
    else:
        print("Syntax error, check code.")
    play = False
    comp = l[randint(0,2)]
