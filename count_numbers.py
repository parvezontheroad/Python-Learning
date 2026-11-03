count=0
n=int(input("enter a number:"))
for i in range(1, n+1):
    if i % 4 == 0 :
        count=count+1
print("TOTAL DIVISIBLE BY 4:", count)