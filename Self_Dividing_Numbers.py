a=int(input())
b=int(input())
for n in range(a,b+1):
    t=n
    c=0
    while n>0:
        r=n%10
        if r==0:
            break
        elif t%r==0:
            c+=1
        n=n//10
        if c==len(str(t)):
            print(t,end=" ")