n,m=map(int,input().split())
for i in range(1,m+1):
     if i%2!=0:
         print("{} x {} = {}".format(n,i,n*i))