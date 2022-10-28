t=int(input())
for i in range (t):
    n=input()
    c=0
    for j in str(n):
        if(n.isdigit()):
            c+=1
    if(c==len(n)):
            print("True")
    else:
            print("False")
    