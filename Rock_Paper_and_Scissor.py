import random

scorec = 0
scoreu = 0

def printrock():
    print('''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    
def printscissor():
    print('''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
    
def printpaper():
    print('''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
    
def continues(scorec, scoreu):
    a = input("Do you want to continue? Enter y or Y for yes and n or N for no: ")
    if(a in ['n', 'N']):
        if(scorec > scoreu):
            print(f"Computer won! Final score: Computer -> {scorec}   User -> {scoreu}\n")
        elif(scorec == scoreu):
            print(f"It's a draw! Final score: Computer -> {scorec}   User -> {scoreu}\n")
        else:
            print(f"User won! Final score: Computer -> {scorec}   User -> {scoreu}\n")
        exit(1)
    elif(a in ['y', 'Y']):
        print(f"Current score: Computer -> {scorec}   User -> {scoreu}\n")
    else:
        print("Looks like you don't wanna play anymore!")
        print("Self-terminating!")
        exit(1)
        

while(1):
    a = int(input("Please enter 1 to choose rock, 2 to choose paper and 3 to choose scissor: "))
    if(a == 1):
        printrock()
    elif(a == 2):
        printpaper()
    elif(a == 3):
        printscissor()
    else:
        print("Wrong input! Please try again!")
        continues(scorec, scoreu)
        continue
        
    b = random.randint(1, 3)
    
    if(b == 1):
        printrock()
    elif(b == 2):
        printpaper()
    elif(b == 3):
        printscissor()
    
    if(a == 1 and b == 2): #rock and paper
        print("Computer wins this round :(")
        scorec += 1
        continues(scorec, scoreu)
    elif(a == 1 and b == 3): #rock and scissor
        print("User wins this round!")
        scoreu += 1
        continues(scorec, scoreu)
    elif(a == 1 and b == 1): #rock and rock
        print("This round is a draw!")
        continues(scorec, scoreu)
    elif(a == 2 and b == 1): #paper and rock
        print("User wins this round!")
        scoreu += 1
        continues(scorec, scoreu)
    elif(a == 2 and b == 2): #paper and paper
        print("This round is a draw!")
        continues(scorec, scoreu)
    elif(a == 2 and b == 3): #paper and scissor
        print("Computer wins this round :(")
        scorec += 1
        continues(scorec, scoreu)
    elif(a == 3 and b == 1): #scissor and rock
        print("Computer wins this round :(")
        scorec += 1
        continues(scorec, scoreu)
    elif(a == 3 and b == 2): #scissor and paper
        print("User wins this round!")
        scoreu += 1
        continues(scorec, scoreu)
    elif(a == 3 and b == 3): #scissor and scissor
        print("This round is a draw!")
        continues(scorec, scoreu)

