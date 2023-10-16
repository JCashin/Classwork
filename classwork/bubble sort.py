

names =["Henry","Steve","Julie","Ava","Tom","Olivia"]
length = len(names)
for i in range(length-1):
    for j in range(length-1-i):
        if names[j]>names[j+1]:
            store = names[j]
            names[j]=names[j+1]
            names[j+1] = store
            print(names)
