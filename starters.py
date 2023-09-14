#14/09/23
total = 0
final = 0
paid = int(input("paid in "))
years = int(input("years"))
for i in range(years):
    start = final
    total = final + paid
    interest = total * 0.1
    final = total + interest
    print(start,paid,final,interest,i+1, "\n")
