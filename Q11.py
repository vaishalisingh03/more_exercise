l = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
i=0
while i<len(l):
    if type(l[i])==list:
        j=0
        while j<len(l[i]):
            print(l[i][j])
            j+=1
    print(".....")
    i+=1