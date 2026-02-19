std=[10,50,55,66]
lrg=std[0]
small=std[0]
total=0
for i in std:
    if i > lrg:
        lrg=i
    if i < small:
        small=i
    
    total += i
    
print(lrg,small,total)