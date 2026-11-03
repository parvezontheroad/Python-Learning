n=int(input("enter a number:"))
count_even=0
count_odd=0
for i in range(1, n+1):
    if i%2==0:
        count_even= count_even+1
    else: count_odd=count_odd+1


print("total even numbers:",count_even)
print("total odd numbers:",count_odd)