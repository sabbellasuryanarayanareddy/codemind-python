x,y=map(int,input().split())
Y=y*2
t=x+Y
if x%2==0 and(y%2==0 or x>0):
    print("YES")
else:
    print("NO")