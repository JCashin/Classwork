data=[]
file = open("File Handing\The New File.txt","w")
file.write("Michael\n")
file.write("William\n")
file.write("Susan")
file.close()
file = open("File Handing\The New File.txt","r")
for line in file:
    data.append(line)
print(data)
