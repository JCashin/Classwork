from re import A


menu = True
lista = [["Note 1","Note 2","Note 3","Note 4"],["Hello","My name is Joe","my address is TA30 5BQ","I have a dog"]]
while menu == True:
    print(lista[0],"\n",lista[1])
    choice = input("add note, remove note, edit note or quit?\n")
    if choice == "add":
        add = input("what do you want to title your new note")
        content = input("what do you want to put in your note")
        lista[0].append(add)
        lista[1].append(content)  
    elif choice == "remove":
        print(lista[0],"\n",lista[1])
        remove = int(input("which item number do you want to remove"))
        lista[0].pop(remove-1)
        lista[1].pop(remove-1)
    elif choice == "edit":
        edit = int(input("which note number do you want to edit?"))
        edita = input("what do you want to change it to?")
        lista[1][edit-1] = edita
    elif choice == "quit":
        menu = False