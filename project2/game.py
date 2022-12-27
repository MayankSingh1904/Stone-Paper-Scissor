import random
l=["rock","paper","scissor"]
while True:
    computerCount=0
    userCount=0
    userchoice=int(input('''
    Game Started(Select an option!1 or 2)
    1 Play
    2 Exit 
    '''))
    if userchoice==1:
        for a in range(1,6):
            userInput=int(input('''Play your turn!
            1 rock
            2 paper
            3 scissor
            
            '''))
            if userInput==1:
                uc="rock"
            elif userInput==2:
                uc="paper"
            elif userInput==3:
                uc="scissor"
            else:
                print("Selection is invalid")
            computerChoice=random.choice(l)
            print("You selected:",uc)
            print("Computer Selected:",computerChoice)
            if computerChoice==uc:
                print("Draw")
                userCount=userCount+1
                computerCount=computerCount+1
            elif (uc=="rock" and computerChoice=="scissor") or (uc=="paper" and computerChoice=="rock") or (uc=="scissor" and computerChoice=="paper"):
                print("You Won")
                userCount=userCount+1
            else:
                print("Computer Won")
                computerCount=computerCount+1
       
        if userCount==computerCount:
            print("Your Total Score is:",userCount)
            print("Computer Total Score is:",computerCount)
            print("Game Drawn")
        elif userCount>computerCount:
            print("Your Total Score is:",userCount)
            print("Computer Total Score is:",computerCount)
            print("You won the Game!")
        else:
            print("Your Total Score is:",userCount)
            print("Computer Total Score is:",computerCount)
            print("You lost the Game!")
    else:
        break
