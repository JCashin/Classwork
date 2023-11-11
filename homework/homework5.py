def addition(a,b): # defining the addition function
    c=a+b
    return c
def subtraction(a,b): # defining the subtraction function
    c=a-b
    return c
def multiplication(a,b): # defining the multiplication function
    c=a*b
    return c
def division(a,b): # defining the division fucntion
    c=a/b
    return c
menu = True
menu2 = True
while menu == True:
    num1= int(input("what is your first number? ")) # input for numbers
    num2= int(input("what is your second number "))
    while menu2 == True:
        choice = input("What operation do you want? Add, Sub, Mult, Div or exit ")
        choice = choice.upper()
        if choice == "ADD":
            answer = addition(num1,num2) # calls add function and passes variable num1 and num2 in, returns c as answer
        elif choice == "SUB":
            answer = subtraction(num1,num2) # calls sub function and passes variable num1 and num2 in, returns c as answer
        elif choice == "MULT":
            answer = multiplication(num1,num2) # calls mult function and passes variable num1 and num2 in, returns c as answer
        elif choice == "DIV":
            answer = division(num1,num2) # calls div function and passes variable num1 and num2 in, returns c as answer
        elif choice == "EXIT":
            exit()
        else:
            print("thats not a valid operation ")
    print("Your answer is:",answer)