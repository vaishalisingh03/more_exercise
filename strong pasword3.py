print("create password")
ch=str(input("enter the alpha"))
if ch>="A" or "a" and ch<="z" or "z":
        digit=(input("enter the number"))
        sc=input("enter the special chr")
        if sc=="#" or sc=="@" or sc=="$" or sc=="&":
            print("your password")
            a=(ch+digit+sc)
            if len(a)>=6 or len(a)<=16:
                print("strong pasword")
                print(a)
            else:
                print("please enter password lenth 6 and 16")
        else:
            print("this is not strong password")
            print("please create strong password")
else:
    print("something wrong")
    
        

