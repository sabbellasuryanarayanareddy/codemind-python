n=input()
N=int(n)**2
auto=int(N)%(10**(len(n)))
if int(n)==auto:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")