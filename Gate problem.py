a = True
while a == True:
    gate = input("what gate do you want: AND, OR, NOT or XOR?\n")
    if gate == "AND":
        inputA, inputB = input("what are your two inputs?").split()
        if inputA == "0":
            if inputB =="0":
                print("0")
            elif inputB =="1":
                print("0")
        elif inputA =="1":
            if inputB =="0":
                print("0")
            elif inputB =="1":
                print("1")
    if gate == "OR":
        inputA, inputB = input("what are your two inputs?").split()
        if inputA == "0":
            if inputB == "0":
                print("0")
            elif inputB == "1":
                print("1")
        elif inputA == "1":
            print("1")
    if gate == "NOT":
        inputA = input("what is your inputs?")
        if inputA == "0":
            print("1")
        elif inputA =="1":
            print("0")
    if gate == "XOR":
        inputA, inputB = input("what are your two inputs?").split()
        if inputA =="0":
            if inputB =="0":
                print("0")
            elif inputB =="1":
                print("1")
        elif inputA =="1":
            if inputB =="0":
                print("1")
            elif inputB =="1":
                print("0")


