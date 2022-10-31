from math import*
t=int(input())
for i in range(t):
    n=int(input())
    sq=sqrt(n)
    if sq==int(sqrt(n)):
        print("True")
    else:
        print("False")