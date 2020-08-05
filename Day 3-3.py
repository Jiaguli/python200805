names=[] 
scores=[]
totl=0

def to_avg(a,b):
    avg=int(a)/int(b)
    return avg

def to_h(c,d):
    h=0
    for i in range(c):
        num=int(d[i])
        if int(num)>int(h):
            h=d[i]
        else:
            h=int(h)
    return h

def to_l(e,f):
    l=100
    for w in range(e):
        num=int(f[w])
        if int(num)<int(l):
            l=f[w]
        else:
            l=int(l)
    return l
        
x=input('班上有幾個人')
x = int(x)
for j in range(x):
    name=input('你是誰')
    names.append(name)
    score=input('你幾分')
    scores.append(score)
    totl=int(score)+int(totl)
    
avg=to_avg(totl,x)
print('班上的平均是',avg)

highest=to_h(x,scores)
print('班上最高分是',highest,'分')

lowest=to_l(x,scores)
print('班上最低分是',lowest,'分')
