data=[]
file = open("File Handing\The New File.txt","w")
file.write("Michael\n")
file.write("William\n")
file.write("Susan")
deez = "mellon"
nuts = "man"
file.write(deez+"\n")
file.write(nuts+"\n")
file.close()
file = open("File Handing\The New File.txt","r")
for line in file:
    data.append(line)
print(data)
