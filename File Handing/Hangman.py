words = ["JAZZ","ELECTRICITY","PLUG","TRUNK","BRONZE","PIANO","DRAKE","SIGHT","FEATHER","GUEST","SHOES","DOGS","SQUARE","UTOPIA"]
menu = True
menuB = True
lives = 6
error = 0
import random
from re import L # setting variables 
while menu == True:
    menuchoice = input("Do you want to:\nA) Play game\nB) Add words to list\nC) Exit\n")
    menuchoice = menuchoice.upper()
    if menuchoice == "A":
        menuB = True
        lives = 6
        randomwords = random.randint(0,len(words)-1)
        randomword = words[randomwords] # picks random number to pick word from list 
        print(randomword) # testing purposes remove when done
        splitword = [*randomword] # splits word into letters
        print(splitword) # testing purposes remove when done
        length = len(splitword)
        mysteryword = []
        for i in splitword:
            mysteryword.append("X") # adds Xs where letters would be in word
        while menuB == True:
            print(mysteryword)
            guess = input("What is your guess? (Word or letter)\n")
            guess = guess.upper()
            print(lives) # testing purposes remove when done
            if len(guess) > 1: # if guess is a word not a letter it'll check if its the guessed word
                if guess == randomword:
                    print("Congratulations, that's the correct word!")
                    file = open("File Handing\Results.txt","a")
                    file.write("\n"+randomword+", "+str(lives)) # if word guessed it will add to text file with number of lives left
                    file.close()
                    menuB = False
                elif guess != randomword:
                    print("Sorry that is incorrect.") # if guess is incorrect it will remove a life
                    lives = lives - 1
            elif len(guess) == 1:
                for i in range(0,len(splitword)):  
                    if guess == splitword[i]:
                        mysteryword[i] = guess
                        for x in range(i,len(splitword)):
                            if guess == splitword[x]:
                                mysteryword[x] = guess
                                for y in range(x,len(splitword)):
                                    if guess == splitword[y]:
                                        mysteryword[y] = guess   
                if splitword.count(guess) == 0:
                    lives = lives - 1
                if mysteryword == splitword:
                    print("Congratulations, that's the correct word!")
                    file = open("File Handing\Results.txt","a")
                    file.write("\n"+randomword+", "+str(lives)) # if word guessed it will add to text file with number of lives left
                    file.close()
                    menuB = False
            print(lives) # testing purposes remove when done
            if lives == 0:
                print("You died :(")
                menuB = False
    elif menuchoice == "B":
        newword = input("What word do you want to add to the list?\n")
        newword = newword.upper()
        words.append(newword) # adds new word to list
        print(words)
    elif menuchoice== "C":
        menu = False # closes menu
        