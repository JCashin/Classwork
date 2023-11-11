def multiply(a,b):
    x=a+b
    y=a*b
    return x,y
num1 = int(input("whats your frist number"))
num2 = int(input("whats your second number"))
answer=multiply(num1,num2)
print(num1,"add",num2,"=",answer[0])
print(num1,"times",num2,"=",answer[1])