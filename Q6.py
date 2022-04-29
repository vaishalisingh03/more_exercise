name=["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
l=[]
i=0
while i<len(name):
    if name[i]  not in l:
        l.append(name[i])
    i+=1
print(l)