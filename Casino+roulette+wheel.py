playersMoney = int(input("What´s your credit ($)?"))
while playersMoney <= 0:
    playersMoney = int(input("You need to have at least 1$ to play. What´s your credit?"))
    
bet = int(input("Place your bet ($):"))
while playersMoney < bet or bet <= 0:
    bet = int(input("Invalid input. Place another bet ($):"))

import random

while playersMoney >= bet:
    chosenNumber = int(input("Choose your number:"))
    while chosenNumber < 0 or chosenNumber > 49:
        chosenNumber = int(input("The number must be between 0 and 49:"))
    
    print("You put", bet, "$ on the number", chosenNumber, "----> Good luck!")
    
    randomNumber = random.randint(0, 49)
    print("Roulette number:", randomNumber)
    if chosenNumber == randomNumber:
        print("You won!!!")
        playersMoney = playersMoney + (50*bet)
        print("You now have:", playersMoney, "$")
        break
    else:
        playersMoney = playersMoney - bet
        print("Sorry, you lost. You now have", playersMoney, "$ left.")
        
    if playersMoney == 0:
        print("You ran out of money, game over.")
        break
    
    bet = int(input("Place a new bet ($):"))
    while playersMoney < bet or bet <= 0:
        bet = int(input("Invalid input. Place another bet ($):"))
