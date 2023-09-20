#asigns variables
name = input("whats your name?")
age = int(input("how old are you?"))
#checks if name is divisible by 2 and if so 0 will be outputted
if len(name) % 2 == 0:
    print("your name has an even number of letters")
else:
    print("your name has an odd number of letters")
#checks if age is 18 or older or younger than 18    
if age >= 18:
    IsAdult = True
if age < 18:
    IsAdult = False
#checks if IsAdult flag is true or false
if IsAdult == True:
    print("you are an adult")
if IsAdult == False:
    print("you are a child")