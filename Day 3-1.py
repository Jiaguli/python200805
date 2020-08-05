end=0


for a in range(1,11):
    for b in range(1,11):
        end=int(a)*int(b)
        a=int(a)
        b=int(b)
        end=int(end)
        print(a,'*',b,'=',end)
    print()