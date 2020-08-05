n=0
ans=1


while int(n)!=7:
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Please choose one service')
    print('1.加法')
    print('2.減法')
    print('3.乘法')
    print('4.除法')
    print('5.平方')
    print('6.階乘')
    print('7.Finish')
    num=input("Your ans")
    n=int(num)
    a=input('輸入第一個數字')
    b=input('輸入第二個數字')
    if n==1:
        ans=int(a)+int(b)
        print('The ans is',ans)
    elif n==2:
        ans = int(a)-int(b)
        print('The ans is',ans)
    elif n==3:
        ans=int(a)*int(b)
        print('The ans is',ans)
    elif n==4:
        ans=int(a)/int(b)
        print('The ans is',ans)
    elif n==5:
        for z in range(b):
            ans=int(ans)*int(a)
            print('The ans is',ans)
    elif n==6:
        a=int(a)+1
        for a in range(1,a,1):
            ans=int(ans)*int(a)
            print('The ans is',ans)
    else:
        n=7

    
    
    
    


   

    