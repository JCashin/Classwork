Green=0
Red=0
score = [[1,2,2,1,1,1,2],[45,30,46,31,10,32,2]] # sets 2d array for keeping score
menu = True
while menu == True: # will ask if want to add score untill N selected
    print(score[0])
    print(score[1])
    add = input("Do you want to add a score to the scoreboard?\nY/N: ")
    if add == "Y":
        points = int(input("How many points did you score?\n"))
        team = input("Did you play for Green or Red?\n") # asks for number of points and team
        team = team.upper()
        if team == "GREEN": # adds team indicator to score[0] and adds number of points to score[1]
            score[0].append(1)
            score[1].append(points)
        elif team == "RED": 
            score[0].append(2)
            score[1].append(points)
            print(score)
            print(score[1])
    elif add == "N":
        menu = False
for i in range(len(score[0])): # counts through score[0] and adds points with indicator 1 to green and indicator 2 to Red
    if score[0][i] == 1:
        Green = Green + score[1][i]
    elif score[0][i] == 2:
        Red = Red + score[1][i]
print("Green scored",Green,"points") # prints number of points per team
print("Red scored",Red,"points")