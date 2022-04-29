words =input("enter tout thought")
list=[]
string=""
for i in words:
    if i==" ":
        list.append(string)
        string="" 
    else:
        string+=i
if string:
    list.append(string)
    print(list)