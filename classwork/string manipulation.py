menu = True
x=0
postcode = input("What is your postcode?\n")
while menu == True:
    if postcode[0].islower() == True or postcode[1].islower() == True or postcode[6].islower() == True or postcode[7].islower() == True or postcode[0].isdigit() == True or postcode[1].isdigit() == True or isdigit[6].islower() == True or postcode[7].isdigit() == True:
        postcode = input("Try again.\n")
    else:
        x=x+1
    if postcode[2].isalpha() == True or postcode[3].isalpha() == True or postcode[5].isalpha() == True:
        postcode = input("Try again.\n")
    else:
        x=x+1
    if postcode[4].isspace() == False:
        postcode = input("Try again.\n")
    if postcode[4].isspace() == True:
        x=x+1
    if x == 3:
        print("Good Job.")
        menu = False


