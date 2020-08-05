book={}
BOOK={}
n=0
while int(n)!=6:
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Please choose one service')
    print('1.建立詞彙')
    print('2.列出所有單字')
    print('3.英翻中')
    print('4.中翻英')
    print('5.測驗')
    print('6.離開')
    num=input("Your ans:")
    n=int(num)
    if n==1:
        word=input('請輸入單字')
        mean=input('請輸入翻譯')
        book[word]=(mean)
        BOOK[mean]=(word)
        #YN=('你要不要繼續)
    elif n==2:
        print(book.keys)
    elif n==3:
        a=input('請輸入單字:')
        a=str(a)
        if a in book:
            ans = book[a]
            print(ans)
        else:
            print('沒有這個單字:')
        print()
    elif n==4:
        b=input('請輸入翻譯')
        b=str(b)
        if b in BOOK:
            ans = BOOK[b]
            print(ans)
        else:
            print('沒有這個單字')
    elif n==5:
        for k,v in book.items():
            print(k)
            b=input('請輸入翻譯')
            if str(v)==str(b):
                print('答對了')
            else:
                print('答錯了')     
    else:
        n=6
        print('謝謝')
    
    
        