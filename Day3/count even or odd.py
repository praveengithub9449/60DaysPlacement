num=list(map(int,input("enter a number in list ").split()))

even=0
odd=0

for i in num:
    if i%2 ==0:
        even += 1
    else :
        odd +=1

print(even)
print(odd)