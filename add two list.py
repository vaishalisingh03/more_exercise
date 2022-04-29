a=[1,1,1,1,1,1]
b=[1,1,1,1,1]
sum=0
for i in (a,b):
    for j in i:
        sum+=j
print(sum)